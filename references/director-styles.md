# 导演风格参数化映射库

> 将导演的视觉语言拆解为 AI 可计算的参数——构图、光影、色调、运镜、材质。
> 不仅涵盖国际电影大师，还包括中国影视、短剧、AI漫剧、社交媒体等多元风格。

### 🚨 去名化使用规范（强制）

> **最终提示词中严禁出现任何导演名、工作室名或 IP 名。** 标题中的导演名仅供 Claude 内部索引匹配用户意图，不可泄漏到输出中。

**四大物理轴降解框架：** 当用户提及某导演风格时，必须将其降解为以下四轴的纯物理参数组合：

| 物理轴 | 含义 | 示例 |
|--------|------|------|
| 🎨 色彩 (Palette) | 色盘、饱和度、色温 | `Desaturated desert palette` / `Neon teal and orange` |
| 💡 灯光 (Lighting) | 光源类型、光行为、氛围 | `Heavy atmospheric haze` / `Smoldering neon glow` |
| 🏛️ 美术 (Art Direction) | 建筑、材质、场景美学 | `Brutalist architecture` / `Pastel dollhouse set` |
| 📷 机位 (Camera) | 焦段、运镜、稳定方式 | `Glacial push-in` / `Strict symmetrical framing` |

**使用流程：** 用户说"维伦纽瓦风格" → Claude 匹配到本库中维伦纽瓦条目 → 提取 `安全提示词` 行 → 嵌入最终提示词中（**不含任何人名**）。

---

## 一、国际电影大师风格

### 克里斯托弗·诺兰 (Christopher Nolan) — 冷峻写实

| 维度 | 参数 |
|------|------|
| **构图** | 宏大尺度、实景比例、IMAX全画幅构图 |
| **光影** | 去饱和冷色调、高对比、自然光为主 |
| **色调** | 深蓝/铅灰/钢铁银/极致黑 |
| **运镜** | 缓慢推轨、IMAX稳定器、极少手持 |
| **材质** | 65mm IMAX胶片颗粒、真实物理特效、实景爆破质感 |
| **提示词模板** | `IMAX 65mm film clarity, fine organic film grain, desaturated cold palette, high-contrast cinematic lighting, practically plausible motion, heavy debris physics` |
| **安全提示词** | `IMAX 65mm film grain, desaturated steel-blue and charcoal palette, high-contrast natural key lighting, monumental practical-scale architecture, glacial dolly push-in, heavy debris particle physics, zero handheld shake` |
| **❌ 禁止** | 禁止出现导演名字；避免直接写"时间穿越""旋转走廊"等诺兰标志性情节符号，改用纯物理参数描述 |

### 丹尼斯·维伦纽瓦 (Denis Villeneuve) — 巨物压迫

| 维度 | 参数 |
|------|------|
| **构图** | 巨物与渺小人物对比、几何对称、粗野主义建筑 |
| **光影** | 弥散柔光、单色光笼罩、体积雾 |
| **色调** | 琥珀/冷白/去饱和暖黄 |
| **运镜** | 极缓推轨、长焦远景、肃穆缓慢 |
| **材质** | 粗砂岩质感、混凝土表面、大气霾 |
| **提示词模板** | `Brutalist minimalist architecture, monumental epic scale, diffused ambient lighting, volumetric fog, atmospheric depth, minimalist desaturated color grading with stark contrast` |
| **安全提示词** | `Brutalist concrete architecture, monolithic scale with tiny human figure for contrast, heavy atmospheric haze with volumetric god rays, desaturated amber-sand palette, glacial push-in on 135mm telephoto, oppressive silence` |
| **❌ 禁止** | 禁止出现导演名字；避免直接写"沙丘""沙虫"等IP符号，用"巨型生物体穿越沙暴"等纯物理描述替代 |

### 韦斯·安德森 (Wes Anderson) — 极致对称童话

