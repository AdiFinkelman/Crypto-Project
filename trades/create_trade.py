import requests
import json

# Function to create a trade
def create_trade():
    url = "http://127.0.0.1:5586/create_trade"
    headers = {"Content-Type": "application/json"}
    data = {
        "symbol": "BTCUSDT",
        "cost": 10000,
        "user_id": 1
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 201:
        trade = response.json()
        print("Trade created successfully:", trade)
        return trade["id"]
    else:
        print("Failed to create trade:", response.json())
        return None

# Function to get a trade
def get_trade(trade_id):
    url = f"http://127.0.0.1:5586/get_trade/{trade_id}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Trade details:", response.json())
    else:
        print("Failed to get trade:", response.json())

# Create a trade and get its details
trade_id = create_trade()
if trade_id:
    get_trade(trade_id)
