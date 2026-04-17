# Informe de Calidad de Datos — Ventas de maquinaria industrial (Construcción/Minería)

## 1. Resumen ejecutivo (½ página)
- Objetivo: evaluar calidad + corregir dataset sucio sintético **65.000 × 10** (maquinaria, repuestos, servicios) por país/sucursal.
- Resultado: tasa de limpieza vs quarantine, principales fallas, impacto esperado.

## 2. Alcance y fuentes
- Archivos:
  - Dirty: `dirty_industrial_sales.csv`
  - Clean: `clean_out/industrial_sales_clean.csv`
  - Quarantine: `clean_out/industrial_sales_quarantine.csv`
  - Perfilado: `profile_out/metrics.json`
  - DQ report: `clean_out/dq_report.json`
  - Plots: `report_out/plots/*`

## 3. Metodología (½ página)
- Ingesta tolerante a líneas rotas: lectura con `engine="python"` + `on_bad_lines="skip"`.
- Normalización:
  - strings: trim + remoción de invisibles (BOM/ZWSP/NULL)
  - fechas: parse multi-formato (ISO/DMY/MDY), invalid → fail
  - números: parse cross-locale (EU/US) + O→0 + limpieza de unidades
- Validaciones de coherencia:
  - `country ↔ branch_code` (prefijo)
  - `line_type ↔ sku_or_service_code` (prefijos `SV-`, `PART-`, `EXC|WHL|BLD|DRL-`)
- Quarantine:
  - default: coherence/id failures
  - strict: parse/coherence/id failures

## 4. Hallazgos principales (1 página)
Rellenar con `clean_out/dq_report.json`:

- Parsing:
  - Fechas: fails = `2207` (**3.42%** de `64442` filas leídas)
  - Números: unit_price fails = `588` (**0.91%**), qty fails = `576` (**0.89%**)
- Identificadores:
  - invoice_id missing = `678` (**1.05%**)
  - invoice_id duplicates = `117` (**0.18%**)
- Coherencia:
  - country↔branch mismatch = `0` (**0.0%**)
  - sku mismatch (service/parts/machine) = `0` / `0` / `0`
- Strings:
  - invisibles en customer_name = `1592`
  - mojibake en customer_name = `166`

## 5. Gráficos (½–1 página)
Insertar:
- `report_out/plots/count_country.png`
- `report_out/plots/count_line_type.png`
- `report_out/plots/count_branch_top20.png`
- `report_out/plots/hist_unit_price_logy.png`
- `report_out/plots/box_unit_price.png`
- `report_out/plots/hist_qty_or_hours.png`
- `report_out/plots/box_qty_or_hours.png`

## 6. Limitaciones y próximos pasos (¼ página)
- Dataset sintético: parte de los hallazgos son esperables por diseño (inyecciones de error).
- Próximo: controles preventivos (contratos/catálogos) + observabilidad (profiling periódico) + flujo de remediación.

