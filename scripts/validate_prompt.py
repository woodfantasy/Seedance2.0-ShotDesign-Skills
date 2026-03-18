#!/usr/bin/env python3
"""
Seedance 2.0 提示词工业级校验脚本
用于在 Agent 生成提示词后进行自动化质量审查。

用法:
    python scripts/validate_prompt.py --text "你的提示词内容"
    python scripts/validate_prompt.py --text "your prompt" --lang en
    python scripts/validate_prompt.py --file prompt.txt
"""

import argparse
import re
import sys
import json


def detect_language(text):
    """自动检测提示词语言（中文/英文）"""
    chinese_chars = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
    total_chars = len(text.strip())
    if total_chars == 0:
        return "cn"
    ratio = chinese_chars / total_chars
    return "cn" if ratio > 0.15 else "en"


def check_length(text, lang):
    """检查提示词长度是否合规"""
    results = []
    if lang == "cn":
        length = len(text)
        max_len = 500
        unit = "字符"
    else:
        length = len(text.split())
        max_len = 1000
        unit = "词"

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


def check_time_slices(text):
    """检查时序切片逻辑"""
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

    if not all_slices:
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
    """检查是否包含易产生 AI 塑料感的废话"""
    results = []
    cgi_words = {
        "cn": ["超清晰", "杰作", "高画质", "超高画质", "超精细"],
        "en": ["masterpiece", "ultra-sharp", "best quality",
               "extremely detailed", "hyper-realistic"]
    }
    # 注意：4k/8k 在品质锚定语境下可能有意义，仅作警告
    soft_warn = ["4k", "8k", "4K", "8K"]

    found_hard = []
    found_soft = []
    text_lower = text.lower()

    for word_list in cgi_words.values():
        for w in word_list:
            if w.lower() in text_lower:
                found_hard.append(w)

    for w in soft_warn:
        if w in text:
            found_soft.append(w)

    if found_hard:
        results.append({
            "level": "warning",
            "code": "CGI_WORDS_DETECTED",
            "message": f"检测到易产生'AI塑料感'的废话词汇：{', '.join(found_hard)}。"
                       f"建议替换为物理材质词（如：35mm胶片颗粒、自然皮肤纹理微瑕）。"
        })
    if found_soft:
        results.append({
            "level": "info",
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
    """检查是否存在逻辑冲突"""
    results = []
    conflict_pairs = [
        (["快速", "高速", "急速", "fast", "rapid"], ["慢动作", "slow motion", "慢镜头", "缓慢"]),
        (["推进", "push in", "dolly in", "zoom in"], ["拉远", "pull out", "dolly out", "zoom out"]),
    ]

    text_lower = text.lower()
    # 按时间段分割检查
    segments = re.split(r'\d+-\d+[s秒][：:；;]?', text)

    for seg in segments:
        seg_lower = seg.lower()
        for fast_words, slow_words in conflict_pairs:
            has_fast = any(w in seg_lower for w in fast_words)
            has_slow = any(w in seg_lower for w in slow_words)
            if has_fast and has_slow:
                results.append({
                    "level": "warning",
                    "code": "MOTION_CONFLICT",
                    "message": f"同一段内可能存在运动冲突（快/慢或推/拉同时出现）。"
                               f"模型接收矛盾信号会导致画面撕裂或果冻效应。"
                })
                break

    if not results:
        results.append({
            "level": "pass",
            "code": "NO_CONFLICT",
            "message": "未检测到逻辑冲突。"
        })
    return results


def validate_prompt(text, lang=None):
    """执行完整校验流程"""
    if lang is None or lang == "auto":
        lang = detect_language(text)

    all_results = []
    all_results.extend(check_length(text, lang))
    all_results.extend(check_time_slices(text))
    all_results.extend(check_camera_language(text))
    all_results.extend(check_cgi_words(text))
    all_results.extend(check_asset_refs(text))
    all_results.extend(check_conflict(text))

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
    lines.append(f"  语言: {'中文' if validation['language'] == 'cn' else '英文'}")
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
    parser.add_argument("--lang", type=str, default="auto",
                        choices=["auto", "cn", "en"],
                        help="语言 (默认自动检测)")
    parser.add_argument("--json", action="store_true",
                        help="以 JSON 格式输出结果")

    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        text = args.text

    validation = validate_prompt(text, args.lang)

    if args.json:
        print(json.dumps(validation, ensure_ascii=False, indent=2))
    else:
        print(format_report(validation))

    sys.exit(0 if validation["passed"] else 1)


if __name__ == "__main__":
    main()
