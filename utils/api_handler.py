import requests


def fetch_products():
    """
    Fetch products from DummyJSON API
    """
    url = "https://dummyjson.com/products"
    response = requests.get(url, timeout=10)
    return response.json().get("products", [])


def create_product_mapping(products):
    """
    Create mapping for product enrichment
    """
    mapping = {}

    for product in products:
        mapping[product["title"]] = {
            "api_price": product.get("price"),
            "category": product.get("category"),
            "brand": product.get("brand")
        }

    return mapping


def enrich_sales_data(sales_data, product_map):
    """
    Enrich sales records using API data
    """
    enriched = []

    for row in sales_data:
        product_info = product_map.get(row["product_name"])

        if product_info:
            row.update(product_info)

        enriched.append(row)

    return enriched
