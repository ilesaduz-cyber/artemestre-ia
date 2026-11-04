# ArteMestre IA 🎨

**Da ideia à arte.** Uma Skill gratuita e aberta que transforma agentes de IA em assistentes de direção criativa, análise de imagens, geração visual, design comercial e arte para jogos.

> **ArteMestre IA** é um conjunto de instruções e fluxos de trabalho, **não** um novo modelo de geração de imagens. Os resultados dependem das ferramentas do agente hospedeiro.

## Para que serve

| Especialidade | Função |
| --- | --- |
| **Direção de Arte** | Composição, cinematografia, cor, perspectiva e iluminação |
| **Personagens Consistentes** | Preservar identidade e referências entre imagens |
| **Arte Comercial** | Campanhas, anúncios, banners, marcas e tipografia |
| **Game Art e 3D** | Concept art, assets, sprites e renders com aparência 3D |
| **Controle de Qualidade** | Conferir fidelidade, detalhes, limitações e exportação |

Inclui **interpretação de imagens anexadas**, reprodução orientada por referência, restauração, modernização, pesquisa visual na web (quando disponível), formatos para impressão e separação de padrões por projeto.

## Instalação rápida

### Claude Code — como plugin

```text
/plugin marketplace add ilesaduz-cyber/artemestre-ia
/plugin install artemestre-ia@artemestre-ia
```

Instalada como plugin, a Skill aparece como `artemestre-ia:artemestre-ia`.

### Claude Code — copiando a pasta

```bash
git clone https://github.com/ilesaduz-cyber/artemestre-ia.git
cp -r artemestre-ia/artemestre-ia ~/.claude/skills/
```

Isso instala para uso pessoal em todos os projetos. Para um projeto só, copie a pasta para `.claude/skills/artemestre-ia/` dentro dele. Abra uma sessão nova depois de instalar.

### Claude.ai — Skills

Baixe `artemestre-ia.zip` na página de **Releases** do repositório (ou gere com `python scripts/build_zip.py`) e importe em **Configurações → Capacidades → Skills**, quando o recurso estiver disponível na sua conta. O ZIP contém apenas a pasta `artemestre-ia/` com `SKILL.md`, referências e metadados.

### ChatGPT e agentes compatíveis com `SKILL.md`

Importe a pasta ou o pacote na interface de Skills do ambiente quando disponível. O modo de instalação e a ativação automática variam conforme a plataforma.

### Assistentes sem sistema de Skills

Forneça `artemestre-ia/SKILL.md` como instrução de sistema ou contexto reutilizável, acompanhada dos módulos relevantes em `references/`. Esse modo é **manual**, não uma instalação automática.

## Exemplos de pedidos

```text
Crie uma arte cinematográfica original de um explorador em um planeta oceânico.

Reproduza a imagem anexada com maior qualidade. Preserve rosto, roupa e composição.

Faça um personagem consistente em três vistas, com fundo transparente.

Crie um banner de lançamento para um aplicativo fictício com tipografia legível.

Crie um conceito visual FPS hiper-realista com três robôs e iluminação volumétrica.

Pesquise estilos visuais atuais para este tema e cite as referências utilizadas.
```

## Como funciona

1. Interpreta a intenção e distingue criação, edição, reprodução fiel e análise.
2. Identifica referências e invariantes (rosto, pose, marca, cores, proporções).
3. Seleciona os módulos especializados necessários.
4. Pesquisa referências recentes somente se houver benefício ou solicitação.
5. Usa ferramentas nativas do agente, se disponíveis, para gerar/editar.
6. Verifica problemas visuais, adequação do formato e limitações reais.
7. Preserva padrões por projeto sem publicar ou salvar arquivos sem consentimento.

## Estrutura

```text
artemestre-ia-public/
├── README.md                 # apresentação em português
├── README.en.md              # English overview
├── LICENSE                   # MIT
├── CONTRIBUTING.md           # contribuições
├── SECURITY.md               # segurança e privacidade
├── CHANGELOG.md              # versões
├── .claude-plugin/           # manifesto de plugin e marketplace (Claude Code)
├── .github/workflows/        # validação automática em cada push e PR
├── artemestre-ia/
│   ├── SKILL.md              # entrada portável
│   ├── agents/openai.yaml    # metadados opcionais
│   └── references/           # módulos especializados
│       ├── art-direction.md
│       ├── character-consistency.md
│       ├── commercial-brand.md
│       ├── game-3d.md
│       ├── image-reference.md
│       ├── production-outputs.md
│       ├── project-memory.md
│       ├── quality-control.md
│       └── visual-research.md
├── docs/
│   ├── COMPATIBILITY.md
│   └── TEST-PLAN.md
└── scripts/
    ├── validate.py           # teste estrutural e de privacidade, offline
    └── build_zip.py          # gera dist/artemestre-ia.zip
```

## Testes

```bash
python scripts/validate.py
python scripts/build_zip.py
```

O `validate.py` confere o frontmatter do `SKILL.md`, se todo módulo citado existe e se todo módulo é roteado, os manifestos do plugin, links relativos e se nenhum segredo, caminho local ou e-mail pessoal entrou nos arquivos públicos. Termos privados extras (nomes de clientes, projetos) podem ir em `private/denylist.txt`, um por linha; a pasta não vai para o Git. O GitHub Actions roda os dois scripts a cada push.

Esses testes não substituem os testes de geração real descritos em [docs/TEST-PLAN.md](docs/TEST-PLAN.md).

## Limitações

- Uma imagem com aparência 3D não é uma malha 3D editável.
- Reprodução com modelos generativos não garante identidade pixel a pixel.
- Não acessa automaticamente arquivos antigos ou memórias de outras plataformas.
- Não instala motores gráficos, conecta contas, publica ou altera projetos por conta própria.
- Não reproduz obras de terceiros de forma integral sem os direitos necessários.

## Comunidade

Sugestões, testes, correções e contribuições são bem-vindos. Leia [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md) e [LICENSE](LICENSE).

**Autor:** Guinão Morais ([@ilesaduz-cyber](https://github.com/ilesaduz-cyber)). **Licença:** MIT. **Origem:** evolução comunitária de um fluxo de direção visual previamente chamado GPT Creative Studio.
