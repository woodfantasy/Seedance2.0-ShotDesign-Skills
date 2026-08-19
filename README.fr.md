[English](README.md) | [中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Português](README.pt.md) | Français

<p align="center"><img src="assets/logo.svg" width="128" height="128" alt="Seedance Shot Design Logo"></p>

<h1 align="center">Seedance 2.5 Shot Design</h1>

<p align="center"><strong>Réalisation, prompts, extension et montage avec routage par mode pour Jimeng Seedance 2.5</strong></p>

<p align="center">
  <img src="https://img.shields.io/badge/version-3.1.0-blue.svg" alt="Version 3.1.0">
  <img src="https://img.shields.io/badge/license-MIT--0-green.svg" alt="MIT-0">
  <img src="https://img.shields.io/badge/platform-Seedance_2.5-purple.svg" alt="Seedance 2.5">
</p>

Seedance Shot Design transforme une idée ou une vidéo validée en plan de production et prompt prêt pour Seedance 2.5. La version 3.0 a été réécrite pour la génération standard de 30 s, les vidéos ultra-longues de 30–180 s, les références multimodales, l’extension, le montage précis et les workflows industriels.

## Principales nouveautés de la 3.0

| Domaine | Adaptation Seedance 2.5 |
|---|---|
| Génération standard | 4–30 s en continu ; exactement 30 s reste en mode standard par défaut |
| Ultra-long | 30–180 s avec bible de continuité, actes, séquences et conclusion |
| Extension | Source ≤30 s, ajout de 4–30 s, résultat ≤60 s ; le prompt ne concerne que la partie ajoutée |
| Médias | Jusqu’à 30 images, 10 vidéos et 10 audios, avec limites par type |
| Montage | Édition intelligente, avancée avec annotations, remplacement/suppression locale et reconstruction du point de vue |
| Audio | Référence audio seule, timbre, dialogues multilingues et suppression de BGM en conservant voix et ambiance |
| Production | Transfert créatif, fond vert, white model brut/fin, transition fluide et storyboard multipanneau |

Les anciennes règles ont été retirées : découpe obligatoire au-delà de 15 s, limite mixte 9/3/3/12, plafond universel de 500 caractères, anglais imposé et affirmations non vérifiées sur le 1080p ou une CLI.

## Nouveautés de la 3.1

| Domaine | Amélioration |
|---|---|
| Guide de première utilisation | Guide rapide, modèle minimal et exemples représentatifs au premier appel |
| Exemples officiels | Exemples de référence de la documentation officielle ByteDance / Dreamina |
| Installation rapide | Prise en charge de l'installation via `npx --yes skills@latest add` |
| Timeline précise | Routage dédié pour les vidéos de 30 s exactes avec contrôle seconde par seconde |

## Modes pris en charge

- `standard` : référence générale / images début-fin, 4–30 s
- `ultra_long` : vidéo ultra-longue, 30–180 s
- `extension` : extension vidéo
- `smart_edit` / `advanced_edit` : édition intelligente / avancée
- `viewpoint` : modification du point de vue spatial
- `bgm` : édition de piste audio
- `creative_transfer` : transfert créatif
- `green_screen` : montage fond vert
- `rough_white_model` / `fine_white_model` : white model brut / fin
- `seamless_transition` : transition vidéo fluide
- `storyboard` : storyboard multipanneau

## Workflow

1. Extraire objectif, durée, format, médias et exigences audio.
2. Choisir un seul mode principal.
3. Charger uniquement les références utiles.
4. Affecter à chaque média une fonction, une portée et des exclusions.
5. Concevoir temps, causalité et continuité.
6. Valider selon le mode et livrer un prompt autonome.

## Installation

### Installation rapide (recommandée)

```bash
npx --yes skills@latest add woodfantasy/Seedance-ShotDesign-Skills -g -y
```

### Installation manuelle

Placez le dossier dans le répertoire de skills de l’agent :

```text
.claude/skills/seedance-shot-design/
~/.codex/skills/seedance-shot-design/
.cursor/skills/seedance-shot-design/
```

Invocation explicite :

```text
Use $seedance-shot-design to design a continuous 30-second vertical suspense film.
```

## Validateur

```bash
python3 scripts/validate_prompt.py --mode standard --duration 30 --resolution 720p --prompt-file prompt.txt
python3 -m unittest scripts/test_validate.py
```

Pour l’extension, `--duration` désigne la durée ajoutée ; `--source-duration` permet de vérifier la limite finale de 60 s.

## Notes plateforme

- Le manuel fourni documente les sorties 480p et 720p. `720P+` est un libellé d’interface, pas un paramètre 1080p confirmé.
- Les recommandations de stabilité sont distinguées des limites strictes.
- Les tokens de l’interface, comme `@图片1`, `@视频1` et `@音频1`, sont conservés.
- La skill conçoit et valide les prompts ; elle ne lance pas de génération et ne consomme pas de crédits.

## Licence

[MIT-0](LICENSE)
