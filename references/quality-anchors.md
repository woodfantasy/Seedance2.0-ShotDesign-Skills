# 品质锚定与后期处理词库

> 在提示词开头声明品质锚定，为模型设置品质基准。比泛词"电影感"精准 10 倍。

### 🚨 反塑料感宣言（强制）

> **以下废话词严禁出现在提示词中：** `4K` / `8K` / `masterpiece` / `best quality` / `ultra HD` / `超清晰` / `杰作` / `极致画质`
>
> **为什么有害？** 这些词会让模型过度激活"锐化+去噪"通路，生成表面涂了油的"塑料 CG 假人感"——过度光滑的皮肤、刺眼的高光、死板的完美。
>
> **正确做法：** 用下方的 **物理介质型号** + **光学瑕疵** + **有机质感** 替代。真实感来源于不完美（Organic Imperfections）。

## 一、品质锚定词库

### 渲染引擎

| 关键词 | 风格偏向 |
|--------|----------|
| UnrealEngine5渲染 | 写实+美观，最通用 |
| Octane物理渲染引擎 | 极致光追、产品广告 |
| Blender Cycles渲染 | 独立制作、艺术化 |
| V-Ray光追渲染 | 建筑可视化、精确光影 |
| Houdini粒子特效引擎 | 流体/爆炸/粒子 |
| Cel-Shaded Toon渲染 | 三渲二/动画化CG，简化光影+描边 |

### 画质规格

| 关键词 | 用途 |
|--------|------|
| IMAX级画质 | 极致清晰+大画幅感 |
| RAW影像质感 | 后期空间大、宽容度高 |
| 杜比视界HDR | 高动态范围、明暗层次丰富 |
| HDR10+ | 标准HDR |

### VFX等级

| 关键词 | 级别 |
|--------|------|
| 工业光魔级VFX特效 | 顶级好莱坞 |
| 院线级CG | 影院上映标准 |
| 好莱坞A级特效 | 大制作标准 |

### 摄影机感

| 关键词 | 质感 |
|--------|------|
| ARRI ALEXA摄影机质感 | 电影标杆色彩 |
| RED摄影机色彩 | 锐利+高分辨率 |
| 65mm胶片颗粒质感 | 大画幅有机颗粒 |
| 35mm胶片颗粒 | 经典电影质感 |
| 16mm胶片颗粒 | 独立电影/复古 |

### 专业胶片型号 (Film Stocks)

> 指定具体胶片型号比笼统的"胶片质感"精准得多。每种胶片都有独特的色彩签名，大模型对这些型号名极度敏感。

| 胶片型号 | 英文提示词 | 色彩签名 | 最佳场景 |
|----------|------------|----------|----------|
| **柯达 Portra 400** | `Shot on Kodak Portra 400` | 温润自然肤色，柔和过渡，低对比 | 人像/情感戏——绝杀 AI 蜡像脸 |
| **Cinestill 800T** | `Shot on Cinestill 800T` | 暖色调，霓虹灯高光处产生迷人的红色晕影 (halation) | 夜景/赛博朋克/霓虹街头 |
| **柯达 Vision3 500T** | `Shot on Kodak Vision3 500T` | 电影工业标准色彩，宽容度，自然色还原 | 通用叙事/院线电影质感 |
| **富士 Pro 400H** | `Shot on Fuji Pro 400H` | 清冷淡雅，薄荷绿偏移，柔和高光 | 日系文艺/小清新/旅拍 |
| **柯达 Ektachrome 100** | `Shot on Kodak Ektachrome E100` | 高饱和幻灯色彩，锝利颗粒 | 复古广告/60-70年代美学 |

**提示词范例：**

```
# 温润人像（反塑料感）
Shot on Kodak Portra 400, natural skin tones with micro-imperfections, soft halation around highlights, fine organic film grain

# 夜景赛博朋克
Shot on Cinestill 800T, red halation bleeding around neon highlights, warm tungsten-balanced tones, visible film grain
```

### 物理模拟

| 关键词 | 模拟类型 |
|--------|----------|
| 流体动力学模拟 | 水/血/液体 |
| 粒子物理引擎 | 火花/灰尘/碎片 |
| 破碎物理模拟 | 建筑/玻璃/岩石破碎 |
| 布料物理模拟 | 衣物/旗帜飘动 |

### 材质质感速查 (Material Textures)

> 材质描述是区分“AI 塑料感”和“电影级质感”的核心。每个材质配套英文提示词，可直接嵌入提示词中。

