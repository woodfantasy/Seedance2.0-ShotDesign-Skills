[English](README.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | Español | [Português](README.pt.md) | [Français](README.fr.md)

<p align="center"><img src="assets/logo.svg" width="128" height="128" alt="Seedance Shot Design Logo"></p>

<h1 align="center">Seedance 2.5 Shot Design</h1>

<p align="center"><strong>Dirección, prompts, extensión y edición con selección de modo para Jimeng Seedance 2.5</strong></p>

<p align="center">
  <img src="https://img.shields.io/badge/version-3.1.0-blue.svg" alt="Versión 3.1.0">
  <img src="https://img.shields.io/badge/license-MIT--0-green.svg" alt="MIT-0">
  <img src="https://img.shields.io/badge/platform-Seedance_2.5-purple.svg" alt="Seedance 2.5">
</p>

Seedance Shot Design convierte una idea o un vídeo aprobado en un plan de producción y un prompt listo para Seedance 2.5. La versión 3.0 es una reescritura para generación estándar de 30 s, vídeo ultralargo de 30–180 s, referencias multimodales, extensión, edición precisa y flujos industriales.

## Novedades de 3.0

| Área | Adaptación a Seedance 2.5 |
|---|---|
| Generación estándar | 4–30 s continuos; exactamente 30 s permanece en modo estándar por defecto |
| Vídeo ultralargo | 30–180 s con biblia de continuidad, actos, secuencias y cierre |
| Extensión | Fuente ≤30 s, añade 4–30 s, resultado ≤60 s; el prompt solo afecta al tramo nuevo |
| Materiales | Hasta 30 imágenes, 10 vídeos y 10 audios, con límites por tipo |
| Edición | Edición inteligente, edición avanzada con anotaciones, sustitución/eliminación local y cambio de punto de vista |
| Audio | Referencia solo de audio, timbre, diálogo multilingüe y eliminación de BGM conservando voz y ambiente |
| Producción | Transferencia creativa, croma, white model grueso/fino, transición fluida y storyboard multipanel |

Se eliminaron las reglas antiguas: división obligatoria por encima de 15 s, límite mixto 9/3/3/12, tope universal de 500 caracteres, inglés forzado y afirmaciones no verificadas sobre 1080p o CLI.

## Novedades de 3.1

| Área | Mejora |
|---|---|
| Guía de primer uso | Guía rápida, plantilla mínima y ejemplos representativos en la primera invocación |
| Ejemplos oficiales | Ejemplos de referencia de la documentación oficial de ByteDance / Dreamina |
| Instalación rápida | Soporte de instalación con `npx --yes skills@latest add` |
| Línea de tiempo precisa | Enrutamiento dedicado para vídeos de exactamente 30 s con control por segundo |

## Modos compatibles

- `standard`: referencia general / fotogramas inicial-final, 4–30 s
- `ultra_long`: vídeo ultralargo, 30–180 s
- `extension`: extensión de vídeo
- `smart_edit` / `advanced_edit`: edición inteligente / avanzada
- `viewpoint`: cambio de perspectiva espacial
- `bgm`: edición de pista de audio
- `creative_transfer`: transferencia creativa
- `green_screen`: edición de croma
- `rough_white_model` / `fine_white_model`: white model grueso / fino
- `seamless_transition`: transición fluida
- `storyboard`: storyboard multipanel

## Flujo de trabajo

1. Extrae objetivo, duración, formato, materiales y audio.
2. Elige un único modo principal.
3. Carga solo las referencias necesarias.
4. Asigna a cada material una función, alcance y exclusiones.
5. Diseña tiempo, causalidad y continuidad.
6. Valida según el modo y entrega un prompt autocontenido.

## Instalación

### Instalación rápida (recomendada)

```bash
npx --yes skills@latest add woodfantasy/Seedance-ShotDesign-Skills -g -y
```

### Instalación manual

Coloca la carpeta en el directorio de skills del agente:

```text
.claude/skills/seedance-shot-design/
~/.codex/skills/seedance-shot-design/
.cursor/skills/seedance-shot-design/
```

Invocación explícita:

```text
Use $seedance-shot-design to design a continuous 30-second vertical suspense film.
```

## Validador

```bash
python3 scripts/validate_prompt.py --mode standard --duration 30 --resolution 720p --prompt-file prompt.txt
python3 -m unittest scripts/test_validate.py
```

En extensión, `--duration` es la duración añadida; `--source-duration` permite verificar el máximo final de 60 s.

## Notas de plataforma

- El manual proporcionado documenta salidas de 480p y 720p. `720P+` aparece como etiqueta de interfaz, no como parámetro 1080p confirmado.
- Las recomendaciones de estabilidad se distinguen de los límites estrictos.
- Se conservan los tokens de la interfaz, por ejemplo `@图片1`, `@视频1` y `@音频1`.
- La skill diseña y valida prompts; no envía generaciones ni consume créditos.

## Licencia

[MIT-0](LICENSE)
