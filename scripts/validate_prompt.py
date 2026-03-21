#!/usr/bin/env python3
"""
Seedance 2.0 提示词工业级校验脚本
用于在 Agent 生成提示词后进行自动化质量审查。

用法:
    python scripts/validate_prompt.py --text "你的提示词内容"
    python scripts/validate_prompt.py --file prompt.txt
"""

import argparse
import re
import sys
import json


# Seedance 为中国自研模型，同时支持中英文提示词


def detect_language(text):
    """检测提示词语言：中文字符占比超30%则为中文，否则为英文。
    覆盖 CJK Unified (U+4E00–U+9FFF)、CJK Extension A (U+3400–U+4DBF)、
    CJK 符号与标点 (U+3000–U+303F)、全角标点 (U+FF00–U+FFEF)。
    """
    def is_cjk(c):
        cp = ord(c)
        return (
            0x4E00 <= cp <= 0x9FFF or    # CJK Unified Ideographs
            0x3400 <= cp <= 0x4DBF or    # CJK Extension A
            0x3000 <= cp <= 0x303F or    # CJK Symbols and Punctuation
            0xFF00 <= cp <= 0xFFEF       # Fullwidth Forms
        )
    chinese_chars = sum(1 for c in text if is_cjk(c))
    total_chars = max(len(text.strip()), 1)
    return "cn" if chinese_chars / total_chars > 0.3 else "en"


def check_length(text, lang="cn"):
    """检查提示词长度是否合规（中文≤500字符 / 英文≤1000词）"""
    results = []

    if lang == "cn":
        length = len(text)
        max_len = 500
        unit = "字符"
    else:
        length = len(text.split())
        max_len = 1000
        unit = "words"

    if length > max_len:
        results.append({
            "level": "error",
            "code": "LENGTH_EXCEEDED",
            "message": f"长度超标！当前 {length} {unit}，上限 {max_len} {unit}。"
                       f"模型注意力会严重衰减，请删减形容词并合并长句。",
            "value": length,
            "limit": max_len
        })
    elif length > max_len * 0.85:
        results.append({
            "level": "warning",
            "code": "LENGTH_NEAR_LIMIT",
            "message": f"长度接近上限：{length}/{max_len} {unit} "
                       f"({length/max_len*100:.0f}%)。建议适当精简。",
            "value": length,
            "limit": max_len
        })
    else:
        results.append({
            "level": "pass",
            "code": "LENGTH_OK",
            "message": f"长度合规：{length}/{max_len} {unit}。",
            "value": length,
            "limit": max_len
        })
    return results


def _detect_declared_duration(text):
    """从提示词中提取声明的时长（秒）"""
    patterns = [
        r'(\d+)\s*秒',
        r'(\d+)\s*[sS](?:ec|econds?)?(?:\s|，|,|$)',
    ]
    durations = []
    for pat in patterns:
        for m in re.finditer(pat, text[:60]):  # 时长声明通常在开头
            durations.append(int(m.group(1)))
    return max(durations) if durations else 0


