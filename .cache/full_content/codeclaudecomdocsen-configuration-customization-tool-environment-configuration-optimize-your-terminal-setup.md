[Skip to main content](#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/light.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=d535f2e20f53cd911acc59ad1b64b2e0)![dark logo](https://mintcdn.com/claude-code/TBPmHzr19mDCuhZi/logo/dark.svg?fit=max&auto=format&n=TBPmHzr19mDCuhZi&q=85&s=28e49a2ffe69101f4aae9bfa70b393d0)](/docs)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘KAsk AI

Search...

Navigation

Configuration

Optimize your terminal setup

[Getting started](/docs/en/overview)[Build with Claude Code](/docs/en/sub-agents)[Deployment](/docs/en/third-party-integrations)[Administration](/docs/en/setup)[Configuration](/docs/en/settings)[Reference](/docs/en/cli-reference)[Resources](/docs/en/legal-and-compliance)

##### Configuration

* [Settings](/docs/en/settings)
* [Permissions](/docs/en/permissions)
* [Sandboxing](/docs/en/sandboxing)
* [Terminal configuration](/docs/en/terminal-config)
* [Model configuration](/docs/en/model-config)
* [Speed up responses with fast mode](/docs/en/fast-mode)
* [Memory management](/docs/en/memory)
* [Customize status line](/docs/en/statusline)
* [Customize keyboard shortcuts](/docs/en/keybindings)

On this page

* [Themes and appearance](#themes-and-appearance)
* [Line breaks](#line-breaks)
* [Notification setup](#notification-setup)
* [iTerm 2 system notifications](#iterm-2-system-notifications)
* [Custom notification hooks](#custom-notification-hooks)
* [Handling large inputs](#handling-large-inputs)
* [Vim Mode](#vim-mode)

### [​](#themes-and-appearance) Themes and appearance

Claude cannot control the theme of your terminal. That’s handled by your terminal application. You can match Claude Code’s theme to your terminal any time via the `/config` command.
For additional customization of the Claude Code interface itself, you can configure a [custom status line](/docs/en/statusline) to display contextual information like the current model, working directory, or git branch at the bottom of your terminal.

### [​](#line-breaks) Line breaks

You have several options for entering line breaks into Claude Code:

* **Quick escape**: Type `\` followed by Enter to create a newline
* **Shift+Enter**: Works out of the box in iTerm2, WezTerm, Ghostty, and Kitty
* **Keyboard shortcut**: Set up a keybinding to insert a newline in other terminals

**Set up Shift+Enter for other terminals**
Run `/terminal-setup` within Claude Code to automatically configure Shift+Enter for VS Code, Alacritty, Zed, and Warp.

The `/terminal-setup` command is only visible in terminals that require manual configuration. If you’re using iTerm2, WezTerm, Ghostty, or Kitty, you won’t see this command because Shift+Enter already works natively.

**Set up Option+Enter (VS Code, iTerm2 or macOS Terminal.app)**
**For Mac Terminal.app:**

1. Open Settings → Profiles → Keyboard
2. Check “Use Option as Meta Key”

**For iTerm2 and VS Code terminal:**

1. Open Settings → Profiles → Keys
2. Under General, set Left/Right Option key to “Esc+“

### [​](#notification-setup) Notification setup

Never miss when Claude completes a task with proper notification configuration:

#### [​](#iterm-2-system-notifications) iTerm 2 system notifications

For iTerm 2 alerts when tasks complete:

1. Open iTerm 2 Preferences
2. Navigate to Profiles → Terminal
3. Enable “Silence bell” and Filter Alerts → “Send escape sequence-generated alerts”
4. Set your preferred notification delay

Note that these notifications are specific to iTerm 2 and not available in the default macOS Terminal.

#### [​](#custom-notification-hooks) Custom notification hooks

For advanced notification handling, you can create [notification hooks](/docs/en/hooks#notification) to run your own logic.

### [​](#handling-large-inputs) Handling large inputs

When working with extensive code or long instructions:

* **Avoid direct pasting**: Claude Code may struggle with very long pasted content
* **Use file-based workflows**: Write content to a file and ask Claude to read it
* **Be aware of VS Code limitations**: The VS Code terminal is particularly prone to truncating long pastes

### [​](#vim-mode) Vim Mode

Claude Code supports a subset of Vim keybindings that can be enabled with `/vim` or configured via `/config`.
The supported subset includes:

* Mode switching: `Esc` (to NORMAL), `i`/`I`, `a`/`A`, `o`/`O` (to INSERT)
* Navigation: `h`/`j`/`k`/`l`, `w`/`e`/`b`, `0`/`$`/`^`, `gg`/`G`, `f`/`F`/`t`/`T` with `;`/`,` repeat
* Editing: `x`, `dw`/`de`/`db`/`dd`/`D`, `cw`/`ce`/`cb`/`cc`/`C`, `.` (repeat)
* Yank/paste: `yy`/`Y`, `yw`/`ye`/`yb`, `p`/`P`
* Text objects: `iw`/`aw`, `iW`/`aW`, `i"`/`a"`, `i'`/`a'`, `i(`/`a(`, `i[`/`a[`, `i{`/`a{`
* Indentation: `>>`/`<<`
* Line operations: `J` (join lines)

See [Interactive mode](/docs/en/interactive-mode#vim-editor-mode) for the complete reference.

Was this page helpful?

YesNo

[Sandboxing](/docs/en/sandboxing)[Model configuration](/docs/en/model-config)

Assistant

Responses are generated using AI and may contain mistakes.