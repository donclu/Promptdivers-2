# Auditoría — Calidad de datos y control de ingestión (Ventas maquinaria)

## Alcance
- Dominio: ventas de maquinaria industrial (construcción/minería), repuestos y servicios; por país y sucursal.
- Riesgo: reporting comercial/contable, pricing, forecasting, conciliación, fraude.
- Evidencia: `profile_out/metrics.json`, `clean_out/dq_report.json`, `clean_out/industrial_sales_quarantine.csv`, `report_out/plots/*`.

## Hallazgos (con severidad)

### HIGH
- **[H-1] Inconsistencia `country↔branch_code`**
  - Evidencia: `country_branch_mismatch = 0`
  - Riesgo: segmentación por país contaminada; agregaciones inválidas.
  - Recomendación: validación en ingestión + catálogo maestro de sucursales + rejects.

- **[H-2] Fechas inválidas / no parseables**
  - Evidencia: `date_parse_fail = 2207`
  - Riesgo: cortes de periodo, aging, forecast erróneo.
  - Recomendación: formato ISO obligatorio + reject/quarantine + contrato de datos.

### MED
- **[M-1] `invoice_id` faltante o duplicado**
  - Evidencia: missing = `678`, dupes = `117`
  - Riesgo: doble conteo; conciliación imposible.
  - Recomendación: constraint de unicidad upstream + reglas de rechazo.

- **[M-2] `unit_price` / `qty_or_hours` con formatos no estándar**
  - Evidencia: unit_price parse fails = `588`, qty parse fails = `576`
  - Riesgo: totales erróneos; outliers falsos.
  - Recomendación: normalización + separación de unidades + campos tipados.

### LOW
- **[L-1] Invisibles / mojibake en `customer_name`**
  - Evidencia: invisibles = `1592`, mojibake = `166`
  - Riesgo: matching/CRM/duplicados.
  - Recomendación: limpieza de encoding + tests de ingestión.

## Controles propuestos
- **Preventivos**: esquema tipado, dominios, catálogos (country/branch/SKU), constraints, contratos.
- **Detectivos**: profiling periódico, drift, alertas por umbrales.
- **Correctivos**: quarantine + workflow de remediación + trazabilidad.

## Estado
- Auditoría: PASS | PARTIAL | FAIL (según umbrales definidos)

