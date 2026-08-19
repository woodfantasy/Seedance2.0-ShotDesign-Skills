[English](README.md) | [中文](README.zh-CN.md) | 日本語 | [한국어](README.ko.md) | [Español](README.es.md) | [Português](README.pt.md) | [Français](README.fr.md)

<p align="center"><img src="assets/logo.svg" width="128" height="128" alt="Seedance Shot Design Logo"></p>

<h1 align="center">Seedance 2.5 Shot Design</h1>

<p align="center"><strong>Jimeng Seedance 2.5 向けのモード認識型演出・プロンプト・延長・編集スキル</strong></p>

<p align="center">
  <img src="https://img.shields.io/badge/version-3.1.0-blue.svg" alt="Version 3.1.0">
  <img src="https://img.shields.io/badge/license-MIT--0-green.svg" alt="MIT-0">
  <img src="https://img.shields.io/badge/platform-Seedance_2.5-purple.svg" alt="Seedance 2.5">
</p>

Seedance Shot Design は、曖昧なアイデアや承認済みの素材を、Seedance 2.5 でそのまま使える制作計画とプロンプトに変換します。3.0 は、30秒標準生成、30〜180秒の超長尺、マルチモーダル参照、動画延長、精密編集、制作ワークフローに対応する全面改訂です。

## 3.0 の主な変更

| 領域 | Seedance 2.5 対応 |
|---|---|
| 標準生成 | 4〜30秒を一回で生成。ちょうど30秒は原則として標準モード |
| 超長尺 | 30〜180秒を continuity bible、幕、シーケンス、結末で制御 |
| 動画延長 | 元動画30秒以下、追加4〜30秒、完成60秒以下。指示は追加部分だけに適用 |
| 素材 | 画像30枚、動画10本、音声10本まで。種類別の時間・ファイル条件を検証 |
| 編集 | スマート編集、注釈ベース編集、局所置換・削除、視点再構築 |
| 音声 | 音声のみの参照、声質、多言語台詞、台詞を残したBGM削除 |
| 制作 | クリエイティブ転送、グリーンバック、粗/精細ホワイトモデル、シームレス遷移、絵コンテ |

旧仕様の「15秒超を強制分割」「9/3/3/12素材上限」「500文字上限」「非中国語を英語へ強制」「未確認の1080p/CLI主張」は削除しました。

## 3.1 の新機能

| 領域 | 内容 |
|---|---|
| 初回利用ガイド | 初回起動時にクイックスタート、最小入力テンプレート、代表例を自動表示 |
| 公式サンプル | ByteDance / Dreamina 公式ドキュメントからの構造参照例を収録 |
| ワンクリックインストール | `npx --yes skills@latest add` によるインストールに対応 |
| 精密タイムライン | 正確な30秒動画で秒単位のタイムライン制御が必要な場合の専用ルーティング |

## 対応モード

- `standard`: 全能参考 / 首尾フレーム、4〜30秒
- `ultra_long`: 超長動画、30〜180秒
- `extension`: 動画延長
- `smart_edit` / `advanced_edit`: スマート / 高度動画編集
- `viewpoint`: 空間視点変更
- `bgm`: 音声トラック編集
- `creative_transfer`: クリエイティブ転送
- `green_screen`: グリーンバック編集
- `rough_white_model` / `fine_white_model`: 粗 / 精細ホワイトモデル
- `seamless_transition`: シームレス動画遷移
- `storyboard`: マルチパネル絵コンテ

## ワークフロー

1. 目的、尺、アスペクト比、素材、音声を整理します。
2. 一つの主モードを選びます。
3. 必要なリファレンスだけを読み込みます。
4. 各素材に役割、適用範囲、除外項目を割り当てます。
5. 時間、因果関係、連続性を設計します。
6. モード別に検証し、自己完結したプロンプトを返します。

## インストール

### 推奨：ワンクリックインストール

```bash
npx --yes skills@latest add woodfantasy/Seedance-ShotDesign-Skills -g -y
```

### 手動インストール

フォルダーを利用するエージェントのスキルディレクトリに配置します。

```text
.claude/skills/seedance-shot-design/
~/.codex/skills/seedance-shot-design/
.cursor/skills/seedance-shot-design/
```

明示的な呼び出し例：

```text
Use $seedance-shot-design to create a continuous 30-second vertical suspense film.
```

## バリデーター

```bash
python3 scripts/validate_prompt.py --mode standard --duration 30 --resolution 720p --prompt-file prompt.txt
python3 -m unittest scripts/test_validate.py
```

延長では `--duration` は追加秒数です。`--source-duration` で元動画の長さを指定すると、最終60秒上限も検証できます。

## 注意事項

- 提供された使用マニュアルで明記されている出力は 480p と 720p です。`720P+` はUIラベルであり、独立した1080p設定とは確認されていません。
- 安定性の推奨値とハード上限を区別します。
- `@图片1`、`@视频1`、`@音频1` など、ユーザー画面の素材トークンをそのまま保持します。
- このスキルはプロンプトを設計・検証しますが、生成ジョブの送信やクレジット消費は行いません。

## ライセンス

[MIT-0](LICENSE)
