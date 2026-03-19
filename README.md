# 🎬 Seedance2.0 Shot Design — 专业分镜提示词工程师

[![版本](https://img.shields.io/badge/version-1.1.0-blue.svg)]()
[![协议](https://img.shields.io/badge/license-MIT--0-green.svg)](LICENSE)
[![平台](https://img.shields.io/badge/platform-Seedance_2.0-purple.svg)]()

> 将你模糊的视频创意，一键转化为即梦 Seedance 2.0 可用的**电影级视频提示词**。

一个基于 [Agent Skills](https://agentskills.io) 规范构建的 Claude Skill，融合好莱坞顶级摄影美学与中国影视工业实践，旨在帮助创作者突破"好看但随机"的 AI 视频困境，实现**精准可控的视觉叙事**。

---

## ✨ 核心能力

| 能力 | 描述 |
|------|------|
| 🎯 **六要素精准组装** | 主体/动作/场景/光影/运镜/音效，结构化高转化公式 |
| 🎬 **专业运镜词典** | 3级运镜体系 + 14种焦段 + 6种焦点控制 + 7种物理机位，中英文对照 |
| 🎨 **28+导演与风格** | 芬奇/迪金斯/黑泽明/新海诚/诺兰/维伦纽瓦/王家卫/张艺谋/仙侠/二次元/小红书... |
| 💡 **光影三层结构** | 光源层→光行为层→色调层，告别"加个灯"的笼统描述 |
| 🔍 **Python硬性校验** | 字数/运镜/时序逻辑/废话检测/资产超限——比"建议"靠谱 |
| 📐 **时间戳分镜法** | `0-3秒/4-8秒/...` 精准时间轴控制，画面不再粘连 |
| 🛡️ **版权安全避障** | 三级渐进式IP回退策略，防止平台拦截 |
| 🔗 **超长视频拼接** | >15秒分段策略+清洁交接帧，实现无缝续接 |
| 🎵 **音效ASMR词库** | 物理拟声描述库，覆盖环境/动作/人声/音乐 |
| 📦 **16大场景模板** | 电商/仙侠/短剧/美食/MV/一镜到底/汽车/微距/自然/游戏PV/恐怖/旅行/宠物/变身/Loop |

---

## 🚀 快速开始

### 1. 安装 Skill

<details>
<summary><b>Claude Code</b></summary>

将 `seedance-shot-design/` 文件夹放入项目根目录的 `.claude/skills/` 下：

```bash
# 克隆到项目的 Skill 目录
git clone https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills.git .claude/skills/seedance-shot-design
```

Claude Code 会自动识别并加载该 Skill。
</details>

<details>
<summary><b>OpenClaw</b></summary>

在你绑定的 IM（如微信、飞书等）中，直接对 OpenClaw Agent 发一条消息：

```
请学习这个技能：https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills
```

Agent 会自动拉取并学会 Seedance Shot Design 技能，之后你就可以直接向它提需求了。
</details>

<details>
<summary><b>Codex</b></summary>

将 Skill 文件夹放入 Codex 的 agents 指令目录：

```bash
git clone https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills.git agents/skills/seedance-shot-design
```

在 Codex 对话中即可调用。
</details>

<details>
<summary><b>Cursor</b></summary>

将 Skill 文件夹放入项目根目录的 `.cursor/skills/` 下：

```bash
git clone https://github.com/woodfantasy/Seedance2.0-ShotDesign-Skills.git .cursor/skills/seedance-shot-design
```

Cursor Agent 模式下会自动读取该 Skill 指令。
</details>

### 2. 使用

直接对 Claude 说：

```
帮我写一段15秒的赛博朋克暴雨追逐的视频提示词
```

Skill 会自动激活并按 5 步工作流生成提示词：
1. **需求解析** — 确认时长/比例/素材/风格
2. **视觉诊断** — 选定镜头语言与导演风格
3. **六要素组装** — 按公式精准撰写
4. **强制校验** — 运行 Python 脚本进行质量审查
5. **专业交付** — 导演阐述 + 完整提示词

### 3. 更多示例

```
# AI漫剧
帮我写一段10秒的AI漫剧风格的霸道总裁短片，竖屏9:16，要有台词和夸张表情特写

# 电商广告
帮我写一段8秒的高端腕表产品广告视频提示词，9:16竖屏

# 短剧对白
帮我写一段12秒的反转短剧片段，要有台词

# 一镜到底
帮我生成一段15秒的一镜到底穿越博物馆的视频提示词

# 带参考素材
我上传了3张角色设定图和1段参考视频，帮我生成15秒的仙侠打斗
```

---

## 📁 项目结构

```
seedance-shot-design/
├── SKILL.md                     # 核心指令（Skill大脑）
├── README.md                    # 本文件
├── scripts/
│   ├── validate_prompt.py       # 提示词工业级校验脚本
│   └── test_validate.py         # 校验脚本测试用例
└── references/
    ├── cinematography.md        # 运镜与焦段专业词典（含物理机位与焦段心理学）
    ├── director-styles.md       # 导演风格参数化映射库（28+风格，含去名化安全提示词）
    ├── seedance-specs.md        # Seedance 2.0官方平台规范
    ├── quality-anchors.md       # 品质锚定与光影库（含材质/灯光/冲突矩阵）
    ├── scenarios.md             # 垂直场景模板库（16大场景 + 物理阻尼工具箱）
    └── audio-tags.md            # 音频与音效标签规范（含空间声学与材质拟声）
```

---

## 🔬 校验脚本

提供独立的 Python 校验工具，可在命令行中单独使用：

```bash
# 直接校验文本
python scripts/validate_prompt.py --text "你的提示词"

# 从文件校验
python scripts/validate_prompt.py --file prompt.txt

# JSON格式输出（便于程序化处理）
python scripts/validate_prompt.py --text "提示词" --json
```

**校验项（v1.1 升级）：**
- ❌ 字数超标（>500字符）
- ❌ 缺少专业运镜术语
- ❌ 废话词硬阻断（masterpiece/杰作/超清晰等 → error）
- ❌ 光学物理冲突（超广角+虚化、手持+绝对对称）
- ❌ 风格冲突矩阵（IMAX vs VHS、胶片 vs 数码、水墨 vs UE5）
- ❌ 资产引用超限（图片>9/视频>3/音频>3/总计>12）
- ❌ 长视频(>5s)无时间切片硬阻断
- ⚠️ 时序切片缺失或重叠
- ⚠️ 声明时长与切片末端不匹配
- ⚠️ 同段内运动逻辑冲突

**运行测试：**
```bash
python -m pytest scripts/test_validate.py -v
```

---

## 🏗️ 设计理念

### 渐进式知识加载（Progressive Disclosure）

遵循 Agent Skills 最佳实践：

- **SKILL.md**（~4000 tokens）：核心工作流 + 结构模板 + 质量检查表
- **references/**（按需加载）：仅在用户提及风格/运镜/品质等需求时才读取对应文件
- **scripts/**（按需执行）：校验脚本仅在生成提示词后执行

### 竞品超越策略

| 对比维度 | 竞品通用做法 | 本Skill做法 |
|----------|-------------|-------------|
| 合规校验 | 纯文本建议 | **Python脚本硬性校验（含光学/风格冲突矩阵）** |
| 导演风格 | 仅国际大导 | **国际+中国+短剧+AI漫剧+社交媒体+二次元+小红书** |
| 场景覆盖 | 偏电影大片 | **16大垂直场景 + 物理阻尼工具箱** |
| 音效描述 | 简单提及 | **空间声学 + 材质拟声精细化词库** |
| 光影描述 | "加个灯" | **光源→光行为→色调三层 + 灯光Recipe + 材质库** |

---

## 📋 版本记录

### v1.1.0 (2026-03-20)
- 🎬 **运镜升级**：新增焦段叙事心理学、动态对焦范式、物理机位章节（7种特种载具）
- 🎨 **导演风格**：新增芬奇/迪金斯/黑泽明/新海诚 + 二次元爆燃/小红书种草（含去名化安全提示词 + 禁止项）
- 💡 **品质升级**：反塑料感宣言、胶片型号库(5种)、材质质感库(8种)、灯光组合速查(4套)、有机瑕疵库、品质冲突矩阵
- 🎬 **场景扩展**：新增游戏PV/恐怖惊悚/旅行城市/宠物萆系/Before-After/Meme-Loop，总计 16 场景 + 物理阻尼附录
- 🎙️ **音效升级**：空间声学修饰词(7种)、材质拟声精细化(7对)
- 🔧 **校验强化**：废话词 warning→error 硬阻断、光学物理冲突检测、风格冲突矩阵、时长感知时间切片，35项测试全通过

### v1.0.0 (2026-03-19)
- 🎉 首次发布
- SKILL.md 核心工作流
- 6 个专业知识库文件
- Python 校验脚本 + 测试用例
- 20+ 导演风格映射
- 10 大垂直场景模板

---

## 📄 许可

MIT-0 (MIT No Attribution) License
