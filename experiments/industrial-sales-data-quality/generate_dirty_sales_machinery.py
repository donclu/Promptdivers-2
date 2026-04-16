import argparse
import csv
import random
import re
from datetime import date, timedelta

COUNTRIES = ["CL", "PE", "MX", "CO", "AR", "US"]
BRANCHES = {
    "CL": ["CL-SCL-01", "CL-ANT-01"],
    "PE": ["PE-LIM-02", "PE-ARE-01"],
    "MX": ["MX-MEX-01", "MX-MTY-01"],
    "CO": ["CO-BOG-01", "CO-MED-01"],
    "AR": ["AR-BUE-01", "AR-CBA-01"],
    "US": ["US-MIA-01", "US-HOU-01"],
}
LINE_TYPES = ["MACHINE", "PARTS", "SERVICE"]
MACHINE_SKUS = ["EXC-320D", "WHL-950H", "BLD-D6R", "DRL-D45KS"]
PARTS_SKUS = ["PART-HYD-07", "PART-FLT-02", "PART-BRK-11", "PART-ENG-99"]
SERVICE_CODES = ["SV-ONSITE-08", "SV-MAINT-03", "SV-TRAIN-01", "SV-INSPECT-02"]

INVISIBLES = ["\ufeff", "\u200b", "\u0000", "\t", "\u00a0"]


def maybe_inject_invisible(s: str, rnd: random.Random) -> str:
    if not s:
        return s
    ch = rnd.choice(INVISIBLES)
    pos = rnd.randrange(0, len(s) + 1)
    return s[:pos] + ch + s[pos:]


def mojibake_like(s: str) -> str:
    return (
        s.replace("í", "Ã­")
        .replace("ó", "Ã³")
        .replace("ñ", "Ã±")
        .replace("á", "Ã¡")
        .replace("é", "Ã©")
        .replace("ú", "Ãº")
    )


def fmt_number_cross_locale(x: float, rnd: random.Random) -> str:
    style = rnd.choice(["EU", "US", "EU_SPACE"])
    s = f"{x:,.2f}"
    if style == "US":
        return s  # 1,234.56
    if style == "EU":
        return s.replace(",", "X").replace(".", ",").replace("X", ".")  # 1.234,56
    return s.replace(",", " ").replace(".", ",")  # 1 234,56


def random_date(rnd: random.Random) -> str:
    base = date(2025, 1, 1)
    d = base + timedelta(days=rnd.randint(0, 500))
    return d.isoformat()


def dirty_date(rnd: random.Random) -> str:
    d = random_date(rnd)
    yyyy, mm, dd = d.split("-")
    variant = rnd.choice(["DMY2", "MDY4", "INVALID"])
    if variant == "DMY2":
        return f"{dd}/{mm}/{yyyy[-2:]}"
    if variant == "MDY4":
        return f"{mm}-{dd}-{yyyy}"
    return "2026-13-40"


def clean_customer_name(rnd: random.Random) -> str:
    bases = [
        "Andes Mining SpA",
        "Constructora del Pacífico",
        "Grupo Cantera SA",
        "Minería del Sur",
        "Servicios Andinos",
        "Delta Obras",
        "StoneWorks LLC",
        "West Quarry Co.",
        "Canteras Oriente",
        "Minera Norte SpA",
        "Obras Sierra",
        "Rock & Drill Inc.",
    ]
    name = rnd.choice(bases)
    if rnd.random() < 0.08:
        name = name.replace(" ", ", ", 1)  # to create unquoted-comma risk
    return name


def unit_price_for(line_type: str, rnd: random.Random) -> float:
    if line_type == "MACHINE":
        return rnd.uniform(20000, 900000)
    if line_type == "PARTS":
        return rnd.uniform(10, 20000)
    return rnd.uniform(30, 250)


def qty_for(line_type: str, rnd: random.Random):
    if line_type == "SERVICE":
        return rnd.choice([0.5, 0.75, 1, 2, 3, 4, 6, 8, 12, 16, 24, 40])
    return rnd.randint(1, 15)


def sku_for(line_type: str, rnd: random.Random) -> str:
    if line_type == "MACHINE":
        return rnd.choice(MACHINE_SKUS)
    if line_type == "PARTS":
        return rnd.choice(PARTS_SKUS)
    return rnd.choice(SERVICE_CODES)


def force_error_row(error_code: str, i: int, rnd: random.Random) -> dict:
    country = rnd.choice(COUNTRIES)
    branch = rnd.choice(BRANCHES[country])
    line_type = rnd.choice(LINE_TYPES)
    sku = sku_for(line_type, rnd)
    inv = f"INV-{country}-2026-FORCE-{i:05d}"
    cust_id = f"CUST-{rnd.randint(1000, 9999):07d}"
    cust_name = clean_customer_name(rnd)
    inv_date = random_date(rnd)
    qty = qty_for(line_type, rnd)
    price = unit_price_for(line_type, rnd)

    row = {
        "invoice_id": inv,
        "invoice_date": inv_date,
        "country": country,
        "branch_code": branch,
        "customer_id": cust_id,
        "customer_name": cust_name,
        "line_type": line_type,
        "sku_or_service_code": sku,
        "qty_or_hours": qty,
        "unit_price": round(price, 2),
    }

    if error_code == "E1":
        row["customer_name"] = maybe_inject_invisible(row["customer_name"], rnd)
    elif error_code == "E2":
        row["customer_name"] = f"ACME \"{row['customer_name']}\""
    elif error_code == "E3":
        row["customer_name"] = mojibake_like(row["customer_name"])
    elif error_code == "E4":
        row["unit_price"] = fmt_number_cross_locale(price, rnd)
    elif error_code == "E5":
        row["qty_or_hours"] = "O.75" if line_type == "SERVICE" else "1O"
    elif error_code == "E6":
        row["unit_price"] = rnd.choice(["NaN", "-", "15%", "12kg", "8h"])
    elif error_code == "E7":
        row["invoice_date"] = dirty_date(rnd)
    elif error_code == "E8":
        row["invoice_id"] = ""
    elif error_code == "E9":
        row["unit_price"] = 9999999
        row["qty_or_hours"] = -3
    elif error_code == "E10":
        row["_broken_line"] = True

    return row


