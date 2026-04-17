#!/bin/bash
# Test Paradoja del Flujo case with Claude Haiku
# Usage: ./experiments/test_paradoja_haiku.sh

set -e

REPO_ROOT="${1:-.}"
MODEL="claude-haiku-4-5-20251001"

cat << 'EOF'
========================================
PARADOJA DEL FLUJO — REASONING TEST
=====================================

Eres un auditor de sistemas experto en reglas de riesgo y lógica.

## Caso (copia exacta — test portátil)

Auditamos un sistema de mapeo jerárquico de procesos y gestión de riesgos. Cinco reglas inmutables:

1. Todo Flujo Maestro contiene ≥1 Subproceso con riesgo > 0.
2. Si un Subproceso maneja "Datos Públicos" → riesgo máximo = "Bajo" (1).
3. Si Subproceso incluye "Tarea de Extracción Automatizada" → hereda "Alto" (3).
4. Flujo Maestro "Admisión de Usuarios" tiene 1 Subproceso: "Validación de Perfil".
5. Subproceso "Validación de Perfil" maneja Datos Públicos Y ejecuta Tarea de Extracción Automatizada.

---

**Tu tarea:**
1. Analiza las 5 reglas y aplícalas al Subproceso "Validación de Perfil".
2. ¿Detectas una contradicción?
3. Si la hay, explica cuál es (en términos de lógica / restricciones).
4. ¿Cuál de las opciones A-E recomendarías? ¿Por qué?

**Opciones de Resolución:**

| Opción | Cambio | Viabilidad |
|--------|--------|-----------|
| A | Suprimir R3 (extracción es segura) | Baja |
| B | Suprimir R5 (no hacer extracción) | Media |
| C | Relajar R2 (público puede tener riesgo > 1) | Baja |
| D | Descomponer R5 (split en 2 subprocesos) | Alta |
| E | Escalar a stakeholder | Honesta |

Responde estructurado, con evidencia.

========================================
EOF

echo ""
echo "Model: $MODEL"
echo "Note: to run with actual API, use claude CLI:"
echo "  echo '<prompt>' | claude -m $MODEL"
echo ""
