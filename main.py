from utils.file_handler import read_sales_data
from utils.data_processor import (
    parse_and_clean_data,
    sales_summary_by_region,
    top_selling_products,
    low_performing_products,
    daily_sales_trend
)
from utils.api_handler import fetch_products, create_product_mapping, enrich_sales_data


def main():
    # Step 1: Read file
    lines = read_sales_data("data/sales_data.txt")

    # Step 2: Clean & validate
    cleaned_data = parse_and_clean_data(lines)

    # Step 3: API integration
    api_products = fetch_products()
    product_map = create_product_mapping(api_products)
    enriched_data = enrich_sales_data(cleaned_data, product_map)

    # Step 4: Analytics
    region_summary = sales_summary_by_region(enriched_data)
    top_products = top_selling_products(enriched_data)
    low_products = low_performing_products(enriched_data)
    daily_trend = daily_sales_trend(enriched_data)

    # Step 5: Report generation
    with open("output/report.txt", "w") as f:
        f.write("SALES ANALYTICS REPORT\n")
        f.write("=" * 40 + "\n\n")

        f.write("OVERALL SUMMARY\n")
        f.write(f"Total Valid Transactions: {len(enriched_data)}\n\n")

        f.write("REGION-WISE PERFORMANCE\n")
        for region, data in region_summary.items():
            f.write(f"{region}: Revenue={data['revenue']} | Transactions={data['transactions']}\n")

        f.write("\nTOP SELLING PRODUCTS\n")
        for product, qty in top_products:
            f.write(f"{product}: {qty}\n")

        f.write("\nLOW PERFORMING PRODUCTS\n")
        for product in low_products:
            f.write(f"{product}\n")

        f.write("\nDAILY SALES TREND\n")
        for date, revenue in daily_trend.items():
            f.write(f"{date}: {revenue}\n")

    print(" Process completed successfully.")
    print(" Report saved to output/report.txt")


if __name__ == "__main__":
    main()
