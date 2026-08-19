[English](README.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | 한국어 | [Español](README.es.md) | [Português](README.pt.md) | [Français](README.fr.md)

<p align="center"><img src="assets/logo.svg" width="128" height="128" alt="Seedance Shot Design Logo"></p>

<h1 align="center">Seedance 2.5 Shot Design</h1>

<p align="center"><strong>Jimeng Seedance 2.5용 모드 인식 연출·프롬프트·연장·편집 스킬</strong></p>

<p align="center">
  <img src="https://img.shields.io/badge/version-3.1.0-blue.svg" alt="Version 3.1.0">
  <img src="https://img.shields.io/badge/license-MIT--0-green.svg" alt="MIT-0">
  <img src="https://img.shields.io/badge/platform-Seedance_2.5-purple.svg" alt="Seedance 2.5">
</p>

Seedance Shot Design은 아이디어나 승인된 원본 영상을 Seedance 2.5에서 바로 사용할 수 있는 제작 계획과 프롬프트로 바꿉니다. 3.0은 30초 표준 생성, 30–180초 초장편, 멀티모달 참조, 영상 연장, 정밀 편집, 산업형 워크플로를 위한 전면 개편입니다.

## 3.0 핵심 변경

| 영역 | Seedance 2.5 대응 |
|---|---|
| 표준 생성 | 4–30초 연속 생성. 정확히 30초면 기본적으로 표준 모드 사용 |
| 초장편 | continuity bible, 막, 시퀀스, 결말로 30–180초 제어 |
| 영상 연장 | 원본 ≤30초, 추가 4–30초, 최종 ≤60초. 프롬프트는 추가 구간에만 적용 |
| 에셋 | 이미지 30개, 영상 10개, 오디오 10개와 유형별 시간/파일 조건 |
| 편집 | 스마트 편집, 주석 기반 고급 편집, 국소 교체/삭제, 시점 재구성 |
| 오디오 | 오디오 전용 참조, 음색, 다국어 대사, 음성/환경음을 보존하는 BGM 제거 |
| 제작 | 크리에이티브 전이, 그린스크린, 거친/정밀 화이트 모델, 심리스 전환, 멀티패널 스토리보드 |

15초 초과 강제 분할, 9/3/3/12 혼합 에셋 제한, 보편적 500자 제한, 비중국어의 영어 강제 변환, 확인되지 않은 1080p 및 CLI 주장은 제거했습니다.

## 3.1 새로운 기능

| 영역 | 내용 |
|---|---|
| 첫 사용 가이드 | 첫 호출 시 빠른 시작, 최소 입력 템플릿, 대표 예시 자동 표시 |
| 공식 예시 | ByteDance / Dreamina 공식 문서의 구조 참조 예시 수록 |
| 원클릭 설치 | `npx --yes skills@latest add` 설치 지원 |
| 정밀 타임라인 | 정확히 30초 영상에서 초 단위 타임라인 제어가 필요한 경우 전용 라우팅 |

## 지원 모드

- `standard`: 전능 참조 / 첫·끝 프레임, 4–30초
- `ultra_long`: 초장편, 30–180초
- `extension`: 영상 연장
- `smart_edit` / `advanced_edit`: 스마트 / 고급 영상 편집
- `viewpoint`: 공간 시점 변경
- `bgm`: 오디오 트랙 편집
- `creative_transfer`: 크리에이티브 전이
- `green_screen`: 그린스크린 편집
- `rough_white_model` / `fine_white_model`: 거친 / 정밀 화이트 모델
- `seamless_transition`: 심리스 영상 전환
- `storyboard`: 멀티패널 스토리보드

## 워크플로

1. 목표, 길이, 화면비, 에셋, 오디오 요구를 추출합니다.
2. 하나의 주 모드를 선택합니다.
3. 필요한 참고 문서만 불러옵니다.
4. 각 에셋에 역할, 범위, 제외 항목을 지정합니다.
5. 시간, 행동 인과, 연속성 상태를 설계합니다.
6. 모드별 검증 후 완전한 복사용 프롬프트를 제공합니다.

## 설치

### 추천: 원클릭 설치

```bash
npx --yes skills@latest add woodfantasy/Seedance-ShotDesign-Skills -g -y
```

### 수동 설치

폴더를 사용하는 에이전트의 스킬 디렉터리에 배치하세요.

```text
.claude/skills/seedance-shot-design/
~/.codex/skills/seedance-shot-design/
.cursor/skills/seedance-shot-design/
```

호출 예시:

```text
Use $seedance-shot-design to design a continuous 30-second vertical suspense film.
```

## 검증기

```bash
python3 scripts/validate_prompt.py --mode standard --duration 30 --resolution 720p --prompt-file prompt.txt
python3 -m unittest scripts/test_validate.py
```

연장 모드에서 `--duration`은 추가 길이입니다. `--source-duration`을 함께 지정하면 최종 60초 제한도 검사합니다.

## 플랫폼 참고

- 제공된 매뉴얼에 명시된 출력은 480p와 720p입니다. `720P+`는 UI 라벨이며 독립된 1080p 설정으로 확인되지 않았습니다.
- 안정성 권고와 하드 제한을 구분합니다.
- `@图片1`, `@视频1`, `@音频1`처럼 사용자 인터페이스에 보이는 에셋 토큰을 그대로 유지합니다.
- 이 스킬은 프롬프트를 설계·검증하며 생성 제출이나 크레딧 소비를 하지 않습니다.

## 라이선스

[MIT-0](LICENSE)