| 维度 | 参数 |
|------|------|
| **构图** | 绝对居中对称、平面化舞台调度、正交摄影 |
| **光影** | 均匀柔光、极少硬影 |
| **色调** | 马卡龙粉/芥末黄/薄荷绿/复古浅蓝 |
| **运镜** | 机械式90度横摇、直线横向推轨、禁用透视变化 |
| **材质** | 精致布景、微缩模型感、复古纸质质感 |
| **提示词模板** | `Perfect symmetrical framing, centered composition, flat spatial depth, pastel color palette (mustard yellow and powder pink), meticulous set design, 90-degree whip pan` |
| **安全提示词** | `Strict symmetrical centered composition, flat theatrical staging with zero depth perspective, pastel macaron palette (mustard yellow, powder pink, mint green), mechanical 90-degree lateral dolly, miniature dollhouse set design, soft even fill lighting with no hard shadows` |
| **❌ 禁止** | 禁止出现导演名字；绝对禁用手持晃动/Handheld；避免任何透视纵深变化，保持扁平正交构图 |

### 王家卫 (Wong Kar-wai) — 霓虹迷幻

| 维度 | 参数 |
|------|------|
| **构图** | 前景遮挡、偷窥角度、逼仄空间 |
| **光影** | 浓郁霓虹、雨水折射、镜面反射 |
| **色调** | 高饱和霓虹红/幽绿/暗蓝 |
| **运镜** | 抽帧拖影、降速快门、手持晃动 |
| **材质** | 胶片刮痕、残影拖尾、湿润质感 |
| **提示词模板** | `Neon-lit urban night, highly saturated contrasting colors (deep vivid reds and emerald greens), shallow depth of field, claustrophobic framing, reflections on wet surfaces, slow shutter speed effect, motion blur trails` |
| **安全提示词** | `Step-printed slow motion with ghosting trails, voyeuristic foreground obstruction (door frames, curtains, glass), neon teal-and-orange split lighting, smoldering atmospheric haze, claustrophobic tight framing, rain-soaked reflective surfaces, slow shutter drag with motion blur` |
| **❌ 禁止** | 禁止出现导演名字；避免自动生成旗袍/花样年华等刻板符号，聚焦于光影和运镜的物理参数 |

### 宫崎骏 (Hayao Miyazaki) — 手绘幻想

| 维度 | 参数 |
|------|------|
| **构图** | 广阔天空占比大、细腻自然景观 |
| **光影** | 柔和自然光、云朵透光 |
| **色调** | 清新自然绿/天空蓝/暖黄 |
| **运镜** | 缓慢平移、飞行跟拍、俯瞰全景 |
| **材质** | 手绘水彩质感、柔和线条、自然肌理 |
| **提示词模板** | `Hand-painted watercolor aesthetic, soft natural lighting, expansive sky composition, gentle breeze animation, lush green natural palette, warm nostalgic tones` |
| **安全提示词** | `Hand-painted watercolor cel animation, soft diffused natural sunlight through cumulus clouds, expansive 70% sky composition, lush green-and-sky-blue pastoral palette, gentle breeze rippling grass and hair, slow pan across meadow, warm nostalgic golden-hour tones` |
| **❌ 禁止** | 禁止出现导演名/工作室名；避免直接引用龙猫/千寻/天空之城等IP形象，用"毛茸茸的巨型森林守护灵"等原创描述替代 |

### 大卫·芬奇 (David Fincher) — 精密惊悚

