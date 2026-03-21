#!/usr/bin/env python3
"""
validate_prompt.py 的测试用例
运行: python -m pytest scripts/test_validate.py -v
"""

import os
import unittest
import importlib.util

# 使用 importlib 加载同目录模块（避免 sys.path 操作）
_spec = importlib.util.spec_from_file_location(
    "validate_prompt",
    os.path.join(os.path.dirname(__file__), "validate_prompt.py")
)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

check_length = _module.check_length
check_time_slices = _module.check_time_slices
check_camera_language = _module.check_camera_language
check_cgi_words = _module.check_cgi_words
check_asset_refs = _module.check_asset_refs
check_conflict = _module.check_conflict
validate_prompt = _module.validate_prompt
_detect_declared_duration = _module._detect_declared_duration
detect_language = _module.detect_language
check_ambiguous_terms = _module.check_ambiguous_terms
validate_multi_segment = _module.validate_multi_segment


class TestCheckLength(unittest.TestCase):
    """字数限制校验"""

    def test_cn_within_limit(self):
        text = "赛博朋克城市夜景" * 10  # 80字符
        results = check_length(text)
        self.assertEqual(results[0]["level"], "pass")

    def test_cn_exceed_limit(self):
        text = "赛" * 501
        results = check_length(text)
        self.assertEqual(results[0]["level"], "error")
        self.assertEqual(results[0]["code"], "LENGTH_EXCEEDED")

    def test_cn_near_limit(self):
        text = "赛" * 430  # 86%
        results = check_length(text)
        self.assertEqual(results[0]["level"], "warning")
        self.assertEqual(results[0]["code"], "LENGTH_NEAR_LIMIT")

    def test_en_within_limit(self):
        text = "word " * 100  # 100 words
        results = check_length(text, lang="en")
        self.assertEqual(results[0]["level"], "pass")

    def test_en_exceed_limit(self):
        text = "word " * 1001  # 1001 words
        results = check_length(text, lang="en")
        self.assertEqual(results[0]["level"], "error")
        self.assertEqual(results[0]["code"], "LENGTH_EXCEEDED")



class TestCheckTimeSlices(unittest.TestCase):
    """时序切片校验"""

    def test_no_time_slices(self):
        results = check_time_slices("一个女人在街上走路，镜头跟拍")
        self.assertTrue(any(r["code"] == "NO_TIME_SLICES" for r in results))

    def test_valid_time_slices_cn(self):
        text = "0-3秒：画面A；3-8秒：画面B；8-12秒：画面C"
        results = check_time_slices(text)
        self.assertTrue(any(r["code"] == "TIME_SLICES_OK" for r in results))

    def test_valid_time_slices_en(self):
        text = "[0-3s] Scene A; [3-8s] Scene B; [8-12s] Scene C"
        results = check_time_slices(text)
        self.assertTrue(any(r["code"] == "TIME_SLICES_OK" for r in results))

    def test_overlapping_time_slices(self):
        text = "0-5秒：画面A；3-8秒：画面B"
        results = check_time_slices(text)
        self.assertTrue(any(r["code"] == "TIME_OVERLAP" for r in results))

    def test_not_from_zero(self):
        text = "3-6秒：画面A；8-10秒：画面B"
        results = check_time_slices(text)
        self.assertTrue(any(r["code"] == "TIME_NOT_FROM_ZERO" for r in results))


class TestCheckCameraLanguage(unittest.TestCase):
    """运镜专业度检测"""

    def test_has_camera_cn(self):
        text = "航拍俯拍城市，Dolly In推进，特写面部表情"
        results = check_camera_language(text)
        self.assertEqual(results[0]["level"], "pass")

    def test_has_camera_en(self):
        text = "Tracking shot through the corridor, close-up on face, dolly in"
        results = check_camera_language(text)
        self.assertEqual(results[0]["level"], "pass")

    def test_no_camera(self):
        text = "一个女人穿着红色裙子在花园里散步，阳光明媚，花朵盛开"
        results = check_camera_language(text)
        self.assertEqual(results[0]["level"], "error")
        self.assertEqual(results[0]["code"], "NO_CAMERA_LANGUAGE")


class TestCheckCgiWords(unittest.TestCase):
    """AI塑料感废话检测"""

    def test_clean_text(self):
        text = "35mm胶片颗粒质感，自然皮肤纹理微瑕"
        results = check_cgi_words(text)
        self.assertTrue(any(r["code"] == "CGI_WORDS_CLEAN" for r in results))

    def test_has_cgi_words(self):
        text = "杰作级画质，超清晰，masterpiece"
        results = check_cgi_words(text)
        self.assertTrue(any(r["code"] == "BANNED_WORDS_DETECTED" for r in results))
        self.assertTrue(any(r["level"] == "error" for r in results))

    def test_soft_resolution(self):
        text = "8K超高清画面，配合UnrealEngine5渲染"
        results = check_cgi_words(text)
        self.assertTrue(any(r["code"] == "RESOLUTION_WORDS" for r in results))


