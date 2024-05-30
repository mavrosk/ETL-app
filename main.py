import argparse
from datetime import datetime, timedelta
from fetch import Fetcher
from transform import Transformer
from load import DataLoader

def main():
    parser = argparse.ArgumentParser(description="ETL for Exchange Rates")
    parser.add_argument("--start_date", type=str, help="Start date in YYYY-MM-DD format")
    parser.add_argument("--end_date", type=str, help="End date in YYYY-MM-DD format")
    args = parser.parse_args()

    start_date = args.start_date or datetime.now().strftime("%Y-%m-%d")
    end_date = args.end_date or start_date

    # Database configuration
    db_config = {
        "dbname": "exchange_rates_db",
        "user": "db_user",
        "password": "db_pass",
        "host": "localhost",
        "port": 5432
    }

    loader = DataLoader(db_config)

    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        data = Fetcher.fetch_data(date_str)
        eur_rate = data["rates"]["EUR"]
        transformed_data = Transformer(data, eur_rate)
        loader.load_data(transformed_data)
        current_date += timedelta(days=1)

if __name__ == "__main__":
    main()
