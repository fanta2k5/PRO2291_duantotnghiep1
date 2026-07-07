import pandas as pd


def check_integrity():

    fact = pd.read_csv("data/dim_fact/fact_sales.csv")
    customer = pd.read_csv("data/dim_fact/dim_customer.csv")
    product = pd.read_csv("data/dim_fact/dim_product.csv")
    location = pd.read_csv("data/dim_fact/dim_location.csv")
    time = pd.read_csv("data/dim_fact/dim_time.csv")

    print("\n===== DATA INTEGRITY CHECK =====")

    print("Null values in fact_sales:")
    print(fact.isnull().sum())

    print("\nDuplicate rows in fact_sales:")
    print(fact.duplicated().sum())

    print("\nCustomer key check:",
          fact["customer_id"].isin(customer["customer_id"]).all())

    print("Product key check:",
          fact["product_id"].isin(product["product_id"]).all())

    print("Location key check:",
          fact["location_id"].isin(location["location_id"]).all())

    print("Date key check:",
          fact["date_id"].isin(time["date_id"]).all())

    print("\nIntegrity Check Completed.")


if __name__ == "__main__":
    check_integrity()