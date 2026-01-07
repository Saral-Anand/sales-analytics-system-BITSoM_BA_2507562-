
def parse_and_clean_data(lines):
    """
    Cleans and validates raw sales data
    """
    cleaned = []

    for line in lines[1:]:
        parts = line.strip().split("|")

        if len(parts) != 8:
            continue

        tid, date, pid, pname, qty, price, cid, region = parts

        # Validation rules
        if not tid.startswith("T"):
            continue

        if cid.strip() == "":
            continue

        try:
            qty = int(qty)
            price = float(price.replace(",", ""))
        except ValueError:
            continue

        if qty <= 0 or price <= 0:
            continue

        cleaned.append({
            "transaction_id": tid,
            "date": date,
            "product_id": pid,
            "product_name": pname,
            "quantity": qty,
            "unit_price": price,
            "customer_id": cid,
            "region": region
        })

    return cleaned


def sales_summary_by_region(data):
    summary = {}

    for row in data:
        revenue = row["quantity"] * row["unit_price"]
        region = row["region"]

        summary.setdefault(region, {"revenue": 0, "transactions": 0})
        summary[region]["revenue"] += revenue
        summary[region]["transactions"] += 1

    return summary


def top_selling_products(data, top_n=5):
    product_sales = {}

    for row in data:
        product_sales[row["product_name"]] = (
            product_sales.get(row["product_name"], 0) + row["quantity"]
        )

    return sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:top_n]


def low_performing_products(data, threshold=10):
    """
    Task 2.3 – Low Performing Products
    """
    product_sales = {}

    for row in data:
        product_sales[row["product_name"]] = (
            product_sales.get(row["product_name"], 0) + row["quantity"]
        )

    return [p for p, q in product_sales.items() if q < threshold]


def daily_sales_trend(data):
    daily = {}

    for row in data:
        revenue = row["quantity"] * row["unit_price"]
        daily[row["date"]] = daily.get(row["date"], 0) + revenue

    return daily