| 材质 | 英文提示词 | 视觉特征 |
|------|------------|----------|
| 皮肤 | `Realistic skin texture with visible pores, subsurface scattering, micro-imperfections` | 毛孔/SSS透光/微瑕疵，反蜜蜡假人感 |
| 发丝 | `Individual hair strands with flyaway wisps, translucent backlit edges` | 发丝飞散+透光边缘，反塑料假发 |
| 丝绸 | `Flowing silk with specular micro-highlights, liquid-smooth draping, light transmission` | 微光泽流转+液态垂坠+半透光 |
| 金属 | `Brushed metal with anisotropic reflection, micro-scratched surface, sharp specular` | 拉丝反射+微划痕+锐利高光 |
| 玻璃 | `Transparent glass with caustic light patterns, refractive distortion, fingerprint smudges` | 焦散光斑+折射畸变+指纹污渍 |
| 食物 | `Glistening food surface with oil sheen, steam wisps rising, juice droplets beading` | 油光/蒸气缚绕/汁液珠化，美食号必备 |
| 玉石 | `Jade with deep subsurface scattering, waxy luster, translucent green-white gradation` | SSS深层透光+蜡质光泽+渐变透亮 |
| 石材 | `Rough-hewn stone with granular surface, moss in crevices, weathered patina` | 粗糥颗粒+苔藓嵌缝+风化层 |

### 动画化 / NPR 材质速查 (Anime / Non-Photorealistic Materials)

> 三渲二 / Cel-Shaded 风格的核心区别在于材质——刷意简化光影和细节，打造「3D 建模 + 手绘效果」。**禁止与上方写实材质混用。**

| 材质 | 英文提示词 | 视觉特征 |
|------|------------|----------|
| Anime 皮肤 | `Anime cel-shaded skin with sharp shadow boundary, no subsurface scattering, clean color blocks` | 硬边阴影分割，无SSS透光，色块清晰，反写实毛孔 |
| Anime 头发 | `Anime hair with stylized highlight band, bold color blocks, flyaway strands at edges` | 高光带（非写实散射），色块分明，边缘飞散发丝 |
| 卡通金属 | `Toon-shaded metal with simplified specular, bold geometric reflection shapes` | 简化高光形状，几何化反射，非物理精确 |
| 卡通织物 | `Flat-shaded fabric with minimal wrinkle detail, bold color fill, anime-style fold lines` | 极简褶纹，色块填充，动画式褶线 |

**品质锚定使用模板：**
```
[时长][品质锚定]，[核心氛围]，
```
**示例：**
```
15秒末日科幻，UnrealEngine5渲染，工业光魔级VFX特效，杜比视界HDR，
冰冷机械美学+末世荒芜氛围，
```

---

## 二、光影三层结构词库

> 拆分为三层描述光影，是大制作提示词的核心技巧。

### 第一层 — 光源层（是什么光、从哪里来）

| 场景类型 | 光源词 |
|----------|--------|
| **灾难/动作** | 暴雨逆光 / 爆炸橙红火光 / 核爆白光 / 闪电侧光 |
| **奇幻/仙侠** | 灵力自发光 / 法阵光环 / 仙雾透光 / 月华清辉 |
| **科幻** | 飞船引擎尾焰光 / 能量球蓝白光 / 全息投影散射 |
| **都市/夜景** | 霓虹灯漫射 / 玻璃幕墙反射 / 车灯流光 / 防空警报红光 |
| **自然/写实** | 黄金时刻侧逆光 / 阴天漫射天光 / 月光冷辉 / 火焰跳动暖光 |
| **室内** | 台灯侧光 / 窗户进光 / 烛光闪烁 / 屏幕冷光 |

### 第二层 — 光行为层（光如何与材质/大气互动）

| 效果 | 描述 |
|------|------|
| 薄雾柔化高光 | 光线穿过雾气被柔化 |
| 强化阴影对比 | 雾层加深暗部 |
| 丁达尔效应/god rays | 光束在尘埃/雾中可见 |
| 体积光穿透 | 光柱穿过空间 |
| 烟尘散射光线 | 粒子折射光 |
| 玻璃折射彩虹光斑 | 棱镜效果 |
| 金属反射高光 | 锐利金属反光 |
| 雨水折射霓虹 | 湿面彩色反射 |
| 次表面散射(SSS) | 皮肤/玉石透光效果 |

