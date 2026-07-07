from cleaner import clean_data
from transform import transform_to_star_schema
from load_sql import load_to_sql
from check_integrity import check_integrity


def main():

    print("=" * 60)
    print("START ETL PIPELINE")
    print("=" * 60)

    # 1. Data Cleaning
    clean_data()

    # 2. Transform
    transform_to_star_schema()

    # 3. Load SQL Server
    load_to_sql()

    # 4. Kiểm tra tính toàn vẹn dữ liệu
    check_integrity()

    print("=" * 60)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()