# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0
portfolio = {}

# Number of stocks user wants to enter
n = int(input("How many stocks do you want to add? "))

for i in range(n):
    stock = input("Enter stock symbol: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock] * quantity
        total_investment += investment

        portfolio[stock] = {
            "Quantity": quantity,
            "Price": stock_prices[stock],
            "Investment": investment
        }

    else:
        print("Stock not available in price list!")

print("\n----- Portfolio Summary -----")

for stock, details in portfolio.items():
    print(
        f"{stock}: Quantity={details['Quantity']}, "
        f"Price=${details['Price']}, "
        f"Investment=${details['Investment']}"
    )

print(f"\nTotal Investment Value: ${total_investment}")

# Save results to text file
with open("portfolio_summary.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("----------------------\n")

    for stock, details in portfolio.items():
        file.write(
            f"{stock}: Quantity={details['Quantity']}, "
            f"Price=${details['Price']}, "
            f"Investment=${details['Investment']}\n"
        )

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\nPortfolio saved to portfolio_summary.txt")