def check_time_slices(text):
    """检查时序切片逻辑（时长感知版）"""
    results = []
    # 匹配多种时间戳格式: [0-3s], [0-3秒], 0-3s：, 0-3秒：
    patterns = [
        r'\[(\d+)-(\d+)s\]',
        r'\[(\d+)-(\d+)秒\]',
        r'(\d+)-(\d+)s[：:·]',
        r'(\d+)-(\d+)秒[：:·]',
        r'(\d+)-(\d+)s\s*[：:]',
        r'(\d+)-(\d+)秒\s*[：:]',
    ]

    all_slices = []
    for pattern in patterns:
        matches = re.findall(pattern, text)
        for m in matches:
            start, end = int(m[0]), int(m[1])
            all_slices.append((start, end))

    # 去重
    all_slices = sorted(set(all_slices))
    declared_duration = _detect_declared_duration(text)

    if not all_slices:
        # 时长感知：>5s 无时间切片为 error，≤5s 为 warning
        if declared_duration > 5:
            results.append({
                "level": "error",
                "code": "LONG_VIDEO_NO_SLICES",
                "message": f"声明时长 {declared_duration}秒 但未使用时间切片！"
                           f"超过5秒的视频必须使用时序切片（如 0-3秒：...；3-7秒：...），"
                           f"否则画面动作会揉作一团。"
            })
        else:
            results.append({
                "level": "warning",
                "code": "NO_TIME_SLICES",
                "message": "未检测到时序切片（如 [0-3s] 或 0-3秒：）。"
                           "若生成长视频(>5s)，画面动作极易粘连崩坏。"
            })
    else:
        # 检查时间段是否有重叠
        for i in range(len(all_slices) - 1):
            if all_slices[i][1] > all_slices[i + 1][0]:
                results.append({
                    "level": "warning",
                    "code": "TIME_OVERLAP",
                    "message": f"时间段重叠：[{all_slices[i][0]}-{all_slices[i][1]}s] "
                               f"与 [{all_slices[i+1][0]}-{all_slices[i+1][1]}s]。"
                })

        # 检查起始是否从0开始
        if all_slices[0][0] != 0:
            results.append({
                "level": "warning",
                "code": "TIME_NOT_FROM_ZERO",
                "message": f"时间戳未从0开始，首段为 [{all_slices[0][0]}-{all_slices[0][1]}s]。"
            })

        # 检查声明时长与切片末端是否匹配
        if declared_duration > 0:
            last_end = all_slices[-1][1]
            if abs(last_end - declared_duration) > 2:
                results.append({
                    "level": "warning",
                    "code": "DURATION_MISMATCH",
                    "message": f"声明时长 {declared_duration}秒，但时间切片结束于 {last_end}秒，"
                               f"差距 {abs(last_end - declared_duration)}秒。请检查是否遗漏时间段。"
                })

        if not results:
            results.append({
                "level": "pass",
                "code": "TIME_SLICES_OK",
                "message": f"检测到 {len(all_slices)} 个时间段，时序逻辑正常。"
            })

    return results


def check_camera_language(text):
    """检查是否包含专业运镜指令"""
    results = []
    camera_words_cn = [
        "特写", "广角", "跟拍", "摇", "推", "拉", "升降", "环绕",
        "航拍", "俯拍", "仰拍", "平移", "跟踪", "手持", "云台",
        "斯坦尼康", "穿越机", "微距", "一镜到底", "慢镜头",
        "全景", "近景", "中景", "远景", "浅景深"
    ]
    camera_words_en = [
        "close-up", "wide", "tracking", "dolly", "pan", "tilt",
        "crane", "orbit", "aerial", "pov", "handheld", "steadicam",
        "zoom", "push", "pull", "arc", "gimbal", "fpv", "macro",
        "slow motion", "low angle", "high angle", "dutch",
        "shot", "mm"  # 如 85mm, 50mm
    ]

    text_lower = text.lower()
    found_cn = [w for w in camera_words_cn if w in text]
    found_en = [w for w in camera_words_en if w in text_lower]

    if not found_cn and not found_en:
        results.append({
            "level": "error",
            "code": "NO_CAMERA_LANGUAGE",
            "message": "缺乏专业运镜指令。画面将随机生成，如同监控探头。"
                       "请添加具体的运镜术语（如 Dolly In, 航拍, Tracking Shot）。"
        })
    else:
        all_found = found_cn + found_en
        results.append({
            "level": "pass",
            "code": "CAMERA_OK",
            "message": f"检测到 {len(all_found)} 个运镜术语：{', '.join(all_found[:5])}"
                       f"{'...' if len(all_found) > 5 else ''}。"
        })
    return results


