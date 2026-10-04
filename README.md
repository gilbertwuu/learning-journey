# Learning Journey

把「我想学」变成有依据的学习路线，再一步步建立可检查的理解。

一个插件，三个 Skill：**Probe → Plan → Teach**。中文优先，也可以跟随学习者使用其他语言。适合已经有好奇的问题、实际目标，或想知道自己该从哪里开始的人。

| Skill | 负责什么 | 交付什么 |
|---|---|---|
| **Probe** | 从真实目标出发，通过具体任务定位知识边界 | 当前位置与各知识点状态；保留回答证据和提示影响 |
| **Plan** | 把已有认识连接到目标能力 | 四部分学习计划、可交互的知识关系看板 |
| **Teach** | 沿认可的路线逐步讲解与检查 | 图文问答笔记、局部进度、Probe 到 Teach 的前后对照 |

每次只提出一个中心问题。听过术语、看完解释、当场答对、延迟还能使用、现实行为改变，是不同的证据。插件不以完成百分比或自信评分代替理解，也不承诺学完理论就解决个人问题。

## 安装

需要支持 Skills/插件的 AI 宿主。本仓库提供 Codex 和 Claude Code 的插件与 marketplace 清单，同时包含标准 Agent Plugins 根清单。发布到 GitHub 不等于被官方插件目录收录。

### Codex App

在 Plugins 中选择 **Add marketplace**，来源填写 `gilbertwuu/learning-journey`，Git ref 选择 `main`，Sparse paths 留空。添加后安装 **Learning Journey**，再开启新对话。不同版本的入口文字可能不同。

### Codex CLI

```bash
codex plugin marketplace add gilbertwuu/learning-journey --ref main
codex plugin add learning-journey@learning-journey-marketplace
```

### Claude Code

```text
/plugin marketplace add gilbertwuu/learning-journey
/plugin install learning-journey@learning-journey-marketplace
```

### 从本地源码试用

在仓库根目录运行：

```bash
codex plugin marketplace add .
codex plugin add learning-journey@learning-journey-marketplace
```

若原来已独立安装同名 `probe`、`plan` 或 `teach`，请在宿主的 Skill 选择器里选择本插件下的入口，避免误选。尤其 `plan` 是**学习计划**，不是软件实施计划。

## 开始学习

在 Codex 中分别使用下面的提示；Claude Code 可从插件的 Skill/命令选择器选择同名入口。

```text
$probe 我想学统计学，主要想读懂产品实验的结果，请帮我定位学习起点。
```

Probe 会先补齐影响范围的背景，再根据实际回答定位。已有目标和回答会沿用，不要求你先给自己打分。

```text
$plan 基于刚才的 Probe，为我制定学习路线。
```

Plan 给出学习终点与起点、关系看板、每段学习深度和第一段边界。蓝色是需要学习，灰色是已有相关认识；灰色不代表整章掌握。

```text
$teach 沿这份 Plan 开始学习。
```

Teach 每次讲清一个关系，再用一个问题检查。继续学习时直接说“继续”，并提供原来的计划或笔记即可。首次路线完成后，对照 Probe 总结具体变化，并根据你的目标给出明确的下一步。

三个阶段也能单独使用；缺少上一步证据时，会先补必要信息，不编造起点。显式要求仅做 Probe 或 Plan 时，阶段结束后不会擅自进入下一阶段。

## 学习笔记

Teach 默认询问一次：使用现有 Obsidian 知识库，还是独立学习库？每个待学知识点一篇 Markdown 笔记，持续保留讲解、图片、问题、原始回答及反馈。一个计划页记录当前路线和首次学习总结。

独立库与既有库分开；没有已知库位置时，默认放在用户文档目录。你可以指定其他位置或要求只在聊天里学习。没有文件写入权限时会提供可导出的 Markdown，不会声称已经保存。Obsidian 只是推荐阅读器，不需要付费同步或专用连接器。

不要把自己的学习库、原始对话或个人评估提交到本插件仓库。仓库中的 Python 示例完全虚构。

## 交互式学习看板

Plan 内置固定版本的 Archify 渲染器，无需另装 Archify Skill 或 npm 依赖。生成和完整校验需要 **Python 3.10+、Node.js 18+、Chrome/Chromium**。讲解与 Probe 不需要这些运行环境。

在仓库根目录生成公开示例：

```bash
python3 skills/plan/scripts/build_board.py \
  examples/python-basics/candidate.json \
  examples/python-basics/notes.json \
  .build/python-demo
```

打开 `.build/python-demo/board.html`。支持深浅主题、分段聚焦、返回全图、节点详情和连线演示。生成目录必须不存在，以保护已经交付的版本；修复同一版本的方法见 [看板文档](skills/plan/references/board.md)。

缺少运行环境时可以先交付文字路线和明确标记的草稿。只有构建退出码为 0、校验回执通过时，才算自动检查通过；人工目视检查和实际教学效果另行验证。插件不会自动安装运行环境。

## 维护与验证

```bash
python3 scripts/validate.py
```

该命令检查清单一致性、三个 Skill、相对文档链接、公开包中的本机路径、示例和渲染器完整性。看板构建另跑上面的示例命令。行为验收场景见 [docs/acceptance.md](docs/acceptance.md)。结构与浏览器检查通过不表示教学效果已经经过对照研究验证。

源码组织：

```text
plugin.json                     标准插件清单
.codex-plugin/plugin.json       Codex 兼容清单
.claude-plugin/                 Claude Code 清单与 marketplace
.agents/plugins/marketplace.json Codex marketplace
skills/probe/                   起点与边界探查
skills/plan/                    路线、看板适配器与内置渲染器
skills/teach/                   教学、问答笔记与阶段对照
examples/python-basics/         虚构公开示例
```

欢迎通过 Issue 提供可复现的问题：使用哪个 Skill、希望发生什么、实际发生什么。请用虚构或匿名内容复现，不上传真实私人学习记录。

## 许可与致谢

本插件原创内容采用 MIT 许可。看板使用 [Archify](https://github.com/tt-a1i/archify) 3.0.1，保留其许可证和第三方声明，具体见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。打包形式参考 [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin)，不包含其源码，也不代表双方有从属或合作关系。

插件格式与安装方式参考 [OpenAI 插件文档](https://developers.openai.com/plugins/build/plugins)。
