import psycopg2
from psycopg2.extras import execute_batch

class DataLoader:
    def __init__(self, db_config):
        self.conn = psycopg2.connect(**db_config)
    
    def load_data(self, data):
        insert_query = """
            INSERT INTO exchange_rates (currency_date, currency_symbol, currency_rate)
            VALUES (%s, %s, %s)
            ON CONFLICT (currency_date, currency_symbol)
            DO UPDATE SET currency_rate = EXCLUDED.currency_rate;
        """
        records = [(data["date"], k, v) for k, v in data["rates"].items()]
        with self.conn.cursor() as cur:
            execute_batch(cur, insert_query, records)
        self.conn.commit()