| 维度 | 参数 |
|------|------|
| **构图** | 精确框取、绝对控制感、主体居中偏移制造不安 |
| **光影** | 低调打光、大面积暗部、单点光源雕刻面部 |
| **色调** | 去饱和黑绿/铅灰/冷青，极低彩度 |
| **运镜** | 精密推轨、缓慢平滑的轨道运动、禁用手持晃动 |
| **材质** | 数码超清斄质感（非ICU粒）、冷硬表面、室内人工光 |
| **提示词模板** | `Low-key lighting with dominant shadows, desaturated green-grey palette, precise dolly tracking, controlled cold atmosphere, clinical digital clarity` |
| **安全提示词** | `Low-key single-source lighting carving face from darkness, desaturated sickly green-grey palette, precise mechanical dolly tracking with zero handheld, clinical digital texture, oppressive controlled framing, subject slightly off-center creating unease` |
| **❌ 禁止** | 禁止出现导演名字；禁用手持晃动；避免"等待室""纸牌屋"等作品符号 |

### 罗杰·迪金斯 (Roger Deakins) — 自然光减法

| 维度 | 参数 |
|------|------|
| **构图** | 空间层次感、前中后景分离、画面内自然框取 |
| **光影** | 极致自然光、窗光/天光为主、最少干预的布光 |
| **色调** | 自然色温、黄金时刻暖调、低对比柔和 |
| **运镜** | 极简克制的运镜、缓慢推轨、长镜头凝视 |
| **材质** | 自然光下的真实肤色、大气透视层次、空气中的微尘 |
| **提示词模板** | `Natural available light only, golden hour warmth, layered spatial depth with atmospheric perspective, minimal camera movement, restrained understated beauty` |
| **安全提示词** | `Natural window light as sole source, golden-hour warmth with soft shadow falloff, layered spatial depth using atmospheric haze between planes, slow contemplative dolly, available-light skin tones, floating dust particles catching light, minimal intervention restrained beauty` |
| **❌ 禁止** | 禁止出现摄影师名字；禁用激烈光效/霓虹/特效灯；避免"银翼杀手""肖申克的救赎"等作品引用 |

### 黑泽明 (Akira Kurosawa) — 天气叙事

| 维度 | 参数 |
|------|------|
| **构图** | 群像调度、强方向性运动线、前景遮挡增层次 |
| **光影** | 天气驱动光线——暴风雨/烈日/大雾本身就是照明 |
| **色调** | 高对比黑白质感（彩色时为暗沉土色/绿） |
| **运镜** | 多机位交叉剪辑、群体动作的长焦压缩、慢动作死亡美学 |
| **材质** | 风雨粒子/泥地飞溅/旗帜狂舞的物理质感 |
| **提示词模板** | `Weather-driven dramatic lighting, torrential rain as narrative force, ensemble group choreography, strong directional movement, telephoto compression of crowd action, slow-motion death aesthetics` |
| **安全提示词** | `Torrential rain as dominant lighting source and narrative force, ensemble warriors in directional formation charge, 200mm telephoto compressing depth, mud splashing with each footstep, banners whipping violently in storm wind, slow-motion blade arc with rain droplets frozen mid-air, high-contrast chiaroscuro` |
| **❌ 禁止** | 禁止出现导演名字；避免"七武士""乱"等作品名；用"古代武士集团"等原创描述 |

### 新海诚 (Makoto Shinkai) — 数码光彩动画

| 维度 | 参数 |
|------|------|
| **构图** | 天空占画面 60%+、极致云层光影细节、青春人物剑影 |
| **光影** | 极致逆光、光线穿透云层的丁达尔效应、黄昏/黄金时刻滥用 |
| **色调** | 极高彩度的蓝/紫/橙天空、色彩爆炸式渐变 |
| **运镜** | 细节特写插入（水滴/树叶/手机屏）、缓慢推轨 |
| **材质** | 数码CG超写实背景 + 简化人物、光斑散景、晶莹的水滴 |
| **提示词模板** | `Hyper-saturated sky gradient (deep blue to vivid orange), dramatic god rays through towering cumulus clouds, digital anime aesthetic with photorealistic backgrounds, youth silhouette against golden-hour sky, crystalline light particles` |
| **安全提示词** | `Digital anime aesthetic, hyper-detailed photorealistic sky with towering cumulus clouds and vivid blue-to-orange gradient, dramatic god rays piercing cloud layers, youth figure silhouette against golden-hour backlight, crystalline rain droplets catching prismatic light, extreme color saturation, detail insert cuts of water droplets on glass` |
| **❌ 禁止** | 禁止出现导演名字；避免"你的名字""天气之子""铃芽之旅"等IP引用；与宫崎骏的区分：宫崎骏=手绘田园暖色，新海诚=数码超写实+天空爆炸色彩 |

