# Visual Quality Control — checklist e testes

## Checagem de toda producao

1. **Objetivo:** entregou o output pedido (imagem, edicao, SVG verdadeiro, modelagem real, etc.)?
2. **Fidelidade:** preservou todos os invariantes, identidade e marcas da referencia?
3. **Composicao:** enquadramento, proporcao, distancia focal implícita, legibilidade, bordas, alinhamento?
4. **Anatomia e estrutura:** maos, dedos, membros, rostos, olhos, perspectiva, volumes, intersecoes, artefatos?
5. **Materiais/iluminacao:** sombras, reflexos, luz, texturas e coerencia do estilo?
6. **Texto/marca:** ortografia, numeros, logotipos, dados comerciais, ausencia de elementos inventados?
7. **Formato:** resolucao, alpha, DPI verificavel, dimensoes, uso em plataforma/impressao, arquivo real?
8. **Integridade:** nao incorporar assinatura/marca d'agua nem copiar ativos protegidos sem autorizacao?

## Testes de roteamento antes de entregar pacote

| Entrada de teste | Expectativa |
| --- | --- |
| 'Crie uma arte abstrata moderna' | Ativar Art Director; criar conforme pedido; sem busca obrigatoria |
| 'Reproduza esta foto sem mudar as pessoas' | Ativar modo fidelidade e image-reference; conservar feicoes; nao estilizar |
| 'Crie vista lateral do personagem oficial' | Recuperar referencia de personagem; avisar caso nao esteja acessivel |
| 'Banner de venda para rede social' | Comercial; objetivo, texto verificavel, composicao de anuncio |
| 'Crie personagem em 3D para o jogo' | Diferenciar render 3D de mesh real; usar game-3d |
| 'Pesquise tendencias atuais deste estilo' | Usar pesquisa atual com fontes, se disponivel |
| 'Melhore qualidade da foto anexada' | Nao redesenhar indiscriminadamente; preferir restauro tecnico |
| 'Salve esta nova arte como oficial' | Solicitar aprovacao explicita e acesso ao destino antes de gravar |

## Registro simples por resultado

- Resultado atendido: sim / parcial / nao.
- Desvios observados e sua gravidade: alto, medio, baixo.
- Proxima correção mais util; nenhuma nova geracao se nao houver necessidade.

Testes de texto/estrutura nao substituem avaliacao visual com arquivos gerados reais.
