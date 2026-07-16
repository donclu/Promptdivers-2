# Promptdivers — Claude Code Plugin

Marco operativo multi-agente (temática Helldivers) empaquetado como plugin nativo de
Claude Code. Autocontenido: incluye skills, comandos y **toda la doctrina** (AGENTS,
squads, protocols, stratagems, docs). Rutas resueltas con `${CLAUDE_PLUGIN_ROOT}`, así
que funciona instalado en cualquier proyecto, no solo dentro de este repo.

## Qué trae

| Componente | Cantidad | Qué es |
|---|---|---|
| **Skills** | 6 | orchestrator, pelican, tactical-signals, stratagem-terminal, orbital-control, ministry-of-truth |
| **Comandos** | 18 | `/status`, `/save`, `/debrief`, `/extract`, `/onboard`, `/induct`, `/orient`, `/promote`, `/escalate`, `/scope-check`, `/abort`, `/total-democracy`, … |
| **Doctrina** | — | `AGENTS.md`, `QUICK_REFERENCE.md`, `ORIENTATION.md`, `protocols/`, `squads/`, `stratagems/`, `docs/`, `templates/` |
| **Semilla** | — | `knowledge/`, `experience/`, `induction/` (ejemplos de referencia) |

## Instalación

Desde una sesión interactiva de Claude Code, apuntando al repo como marketplace local:

```
/plugin marketplace add /ruta/al/repo/Promptdivers-2
/plugin install promptdivers@promptdivers-marketplace
```

O, si publicas el repo en GitHub:

```
/plugin marketplace add donclu/Promptdivers-2
/plugin install promptdivers@promptdivers-marketplace
```

Reinicia la sesión tras instalar para que se registren skills y comandos.

## Modelo de rutas

- **Doctrina (solo lectura)** viaja dentro del plugin y se referencia con
  `${CLAUDE_PLUGIN_ROOT}/…` — p.ej. `${CLAUDE_PLUGIN_ROOT}/protocols/tactical-signals.md`.
- **Estado por-proyecto (lectura/escritura)** se deja relativo y lo crea el agente en el
  proyecto del usuario: `PROJECT_LOG.md`, `GALACTIC_WAR_MAP.md`, `NEXT_MISSION.md`,
  `missions/`, `knowledge/`, `experience/`.

## Regla de Squad B

**THE FORGE** y **THE EXECUTOR** no pueden ser el mismo agente en una misma corrida.

## Fuente

Generado desde [Promptdivers-2](https://github.com/donclu/Promptdivers-2) v3.5.0.
La fuente de verdad de reglas/stack/permisos sigue siendo `AGENTS.md`.
