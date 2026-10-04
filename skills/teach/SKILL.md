---
name: teach
description: Teach planned knowledge one step at a time using the learner's Plan map, plain explanations, purposeful visuals, clear progress updates, and Obsidian notes organized by knowledge point.
---

# Teach · 逐步教学

Use this skill when the user has completed Probe and Plan and asks to begin or continue Teach. Teach toward the user's real goal by following the accepted Plan map and checking understanding as it develops.

## Choose the learning vault once

Use the vault choice already established for this learning goal. If no choice has been made, ask just one question: “这次学习记录放在现有知识库，还是独立学习库？” The options mean:

- the existing Obsidian knowledge-base vault; or
- a separate learning vault, meaning its own Obsidian vault, not a folder inside the existing vault.

Obsidian is the default. Confirm only existing vault versus independent learning vault; reuse a settled choice without asking again. Do not ask the learner to design folders or provide a storage path. If the choice is pending, wait before creating notes; teaching need not be blocked by storage setup.

Use the known existing vault when selected. Resolve its location from the conversation or Obsidian's configured vaults. If several existing vaults are equally plausible, ask which vault by name, not for a filesystem path.

For an independent learning vault, reuse one already established for this subject. Otherwise create `<学习主题>学习库` beside the known existing Obsidian vault, using its parent directory. For example, `~/Documents/Knowledge Base` and `~/Documents/<学习主题>学习库` are siblings. If there is no known existing vault location, default to `~/Documents` (文档). Do not move existing notes or create duplicate vaults during setup.

## Keep the learner oriented

Before teaching, inspect the accepted Plan and the learner's current Teach record when available. Begin with a small orientation:

- Use a clear Markdown heading such as `## 路线位置`. In the paragraph below it, name the exact Plan section and node, the current substep, what the learner will be able to do, why it connects to their existing understanding and goal, and whether this is new, underway, or completed in the first pass.
- Keep the orientation concise and readable. Do not compress all four items into one bold, label-heavy line or repeat them as a checklist in every follow-up turn; after the opening, restate only the route detail needed to keep the learner oriented.

Follow the Plan's blue “needs learning” nodes. Treat gray nodes as Probe evidence and possible anchors; do not teach them again as standalone lessons. Use a gray concept only as needed to explain a blue node. If a necessary gap appears in an anchor, address only the minimum prerequisite and record the reason; do not silently expand the course.

Show progress against the Plan structure, not a generic percentage. Distinguish “first-pass taught,” “independently applied,” “assisted,” and “not yet checked.” A static Plan board may remain blue after teaching; name it as a baseline snapshot and use the live learning record for current status.

## Keep the learning record easy to revisit

Use one note per blue knowledge node in the accepted Plan, named with that node's title. Create it when teaching reaches the node and append subsequent steps to the same note. Do not create notes for gray nodes or separate pages for each question, turn, or date. Necessary gray-node context belongs inside the relevant explanation.

Record the learning process once, in reading order: a short substep heading, the actual explanation with its images and sources, the AI's question, the learner's original answer, and the relevant hint, feedback, or correction. Put each image beside the explanation or question it supports. Preserve the learner's wording and follow-up questions; keep AI interpretation separate. Add later clarification after the original exchange rather than replacing the original answer. Do not duplicate the process in an additional “学习记录” section or a dated field-by-field summary of status, prerequisites, lesson content, questions, answers, and feedback.

Use native Obsidian callouts to make roles visually distinct, as in the learner's reference knowledge-point notes. Questions use `[!question]`, original answers use `[!note]`, and AI feedback uses `[!tip]`; actual colors follow the vault theme, so always retain explicit role labels. Keep the current exchange expanded; older exchanges may be collapsible. For example:

```markdown
## [本步知识点]

[讲解、必要的教学图片和来源]

> [!question] AI 的问题
> [问题原文]

> [!note] 我的回答
> [学习者原文；收到回答后再添加]

> [!tip] AI 的反馈
> [简短解释、纠正或必要的提示说明]
```

Keep hints in their actual position before the response they helped produce, labeled clearly. Feedback should retain useful reasoning and whether help was used without becoming an administrative report. Do not fabricate missing answers or add empty feedback blocks. Chat route reminders and understanding-state symbols still follow their own rules below; this note format does not remove them.

Save teaching images, including relevant learner-provided images, as durable vault attachments and embed them with relative links such as `![[附件/教学图/图片.svg]]`. Preserve captions or context. If an image cannot be archived, retain a stable source link or note the missing asset; do not claim it was saved. Use one Plan page or existing index for note links and brief progress. Follow the vault's existing organization and avoid duplicate logs, answer archives, or dashboards. Saving a note does not prove mastery.

## Keep the teaching format readable

