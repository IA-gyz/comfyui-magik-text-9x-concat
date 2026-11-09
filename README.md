# Magik Text 9x Concat

Extract this folder into ComfyUI/custom_nodes/, restart ComfyUI, then refresh the browser.
Find **Magik Text 9x Concat** under **Magik/text**.

Nine multiline STRING inputs are concatenated in numerical order into one STRING output (`concat`). Inputs can also receive connected strings using ComfyUI widget-to-input conversion.

- `delimiter`: inserted between all nine inputs; default is a comma. Enter literal `\n` for line breaks.
- Empty inputs retain their position, matching the original node: they still contribute delimiters.
- `Enable Dynamic Prompts`: resolves choices such as `{red|blue}` in text widgets when queued. Supports nested choices and escaped braces/pipes. Connected strings pass through as supplied.

Installs alongside the original Magik Text Concatenate. No extra dependencies.