class TestCheckAssetRefs(unittest.TestCase):
    """资产引用校验"""

    def test_no_refs(self):
        results = check_asset_refs("纯文本提示词，无任何引用")
        self.assertTrue(any(r["code"] == "NO_ASSET_REFS" for r in results))

    def test_valid_refs(self):
        text = "@图片1为首帧，参考@视频1的运镜，@音频1为配乐"
        results = check_asset_refs(text)
        self.assertTrue(any(r["code"] == "ASSET_REFS_OK" for r in results))

    def test_image_exceeded(self):
        refs = " ".join([f"@图片{i}" for i in range(1, 11)])
        results = check_asset_refs(refs)
        self.assertTrue(any(r["code"] == "IMAGE_REF_EXCEEDED" for r in results))

    def test_video_exceeded(self):
        refs = "@视频1 @视频2 @视频3 @视频4"
        results = check_asset_refs(refs)
        self.assertTrue(any(r["code"] == "VIDEO_REF_EXCEEDED" for r in results))

    def test_total_exceeded(self):
        refs = " ".join([f"@图片{i}" for i in range(1, 10)])
        refs += " @视频1 @视频2 @视频3 @音频1"
        results = check_asset_refs(refs)
        self.assertTrue(any(r["code"] == "TOTAL_REF_EXCEEDED" for r in results))


class TestCheckConflict(unittest.TestCase):
    """逻辑冲突检测"""

    def test_no_conflict(self):
        text = "0-3秒：Fast Tracking追逐；3-8秒：Slow Motion慢镜头回顾"
        results = check_conflict(text)
        self.assertTrue(any(r["code"] == "NO_CONFLICT" for r in results))

    def test_speed_conflict(self):
        text = "快速追逐同时慢动作展示细节"
        results = check_conflict(text)
        self.assertTrue(any(r["code"] == "MOTION_CONFLICT" for r in results))

    def test_direction_conflict(self):
        text = "Dolly In推进同时Pull Out拉远"
        results = check_conflict(text)
        self.assertTrue(any(r["code"] == "MOTION_CONFLICT" for r in results))

    def test_optical_conflict_wide_bokeh(self):
        """14mm超广角 + 浅景深虚化 = 光学冲突"""
        text = "14mm ultra-wide拍摄，背景浅景深虚化散景"
        results = check_conflict(text)
        self.assertTrue(any(r["code"] == "OPTICAL_CONFLICT" for r in results))

    def test_optical_conflict_handheld_symmetry(self):
        """手持晃动 + 绝对对称 = 构图冲突"""
        text = "手持微晃拍摄，绝对对称构图"
        results = check_conflict(text)
        self.assertTrue(any(r["code"] == "OPTICAL_CONFLICT" for r in results))

    def test_style_conflict_imax_vhs(self):
        """IMAX清晰 + VHS降解 = 品质冲突"""
        text = "IMAX 65mm清晰画质，VHS录像带质感"
        results = check_conflict(text)
        self.assertTrue(any(r["code"] == "STYLE_CONFLICT" for r in results))

    def test_style_conflict_film_digital(self):
        """胶片颗粒 + 锐利数码 = 品质冲突"""
        text = "35mm胶片颗粒质感，锐利数码电商质感"
        results = check_conflict(text)
        self.assertTrue(any(r["code"] == "STYLE_CONFLICT" for r in results))

    def test_style_conflict_ink_ue5(self):
        """水墨 + UE5光追 = 风格冲突"""
        text = "水墨宣纸笔触，unreal engine光追渲染"
        results = check_conflict(text)
        self.assertTrue(any(r["code"] == "STYLE_CONFLICT" for r in results))

    def test_no_style_conflict(self):
        """正常提示词无冲突"""
        text = "35mm胶片颗粒，自然光，手持微晃"
        results = check_conflict(text)
        self.assertTrue(any(r["code"] == "NO_CONFLICT" for r in results))

    def test_style_conflict_celshade_pbr(self):
        """三渲二/Cel-Shade + 写实PBR材质 = 风格冲突"""
        text = "三渲二卡通渲染，写实皮肤纹理with visible pores and subsurface scattering"
        results = check_conflict(text)
        self.assertTrue(any(r["code"] == "STYLE_CONFLICT" for r in results))

    def test_no_conflict_celshade_alone(self):
        """纯三渲二提示词，无写实材质 = 无冲突"""
        text = ("3D Cel-Shaded Toon渲染，Anime风格硬边阴影，"
                "粗描边轮廓线，高饱和角色色盘")
        results = check_conflict(text)
        self.assertTrue(any(r["code"] == "NO_CONFLICT" for r in results))

    def test_style_conflict_slowmo_speedramp(self):
        """Slow Motion + Speed Ramp = 速度冲突"""
        text = "慢镜头特写，Speed Ramp变速加速"
        results = check_conflict(text)
        self.assertTrue(any(r["code"] == "STYLE_CONFLICT" for r in results))


