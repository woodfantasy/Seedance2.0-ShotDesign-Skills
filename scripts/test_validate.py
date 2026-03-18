#!/usr/bin/env python3
"""
validate_prompt.py 的测试用例
运行: python -m pytest scripts/test_validate.py -v
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.dirname(__file__))
from validate_prompt import (
    detect_language, check_length, check_time_slices,
    check_camera_language, check_cgi_words, check_asset_refs,
    check_conflict, validate_prompt
)


class TestDetectLanguage(unittest.TestCase):
    """语言自动检测"""

    def test_chinese_text(self):
        self.assertEqual(detect_language("一个穿红色衣服的女子在雨中奔跑"), "cn")

    def test_english_text(self):
        self.assertEqual(detect_language("A woman in red runs through the rain"), "en")

    def test_mixed_mostly_chinese(self):
        self.assertEqual(detect_language("Epic航拍Dolly In，城市夜景霓虹灯漫射"), "cn")

    def test_empty_text(self):
        self.assertEqual(detect_language(""), "cn")


class TestCheckLength(unittest.TestCase):
    """字数/词数限制校验"""

    def test_cn_within_limit(self):
        text = "赛博朋克城市夜景" * 10  # 80字符
        results = check_length(text, "cn")
        self.assertEqual(results[0]["level"], "pass")

    def test_cn_exceed_limit(self):
        text = "赛" * 501
        results = check_length(text, "cn")
        self.assertEqual(results[0]["level"], "error")
        self.assertEqual(results[0]["code"], "LENGTH_EXCEEDED")

    def test_cn_near_limit(self):
        text = "赛" * 430  # 86%
        results = check_length(text, "cn")
        self.assertEqual(results[0]["level"], "warning")
        self.assertEqual(results[0]["code"], "LENGTH_NEAR_LIMIT")

    def test_en_within_limit(self):
        text = " ".join(["word"] * 500)
        results = check_length(text, "en")
        self.assertEqual(results[0]["level"], "pass")

    def test_en_exceed_limit(self):
        text = " ".join(["word"] * 1001)
        results = check_length(text, "en")
        self.assertEqual(results[0]["level"], "error")


class TestCheckTimeSlices(unittest.TestCase):
    """时序切片校验"""

    def test_no_time_slices(self):
        results = check_time_slices("一个女人在街上走路，镜头跟拍")
        self.assertTrue(any(r["code"] == "NO_TIME_SLICES" for r in results))

    def test_valid_time_slices_cn(self):
        text = "0-3秒：画面A；4-8秒：画面B；9-12秒：画面C"
        results = check_time_slices(text)
        self.assertTrue(any(r["code"] == "TIME_SLICES_OK" for r in results))

    def test_valid_time_slices_en(self):
        text = "[0-3s] Scene A; [4-8s] Scene B; [9-12s] Scene C"
        results = check_time_slices(text)
        self.assertTrue(any(r["code"] == "TIME_SLICES_OK" for r in results))

    def test_overlapping_time_slices(self):
        text = "0-5秒：画面A；3-8秒：画面B"
        results = check_time_slices(text)
        self.assertTrue(any(r["code"] == "TIME_OVERLAP" for r in results))

    def test_not_from_zero(self):
        text = "3-6秒：画面A；7-10秒：画面B"
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
        self.assertTrue(any(r["code"] == "CGI_WORDS_DETECTED" for r in results))

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
        text = "0-3秒：Fast Tracking追逐；4-8秒：Slow Motion慢镜头回顾"
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


class TestValidatePromptEndToEnd(unittest.TestCase):
    """端到端校验"""

    def test_good_prompt_passes(self):
        prompt = (
            "15秒赛博朋克暴雨追逐，UnrealEngine5渲染，"
            "0-3秒：Aerial航拍俯冲，摩天楼群刺破铅灰雨云；"
            "4-7秒：Low Angle仰拍慢镜头，主角从水花中起身；"
            "8-11秒：微距特写面部雨水滚落，Handheld抖动；"
            "12-15秒：Slow Crane Up仰拍。"
        )
        result = validate_prompt(prompt, "cn")
        self.assertTrue(result["passed"])
        self.assertEqual(result["summary"]["errors"], 0)

    def test_bad_prompt_fails(self):
        prompt = "赛" * 501  # 超长 + 无运镜
        result = validate_prompt(prompt, "cn")
        self.assertFalse(result["passed"])
        self.assertGreater(result["summary"]["errors"], 0)

    def test_minimal_prompt_warnings(self):
        prompt = "一个女人走在路上"
        result = validate_prompt(prompt, "cn")
        # 会通过（无error），但有warning
        self.assertFalse(result["passed"])  # 缺少运镜会报error


class TestAutoLangDetection(unittest.TestCase):
    """自动语言检测集成测试"""

    def test_auto_cn(self):
        result = validate_prompt("航拍城市夜景，Dolly In推进", lang="auto")
        self.assertEqual(result["language"], "cn")

    def test_auto_en(self):
        result = validate_prompt(
            "Aerial city night view, Dolly In push forward", lang="auto"
        )
        self.assertEqual(result["language"], "en")


if __name__ == "__main__":
    unittest.main()
