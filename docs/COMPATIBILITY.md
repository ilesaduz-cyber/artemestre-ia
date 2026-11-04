# Compatibility matrix

| Platform | Delivery mechanism | Auto-selection | Image output | Notes |
| --- | --- | --- | --- | --- |
| Claude Code | `~/.claude/skills/artemestre-ia/` or `.claude/skills/artemestre-ia/` | Supported when relevant | Requires image tools | Uses standard `SKILL.md` layout |
| ChatGPT with custom Skills | Import ZIP in a supported Skills UI | Depends on configuration | Requires built-in image generation | Keep personal canon outside public package |
| Other agents with Agent Skills support | Vendor skill directory | Depends on vendor | Depends on host tool | Use `SKILL.md` and `references/` |
| Generic assistants | Paste `SKILL.md` instructions | Manual | Depends on host tool | Does not install automatically |

This repository does not bundle model weights or a 3D engine. Compatibility is a documentation claim, not a live integration test on every platform.