---

## 二、中国影视风格

### 张艺谋式东方美学 — 色彩叙事

| 维度 | 参数 |
|------|------|
| **构图** | 大面积色块构图、人物在色彩中的对比 |
| **光影** | 高饱和主色调、单色光源为主 |
| **色调** | 浓烈的红/金/暗绿/靛蓝（视主题而定） |
| **运镜** | 大气远景航拍、缓慢推进、仪式感调度 |
| **材质** | 绸缎/竹林/黄沙/青瓦白墙的物理质感 |
| **提示词模板** | `东方电影美学，大面积中国红色块构图，绸缎在风中飘动的流体质感，高饱和色彩叙事，仪式感镜头调度，Slow Crane Up，写实材质纹理` |

### 仙侠/修真 — 中国风奇幻

| 维度 | 参数 |
|------|------|
| **构图** | 云海仙境、悬崖古寺、飞天衣袂 |
| **光影** | 丁达尔光束穿云、灵光自发光、仙气弥漫 |
| **色调** | 金青/暗紫/仙白/玄黑 |
| **运镜** | 航拍穿越云海、摇臂升降揭示仙境、推轨穿过门扉 |
| **材质** | 3D国漫CG渲染、水墨粒子特效 |
| **提示词模板** | `中国仙侠风格，3D国漫CG渲染质感，云雾缭绕的仙境，金青色调，丁达尔光束穿透云层，灵力粒子漂浮，白衣飘逸，航拍穿越云海，空灵环境音` |

### 古偶/古装剧 — 柔光奇幻

| 维度 | 参数 |
|------|------|
| **构图** | 花瓣纷飞、灯笼/烛光前景、柔美对称 |
| **光影** | 柔和侧逆光、golden hour暖调 |
| **色调** | 柔粉/暖金/桃花色系 |
| **运镜** | Smooth Orbit环绕人物、Dolly In聚焦眼神、慢镜头飘逸 |
| **材质** | 丝绸光泽、发丝飘动、花瓣物理飘落 |
| **提示词模板** | `中国古装美学，柔光侧逆光，golden hour暖调，花瓣在空中飘落的物理飘散效果，丝绸衣裙随风飘动，Smooth Orbit缓缓环绕角色，浅景深聚焦面部，古筝悠扬BGM` |

### 都市情感剧 — 写实自然光

| 维度 | 参数 |
|------|------|
| **构图** | 城市街景、生活化场景、自然取景 |
| **光影** | 自然光/城市路灯/室内台灯 |
| **色调** | 自然色温、轻度去饱和 |
| **运镜** | 手持微晃、跟拍、Steadicam流畅跟随 |
| **材质** | 35mm胶片颗粒、真实皮肤质感 |
| **提示词模板** | `都市情感写实风格，35mm胶片质感，自然色温，手持微晃跟拍，城市街景自然光，角色微表情特写，浅景深虚化背景，环境城市白噪音` |

---

## 三、新媒体与短视频风格

### AI漫剧 — 动态漫画

| 维度 | 参数 |
|------|------|
| **构图** | 漫画分格感、动态线条、情绪放大 |
| **色调** | 高饱和动漫色彩 或 赛璐璐扁平 |
| **运镜** | 快速Push In表情特写、Speed Line效果 |
| **材质** | 赛璐璐上色/3D卡通渲染/漫画网点 |
| **提示词模板** | `动态漫画风格，赛璐璐上色，高饱和色彩，动态线条效果，快速Push In表情特写，夸张的情绪演绎，漫画式分镜感，配合节奏感BGM` |

