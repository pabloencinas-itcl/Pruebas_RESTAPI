# smolagents architecture overview

`smolagents` is a small but capable Python framework for building LLM-driven agents. Its architecture is built around a compact execution core that coordinates model calls, tool use, memory, and code execution. The repository supports two main agent styles: a code-first loop where the model emits Python actions, and a more traditional tool-calling style for JSON/text-based tool invocation. Around that core sit pluggable model adapters, an extensible tool system, persistence and inspection utilities, and multiple execution backends for safer or more specialized runs.

A useful way to read the codebase is as a set of boundaries:

- **Agent orchestration** handles the ReAct-style loop, prompting, parsing, and final-answer handling.
- **Model adapters** normalize many LLM providers behind one interface.
- **Tools** are the extension surface for capabilities such as search, browser access, retrieval, SQL, and custom integrations.
- **Memory and serialization** keep multi-step runs inspectable and reusable.
- **Executors** isolate or specialize code execution, including safer remote backends.
- **CLI and UI layers** assemble these pieces into runnable entry points without taking over core behavior.

The surrounding repository reinforces that split: `src/smolagents/` contains the reusable library, `examples/` shows concrete compositions of the building blocks, `tests/` validates the behavior of each boundary, and `docs/source/` explains the framework through conceptual guides, tutorials, references, and examples.

## Sections

- [Architecture Overview and Core Loop](Architecture-Overview-and-Core-Loop.md) — The central agent execution model, including the code-first ReAct loop and how the core package is organized.
- [Model Abstraction and Provider Integration](Model-Abstraction-and-Provider-Integration.md) — How different LLM providers are normalized behind a shared model interface.
- [Tool System and Extension Points](Tool-System-and-Extension-Points.md) — The tool architecture, validation, and extension surfaces for adding capabilities.
- [Memory, Serialization, and Run State](Memory,-Serialization,-and-Run-State.md) — How agent state is stored, inspected, and persisted across runs.
- [Execution Backends and Security Boundary](Execution-Backends-and-Security-Boundary.md) — The local and remote execution options and the security model around code execution.
- [CLI, UI, and Library Assembly](CLI,-UI,-and-Library-Assembly.md) — How the package is wired into command-line and Gradio entry points.