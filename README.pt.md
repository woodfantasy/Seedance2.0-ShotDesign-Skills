[English](README.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | Português | [Français](README.fr.md)

<p align="center"><img src="assets/logo.svg" width="128" height="128" alt="Seedance Shot Design Logo"></p>

<h1 align="center">Seedance 2.5 Shot Design</h1>

<p align="center"><strong>Direção, prompts, extensão e edição com roteamento por modo para Jimeng Seedance 2.5</strong></p>

<p align="center">
  <img src="https://img.shields.io/badge/version-3.1.0-blue.svg" alt="Versão 3.1.0">
  <img src="https://img.shields.io/badge/license-MIT--0-green.svg" alt="MIT-0">
  <img src="https://img.shields.io/badge/platform-Seedance_2.5-purple.svg" alt="Seedance 2.5">
</p>

Seedance Shot Design transforma uma ideia ou vídeo aprovado em plano de produção e prompt pronto para o Seedance 2.5. A versão 3.0 foi reescrita para geração padrão de 30 s, vídeos ultralongos de 30–180 s, referências multimodais, extensão, edição precisa e fluxos industriais.

## Principais mudanças da 3.0

| Área | Adaptação ao Seedance 2.5 |
|---|---|
| Geração padrão | 4–30 s contínuos; exatamente 30 s permanece no modo padrão por padrão |
| Ultralongo | 30–180 s com bíblia de continuidade, atos, sequências e encerramento |
| Extensão | Fonte ≤30 s, acrescenta 4–30 s, final ≤60 s; o prompt afeta apenas o trecho novo |
| Materiais | Até 30 imagens, 10 vídeos e 10 áudios, com limites por tipo |
| Edição | Edição inteligente, avançada com anotações, substituição/remoção local e reconstrução de ponto de vista |
| Áudio | Referência apenas de áudio, timbre, diálogo multilíngue e remoção de BGM preservando voz e ambiente |
| Produção | Transferência criativa, chroma key, white model bruto/fino, transição contínua e storyboard multipainel |

Foram removidas as regras antigas: divisão obrigatória acima de 15 s, limite misto 9/3/3/12, teto universal de 500 caracteres, inglês forçado e alegações não verificadas de 1080p ou CLI.

## Novidades da 3.1

| Área | Melhoria |
|---|---|
| Guia de primeiro uso | Guia rápido, modelo mínimo e exemplos representativos na primeira invocação |
| Exemplos oficiais | Exemplos de referência da documentação oficial ByteDance / Dreamina |
| Instalação rápida | Suporte a instalação com `npx --yes skills@latest add` |
| Linha do tempo precisa | Roteamento dedicado para vídeos de exatamente 30 s com controle por segundo |

## Modos compatíveis

- `standard`: referência geral / quadros inicial-final, 4–30 s
- `ultra_long`: vídeo ultralongo, 30–180 s
- `extension`: extensão de vídeo
- `smart_edit` / `advanced_edit`: edição inteligente / avançada
- `viewpoint`: alteração de perspectiva espacial
- `bgm`: edição de faixa de áudio
- `creative_transfer`: transferência criativa
- `green_screen`: edição com chroma key
- `rough_white_model` / `fine_white_model`: white model bruto / fino
- `seamless_transition`: transição contínua
- `storyboard`: storyboard multipainel

## Fluxo de trabalho

1. Extrai objetivo, duração, proporção, materiais e áudio.
2. Escolhe um único modo principal.
3. Carrega apenas as referências necessárias.
4. Vincula cada material a função, escopo e exclusões.
5. Planeja tempo, causalidade e continuidade.
6. Valida pelo modo e entrega um prompt autocontido.

## Instalação

### Instalação rápida (recomendada)

```bash
npx --yes skills@latest add woodfantasy/Seedance-ShotDesign-Skills -g -y
```

### Instalação manual

Coloque a pasta no diretório de skills do agente:

```text
.claude/skills/seedance-shot-design/
~/.codex/skills/seedance-shot-design/
.cursor/skills/seedance-shot-design/
```

Invocação explícita:

```text
Use $seedance-shot-design to design a continuous 30-second vertical suspense film.
```

## Validador

```bash
python3 scripts/validate_prompt.py --mode standard --duration 30 --resolution 720p --prompt-file prompt.txt
python3 -m unittest scripts/test_validate.py
```

Na extensão, `--duration` é o tempo acrescentado; `--source-duration` verifica o limite final de 60 s.

## Notas da plataforma

- O manual fornecido documenta saída em 480p e 720p. `720P+` é um rótulo da interface, não um parâmetro 1080p confirmado.
- Recomendações de estabilidade são separadas dos limites rígidos.
- Tokens da interface, como `@图片1`, `@视频1` e `@音频1`, são preservados.
- A skill projeta e valida prompts; não envia gerações nem consome créditos.

## Licença

[MIT-0](LICENSE)