def check_cgi_words(text):
    """检查是否包含易产生 AI 塑料感的废话（硬阻断）"""
    results = []
    # 硬黑名单：直接阻断（error），这些词无任何合理使用场景
    banned_hard = {
        "cn": ["超清晰", "杰作", "高画质", "超高画质", "超精细",
               "极致画质", "完美画质"],
        "en": ["masterpiece", "ultra-sharp", "best quality",
               "extremely detailed", "hyper-realistic",
               "ultra hd", "super resolution"]
    }
    # 软警告：4k/8k 在品质锚定语境下可能有意义，仅作警告
    soft_warn = ["4k", "8k", "4K", "8K"]

    found_hard = []
    found_soft = []
    text_lower = text.lower()

    for word_list in banned_hard.values():
        for w in word_list:
            if w.lower() in text_lower:
                found_hard.append(w)

    for w in soft_warn:
        if w in text:
            found_soft.append(w)

    if found_hard:
        results.append({
            "level": "error",
            "code": "BANNED_WORDS_DETECTED",
            "message": f"❌ 检测到廉价 AI 塑料感词汇：{', '.join(found_hard)}。"
                       f"请立即使用 quality-anchors.md 中的胶片型号/材质质感/有机瑕疵进行替换！"
        })
    if found_soft:
        results.append({
            "level": "warning",
            "code": "RESOLUTION_WORDS",
            "message": f"检测到分辨率词汇：{', '.join(found_soft)}。"
                       f"若用于品质锚定（如配合渲染引擎声明）可保留，否则建议移除。"
        })

    if not found_hard and not found_soft:
        results.append({
            "level": "pass",
            "code": "CGI_WORDS_CLEAN",
            "message": "未检测到AI塑料感废话词汇。"
        })
    return results


def check_asset_refs(text):
    """检查多模态资产引用是否超限"""
    results = []
    img_refs_cn = re.findall(r'@图片(\d+)', text)
    img_refs_en = re.findall(r'@image(\d+)', text, re.IGNORECASE)
    vid_refs_cn = re.findall(r'@视频(\d+)', text)
    vid_refs_en = re.findall(r'@video(\d+)', text, re.IGNORECASE)
    aud_refs_cn = re.findall(r'@音频(\d+)', text)
    aud_refs_en = re.findall(r'@audio(\d+)', text, re.IGNORECASE)

    # 中英文引用分别匹配，用 set() 按数字去重（如 @Image1 和 @image1 只计一次）
    img_count = len(set(img_refs_cn + img_refs_en))
    vid_count = len(set(vid_refs_cn + vid_refs_en))
    aud_count = len(set(aud_refs_cn + aud_refs_en))
    total = img_count + vid_count + aud_count

    if img_count > 9:
        results.append({
            "level": "error",
            "code": "IMAGE_REF_EXCEEDED",
            "message": f"图片引用超限：{img_count}/9。"
        })
    if vid_count > 3:
        results.append({
            "level": "error",
            "code": "VIDEO_REF_EXCEEDED",
            "message": f"视频引用超限：{vid_count}/3。"
        })
    if aud_count > 3:
        results.append({
            "level": "error",
            "code": "AUDIO_REF_EXCEEDED",
            "message": f"音频引用超限：{aud_count}/3。"
        })
    if total > 12:
        results.append({
            "level": "error",
            "code": "TOTAL_REF_EXCEEDED",
            "message": f"混合文件总数超限：{total}/12（图片{img_count}+视频{vid_count}+音频{aud_count}）。"
        })

    if not results:
        if total > 0:
            results.append({
                "level": "pass",
                "code": "ASSET_REFS_OK",
                "message": f"资产引用合规：图片{img_count}/9，视频{vid_count}/3，"
                           f"音频{aud_count}/3，总计{total}/12。"
            })
        else:
            results.append({
                "level": "pass",
                "code": "NO_ASSET_REFS",
                "message": "纯文本模式，无资产引用。"
            })
    return results


