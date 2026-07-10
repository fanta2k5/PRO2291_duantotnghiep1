import pandas as pd
from sqlalchemy import create_engine, text

# =========================
# KẾT NỐI SQL SERVER
# =========================

SERVER = r"NGUYENTHUC\MSSQLSERVER1"
DATABASE = "SalesAnalyticsDW"

connection_string = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)


def load_to_sql():

    print("=" * 60)
    print("LOAD DATA TO SQL SERVER")
    print("=" * 60)

    # =========================
    # ĐỌC FILE CSV
    # =========================

    dim_customer = pd.read_csv(
        "data/dim_fact/dim_customer.csv"
    )

    dim_product = pd.read_csv(
        "data/dim_fact/dim_product.csv"
    )

    dim_location = pd.read_csv(
        "data/dim_fact/dim_location.csv"
    )

    dim_time = pd.read_csv(
        "data/dim_fact/dim_time.csv"
    )

    fact_sales = pd.read_csv(
        "data/dim_fact/fact_sales.csv",
        low_memory=False
    )

    # ========================================================
    # XỬ LÝ DỮ LIỆU TRƯỚC KHI NẠP
    # ========================================================
    
    # 1. Loại bỏ các dòng bị trùng mã sản phẩm ở dim_product, giữ lại dòng đầu tiên
    dim_product = dim_product.drop_duplicates(subset=['product_id'], keep='first')

    # 2. Loại bỏ cột 'is_outlier' thừa trong fact_sales nếu tồn tại
    if 'is_outlier' in fact_sales.columns:
        fact_sales = fact_sales.drop(columns=['is_outlier'])

    # =========================
    # XÓA DỮ LIỆU CŨ
    # =========================
    print("Deleting old data...")

    with engine.begin() as conn:

        # Xóa Fact trước
        conn.execute(text("DELETE FROM fact_sales"))

        # Sau đó mới xóa Dimension
        conn.execute(text("DELETE FROM dim_time"))
        conn.execute(text("DELETE FROM dim_location"))
        conn.execute(text("DELETE FROM dim_product"))
        conn.execute(text("DELETE FROM dim_customer"))

    print("Old data deleted successfully.")

    # =========================
    # LOAD DỮ LIỆU
    # =========================

    print("Loading dim_customer...")
    dim_customer.to_sql(
        "dim_customer",
        engine,
        if_exists="append",
        index=False
    )
    print(f"Loaded {len(dim_customer):,} rows.")

    print("Loading dim_product...")
    dim_product.to_sql(
        "dim_product",
        engine,
        if_exists="append",
        index=False
    )
    print(f"Loaded {len(dim_product):,} rows.")

    print("Loading dim_location...")
    dim_location.to_sql(
        "dim_location",
        engine,
        if_exists="append",
        index=False
    )
    print(f"Loaded {len(dim_location):,} rows.")

    print("Loading dim_time...")
    dim_time.to_sql(
        "dim_time",
        engine,
        if_exists="append",
        index=False
    )
    print(f"Loaded {len(dim_time):,} rows.")

    print("Loading fact_sales...")
    fact_sales.to_sql(
        "fact_sales",
        engine,
        if_exists="append",
        index=False
    )
    print(f"Loaded {len(fact_sales):,} rows.")

    print("=" * 60)
    print("LOAD SQL COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    load_to_sql()