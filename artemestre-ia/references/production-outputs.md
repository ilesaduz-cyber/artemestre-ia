# Entrega tecnica — formatos, dimensoes e impressao

- Perguntar tamanho/formato somente se ele for indispensavel e nao puder ser inferido do pedido.
- Distinguir proporcao da imagem de resolucao real; nunca afirmar 4K, 300 DPI ou dimensao especifica sem verificar arquivo resultante.
- Para print, definir dimensoes fisicas, sangria quando cabivel, margens, modo de cor e requisitos da grafica. Um JPEG RGB a 300 DPI declarado nao substitui PDF/X, CMYK ou arte final com sangria real.
- Calculo de pixels para tamanho fisico: pixels = polegadas x DPI. Converter cm para polegadas dividindo por 2.54.
- Transparencia somente quando arquivo suportar canal alpha e tiver sido verificada. JPEG nao tem transparencia.
- Diferenciar arquivo de visualizacao, master editavel, vetor SVG, mapa de textura, spritesheet e modelo 3D real.
- Conferir dimensoes, modo de cor, alpha, peso e extensao antes de dizer que entregou 'pronto para impressao' ou 'pronto para engine'.
- Se a ferramenta disponivel produz apenas raster, explicar a etapa complementar necessaria ao formato profissional.
