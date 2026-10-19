# MoA (Mixture-of-Agents) 双模型协同二次元皮肤生成工作流

## 1. 架构背景与分工哲学

在《Minecraft》64×64 高精二次元皮肤生成任务中，通用单模型生成面临两大瓶颈：
1. **纯代码模型**（如 DeepSeek）：精于 Python 代码与工具调用，但缺乏二次元美学经验与立体视觉先验，容易陷入高频噪点抖色（Dithering）、胡须下巴等 3D 畸变。
2. **多模态大模型**（如 Gemini）：具有顶级的二次元角色辨识度、配色感与 3D 空间结构先验，但如果在单次 prompt 中直接生成几千行像素数值，容易出现局部坐标偏移或注意力漂移。

**MoA 解决方案**：将两个模型按能力图谱解耦，建立工业级闭环流水线：
- **Gemini (Aesthetic Architect & Critic)**：
  - 主导全局审美架构设计（`spec_schema.py`），定义高保真调色板（Palette）、立体拓扑规格与硬性负面规则（Negative Rules）。
  - 作为质量审查官（Critic），检测装配产物并输出结构化补丁协议（`CriticPatch`）。
- **DeepSeek (Precise Coder & Execution)**：
  - 严格依据规格与预制件库（`prefabs/`），调用 `SkinBuilder` 流畅 API 装配 64×64 贴图。
  - 毫秒级消费 Critic 发出的补丁指令，执行确定性像素重写与校验。

```
                    ┌─────────────────────────────────┐
                    │  Gemini: Aesthetic Architect    │
                    │  - Character & Palette Spec     │
                    │  - Topology & Negative Rules    │
                    └────────────────┬────────────────┘
                                     │  spec_schema.json
                                     ▼
                    ┌─────────────────────────────────┐
                    │  DeepSeek: Precise Coder        │
                    │  - SkinBuilder Prefab Assembly  │
                    │  - Coordinate & Face Mapping    │
                    └────────────────┬────────────────┘
                                     │  Raw 64x64 Texture
                                     ▼
                    ┌─────────────────────────────────┐
                    │  Gemini: Critic & Review Loop   │
                    │  - Check Chin / Back / Eyes     │
                    │  - Generate CriticPatch Actions │
                    └────────────────┬────────────────┘
                                     │  CriticPatch (if REVISE)
                                     ▼
                        DeepSeek Coder Apply Patch
                                     │  (PASS / Score >= 95)
                                     ▼
                    ┌─────────────────────────────────┐
                    │  Automated 3D Showcase & Export │
                    │  - Headless Browser 3D Render   │
                    │  - Blockbench .bbmodel Ready    │
                    └─────────────────────────────────┘
```

---

## 2. 核心模块与协议

### 2.1 美学规格协议 (`scripts/moa/spec_schema.py`)
定义强类型角色数据结构：
- `PaletteSpec`：精准定义皮肤底色、腮红、发色（基色/阴影/高光）、眼瞳渐变与服饰高对比度色彩。
- `TopologySpec`：定义 Slim/Classic 肢体模型、眼睛行位（Row 4-6）、发型组件（双马尾）与负面规则列表（`no_mouth_on_chin_row`, `no_flat_tails_on_body_back`, `no_dithering_on_face`）。

### 2.2 审查与补丁协议 (`scripts/moa/critic_protocol.py`)
- `CriticPatch`：精确描述修复动作（`replace`/`blend`/`clear`）、目标面与层级（如 `head.front.base`）、受影响行列范围及修改原因。
- `CriticReview`：聚合多个补丁项，给出审核状态（`PASS`/`REVISE`）与置信度评分。

### 2.3 二次元预制件库 (`scripts/prefabs/`)
- `anime_eyes.py`：灵动水灵大眼睛（睫毛行 + 深色虹膜/高光 + 浅色虹膜/巩膜）。
- `drills_twintail.py`：立体螺旋钻头卷发，侧面与背面阶梯式外层立体建模。
- `lolita_skirt.py`：倒 V 字开叉蓬蓬裙、胸前蕾丝领花、金扣披肩与条纹高筒袜。

### 2.4 协同流水线核心 (`scripts/moa/pipeline.py`)
- 自动驱动基础装配、审查、打补丁的闭环反馈，直至达到满分标准。

---

## 3. 自动化验证与质量门禁

运行完整测试套件：
```bash
python tests/test_moa_pipeline.py
```
测试覆盖：
1. `test_prefabs_standalone`：预制件与 SkinBuilder 像素尺寸严密契合，0 越界。
2. `test_moa_pipeline_pass`：合规角色规格一键装配并通过审核（Score >= 95）。
3. `test_moa_pipeline_critic_patch`：人工注入下巴深色噪点缺陷，审查官成功拦截并自动应用 Patch 修复。
