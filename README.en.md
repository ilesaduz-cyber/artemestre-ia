# ArteMestre IA

**From idea to artwork.** A portable, open-source visual direction Skill for compatible AI assistants. Its modules cover art direction, consistent characters, commercial design, game assets, 3D-looking renders, image-reference analysis, research and quality control.

ArteMestre IA is **instructions, not an image model**. The host needs vision/image tools for visual output, and web access for research.

## Install

- **Claude Code (plugin):** `/plugin marketplace add ilesaduz-cyber/artemestre-ia`, then `/plugin install artemestre-ia@artemestre-ia`.
- **Claude Code (project):** copy `artemestre-ia/` to `.claude/skills/artemestre-ia/`.
- **Claude Code (personal):** copy it to `~/.claude/skills/artemestre-ia/`.
- **Claude.ai:** upload `artemestre-ia.zip` from the Releases page (or build it with `python scripts/build_zip.py`) if custom Skills are enabled for your account.
- **Other compatible agents:** import the folder containing `SKILL.md` using the platform's supported path.
- **Without Skills support:** supply `SKILL.md` and relevant `references/` documents as instructions manually.

## Examples

- Create an original cinematic sci-fi scene.
- Enhance an attached portrait without changing the person's features.
- Generate consistent front and side character views.
- Plan a 3D-looking game scene and distinguish it from an actual editable mesh.
- Research current visual references and cite them when tools are available.

For full structure and testing instructions, see [README.md](README.md).

**License:** MIT. No private project assets are included.
