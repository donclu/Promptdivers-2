# Recomendaciones — Roadmap 30/60/90 (Ventas maquinaria)

## Top 5 (Quick wins — 30 días)
1) **Contrato de datos** (schema + tipos + dominios) + validación en ingestión
   - Corta: fechas inválidas, números con unidades, columnas corridas.
2) **Catálogo maestro** de `country`/`branch_code`
   - Rechazo automático si no match.
3) **Reglas de unicidad** para `invoice_id`
   - No imputar IDs; remediación upstream.
4) **Normalización de numéricos** (locale + separadores) y separación de unidades
   - `qty_or_hours` numérico + `unit` opcional.
5) **Quarantine workflow**
   - SLA + owner + trazabilidad (qué filas, por qué, quién corrige).

## 60 días (Controles y observabilidad)
- Perfilado automatizado: métricas diarias (nulos, parse_fail, outliers) + alertas.
- Detección de drift por país/sucursal (cambios súbitos de distribución).
- Tests de regresión de ingestión (fixtures con casos sucios conocidos).

## 90 días (Gobierno y escalado)
- Data stewardship por dominio (ventas/servicios/repuestos).
- Linaje y auditoría: log de transformaciones y versionado de reglas.
- Integración con BI/finanzas: reconciliación y controles contables.

## Umbrales sugeridos (para “PASS”)
- `invoice_id_missing == 0`
- `invoice_id_dupe == 0`
- `country_branch_mismatch <= 0.1%`
- `date_parse_fail <= 0.5%` (ideal: 0 con ingestión estricta)
- `unit_price_parse_fail <= 0.5%`
- `qty_parse_fail <= 0.5%`

