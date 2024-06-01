class Transformer:
    @staticmethod
    def transform(data):
        usd_to_eur = data['rates']['EUR']
        transformed_data = []
        date_str = data['timestamp']
        for currency, rate in data['rates'].items():
            transformed_data.append({
                'currency_date': date_str,
                'currency_symbol': currency,
                'currency_rate': rate / usd_to_eur
            })
        return transformed_data
