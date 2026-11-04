# Protocolo de imagem enviada — analise, reproducao e melhoria

1. Inspecionar a imagem fornecida antes de propor novas artes. Descrever somente o que e visivel: personagens, materiais, disposicao, cores, textos legiveis, danos e artefatos. Nao inferir identidade de pessoas reais.
2. Classificar o objetivo: **analise**, **edicao localizada**, **restauro**, **upscale**, **recriacao fiel**, **variacao guiada**, **estilizacao**. Nao assumir que 'melhorar' significa mudar estilo.
3. Criar mapa de invariantes: identidade visual, feicoes, tonalidade de pele, cabelo, silhueta, pose, figurino, logotipo, texto, fundo, enquadramento, perspectiva, escala, numero de objetos.
4. Em edicao, explicitar somente a regiao/atributo autorizado a mudar; evitar recaracterizar fundo, rosto, textos e marcas. Se o usuario pedir manter todas as feicoes, usar a imagem original como fonte, nao gerar um sósia livre.
5. Em restauro, priorizar remocao de riscos, manchas, ruido, desfoque moderado e ajuste tonal. Informar quando detalhes ausentes precisarem ser inferidos. Em imagens historicas, nao inventar objetos ou pessoas.
6. Em reproducao fiel, preservar enquadramento e conteudo, mas esclarecer que um modelo generativo pode variar detalhes e nao equivale a copia pixel perfeita. Se upscale deterministico estiver disponivel e atender, preferi-lo a redesenho generativo.
7. Para impressao, consultar `production-outputs.md`; para personagens recorrentes consultar `character-consistency.md`.
8. Checklist antes de entrega: nao surgiram personagens/objetos a mais, textos nao mudaram, partes anatômicas estao coerentes, fundo e marca foram preservados, modificacoes condizem com pedido.
