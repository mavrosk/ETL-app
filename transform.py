class Transformer:
    @staticmethod
    def transform(data):
        usd_to_eur = data['rates']['EUR']
        transformed_data = []
        for currency, rate in data['rates'].items():
            transformed_data.append({
                'currency_date': data['timestamp'],
                'currency_symbol': currency,
                'currency_rate': rate / usd_to_eur
            })
        return transformed_data