def probabilistic_corrupt(row: dict, rnd: random.Random) -> dict:
    if rnd.random() < 0.03:
        row["customer_name"] = maybe_inject_invisible(str(row["customer_name"]), rnd)
    if rnd.random() < 0.015:
        row["customer_name"] = f"\"{row['customer_name']}\""
    if rnd.random() < 0.015:
        row["customer_name"] = mojibake_like(str(row["customer_name"]))

    if rnd.random() < 0.05:
        try:
            row["unit_price"] = fmt_number_cross_locale(float(row["unit_price"]), rnd)
        except Exception:
            pass

    if rnd.random() < 0.008:
        row["qty_or_hours"] = "1O0.50" if row["line_type"] == "SERVICE" else "1O"

    if rnd.random() < 0.02:
        pick = rnd.choice(["NaN", "-", "15%", "12kg", "8h"])
        if rnd.random() < 0.5:
            row["unit_price"] = pick
        else:
            row["qty_or_hours"] = pick

    if rnd.random() < 0.03:
        row["invoice_date"] = dirty_date(rnd)

    if rnd.random() < 0.01:
        row["invoice_id"] = ""

    if rnd.random() < 0.01:
        row["unit_price"] = rnd.choice([9999999, -2500, 0])
    if rnd.random() < 0.01:
        row["qty_or_hours"] = rnd.choice([-3, 0, 200])

    if rnd.random() < 0.007:
        row["_broken_line"] = True

    return row


def generate_clean_row(seq: int, rnd: random.Random) -> dict:
    country = rnd.choice(COUNTRIES)
    branch = rnd.choice(BRANCHES[country])
    line_type = rnd.choice(LINE_TYPES)
    sku = sku_for(line_type, rnd)
    inv = f"INV-{country}-2026-{seq:06d}"
    cust_id = f"CUST-{rnd.randint(1000, 9999):07d}"
    cust_name = clean_customer_name(rnd)
    inv_date = random_date(rnd)
    qty = qty_for(line_type, rnd)
    price = round(unit_price_for(line_type, rnd), 2)
    return {
        "invoice_id": inv,
        "invoice_date": inv_date,
        "country": country,
        "branch_code": branch,
        "customer_id": cust_id,
        "customer_name": cust_name,
        "line_type": line_type,
        "sku_or_service_code": sku,
        "qty_or_hours": qty,
        "unit_price": price,
    }


def write_row(fh, writer, row: dict, rnd: random.Random, header: list):
    if row.get("_broken_line"):
        variant = rnd.choice(["SEMICOLON", "TAB", "SHIFT_COMMA"])
        values = [str(row.get(k, "")) for k in header]
        if variant == "SEMICOLON":
            fh.write(";".join(values) + "\n")
            return
        if variant == "TAB":
            fh.write("\t".join(values) + "\n")
            return
        idx = header.index("customer_name")
        values[idx] = values[idx].replace(" ", ", ", 1)
        fh.write(",".join(values) + "\n")
        return

    writer.writerow({k: row.get(k, "") for k in header})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="dirty_industrial_sales.csv")
    ap.add_argument("--rows", type=int, default=65000)
    ap.add_argument("--seed", type=int, default=1337)
    ap.add_argument("--sample", type=int, default=120)
    args = ap.parse_args()

    rnd = random.Random(args.seed)

    header = [
        "invoice_id",
        "invoice_date",
        "country",
        "branch_code",
        "customer_id",
        "customer_name",
        "line_type",
        "sku_or_service_code",
        "qty_or_hours",
        "unit_price",
    ]

    forced_errors = ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10"]
    forced_rows = []
    for e in forced_errors:
        for i in range(20):
            forced_rows.append(force_error_row(e, i, rnd))

    remaining = max(0, args.rows - len(forced_rows))
    all_rows = forced_rows[:]
    for seq in range(1, remaining + 1):
        row = generate_clean_row(seq, rnd)
        row = probabilistic_corrupt(row, rnd)
        all_rows.append(row)

    rnd.shuffle(all_rows)

    with open(args.out, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=header, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for row in all_rows:
            write_row(fh, writer, row, rnd, header)

    if args.sample and args.sample > 0:
        sample_path = re.sub(r"\.csv$", "", args.out) + f".sample{args.sample}.csv"
        with open(sample_path, "w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=header, quoting=csv.QUOTE_MINIMAL)
            writer.writeheader()
            for row in all_rows[: args.sample]:
                write_row(fh, writer, row, rnd, header)


if __name__ == "__main__":
    main()

