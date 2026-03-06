# Binance Futures Testnet Trading Bot

A simple Python CLI trading bot that places **MARKET** and **LIMIT** orders on the Binance Futures Testnet. This project was developed as part of the Python Developer Intern application task.

The application provides a structured and reusable codebase with input validation, logging, and error handling.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL sides
- CLI-based user input
- Input validation for order parameters
- Logging of API requests and responses
- Exception handling for API and input errors
- Modular project structure

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py           # Binance Futures client wrapper
│   ├── orders.py           # Order placement logic
│   ├── validators.py       # Input validation functions
│   └── logging_config.py   # Logging configuration
│
├── cli.py                  # CLI entry point
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── .env                    # API credentials (not committed)
└── trading_bot.log         # Generated log file
```

---

## Architecture

```
CLI Layer → Order Service → Binance Client
```

| Layer | File | Responsibility |
|---|---|---|
| CLI Layer | `cli.py` | Handles user input through command-line arguments |
| Order Service | `orders.py` | Contains the logic for placing orders |
| Client Wrapper | `client.py` | Manages connection to the Binance Futures Testnet API |
| Validators | `validators.py` | Ensures user inputs are valid before sending API requests |
| Logging | `logging_config.py` | Logs API requests, responses, and errors |

---

## Requirements

- Python 3.x
- Binance Futures Testnet account
- API Key and Secret

---

## Installation

**1. Clone the repository:**

```bash
git clone https://github.com/yourusername/trading-bot.git
cd trading-bot
```

**2. Install dependencies:**

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file in the project root:

```env
API_KEY=your_api_key
API_SECRET=your_secret_key
```

> These credentials are used to authenticate with the Binance Futures Testnet API.

---

## Usage

The bot accepts the following CLI parameters:

| Parameter | Description |
|---|---|
| `--symbol` | Trading pair (e.g. `BTCUSDT`, `ETHUSDT`) |
| `--side` | Order side (`BUY` or `SELL`) |
| `--type` | Order type (`MARKET` or `LIMIT`) |
| `--quantity` | Quantity to trade |
| `--price` | Required only for LIMIT orders |

### Example Commands

**MARKET Order:**

```bash
python cli.py --symbol ETHUSDT --side BUY --type MARKET --quantity 0.05
```

**LIMIT Order:**

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 80000
```

### Sample Output

```
Order Request Summary
----------------------
Symbol   : ETHUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.05

Order Response
----------------------
Order ID          : 8479535465
Status            : NEW
Executed Quantity : 0.000
Average Price     : 0.00
```

---

## Logging

All API requests, responses, and errors are logged to:

```
trading_bot.log
```

**Example log entry:**

```
INFO  Order Request:  {'symbol': 'ETHUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.05}
INFO  Order Response: {...}
```

---

## Error Handling

The application handles the following error cases:

- Invalid order types
- Invalid order sides
- Invalid quantities
- Missing price for LIMIT orders
- Binance API errors
- Network failures

---

## Dependencies

```
python-binance
python-dotenv
```

Install using:

```bash
pip install -r requirements.txt
```

---

## Notes

- The bot interacts with the **Binance Futures Testnet**, not the live trading environment.
- Testnet funds are **simulated** and used only for testing purposes.

---

## Author

**Vishal Bhingarde**  
*Python Developer Intern Application Task*