### 竖屏短剧 — 9:16快节奏

| 维度 | 参数 |
|------|------|
| **构图** | 竖屏9:16、人物居中、大头大脸 |
| **色调** | 高对比鲜艳、滤镜感 |
| **运镜** | 快速切镜、Whip Pan转场、正反打 |
| **材质** | 数码清晰质感、轻度磨皮 |
| **提示词模板** | `竖屏9:16，短剧节奏，快切镜头，正反打对话，高对比鲜艳色调，人物居中构图占画面70%，清晰数码质感，快节奏BGM` |

### Vlog纪实 — 第一人称

| 维度 | 参数 |
|------|------|
| **构图** | POV第一人称、自拍角度 |
| **色调** | 自然色温、生活感 |
| **运镜** | POV主观视角、手持自然晃动 |
| **材质** | 手机/GoPro质感、轻微广角畸变 |
| **提示词模板** | `Vlog纪实风格，POV第一人称视角，手持自然晃动，轻微广角畸变，自然色温，生活化场景，环境真实声音，无BGM` |

### 社交媒体病毒传播 — 极致吸睛

| 维度 | 参数 |
|------|------|
| **构图** | 前3秒必须有视觉冲击、居中大主体 |
| **色调** | 超饱和、高对比 |
| **运镜** | 开场Zoom In冲击、Speed Ramp慢转快 |
| **材质** | 锐利数码、HDR效果 |
| **提示词模板** | `社交媒体竖屏，前3秒极致视觉冲击，Speed Ramp从慢动作突变快进，超饱和鲜艳色彩，高对比HDR效果，主体占画面80%以上，强节奏感配乐卡点` |

### 二次元变身 / 热血战斗 — 动漫爆燃

> **注意：** 本条目专注于「爆燃战斗 / 变身」场景。若用户需要的是沉稳叙事型的二次元游戏剧情 CG / PV，请使用下方「三渲二 / Cel-Shaded CG」条目。

| 维度 | 参数 |
|------|------|
| **构图** | 冲击帧居中放大、速度线汇聚、气场爆发放射状构图 |
| **色调** | 极高饱和 + 技能色光（火红/电蓝/金黄） |
| **运镜** | Speed Ramp变速 + 定格冲击帧 + 360°环绕 + 急推特写 |
| **材质** | 赛璐璐上色/3D卡通渲染、粒子爆散特效、能量拖尾 |
| **提示词模板** | `二次元动漫爆燃风格，变身光效爆发，速度线汇聚，冲击帧定格放大，极高饱和色彩，能量粒子拖尾，Speed Ramp从慢动作突然加速，气场冲击波扩散` |

### 三渲二 / Cel-Shaded CG — 动画化游戏剧情

> **定位：** 用于游戏剧情CG、PV预告、角色传记、过场动画等沉稳叙事场景。与上方「二次元爆燃」的核心区别：这里追求的是「电影级叙事 + 动画化渲染」，而非「节奏爆炸 + 特效堆叠」。
>
> **代表作参考风格：** 《原神》《崩坏：星穹铁道》《鬼灭之刃》（ufotable级）《蓝色禁区》—— 3D建模 + 卡通渲染管线，保留二维动画的手绘美感。

