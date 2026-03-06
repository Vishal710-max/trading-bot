import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_quantity
from bot.logging_config import setup_logging

def main():

    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    side = validate_side(args.side)
    order_type = validate_order_type(args.type)
    validate_quantity(args.quantity)

    if order_type == "LIMIT" and args.price is None:
        raise ValueError("Price is required for LIMIT orders")

    client = get_client()

    print("\nOrder Request Summary")
    print("----------------------")
    print("Symbol:", args.symbol)
    print("Side:", side)
    print("Type:", order_type)
    print("Quantity:", args.quantity)
    print("Price:", args.price)

    response = place_order(
        client,
        args.symbol,
        side,
        order_type,
        args.quantity,
        args.price
    )

    print("\nOrder Response")
    print("----------------------")
    print("\nFull API Response:")
    print(response)

    if "orderId" in response:

        print("\nOrder Response")
        print("----------------------")
        print("Order ID:", response["orderId"])
        print("Status:", response["status"])
        print("Executed Quantity:", response["executedQty"])
        print("Average Price:", response.get("avgPrice", "N/A"))

    elif "error" in response:

        print("\nOrder Failed")
        print(response["error"])

    else:

        print("\nUnexpected response from Binance.")
if __name__ == "__main__":
    main()