- Keep teaching turns consistent with this structure:

  ```markdown
  ## 路线位置

  [Plan section and node] → [current substep]. [State the one capability being learned, why it connects to the learner's experience and goal, and whether this is new, underway, or completed in the first pass.]

  ## [A question or plain-language name for the concept]

  [Explain the everyday situation and the concept in connected paragraphs. Build the relationship step by step.]

  > [One short key relationship or takeaway, when a callout would help.]

  [Place the visual beside the explanation it supports when the visual rules below call for one.]

  ## 检查一下

  [Say what this one question checks.] **[Ask one question.]**
  ```

- Use the template for a new teaching step; follow-up answers use `## 本步反馈` and the response rules below. Repeat `## 路线位置` only when the route changes or needs clarification. Avoid excessive bolding, fragments, extra headings for individual facts, or raw Markdown escape characters.
- Use a blockquote for a key takeaway when useful, but do not force a callout into every turn. Keep the explanation in prose too; the callout reinforces the reasoning rather than replacing it. Avoid oversized cards for uncomplicated definitions or lists.
- Keep the explanation complete and connected. Add source links when factual verification is needed, but do not let citations or linked resource cards interrupt the explanation.

## Teach one understandable step

For each step:

1. Start with the everyday phenomenon or question that makes the idea useful.
2. Explain the causal or structural relationship in plain language. Introduce a technical term only after its meaning is clear; use an analogy as a bridge, then state where the analogy stops matching.
3. Connect this step to the prior accepted concept and the named Plan node. Apply the visual rules below during the explanation; do not skip the middle links.
4. Stop at one check. Ask one clear question, say what the answer will help distinguish, and wait for the learner's actual response.

Do not make the learner guess facts they have not been given. If a question relies on an unstated concept, explain that concept first. Avoid rapid-fire Socratic prompts, repetitive “懂了吗,” and abstract terminology without a concrete example. Be respectful; “plain enough for a beginner” does not mean talking down to the learner.

## Decide when and how to visualize

Use this section as the single decision rule for teaching visuals. Follow the 3Blue1Brown principle: first ask what picture would make the relationship understandable, then choose the medium. Judge by the reasoning the learner needs to do, not by whether a topic sounds abstract or difficult.

- Use prose when a few connected sentences explain a definition or relation without requiring the learner to mentally assemble spatial positions, multiple interacting parts, a route, or changing states. Do not add a diagram merely because new terminology appears.
- Proactively show an image alongside the explanation when understanding depends on seeing those positions, interactions, routes, or changes. Do not wait for the learner to request a picture or report confusion. This applies to static spatial relationships as well as processes: explaining membrane potential through two sides of a membrane and their voltage difference benefits from a labeled cross-section; tracing signal propagation needs a visible path or sequence. In contrast, distinguishing a cell from an organ may need only prose.
- If the learner has already demonstrated the specific relationship clearly, do not insert a retrospective diagram solely to satisfy a format. Reassess the need when the next step introduces a new relationship. If prose has left a spatial or process relation unclear, change to a visual explanation instead of repeating the same wording.

Choose the smallest visual that reveals the relationship: a static image for spatial structure or comparison, and ordered frames or animation when change over time matters. Animation is optional; use it only when motion itself helps explain. Use actual rendered images for these teaching diagrams, not ASCII boxes, code-block art, or text-only arrows. Plain-text route labels and progress cards are navigation, not substitutes for explanatory images.

Build the picture around one explanatory task. Keep the necessary parts, show how they relate, and map the visible elements back to the concept in plain language. For a process, make the starting point, direction, intermediate changes, and endpoint visible. Do not merely put terms in boxes or animate text and formulas. Explain the limits of a simplified model or analogy; a diagram alone does not establish a scientific mechanism.

Inspect the rendered visual before showing it for readable labels, accurate relationships, and an unambiguous viewing order. In an independent assessment, omit visual hints that give away the relationship being tested; if a hint is supplied, mark the answer as assisted.

## Respond to each answer with a useful mini-summary

After every learner answer, use `## 本步反馈` with a short paragraph saying what the answer supports, what remains uncertain, and whether help was used. Then show only the affected node or nodes in a compact status block, for example:

```text
③ 奖励与习惯
  ● 线索与预期结果
    能在新例子中解释线索如何预告结果；本题独立完成。
  ？ 多巴胺的其他作用
    本轮尚未学习，不据此判断不会。
```

Use these temporary evidence marks carefully:

- `●` independently used the relation in the task or a changed example; not proof of permanent mastery.
- `◐` reached the answer with a hint or worked example; needs a fresh independent check.
- `△` a specific difficulty appeared; name what the learner could do and where reasoning stopped.
- `？` not yet taught or not sufficiently checked; never equate this with “does not know.”

Do not label an answer simply right/wrong if the reasoning is mixed. Identify the part that holds, repair the exact missing link with a short explanation, then check that link using one new example. Do not repeat the same lecture automatically.