| 维度 | 参数 |
|------|------|
| **构图** | 电影级调度（远景建置、中景叙事、特写情感）、画面空间感比写实略简化、注重角色剑影比例 |
| **光影** | 简化光源、Anime式硬边阴影二值化（sharp shadow cutoff）、强轮廓 Rim Light 分离角色与背景、减少光影渐变层次 |
| **色调** | 高饱和 Anime 色盘（HSL 精调）、明暗硬边分割、根据角色属性选主色调（火红/冰蓝/暗紫/金色） |
| **运镜** | 电影级运镜（复用现有运镜体系）、长焦浅景深特写 + 史诗航拍、Orbit环绕角色展示 |
| **材质** | **动画化材质（核心区别点）：** Cel-shaded flat shading + 描边轮廓线（bold ink outlines）+ Anime头发高光带 + 简化折皱色块填充、**禁用写实 PBR 材质词（毛孔/SSS/微瑕疵）** |
| **提示词模板** | `3D cel-shaded toon rendering with bold ink outlines, anime-style sharp shadow cutoff, high-saturation character color palette, simplified flat material shading, strong rim light separating character from background, cinematic depth of field with anime bokeh` |
| **安全提示词** | `3D Cel-Shaded Toon渲染，Anime风格硬边阴影二值化，粗描边轮廓线，高饱和角色色盘，简化平涂材质，强Rim Light分离角色与背景，电影级景深与Anime散景` |
| **❤️ 与「二次元爆燃」的配合** | 同一角色的叙事性CG用本条目，战斗片段用上方「二次元爆燃」，两者可在同一PV内分段切换 |
| **❌ 禁止** | 禁用写实材质词（visible pores / subsurface scattering / micro-imperfections）；禁止与写实光追渲染混用 |

### 小红书种草 — 精致生活感

| 维度 | 参数 |
|------|------|
| **构图** | 干净白色/奶油色背景、产品平铺构图、留白充足 |
| **色调** | 马卡龙淡彩 + 微暖偏移、柔和不刺眼 |
| **运镜** | 固定镜头 / 缓慢推进 / 俯拍平铺 |
| **材质** | 数码清晰但不锐利、柔光无硬影、产品质感突出 |
| **提示词模板** | `小红书种草风格，干净奶油色背景，产品平铺居中，柔和自然光，马卡龙淡彩色调，大面积留白，Overhead俯拍，精致生活感` |

---

## 四、特殊风格

### VHS复古录像带

| 参数 | 值 |
|------|-----|
| **视觉特征** | 扫描线、色彩溢出、跟踪错误、低分辨率 |
| **提示词** | `VHS analog aesthetic, scan lines, color bleeding, tracking distortion, warm muted tones, 4:3 aspect ratio, retro camcorder feel` |

### 赛博朋克未来都市

| 参数 | 值 |
|------|-----|
| **视觉特征** | 霓虹灯阵、雨夜反射、全息投影、暗色基调 |
| **提示词** | `Cyberpunk neon city, rain-soaked streets with neon reflections, holographic billboards, dark atmospheric haze, teal and magenta color split, volumetric fog` |

### 水墨东方

| 参数 | 值 |
|------|-----|
| **视觉特征** | 笔墨浸染、留白构图、山水意境 |
| **提示词** | `中国水墨画风格，ink-wash sumi-e aesthetic，笔墨在宣纸上浸染扩散，大面积留白，山水意境，黑白灰为主色调，淡彩点缀，墨韵流动` |

### 像素风/复古游戏

| 参数 | 值 |
|------|-----|
| **视觉特征** | 低分辨率方块、8-bit色板、像素化动画 |
| **提示词** | `Pixel art retro game aesthetic, low-resolution blocky style, 8-bit color palette, pixelated character animation, chiptune sound effects` |

### MV音乐视觉

| 参数 | 值 |
|------|-----|
| **视觉特征** | 节奏卡点、频闪、色光轮换、舞台灯光 |
| **提示词** | `Music video aesthetic, beat-synced editing, strobe lighting effects, color wash transitions, 16:9 widescreen, dynamic stage lighting, silhouette backlit shots` |

### 微缩模型/定格动画

| 参数 | 值 |
|------|-----|
| **视觉特征** | 移轴摄影效果、微缩比例感、逐帧动画质感 |
| **提示词** | `Tilt-shift miniature effect, stop-motion animation feel, handcrafted texture, miniature model scale, frame-by-frame movement, warm practical lighting` |