def check_conflict(text):
    """检查运动冲突 + 光学物理冲突 + 风格冲突"""
    results = []

    # === 运动逻辑冲突（按时间段分割检查） ===
    motion_conflicts = [
        (["快速", "高速", "急速", "fast", "rapid"],
         ["慢动作", "slow motion", "慢镜头", "缓慢"],
         "速度冲突：快速与慢动作同段出现"),
        (["推进", "push in", "dolly in", "zoom in"],
         ["拉远", "pull out", "dolly out", "zoom out"],
         "运动冲突：推进与拉远同段出现"),
    ]

    segments = re.split(r'\d+-\d+[s秒][：:；;]?', text)
    for seg in segments:
        seg_lower = seg.lower()
        for group_a, group_b, desc in motion_conflicts:
            has_a = any(w in seg_lower for w in group_a)
            has_b = any(w in seg_lower for w in group_b)
            if has_a and has_b:
                results.append({
                    "level": "warning",
                    "code": "MOTION_CONFLICT",
                    "message": f"同一段内{desc}。"
                               f"模型接收矛盾信号会导致画面撕裂或果冻效应。"
                })
                break

    # === 光学物理冲突（全文检查） ===
    optical_conflicts = [
        (["14mm", "ultra-wide", "超广角", "ultra wide"],
         ["bokeh", "浅景深", "虚化", "奶油般", "creamy bokeh", "shallow depth"],
         "光学冲突！超广角(14mm)物理上无法产生强烈背景虚化，会造成 AI 渲染崩溃。请修改焦段或景深描述"),
        (["手持", "handheld", "手持晃动", "手持微晃"],
         ["绝对对称", "perfectly symmetrical", "完美对称", "严格对称"],
         "构图冲突！手持晃动不可能保持绝对对称构图，请选择三脚架/云台或放弃对称"),
    ]

    text_lower = text.lower()
    for group_a, group_b, desc in optical_conflicts:
        has_a = any(w in text_lower for w in group_a)
        has_b = any(w in text_lower for w in group_b)
        if has_a and has_b:
            results.append({
                "level": "error",
                "code": "OPTICAL_CONFLICT",
                "message": f"❌ {desc}。"
            })

    # === 风格冲突矩阵（全文检查） ===
    style_conflicts = [
        (["imax", "65mm清晰", "65mm", "imax清晰"],
         ["vhs", "录像带", "scan lines", "扫描线", "低分辨率"],
         "品质冲突！IMAX极致清晰与VHS模拟降解不可混用，请二选一"),
        (["胶片颗粒", "film grain", "有机噪点", "胶片质感"],
         ["锐利数码", "sharp digital", "电商质感", "锐利电商"],
         "品质冲突！胶片有机颗粒与锐利数码质感互斥——电商禁胶片，影片禁数码锐"),
        (["水墨", "ink wash", "宣纸", "写意", "水墨画"],
         ["ue5", "unreal engine", "光追", "ray tracing", "写实渲染"],
         "风格冲突！水墨写意与UE5写实光追互斥，若要融合请用'3D渲染水墨质感'"),
        (["cel-shad", "toon render", "卡通渲染", "三渲二", "cel shad",
          "赛璐璐", "cel-shaded", "toon渲染"],
         ["subsurface scattering", "sss透光", "皮肤毛孔", "visible pores",
          "micro-imperfections", "微瑕疵", "写实皮肤", "realistic skin"],
         "风格冲突！三渲二/Cel-Shade卡通渲染与写实PBR材质(SSS/毛孔/微瑕疵)互斥——"
         "三渲二应使用动画化材质（硬边阴影+色块填充），不要叠加写实材质词"),
        (["slow motion", "慢镜头", "慢动作"],
         ["speed ramp", "变速"],
         "速度冲突！Slow Motion 慢镜头与 Speed Ramp 变速不可在同一时间切片内同时使用——"
         "请分时间切片使用，慢镜和变速不在同段重叠"),
    ]

    for group_a, group_b, desc in style_conflicts:
        has_a = any(w in text_lower for w in group_a)
        has_b = any(w in text_lower for w in group_b)
        if has_a and has_b:
            results.append({
                "level": "error",
                "code": "STYLE_CONFLICT",
                "message": f"❌ {desc}。"
            })

    if not results:
        results.append({
            "level": "pass",
            "code": "NO_CONFLICT",
            "message": "未检测到逻辑/光学/风格冲突。"
        })
    return results