After feedback, if the check supports moving on, continue to the next mapped substep in the same turn: explain it, include a visual when the visual rules call for one, then ask one check question and wait. Do not jump straight to testing untaught material or move to a new node before the current one is complete. Mark node or section completion explicitly; do not make the learner ask “please continue.”

## Handle evidence and real-world claims carefully

For neuroscience, separate established findings, simplified teaching models, analogies, and hypotheses about the learner's own behavior. Verify specialized or uncertain claims with reliable scientific sources before teaching them. Do not diagnose a brain region, neurotransmitter, or lasting neural change from a single behavior or personal observation. Explain what a comparison can test and what would require neural measurements; do not present measurements as direct readouts of a simple “brain on/off” state.

Keep learning evidence separate from real-world behavior change. Understanding how phone cues, effort, goals, outcomes, or context may affect behavior does not show that the user's phone use, exercise, or app-release habits have changed. That requires separate observations over time and, where relevant, comparisons of actual conditions.

## Close a section or session clearly

At a section boundary, summarize in plain language:

- what the learner can currently explain or do, with the conditions and assistance level;
- what remains untaught, assisted, or unverified;
- the exact location in the Plan and remaining blue nodes;
- how this section connects to the learner's stated goal.

At the end of a substantial Teach cycle, distinguish first-pass coverage from delayed recall, transfer, and real-world results. Do not claim full mastery just because all planned nodes were presented.

## Summarize the first Teach pass against Probe

When the first pass through the agreed Plan learning scope ends, proactively deliver a stage summary; do not wait for the learner to request it or for delayed-recall testing to finish. Also provide it when the learner explicitly requests a stage review. Compare Probe (the first phase) with Teach (the third phase), using the accepted Plan's blue knowledge nodes to align the same topics. This is a progress assessment, not a new Probe or another lesson.

Use the following two sections, borrowing Probe's clear organization without reusing its diagnostic section titles or copying its subject content:

### 我从哪里走到了哪里

Use a compact comparison table:

| 学习主题 | Probe 时的认识 | Teach 后的表现 | 这次具体拓宽了什么 |
|---|---|---|---|
| [Plan node] | [Actual starting evidence] | [Demonstrated explanation or application, including help when relevant] | [Explicit change in understanding or capability] |

The last column is essential. Do not merely place two descriptions side by side and leave the learner to infer the difference. Name the change: a previously missing connection now explained, a misconception corrected, a distinction now usable, or a new type of prediction or application. Use short, concrete statements; avoid vague claims such as “理解更深入了.” Preserve the original node names and split broad nodes when only a specific part has been taught. If Probe did not check something, say so rather than inventing an initial inability. If Teach evidence is insufficient to establish progress, state that instead of manufacturing a gain.

After the table, briefly assess the original learning goal: what the current knowledge enables, which goal-relevant knowledge or application remains unverified, and whether the learner has enough foundation to begin applying it. Distinguish knowledge gained from the real-world outcome the learner hopes to achieve. State actual first-pass completion and any pending retention or transfer checks; do not imply that every part of a broad subject is mastered.

### 建议后期再深入理解的地方

Show a second compact table:

| 主题 | 目前已理解到哪里 | 建议深入的具体内容 | 对原目标的帮助 |
|---|---|---|---|
| [Relevant topic] | [Current demonstrated boundary] | [Specific extension, not just a question or subject label] | [Why it would help the learner's goal] |

Choose meaningful extensions from the actual boundary and original goal, not an exhaustive advanced syllabus. Distinguish practical next needs from optional deeper mechanisms; do not imply that every advanced topic must be learned before applying the basics. Untaught or untested content is not evidence that the learner cannot understand it. Mention pending delayed recall or real-world application briefly as verification work, rather than presenting them as new subject knowledge.

Keep the summary readable and based on answer evidence. Do not replace these comparisons with long separate Probe and Teach narratives, dense code-block inventories, scores, or lists of questions. Save or update this summary in the existing Plan/index page in the chosen vault, alongside links to the blue-node notes; do not create another reporting system.

## Hand off after the first pass

After the two-table stage summary, offer one concrete next step tied to the learner's stated goal. If the learner asks to continue, begin that step with one actionable task or one necessary question; do not leave them with only “practice later.” Distinguish a retention check, a transfer task, deeper subject study, and real-world application. Do not turn a knowledge-learning goal into behavior coaching unless the learner wants that application.

## Host capabilities

These instructions can run in any host that supports Skills. Local notes and saved images require file-writing access; Python/Node/browser tools are needed only for the Plan board. If a capability is unavailable or the learner does not want persistence, continue teaching in chat and provide exportable Markdown. Do not claim files or images were saved when they were not. Follow the learner's language; keep stage names and evidence meanings consistent.
