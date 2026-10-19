# MoA (Mixture of Agents) 协同皮肤生成工作流规范

## 1. 架构定位与设计哲学

在 Minecraft 64×64 高精二次元皮肤生成任务中，单一模型往往存在明显的短板：
- **推理与视觉大模型 (如 Gemini)**：擅长全局审美把控、角色解剖学特征提炼、色彩和谐度规划与负向审美缺陷审查（Critic），但在局部 64×64 绝对像素坐标计算和稠密 UV 空间映射时容易产生漂移。
- **高阶代码与逻辑大模型 (如 DeepSeek)**：擅长严格的像素级数组计算、UV 变换公式推导、无越界内存组装（Coder），但若缺乏先验规则引导，极易在无约束状态下生成低对比度噪点、下巴长胡子（把阴影当嘴唇）或躯干露肉穿帮。

**MoA (Mixture of Agents) 协作架构**将两者的核心优势深度整合，形成**「Gemini 架构与审美质检 + DeepSeek 结构化代码组装」**的闭环系统：

```
                      ┌───────────────────────────────────────────────┐
                      │            Gemini 审美架构师 (Architect)        │
                      │  - 原作立绘特征分解 (Palette / Topology Spec)    │
                      │  - 负向审美规则注入 (Negative Rules)            │
                      └──────────────────────┬────────────────────────┘
                                             │ CharacterSpec (JSON)
                                             ▼
                      ┌───────────────────────────────────────────────┐
                      │          DeepSeek 精准码农 (Coder / Builder)   │
                      │  - 调取结构化预制件库 (Prefabs Library)          │
                      │  - 双层 UV 绝对坐标像素矩阵装配 (SkinBuilder)   │
                      └──────────────────────┬────────────────────────┘
                                             │ 初始组装皮肤
                                             ▼
                      ┌───────────────────────────────────────────────┐
                      │             Gemini 视觉质检官 (Critic)         │
                      │  - 负向规则扫描 (穿帮露肉 / 像素胡须 / 扁平发束) │
                      │  - 生成像素级补丁清单 (CriticPatch)             │
                      └──────────────────────┬────────────────────────┘
                                             │ CriticReview (PASS / REVISE)
                         [REVISE]            ▼             [PASS]
                            └───────> DeepSeek 打补丁 ───────> 最终产物落盘
```

---

## 2. 核心预制件库 (Prefabs Library)

`scripts/prefabs/` 沉淀了二次元高精皮肤的标准结构化组件：

| 预制件 | 对应文件 | 特性与技术规范 |
| :--- | :--- | :--- |
| **灵动二次元大眼** | `anime_eyes.py` | 3×2 渐变双色瞳孔（深青深浅青高光）、外圈深色眼线、上高光反光点、微粉腮红，支持行高配置 |
| **立体钻头螺旋双马尾** | `drills_twintail.py` | 头顶第二层粉色双发带、侧发阶梯式 45° 螺旋卷、发尾微收，杜绝后背扁平假发 |
| **多层洛丽塔开叉长裙** | `lolita_skirt.py` | 倒 V 字开叉红绒外袍、腹部多层褶皱象牙白衬裙（彻底杜绝露肉）、粉紫黑细条纹长筒袜 |
| **浮起泡泡袖与花边手套** | `puff_sleeves.py` | 基础层手臂深浅阴影、第二层肩部 (+0.5px) 浮起大体块泡泡袖、袖口象牙白花边 |
| **斜跨缎带与金扣披风** | `ribbon_sash.py` | 斜跨粉白双色糖果缎带、第二层后背红丝绒披风、金扣连接环 |

---

## 3. 审美闭环质检协议 (Critic Protocol)

### 3.1 负向规则清单 (Negative Rules)
- `no_mouth_on_chin_row`：禁止在 `head.front` 第 7 行（下巴边缘）涂抹深色像素，防止在 3D 渲染器中呈现类似胡须的穿帮瑕疵。
- `no_flat_tails_on_body_back`：禁止在 `body.back` 躯干后背大面积平铺黄色发块，强制发卷分布于侧面与第二层空间。
- `no_bare_skin_on_torso`：禁止在 `body.front` 腹部区域保留基础层裸肤色，必须完全被象牙白衬裙/褶皱花边覆盖。
- `must_have_puff_sleeves`：检查 `rightArm.outer` / `leftArm.outer` 肩部是否具有第二层立体泡泡袖像素体积。

### 3.2 补丁数据结构 (`CriticPatch`)
```json
{
  "face": "body.front",
  "layer": "base",
  "row": 9,
  "col_range": [3, 4],
  "action": "replace",
  "color": [254, 250, 242, 255],
  "reason": "Fill bare skin on body.front base with ivory petticoat frill."
}
```

---

## 4. 运行与验证

### 4.1 执行 MoA 生成流水线
```bash
python scripts/generate_beatrice_moa.py
```

### 4.2 运行自动化单元测试
```bash
python -m unittest discover -s tests
```

### 4.3 产出规范检查
- 图像尺寸：64×64 RGBA PNG，零无效 Alpha。
- 规范校验：`skin_tools.validate_skin` 报告 `passed: True` 且 `errors: []`。
- 3D 预览：`scripts/render_showcase.py` 自动化调用 Chromium 生成全视角 3D 看板。