class TestValidatePromptEndToEnd(unittest.TestCase):
    """端到端校验"""

    def test_good_prompt_passes(self):
        prompt = (
            "15秒赛博朋克暴雨追逐，UnrealEngine5渲染，"
            "0-3秒：Aerial航拍俯冲，摩天楼群刺破铅灰雨云；"
            "3-7秒：Low Angle仰拍慢镜头，主角从水花中起身；"
            "7-11秒：微距特写面部雨水滚落，Handheld抖动；"
            "11-15秒：Slow Crane Up仰拍。"
        )
        result = validate_prompt(prompt)
        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["errors"], 0)

    def test_bad_prompt_fails(self):
        prompt = "赛" * 501  # 超长 + 无运镜
        result = validate_prompt(prompt)
        self.assertFalse(result["passed"])
        self.assertGreater(result["summary"]["errors"], 0)

    def test_minimal_prompt_warnings(self):
        prompt = "一个女人走在路上"
        result = validate_prompt(prompt)
        # 会通过（无error），但有warning
        self.assertFalse(result["passed"])  # 缺少运镜会报error


class TestDurationAwareSlices(unittest.TestCase):
    """时长感知的时间切片检测"""

    def test_long_video_no_slices_is_error(self):
        """10秒视频无时间切片 = error"""
        text = "10秒赛博朋克夜景，主角在雨中奔跑"
        results = check_time_slices(text)
        self.assertTrue(any(r["code"] == "LONG_VIDEO_NO_SLICES" for r in results))
        self.assertTrue(any(r["level"] == "error" for r in results))

    def test_short_video_no_slices_is_warning(self):
        """5秒视频无时间切片 = warning"""
        text = "5秒微距拍摄，水滴碰撞"
        results = check_time_slices(text)
        self.assertTrue(any(r["code"] == "NO_TIME_SLICES" for r in results))
        self.assertTrue(any(r["level"] == "warning" for r in results))

    def test_duration_mismatch(self):
        """声明15秒但切片只到10秒"""
        text = "15秒赛博朋克夜景，0-3秒：画面A；3-7秒：画面B；7-10秒：画面C"
        results = check_time_slices(text)
        self.assertTrue(any(r["code"] == "DURATION_MISMATCH" for r in results))

    def test_detect_declared_duration(self):
        self.assertEqual(_detect_declared_duration("10秒赛博朋克"), 10)
        self.assertEqual(_detect_declared_duration("15秒大片"), 15)
        self.assertEqual(_detect_declared_duration("一只猫在睡觉"), 0)


class TestDetectLanguage(unittest.TestCase):
    """Language auto-detection"""

    def test_chinese_text(self):
        self.assertEqual(detect_language("赛博朋克城市夜景，航拍俯冲"), "cn")

    def test_english_text(self):
        self.assertEqual(detect_language("Cyberpunk city night, aerial dive"), "en")

    def test_mixed_mostly_chinese(self):
        self.assertEqual(detect_language("赛博朋克城市夜景Aerial航拍"), "cn")

    def test_mixed_mostly_english(self):
        self.assertEqual(detect_language("Cyberpunk night scene, Dolly In push, 特写"), "en")


class TestEnglishPromptEndToEnd(unittest.TestCase):
    """English prompt end-to-end"""

    def test_good_english_prompt_passes(self):
        prompt = (
            "15s cyberpunk rain chase, UE5 rendering. "
            "0-3s: Aerial drone shot dive over skyscrapers. "
            "3-7s: Low angle shot slow-motion, hero rising. "
            "7-11s: ECU face detail, rain rolling. "
            "11-15s: Slow crane shot up, silhouette."
        )
        result = validate_prompt(prompt, lang="en")
        self.assertTrue(result["passed"])
        self.assertEqual(result["language"], "en")


