# Minecraft Pixel Skin v0.0.1

Minecraft 64×64 高精二次元皮肤工程流与设计套件首个版本发布！

## ✨ 核心特性

1. **SkinBuilder 流程 API (`scripts/skin_builder.py`)**
   - 面向对象流式构建 Minecraft 64×64 皮肤；
   - 自动处理基础层（Body/Head/Arms/Legs）与浮动外层（Outer Layer）；
   - 内置防呆尺寸与类型校验，告别手动算坐标。

2. **无头 3D 自动化渲染看板 (`scripts/render_showcase.py`)**
   - 基于 Chromium / Edge 无头驱动 + `skinview3d`；
   - 支持正面全身、背面全身、面部特写、俯仰微动等多视角渲染并自动合成高清看板图。

3. **二次元皮肤设计指南 (`docs/ANIME_SKIN_GUIDE.md`)**
   - 规范化总结 8×8 幼态二次元面容法则（瓷白肌底、卧蚕微渐变、水湖蓝水晶瞳、告别下巴胡渣点）；
   - 香草奶金低饱和发色梯级调色方案（告别高饱和度暗沉与脏斑）；
   - 浮动外层（Outer Layer 3D Depth）层级排布规范。

4. **完整工程级示例：Re:Zero 碧翠丝 (Beatrice) (`examples/beatrice/`)**
   - `beatrice_skin.png`：标准 64×64 Slim (Alex 3px) 皮肤文件；
   - `beatrice.bbmodel`：Blockbench 原生 3D 皮肤工程文件，可直接双击打开涂鸦编辑；
   - `beatrice_3d_render.png`：高清 3D 渲染效果展示图；
   - `beatrice_preview.html`：本地可交互 3D 旋转预览页面。

5. **自动化测试套件 (`tests/`)**
   - 覆盖尺寸断言、Slim 手臂规范检验、外层透明度保护等单元测试。
