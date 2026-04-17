# Experimento 2: La Paradoja del Flujo Maestro
**Tipo:** Prueba de razonamiento lógico | **Modelo:** Haiku | **Fecha:** 2026-04-17

---

## Caso (copia exacta — test portátil)

Auditamos un sistema de mapeo jerárquico de procesos y gestión de riesgos. Cinco reglas inmutables:

1. Todo Flujo Maestro contiene ≥1 Subproceso con riesgo > 0.
2. Si un Subproceso maneja "Datos Públicos" → riesgo máximo = "Bajo" (1).
3. Si Subproceso incluye "Tarea de Extracción Automatizada" → hereda "Alto" (3).
4. Flujo Maestro "Admisión de Usuarios" tiene 1 Subproceso: "Validación de Perfil".
5. Subproceso "Validación de Perfil" maneja Datos Públicos Y ejecuta Tarea de Extracción Automatizada.

---

## Análisis: Trazo de Contradicción

**Aplicando reglas a "Validación de Perfil":**

| Regla | Implicación | Valor |
|-------|-------------|-------|
| R5 + R2 | Maneja Datos Públicos → riesgo ≤ 1 | Risk ≤ 1 |
| R5 + R3 | Ejecuta Extracción Automatizada → riesgo = 3 | Risk = 3 |
| **Lógica** | **Risk ≤ 1 AND Risk = 3** | **CONTRADICCIÓN** |

**Fórmula:**
```
∃ Subproceso S : 
  (Data = Public ∧ Task = Extraction)
  ∧ (Risk(S) ≤ 1) from R2
  ∧ (Risk(S) = 3) from R3
  ≡ FALSE (insatisfacible)
```

---

## Resultado: Estado del Sistema

🔴 **ESTADO: IRRESOLUTIBLE SIN MODIFICACIÓN DE REGLAS**

El sistema no puede estar en estado consistente. Una de estas es verdad:

- **R2 es suposición incorrecta** → Datos públicos pueden tener riesgo > 1 si hay extracción.
- **R3 es suposición incorrecta** → Extracción no siempre heredan riesgo 3.
- **R5 está sobreespecificada** → "Validación de Perfil" no puede hacer ambas cosas.
- **Arquitectura inviable** → Hay inconsistencia en el diseño del Flujo Maestro.

---

## Opciones de Resolución

| Opción | Cambio | Costo | Viabilidad |
|--------|--------|-------|-----------|
| A | Suprimir R3 (extracción es segura) | Asunción de seguridad sin prueba | Baja |
| B | Suprimir R5 (no hacer extracción) | Rediseño de funcionalidad | Media |
| C | Relajar R2 (público puede tener riesgo > 1) | Impacto normativo | Baja |
| D | Descomponer R5 (split en 2 subprocesos) | +1 arch complexity | **Alta** |
| E | Escalar a stakeholder | Requiere decisión humana | Honesta |

**Recomendación:** **D** (descomposición) si R2 y R3 son hard constraints.  
**Fallback:** **E** (escalada + revisión de supuestos).

---

## Conclusión

✅ **Paradoja detectada correctamente.**  
✅ **Cadena de razonamiento válida.**  
🟡 **Sistema requiere reparación de reglas o arquitectura.**

**Para el siguiente modelo:** Mismo caso, distinto modelo. ¿Encuentra la contradicción? ¿Qué opción recomienda?

---

**Etiquetas:** `reasoning` `logic` `contradiction-resolution` `business-rules` `audit`  
**Reusar:** Copiar bloque "Caso" a cualquier modelo LLM para comprobar capacidad de razonamiento.
