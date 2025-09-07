import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        print("command-line argument is not a number")
        sys.exit(1)

    try:
        response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
        response.raise_for_status()
        data = response.json()

        bitcoin_price = float(data['data']['priceUsd'])
    except requests.RequestException:
        print("Error: Unable to fetch Bitcoin price from the API.")
        sys.exit(1)
    total_cost = num_bitcoins * bitcoin_price

    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
