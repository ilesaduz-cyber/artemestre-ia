# Histórico de versões

## 3.0.0 — 2026-11-04

- Nome público em português: ArteMestre IA.
- README completo em português e resumo em inglês.
- Distribuição portátil em pasta e ZIP de Skill.
- Regras de segurança, fidelidade e pesquisa mantidas da base comunitária.
- Validação estrutural reescrita: falha de verdade (sem `assert`), checa links, manifestos, módulos não roteados, segredos e caminhos locais; termos privados ficam em `private/denylist.txt`, fora do Git.
- Manifesto de plugin e marketplace para instalar pelo `/plugin` do Claude Code.
- `scripts/build_zip.py` gera o ZIP da Skill; GitHub Actions valida e gera o ZIP a cada push.
- Removido `README.pt-BR.md`, que ainda descrevia a versão antiga.

## 2.1.0 — Community Edition

- Consolidação dos cinco módulos de direção e revisão visual.