### 常用灯光组合速查 (Lighting Recipes)

> 完整的布光方案（Key + Fill + Rim + Accent），比单个光源词效果强 5 倍。

| 场景 | 灯光组合 (Recipe) | 英文提示词 |
|------|---------------------|------------|
| **产品棚拍** | 主光侧前45° + 柔光箱填光 + rim light勾勒轮廓 + 底部反射板 | `Studio hero lighting, 45-degree key light with soft fill, rim light outlining product silhouette, gradient backdrop` |
| **夜景霓虹** | 霓虹灯多色源 + 湿地面反射 + 卷帘门口逾光 + 蓝紫补光 | `Neon multi-source lighting, wet surface reflections, rim spill from shopfront, blue-purple ambient fill` |
| **车内光线** | 仪表盘微光 + 路灯流动光影 + 后视镜反射 + 苏醒暗部 | `Dashboard glow illuminating face from below, passing streetlight shadows sweeping across interior, rearview mirror reflections` |
| **演唱会/舞台** | 追光灰主光 + 多色渗透光 + 干冰地面雾 + 频闪补光 | `Follow-spot key light, colored gel wash from sides, dry-ice floor fog catching laser beams, strobe accent` |

### 第三层 — 色调层（整体冷暖和对比）

| 风格 | 色调公式 |
|------|----------|
| 灾难/压迫 | 冷蓝底调 + 熔岩红高光 |
| 赛博朋克 | 冷蓝底调 + 霓虹紫红高光 |
| 仙侠/奇幻 | 暗青底调 + 金色/荧光高光 |
| 末日/恐怖 | 灰绿底调 + 暗红强化 |
| 暖色/史诗 | 暗棕底调 + 橙金高光 |
| 高级灰 | 低饱和灰调 + 微暖高光 |
| 梦幻/童话 | 柔粉底调 + 金色微光 |
| 社媒鲜亮 | 高饱和底调 + 强对比高光 + 微暖偏移 |

**三层结构使用模板：**
```
光影：[光源词1]+[光源词2]（光源层），
[光行为词1]+[光行为词2]（光行为层），
[色调公式]（色调层）。
```

---

## 三、大气与镜头质感效果词库

### 大气效果

| 效果类型 | 关键词 |
|----------|--------|
| 薄雾/朦胧 | 薄雾弥散 / 潮湿朦胧氛围 / 灰白色海雾包裹 |
| 丁达尔效应 | 丁达尔效应清晰 / 光束穿透雾层 / god rays射线 |
| 热浪/蒸汽 | 热浪蒸腾 / 蒸汽气团上涌 / 高温气流扭曲画面 |
| 烟尘粒子 | 爆炸烟尘 / 细粒子悬浮 / 粉尘弥散光线 |
| 雨/雪/风 | 暴雨倾盆 / 雪花缓落 / 风沙弥漫 |
| 大气连贯 | 每帧都有自然的薄雾弥散效果 / 全程雨雾弥漫 |

### 镜头质感效果（"不完美"增强真实感）

| 效果类型 | 关键词 |
|----------|--------|
| 镜头附着物 | 雾水珠附着镜头前 / 雾粒粘镜 / 雨滴溅到镜头 |
| 光学畸变 | 镜头畸变效果 / 雾层折射 / 广角边缘畸变 |
| 镜头震动 | 镜头剧烈抖动 / 爆炸冲击波震动镜头 |
| 镜头耀斑 | lens flare / 逆光眩光 / 光斑散射 |
| 色差 | chromatic aberration / 边缘色散 |

### 有机物理瑕疵 (Organic Imperfections)

> “真实感来源于不完美”——以下瑕疵词是对抗 AI “塑料感”的核心武器，每条提示词至少使用 1-2 个。

**光学瑕疵：**

| 瑕疵 | 英文提示词 | 视觉效果 |
|------|------------|----------|
| 胶片红色光晕 | `Cinematic halation` | 高光处弥散的温暖红色光晖，胶片特有 |
| 变形宽银幕眩光 | `Anamorphic lens flares` | 水平拉丝式眼光，2.35:1宽银幕标志 |
| 桶形畸变 | `Barrel distortion` | 广角镜头边缘拉伸，增强空间压迫感 |
| 周边暗角 | `Natural optical vignetting` | 边缘自然压暗，引导视觉聚焦中心 |

**物理质感：**

