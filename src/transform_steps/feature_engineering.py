import pandas as pd


class FeatureEngineering:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Đọc dữ liệu từ file CSV"""
        try:
            self.df = pd.read_csv(self.file_path)
            print("Đọc dữ liệu thành công!")
            print(f"Kích thước dữ liệu: {self.df.shape}")
        except Exception as e:
            print(f"Lỗi khi đọc dữ liệu: {e}")

    def create_revenue(self):
        """Tạo cột doanh thu"""
        if self.df is None:
            raise ValueError("Vui lòng load dữ liệu trước.")

        self.df["revenue"] = (
            self.df["qty_ordered"] * self.df["price"]
        )

        print("Đã tạo cột revenue.")

    def create_discount_rate(self):
        """Tạo tỷ lệ giảm giá"""
        if self.df is None:
            raise ValueError("Vui lòng load dữ liệu trước.")

        if "discount_amount" in self.df.columns:
            self.df["discount_rate"] = (
                self.df["discount_amount"]
                / self.df["revenue"]
            ) * 100

            # Xử lý chia cho 0
            self.df["discount_rate"] = (
                self.df["discount_rate"]
                .fillna(0)
                .replace([float("inf"), -float("inf")], 0)
            )

            print("Đã tạo cột discount_rate.")

    def create_time_features(self, date_col):
        """Tạo các đặc trưng liên quan đến thời gian"""
        if self.df is None:
            raise ValueError("Vui lòng load dữ liệu trước.")

        self.df[date_col] = pd.to_datetime(
            self.df[date_col],
            errors="coerce"
        )

        self.df["year"] = self.df[date_col].dt.year
        self.df["month"] = self.df[date_col].dt.month
        self.df["quarter"] = self.df[date_col].dt.quarter
        self.df["day"] = self.df[date_col].dt.day
        self.df["day_of_week"] = self.df[date_col].dt.day_name()
        self.df["year_month"] = self.df[date_col].dt.strftime("%Y-%m")
        self.df["is_weekend"] = (
            self.df[date_col].dt.weekday >= 5
        ).astype(int)

        print("Đã tạo các time features.")

    def create_order_value(self):
        """Tính tổng giá trị của từng đơn hàng"""
        if self.df is None:
            raise ValueError("Vui lòng load dữ liệu trước.")

        self.df["order_value"] = (
            self.df.groupby("order_id")["revenue"]
            .transform("sum")
        )

        print("Đã tạo cột order_value.")

    def get_data(self):
        """Trả về DataFrame sau khi xử lý"""
        if self.df is None:
            raise ValueError("Chưa có dữ liệu.")

        return self.df


def add_features(df):
    df = df.copy()

    df["order_date"] = pd.to_datetime(
        df["order_date"],
        errors="coerce"
    )

    df["revenue"] = df["qty_ordered"] * df["price"]

    df["profit"] = df["total"] - df["discount_amount"]

    df["discount_rate"] = (
        df["discount_amount"] / df["revenue"]
    ) * 100

    df["discount_rate"] = (
        df["discount_rate"]
        .fillna(0)
        .replace([float("inf"), -float("inf")], 0)
    )

    df["quarter"] = df["order_date"].dt.quarter
    df["day"] = df["order_date"].dt.day
    df["day_of_week"] = df["order_date"].dt.day_name()
    df["year_month"] = df["order_date"].dt.strftime("%Y-%m")

    df["order_value"] = (
        df.groupby("order_id")["revenue"]
        .transform("sum")
    )

    print("Feature Engineering hoàn tất.")

    return df