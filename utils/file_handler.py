def read_sales_data(file_path):
    """
    Reads pipe-separated sales data with encoding handling
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()
    except UnicodeDecodeError:
        with open(file_path, "r", encoding="latin-1") as file:
            return file.readlines()
    except FileNotFoundError:
        print(" sales_data.txt not found")
        return []
