# 0.1.0 打包复核

## 保留的核心

Probe 仍只定位起点与边界，背景不充分时只问一个关键问题。Plan 仍承接真实 Probe 证据，输出四部分和蓝灰两色看板。Teach 仍逐步讲解、等待真实回答、保留提示影响，并按蓝色知识点保存图文问答；首轮结束对照 Probe 总结。

## 本次针对公开分发的改动

- 独立打包三个 Skill；原先安装的本机版本未修改。
- Plan 默认使用包内 Archify 3.0.1，去掉固定本机脚本路径；渲染器更新跟随插件版本，不自动查询上游更新。
- 删除真实学习参考 HTML、个人节点说明和历史校验文件；用明确标记为虚构的 Python 示例替换。
- Teach 补齐公开名称、选择器说明及默认提示；首次完成后给出具体下一步；没有文件权限时提供可导出的 Markdown。
- 增加标准插件清单、Codex/Claude Code 兼容清单、两个 marketplace、MIT 许可及第三方声明。

## 已验证

- 三个 Skill 均通过 Skill Creator 的 quick_validate。
- 包级校验通过：清单一致、Skill 入口、文档链接、个人绝对路径检查、示例关系、内置渲染器哈希。
- 虚构看板的 validate / deliver / check / browser-check 四个门禁通过。
- 人工浏览器检查：三段节点均可进入详情；关闭详情恢复全图；明暗主题；详情文字、已知与待学说明可读。
- Codex CLI 成功注册本地 marketplace，安装后返回 installed=true、enabled=true；安装目录内三个入口存在。

## 尚未验证

GitHub 远端发布与从 GitHub 全新安装，Claude Code 的实际安装，以及另一位学习者完整跑通 Probe→Plan→Teach。CI 已配置，但远端执行结果要等仓库发布后验证。

这些检查证明打包与工具链在当前环境中可用，不证明学习方法具有普遍教学效果。推荐用 docs/acceptance.md 中的虚构场景继续试用。
