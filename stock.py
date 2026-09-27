import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 175,
    "AMZN": 190,
    "META": 500,
    "NVDA": 120,
    "NFLX": 700
}


# Display available stocks
def show_available_stocks():
    print("\nAVAILABLE STOCKS")

    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")



# Add a stock to the portfolio
def add_stock(portfolio):
    show_available_stocks()

    stock = input("\nEnter stock symbol: ").upper().strip()

    if stock not in stock_prices:
        print("Stock not found in the available list.")
        return

    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    # If stock already exists, add the new quantity
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity

    print(f"{quantity} shares of {stock} added successfully.")


# Remove a stock from the portfolio
def remove_stock(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    stock = input("\nEnter stock symbol to remove: ").upper().strip()

    if stock in portfolio:
        del portfolio[stock]
        print(f"{stock} removed from your portfolio.")
    else:
        print("Stock is not present in your portfolio.")


# Display portfolio
def show_portfolio(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty.")
        return 0

    print("\nPORTFOLIO")
    print(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Investment':<15}")
    print("-" * 49)

    total_investment = 0

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = quantity * price

        total_investment += investment

        print(
            f"{stock:<10}"
            f"{quantity:<12}"
            f"${price:<11}"
            f"${investment:<15}"
        )

    print("-" * 49)
    print(f"{'TOTAL INVESTMENT':<34}${total_investment}")

    return total_investment


# Save portfolio as TXT file
def save_as_txt(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty. Nothing to save.")
        return

    total = 0

    with open("stock_portfolio.txt", "w") as file:
        file.write("STOCK PORTFOLIO TRACKER\n")
        

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = quantity * price
            total += investment

            file.write(
                f"Stock: {stock}\n"
                f"Quantity: {quantity}\n"
                f"Price: ${price}\n"
                f"Investment: ${investment}\n"
            )

        file.write(f"\nTOTAL INVESTMENT: ${total}\n")

    print("\nPortfolio saved successfully as 'stock_portfolio.txt'.")


# Save portfolio as CSV file
def save_as_csv(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty. Nothing to save.")
        return

    total = 0

    with open("stock_portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(
            ["Stock", "Quantity", "Price", "Investment"]
        )

        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = quantity * price
            total += investment

            writer.writerow(
                [stock, quantity, price, investment]
            )

        writer.writerow([])
        writer.writerow(["TOTAL INVESTMENT", "", "", total])

    print("\nPortfolio saved successfully as 'stock_portfolio.csv'.")


# Main program
def main():

    portfolio = {}

    print("       STOCK PORTFOLIO TRACKER")
    

    while True:

        print("\n         MENU         ")
        print("1. Show Available Stocks")
        print("2. Add Stock")
        print("3. View Portfolio")
        print("4. Remove Stock")
        print("5. Save Portfolio as TXT")
        print("6. Save Portfolio as CSV")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_available_stocks()

        elif choice == "2":
            add_stock(portfolio)

        elif choice == "3":
            show_portfolio(portfolio)

        elif choice == "4":
            remove_stock(portfolio)

        elif choice == "5":
            save_as_txt(portfolio)

        elif choice == "6":
            save_as_csv(portfolio)

        elif choice == "7":
            print("\nThank you for using Stock Portfolio Tracker!")
            break

        else:
            print("\nInvalid choice. Please select 1-7.")


# Start the program
if __name__ == "__main__":
    main()