| 瑕疵 | 英文提示词 | 视觉效果 |
|------|------------|----------|
| 眉毛皮肤 | `Realistic skin texture with visible pores and micro-imperfections` | 反塑料感第一利器，告别蓁像脸 |
| 汗水反光 | `Sweat glistening on skin surface` | 细微的液体反射，增强真实触感 |
| 微尘飘浮 | `Floating dust particles caught in light` | 空气中的微尘在光束中闪烁，空间立体感 |
| 织物微纤维 | `Fabric micro-fiber detail under light` | 衣物表面的微观纹理，材质真实感 |
| 发丝光泽 | `Individual hair strands catching light` | 毛发反光与飞散，告别塑料假发 |

**环境有机物：**

| 瑕疵 | 英文提示词 | 视觉效果 |
|------|------------|----------|
| 雨滴玻璃 | `Rain droplets trickling down glass surface` | 湿润环境感 |
| 凝结水雾 | `Condensation fog on cold surfaces` | 温度差的物理表现 |
| 落叶碎屑 | `Scattered leaves and organic debris` | 场景自然生活感 |
| 光斜进的灰尘 | `Dust motes drifting through shafts of light` | 空间体积感+光线可见 |

**反塑料感提示词范例：**

```
# 人像反塑料感套件
Shot on Kodak Portra 400, realistic skin texture with visible pores, sweat glistening on forehead, cinematic halation, fine organic film grain, floating dust particles in warm backlight

# 夜景反塑料感套件
Shot on Cinestill 800T, anamorphic lens flares, red halation around neon signs, rain droplets on lens surface, natural optical vignetting, visible film grain
```

---

## 四、后期处理与收束词库

### 后期处理词（可叠加使用）

暗角 / 胶片颗粒 / 电子噪点 / 色差(chromatic aberration) / 轻微镜头失真 / 运动模糊 / 轻微过曝 / 胶片刮痕 / 暗角渐深

### 张力宣言（按风格分类）

| 风格 | 收束句 |
|------|--------|
| 压迫/灾难 | 窒息式压迫感+诡谲朦胧氛围，无冗余画面，全程高张力 |
| 科幻/未来 | 冰冷机械美学，每帧可截图成壁纸，镜头感拉满 |
| 仙侠/奇幻 | 仙气飘渺，如梦似幻，全程不要现代感痕迹 |
| 都市/情感 | 温度感十足，每帧有呼吸感，镜头语言克制而有力 |
| 动作/热血 | 肾上腺素拉满，节奏紧绷，剪辑感强烈 |
| 孤寂/文艺 | 留白充分，克制的情绪张力，画面呼吸感强 |
| 可爱/治愈 | 满屏治愈感，色彩明快，让人嘴角上扬 |

**收束句模板：**
```
[后期处理词1]+[后期处理词2]收尾，[情绪形容词]氛围，[质量宣言]。
```

---

## 五、品质冲突矩阵 (Conflict Matrix)

> **矛盾的品质词组合会让模型输出四不像。** Claude 必须在组装提示词时主动检测并避免以下冲突。

| 冲突对 A | 冲突对 B | 为什么冲突 | 解决方案 |
|---------|---------|------------|----------|
| IMAX 65mm 极致清晰 | VHS 模拟降解 | 一个要极致锐利，一个要刻意降解 | 二选一，不可混用 |
| UE5 写实光追 | 水墨宣纸笔触 | 一个物理渲染，一个抽象二维 | 二选一；若要融合用“3D渲染水墨质感” |
| 胶片颗粒 + 有机噪点 | 锐利数码电商质感 | 一个要粗糥不完美，一个要完美无瑕 | 根据场景选择；电商禁胶片，影片禁数码锐 |
| 手持晃动 / Handheld | 绝对对称构图 | 运镜与构图逻辑矛盾 | 对称构图强制用三脚架/云台 |
| Slow Motion 慢镜头 | Speed Ramp 变速 | 同一时间切片内不可同时慢和加速 | 分时间切片使用，不在同段重叠 |
| 三渲二Cel-Shade/卡通渲染 | 写实PBR材质/SSS/皮肤毛孔/微瑕疵 | 一个刻意简化光影和材质，一个追求物理精确 | 二选一；三渲二提示词禁用写实材质词 |

**使用规则：**
- Claude 在 Step 3 组装提示词时必须交叉检查本矩阵
- 校验脚本可检测"运动逻辑冲突"已覆盖部分场景
- 若用户坚持矛盾组合，在导演阐述中主动说明取舍和风险
