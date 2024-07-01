# Botnance - Trading Platform Backend
Welcome to the backend of our comprehensive trading platform! This project provides a robust backend system to support various features for trading. Our platform offers advanced charting capabilities, backtesting for trading strategies, support for self-trades and bot trades, real-time coin prices, and RTL support in Hebrew.

## Features

- **Live Chart**: Generate and display advanced charts for analyzing market trends.
- **Strategies:** Explain various trading strategies with detailed documentation.
- **Individual Trades**: Execute trades manually through the platform.
- **Trades Table:** View a table of all trades, including both open and closed trades.
- **Bot Manager**: Automate trading with bot functionality.
- **Prices List**: Retrieve real-time and historical prices for various cryptocurrencies.
- **Backtesting**: Test trading strategies using historical market data.
- **RTL Support**: Interface and documentation available in Hebrew with Right-to-Left text support.

## Technologies Used

- **Programming Language**: Python
- **Web Framework**: Binance API, ccxt
- **Database**: sqlite3

## Installation

To get started with the backend, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone git@github.com:AdiFinkelman/Crypto-Project.git
   ```

2. **Set Up a Virtual Environment**
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Start the Application**
   ```bash
   python ./app.py
   ```

## Configuration
Configure the following settings:

```python
SECRET_KEY = "your-secret-key"
ALLOWED_HOSTS = ["localhost", "127.0.0.1:5586"]
```

## API Endpoints

### Charting
**GET /binance**  
Retrieve a list of available coins from Binance.  
**Params:** None

**GET /binance/<coin>**  
Retrieve chart data for a given market symbol.  
**Params:** 
- `coin` (string): The market symbol for the coin.
- `timeframe` (string): The timeframe for the chart data (e.g., `1d`, `1h`). Default is `1d`.

### Backtesting
**POST /backtest/<strategy_name>**  
Submit a trading strategy for backtesting.  
**Params:** 
- `strategy_name` (string): The name of the trading strategy.
- `timeframe` (string): The timeframe for backtesting (e.g., `1h`). Default is `1h`.
- `interval` (integer): The interval for backtesting (e.g., `30`). Default is `30`.

**Body:** JSON payload with strategy parameters.

### Self-Trades
**POST /trade/buy**  
Execute a manual trade.  
**Body:** JSON payload with trade details.
- `symbol` (string): The market symbol for the trade.
- `cost` (integer): The cost of the trade.
- `start_time` (string): The start time of the trade in `YYYY-MM-DD HH:MM:SS` format.
- `bot_name` (string): The name of the bot executing the trade.

### Trades by Bots
**POST /trades/bot**  
Submit a trade request for a trading bot.  
**Body:** JSON payload with bot trading instructions.

### Coin Prices
**GET /coins/{symbol}/price**  
Retrieve the current price for a cryptocurrency.  
**Params:** 
- `symbol` (string): The market symbol for the coin.

### RTL Support
**GET /rtl/text**  
Get RTL formatted text.  
**Body:** JSON payload with text content.

### Strategies
**GET /strategies**  
Retrieve a list of available trading strategies.  
**Params:** None

**GET /strategy_descriptions**  
Retrieve descriptions for all trading strategies.  
**Params:** None

### Trades Table
**GET /trades**  
Retrieve a list of all trades (open and closed).  
**Params:** None

**GET /trade/<int:trade_id>**  
Retrieve a specific trade by ID.  
**Params:** 
- `trade_id` (integer): The ID of the trade.

**PUT /trade/<int:trade_id>**  
Update a trade by ID.  
**Params:** 
- `trade_id` (integer): The ID of the trade.

**Body:** JSON payload with update details.
- `end_time` (string): The end time of the trade in `YYYY-MM-DD HH:MM:SS` format. Default is the current time.

**GET /trade/status/<int:trade_id>**  
Update the status of a trade to "sold" by ID.  
**Params:** 
- `trade_id` (integer): The ID of the trade.

### Balance
**GET /balance**  
Retrieve the current account balance.  
**Params:** None

## Contributing

We welcome contributions to improve the platform! To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request with a detailed description of your changes.

   
   
