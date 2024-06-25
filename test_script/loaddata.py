import csv
import requests
from datetime import date

def load_data_from_csv(csv_file, api_url):
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            current_date = date.today().isoformat()
            
            transaction_data = {
                'id': row['id'],
                'description': row['description'],
                'amount': float(row['amount']) if row['amount'] else 0.0,
                'date': current_date  
            }

            response = requests.post(api_url, json=transaction_data)

            if response.status_code == 201:
                print(f"Transacción creada exitosamente: {transaction_data}")
            else:
                print(f"Error al crear transacción: {response.status_code} - {response.text}")

if __name__ == "__main__":
    api_url = 'http://127.0.0.1:8000/api/transactions/'  
    csv_file = 'data.csv'  
    load_data_from_csv(csv_file, api_url)
