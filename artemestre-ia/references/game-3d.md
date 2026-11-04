# Game Asset Creator e 3D Art

## Saidas distintas

- **Arte com aparencia 3D:** imagem renderizada 2D em PNG/JPEG/WebP; luz, material PBR plausivel, oclusao, reflexos e perspectiva. Nao e mesh.
- **Modelo 3D real:** geometria, texturas, materiais, UV, rig e formatos (GLB/GLTF/OBJ/FBX) requerem ferramentas de modelagem e verificacao apropriadas. Nao prometer exportacao nativa sem acesso a pipeline real.
- **Sprite / spritesheet:** exigir orientacao, tamanho de frame, grade, alpha, pivot, poses, FPS se animado e consistencia de silhueta. Manter sujeito dentro dos quadros.
- **Cenario / UI / icone:** projetar para camera, motor grafico, resolucao e integracao concretos quando informados.

## Checklist de cena

Definir sujeito, escala, estilo, camera, luz principal e preenchimento, materiais, detalhes, fundo, alpha, sombras e limites de textura. Para estilo 'moderno', evitar brilho excessivo e detalhes que prejudiquem legibilidade no tamanho de uso.

Em game assets, evitar fundo incorporado quando transparência e requerida. Confirmar que bordas nao cortam personagem e que luz/cor condizem com o pack. Nao modificar nenhum arquivo do jogo sem aprovacao de alteracao.
