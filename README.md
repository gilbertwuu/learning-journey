# Learning Journey

Turn “I want to learn” into a learning path grounded in what you already know, then build understanding you can demonstrate, one step at a time.

One plugin, three skills: **Probe → Plan → Teach**. Chinese is the default language, but the plugin can follow the learner's preferred language. It is designed for people with a question, a practical goal, or a need to find the right starting point.

| Skill | Purpose | Output |
|---|---|---|
| **Probe** | Start from a real goal and use concrete tasks to identify the boundaries of your knowledge | A starting-point assessment and the status of individual concepts, preserving answer evidence and the effect of hints |
| **Plan** | Connect existing understanding to the target ability | A four-part learning plan and an interactive map of concept relationships |
| **Teach** | Explain and check understanding step by step along the agreed path | Illustrated Q&A notes, progress on individual concepts, and a comparison with the original Probe |

Each turn focuses on one central question. Recognizing a term, reading an explanation, answering correctly immediately, using knowledge after a delay, and changing real-world behavior are different kinds of evidence. The plugin does not substitute completion percentages or confidence scores for understanding, or promise that learning theory will solve personal problems.

## Installation

An AI host that supports skills or plugins is required. This repository includes plugin and marketplace manifests for Codex and Claude Code, plus a standard Agent Plugins root manifest. Publication on GitHub does not mean inclusion in an official plugin directory.

### Codex App

In Plugins, choose **Add marketplace**, enter `gilbertwuu/learning-journey` as the source, set Git ref to `main`, and leave Sparse paths empty. Then install **Learning Journey** and start a new conversation. Interface labels may vary by version.

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

### Try the local source

Run from the repository root:

```bash
codex plugin marketplace add .
codex plugin add learning-journey@learning-journey-marketplace
```

If you already have standalone skills named `probe`, `plan`, or `teach`, select the entries belonging to this plugin in your host's skill picker. In particular, `plan` creates a **learning plan**, not a software implementation plan.

## Start learning

Use the following prompts in Codex. In Claude Code, select the corresponding entries from the plugin's skill or command picker.

```text
$probe I want to learn statistics so I can understand product experiment results. Help me find my starting point.
```

Probe first clarifies any background that affects the scope, then identifies your starting point from your actual answers. It reuses existing goals and responses rather than asking you to rate yourself.

```text
$plan Build a learning path based on the Probe we just completed.
```

Plan defines the destination and starting point, maps concept relationships, specifies the depth of each stage, and sets the boundaries of the first stage. Blue indicates material to learn; gray indicates relevant prior understanding, not mastery of an entire chapter.

```text
$teach Start teaching me along this Plan.
```

Teach explains one relationship at a time, then checks it with one question. To resume, say “continue” and provide the previous plan or notes. After the first pass through the path, it compares your progress with the original Probe and gives you a concrete next step tied to your goal.

Each stage can also be used independently. If evidence from an earlier stage is missing, the plugin gathers the necessary information rather than inventing a starting point. If you explicitly request only Probe or Plan, it will not move to the next stage on its own.

## Learning notes

By default, Teach asks once whether to use an existing Obsidian vault or a separate learning vault. Each concept to be learned gets a Markdown note that preserves explanations, images, questions, original answers, and feedback. A plan page records the current path and the first-pass summary.

A separate vault stays separate from any existing vault. If no location is known, it defaults to the user's documents directory. You can specify another location or ask to learn only in chat. Without file-writing access, the plugin provides exportable Markdown instead of claiming that notes have been saved. Obsidian is a suggested reader; paid sync and dedicated connectors are not required.

Do not commit your personal learning vault, original conversations, or individual assessments to this plugin repository. The Python example in this repository is entirely fictional.

## Interactive learning board

Plan bundles a fixed version of the Archify renderer. No separate Archify skill or npm dependencies are needed. Generation and full validation require **Python 3.10+, Node.js 18+, and Chrome/Chromium**. Explanations and Probe do not require these runtimes.

Generate the public example from the repository root:

```bash
python3 skills/plan/scripts/build_board.py \
  examples/python-basics/candidate.json \
  examples/python-basics/notes.json \
  .build/python-demo
```

Open `.build/python-demo/board.html`. The board supports light and dark themes, stage focus, returning to the full map, node details, and connection demonstrations. The output directory must not already exist, to protect previously delivered versions. See the [board documentation](skills/plan/references/board.md) for instructions on repairing an existing version.

If the runtime requirements are missing, the plugin can provide a text learning path and a clearly labeled draft. Automated checks count as passed only when the build exits with code 0 and the validation receipt confirms success. Visual review and actual teaching effectiveness require separate verification. The plugin does not automatically install runtimes.

## Maintenance and validation

```bash
python3 scripts/validate.py
```

This command checks manifest consistency, the three skills, relative documentation links, local machine paths in the public package, examples, and renderer integrity. Run the example command above separately to build and check the board. Behavioral acceptance scenarios are in [docs/acceptance.md](docs/acceptance.md). Passing structural and browser checks does not mean teaching effectiveness has been validated in a controlled study.

Source layout:

```text
plugin.json                      Standard plugin manifest
.codex-plugin/plugin.json        Codex compatibility manifest
.claude-plugin/                  Claude Code manifests and marketplace
.agents/plugins/marketplace.json Codex marketplace
skills/probe/                    Starting-point and knowledge-boundary assessment
skills/plan/                     Learning paths, board adapter, and bundled renderer
skills/teach/                    Teaching, Q&A notes, and stage comparisons
examples/python-basics/          Fictional public example
```

Issues with reproducible examples are welcome. Include the skill used, the expected behavior, and what actually happened. Use fictional or anonymized content rather than private learning records.

## License and acknowledgments

Original content in this plugin is licensed under MIT. The board uses [Archify](https://github.com/tt-a1i/archify) 3.0.1 and retains its license and third-party notices; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). The packaging approach was inspired by [Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin). This repository does not include its source code or imply any affiliation or partnership.

Plugin format and installation instructions reference the [OpenAI plugin documentation](https://developers.openai.com/plugins/build/plugins).