def check_ambiguous_terms(text, lang="cn"):
    """检测可能触发 Seedance 审核的裸英文运镜术语（可被误判为人名/品牌名）"""
    results = []
    # 高风险裸词：可作为人名/品牌名
    high_risk = {
        "Dolly": "推轨推进 / dolly tracking shot",
        "Aerial": "航拍 / aerial drone shot",
        "Crane": "摇臂升降 / crane shot",
        "Pan": "水平摇摄 / pan shot",
        "Arc": "弧形环绕 / arc shot",
        "Dutch": "荷兰角倾斜 / dutch angle shot",
        "Steadicam": "斯坦尼康稳定 / steadicam stabilized shot",
    }
    # 安全后缀：如果裸词后面紧跟这些词，说明上下文明确，风险降低
    safe_suffixes = [
        "shot", "camera", "movement", "drone", "tracking",
        "angle", "stabilized", "jib", "in", "out", "up", "down",
        "left", "right", "zoom", "back", "forward"
    ]

    found = []
    for bare_word, safe_alt in high_risk.items():
        # 用正则查找裸词（前后非英文字母，不区分大小写）
        pattern = r'(?<![a-zA-Z])' + re.escape(bare_word) + r'(?![a-zA-Z])'
        matches = list(re.finditer(pattern, text, re.IGNORECASE))
        for m in matches:
            # 检查后面是否有安全后缀
            after = text[m.end():m.end()+20].strip().lower()
            has_safe_suffix = any(after.startswith(s) for s in safe_suffixes)
            if not has_safe_suffix:
                found.append((bare_word, safe_alt))
                break  # 每个裸词只报一次

    if found:
        if lang == "cn":
            word_list = ", ".join(f"`{w}`" for w, _ in found)
            alt_list = "; ".join(f"{w}→{a.split(' / ')[0]}" for w, a in found)
            results.append({
                "level": "warning",
                "code": "AMBIGUOUS_CAMERA_TERM",
                "message": f"检测到裸英文运镜词 {word_list}，"
                           f"Seedance 可能误判为人名而触发违规。"
                           f"建议改用中文：{alt_list}"
            })
        else:
            word_list = ", ".join(f"`{w}`" for w, _ in found)
            alt_list = "; ".join(f"{w}→{a.split(' / ')[1]}" for w, a in found)
            results.append({
                "level": "warning",
                "code": "AMBIGUOUS_CAMERA_TERM",
                "message": f"Bare camera terms {word_list} detected — "
                           f"Seedance may flag these as person names. "
                           f"Use full phrases: {alt_list}"
            })
    else:
        results.append({
            "level": "pass",
            "code": "NO_AMBIGUOUS_TERMS",
            "message": "未检测到审核风险裸英文运镜词。"
        })
    return results


def validate_multi_segment(segments, lang=None):
    """校验多段分镜提示词：逐段独立校验 + 跨段一致性检查。
    segments: list of str, 每段提示词文本。
    """
    if not segments:
        return {"passed": False, "error": "无提示词段落"}

    if lang is None:
        lang = detect_language(segments[0])

    per_segment = []
    for i, seg in enumerate(segments):
        result = validate_prompt(seg, lang=lang)
        result["segment"] = i + 1
        per_segment.append(result)

    # === 跨段一致性检查 ===
    cross_results = []

    # 1. 风格总纲一致：比较每段的第一行（去除时长前缀后）
    first_lines = []
    for seg in segments:
        line = seg.strip().split('\n')[0] if seg.strip() else ""
        first_lines.append(line)

    if len(set(first_lines)) > 1:
        cross_results.append({
            "level": "warning",
            "code": "INCONSISTENT_STYLE_ANCHOR",
            "message": "跨段一致性警告：各段首行风格总纲不一致。"
                       "多段分镜应使用相同的风格/色调总纲句以确保视觉连贯。"
        })

    # 2. 光影结构一致：检测包含「光影」或「Lighting」的行
    def extract_lighting(text):
        for line in text.strip().split('\n'):
            if '光影' in line or 'Lighting' in line or 'lighting' in line:
                return line.strip()
        return ""

    lighting_lines = [extract_lighting(seg) for seg in segments]
    non_empty = [l for l in lighting_lines if l]
    if non_empty and len(set(non_empty)) > 1:
        cross_results.append({
            "level": "warning",
            "code": "INCONSISTENT_LIGHTING",
            "message": "跨段一致性警告：各段光影描述不一致。"
                       "多段分镜应保持统一的光影三层结构以确保拼接无缝。"
        })

    # 3. 禁止项一致：检测包含「禁止」或「Negative」的行
    def extract_negative(text):
        for line in text.strip().split('\n'):
            if '禁止' in line or 'Negative' in line or 'negative' in line:
                return line.strip()
        return ""

    neg_lines = [extract_negative(seg) for seg in segments]
    non_empty_neg = [n for n in neg_lines if n]
    if non_empty_neg and len(set(non_empty_neg)) > 1:
        cross_results.append({
            "level": "warning",
            "code": "INCONSISTENT_NEGATIVE",
            "message": "跨段一致性警告：各段禁止项声明不一致。"
                       "多段分镜应使用统一的禁止项。"
        })

    if not cross_results:
        cross_results.append({
            "level": "pass",
            "code": "CROSS_SEGMENT_OK",
            "message": f"跨段一致性检查通过：{len(segments)} 段风格/光影/禁止项一致。"
        })

    all_passed = all(r["passed"] for r in per_segment)
    cross_errors = [r for r in cross_results if r["level"] == "error"]
    overall_passed = all_passed and len(cross_errors) == 0

    return {
        "language": lang,
        "segment_count": len(segments),
        "passed": overall_passed,
        "per_segment": per_segment,
        "cross_segment": cross_results
    }