class TestCheckAmbiguousTerms(unittest.TestCase):
    """审核风险裸英文运镜词检测"""

    def test_bare_dolly_in_cn_warns(self):
        """中文提示词中裸写 Dolly 应触发警告"""
        text = "Dolly穿过寺门进入庭院"
        results = check_ambiguous_terms(text, lang="cn")
        self.assertTrue(any(r["code"] == "AMBIGUOUS_CAMERA_TERM" for r in results))

    def test_dolly_tracking_shot_en_passes(self):
        """英文提示词中 dolly tracking shot 完整短语应通过"""
        text = "dolly tracking shot slowly pushing forward"
        results = check_ambiguous_terms(text, lang="en")
        self.assertTrue(any(r["code"] == "NO_AMBIGUOUS_TERMS" for r in results))

    def test_chinese_camera_words_pass(self):
        """纯中文运镜词应通过"""
        text = "航拍缓慢推进，推轨穿过寺门，摇臂升降揭示仙境"
        results = check_ambiguous_terms(text, lang="cn")
        self.assertTrue(any(r["code"] == "NO_AMBIGUOUS_TERMS" for r in results))

    def test_bare_aerial_in_en_warns(self):
        """英文提示词中裸写 Aerial 无后缀应触发警告"""
        text = "Aerial slow descent through clouds"
        results = check_ambiguous_terms(text, lang="en")
        self.assertTrue(any(r["code"] == "AMBIGUOUS_CAMERA_TERM" for r in results))

    def test_aerial_drone_shot_en_passes(self):
        """英文 aerial drone shot 完整短语应通过"""
        text = "aerial drone shot over the city"
        results = check_ambiguous_terms(text, lang="en")
        self.assertTrue(any(r["code"] == "NO_AMBIGUOUS_TERMS" for r in results))


class TestMultiSegmentValidation(unittest.TestCase):
    """多段分镜校验"""

    STYLE_LINE = "15秒落日沙漠武术，写实电影质感，暗金暖色调，苍芒孤寂氛围。"
    LIGHTING = "光影：落日低角度逆光暗金+沙面散射暖光，热浪折射柔化轮廓，暗金暖底调。"
    NEGATIVE = "禁止：任何文字、字幕、LOGO或水印"

    def _make_segment(self, style=None, lighting=None, negative=None):
        s = style or self.STYLE_LINE
        l = lighting or self.LIGHTING
        n = negative or self.NEGATIVE
        return (
            f"{s}\n"
            f"0-3秒：航拍缓慢下降，广袤沙漠延伸至地平线。\n"
            f"3-7秒：推轨缓推至中景，武者双手握棍起势。\n"
            f"7-11秒：侧面跟拍，棍棒横扫掀起扩散。\n"
            f"11-15秒：缓慢推进背影，画面趋于静止。\n"
            f"{l}\n"
            f"音效：风卷沙面、棍棒破空。\n"
            f"{n}"
        )

    def test_consistent_segments_pass(self):
        """风格/光影/禁止项一致的多段应通过跨段检查"""
        segments = [self._make_segment() for _ in range(4)]
        result = validate_multi_segment(segments, lang="cn")
        self.assertEqual(result["segment_count"], 4)
        self.assertTrue(any(
            r["code"] == "CROSS_SEGMENT_OK" for r in result["cross_segment"]
        ))

    def test_inconsistent_style_warns(self):
        """风格总纲不一致应触发警告"""
        seg1 = self._make_segment(style="15秒落日沙漠武术，写实电影质感，暗金暖色调。")
        seg2 = self._make_segment(style="15秒赛博朋克夜景，霾虹灯光，冷蓝色调。")
        result = validate_multi_segment([seg1, seg2], lang="cn")
        self.assertTrue(any(
            r["code"] == "INCONSISTENT_STYLE_ANCHOR" for r in result["cross_segment"]
        ))

    def test_inconsistent_lighting_warns(self):
        """光影不一致应触发警告"""
        seg1 = self._make_segment()
        seg2 = self._make_segment(lighting="光影：霾虹冷光+湿气折射，冷蓝绿色调。")
        result = validate_multi_segment([seg1, seg2], lang="cn")
        self.assertTrue(any(
            r["code"] == "INCONSISTENT_LIGHTING" for r in result["cross_segment"]
        ))

    def test_inconsistent_negative_warns(self):
        """禁止项不一致应触发警告"""
        seg1 = self._make_segment()
        seg2 = self._make_segment(negative="禁止：任何文字")
        result = validate_multi_segment([seg1, seg2], lang="cn")
        self.assertTrue(any(
            r["code"] == "INCONSISTENT_NEGATIVE" for r in result["cross_segment"]
        ))


if __name__ == "__main__":
    unittest.main()
