# Registro de cambios / Changelog

Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).

## [Sin publicar / Unreleased]

### Cambiado / Changed
- La procedencia de las 37 skills se verificó byte a byte contra la API pública de ClawHub y quedó registrada en `procedencia.json`. / The provenance of the 37 skills was verified byte for byte against ClawHub's public API and recorded in `procedencia.json`.
- Los README distinguen skills de la comunidad (15, copias sin cambios), derivadas (2) y propias (20), con el autor real de cada una. / The READMEs tell community (15, unchanged copies), derived (2) and own (20) skills apart, with each one's real author.

### Corregido / Fixed
- Se quitó la afirmación falsa de que 13 skills propias estaban publicadas en ClawHub y los `homepage` de `clawic.com` que daban 404. / Removed the false claim that 13 own skills were published on ClawHub, and the `clawic.com` homepages that returned 404.
- `meeting-notes` deja de figurar con autor no identificable: es de `tinadu-ai`. `cybersecurity`, `content-marketing` y `seo` se acreditan a `ivangdavila`. / `meeting-notes` no longer lists an unidentifiable author: it is by `tinadu-ai`. `cybersecurity`, `content-marketing` and `seo` are credited to `ivangdavila`.
- `programming` y `graphic-design` se declaran como derivadas de sus autores originales. / `programming` and `graphic-design` are declared as derived from their original authors.

### Añadido / Added
- `LICENSE` (MIT), `NOTICE.md` con los avisos de terceros (MIT-0 de ClawHub y MIT de `mattpocock/skills`), `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`.
- `scripts/procedencia.py` y sus pruebas, y CI con escaneo de secretos, comprobación de procedencia y verificación semanal contra ClawHub. / `scripts/procedencia.py` and its tests, and CI with secret scanning, a provenance check and a weekly verification against ClawHub.