def validate_prompt(text, lang=None):
    """执行完整校验流程"""
    if lang is None:
        lang = detect_language(text)

    all_results = []
    all_results.extend(check_length(text, lang))
    all_results.extend(check_time_slices(text))
    all_results.extend(check_camera_language(text))
    all_results.extend(check_cgi_words(text))
    all_results.extend(check_asset_refs(text))
    all_results.extend(check_conflict(text))
    all_results.extend(check_ambiguous_terms(text, lang))

    errors = [r for r in all_results if r["level"] == "error"]
    warnings = [r for r in all_results if r["level"] == "warning"]
    passed = [r for r in all_results if r["level"] == "pass"]
    infos = [r for r in all_results if r["level"] == "info"]

    return {
        "language": lang,
        "passed": len(errors) == 0,
        "summary": {
            "errors": len(errors),
            "warnings": len(warnings),
            "passed": len(passed),
            "infos": len(infos)
        },
        "results": all_results
    }


def format_report(validation):
    """格式化输出校验报告"""
    lines = []
    lines.append("")
    lines.append("=" * 50)
    lines.append("  Seedance 2.0 提示词审查报告")
    lines.append("=" * 50)
    lang = validation.get("language", "cn")
    lang_display = "中文 (Chinese)" if lang == "cn" else "English"
    lines.append(f"  语言: {lang_display}")
    lines.append("")

    icon_map = {
        "error": "❌",
        "warning": "⚠️ ",
        "pass": "✅",
        "info": "ℹ️ "
    }

    for r in validation["results"]:
        icon = icon_map.get(r["level"], "  ")
        lines.append(f"  {icon} [{r['code']}] {r['message']}")

    lines.append("")
    lines.append("-" * 50)
    s = validation["summary"]
    if validation["passed"]:
        lines.append(f"  结论: 审查通过 ✅ "
                     f"({s['passed']}项通过, {s['warnings']}项警告, {s['infos']}项提示)")
        lines.append("  可向用户交付最终提示词。")
    else:
        lines.append(f"  结论: 审查未通过 ❌ "
                     f"({s['errors']}项错误, {s['warnings']}项警告)")
        lines.append("  请根据上述错误重新精简并重写提示词，然后再次校验！")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Seedance 2.0 提示词校验工具"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", type=str, help="提示词文本内容")
    group.add_argument("--file", type=str, help="包含提示词的文件路径")

    parser.add_argument("--lang", type=str, choices=["cn", "en", "auto"],
                        default="auto",
                        help="提示词语言 (auto=自动检测, cn=中文, en=英文)")
    parser.add_argument("--json", action="store_true",
                        help="以 JSON 格式输出结果")

    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        text = args.text

    lang = None if args.lang == "auto" else args.lang
    validation = validate_prompt(text, lang=lang)

    if args.json:
        print(json.dumps(validation, ensure_ascii=False, indent=2))
    else:
        print(format_report(validation))

    raise SystemExit(0 if validation["passed"] else 1)


if __name__ == "__main__":
    main()
