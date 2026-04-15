import random

print("Hello, Welcome to Chillhaus_Bar")
print("Before you start, please check your balance.")
print("If you don't have balance, deposit first before ordering.\n")

def show_menu():
    print("\n===== CHILLHAUS_BAR MONEY DEPOSIT =====")
    print("[1] Balance")
    print("[2] Deposit")
    print("[3] Order")
    print("[4] Exit")
    print("[5] Order History")
    print("=======================================")

def show_order_menu():
    print("\n===== CHILLHAUS BAR MENU =====")

    print("\n--- COCKTAILS ---")
    print("1. Mango Mojito – ₱180")
    print("2. Calamansi Whisky Sour – ₱170")
    print("3. Boracay Sunset – ₱160")

    print("\n--- LOCAL DRINKS ---")
    print("4. San Mig Light – ₱70")
    print("5. Pale Pilsen – ₱75")
    print("6. Red Horse – ₱80")
    print("7. Tanduay Rum – ₱60 per shot")

    print("\n--- CLASSIC COCKTAILS ---")
    print("8. Margarita – ₱150")
    print("9. Mojito – ₱150")
    print("10. Long Island – ₱220")

    print("\n--- NON-ALCOHOLIC ---")
    print("11. Fresh Calamansi Juice – ₱60")
    print("12. Soft Drinks – ₱35")
    print("13. Bottled Water – ₱25")

    print("\n--- BAR BITES ---")
    print("14. Sizzling Sisig – ₱180")
    print("15. Calamares – ₱150")
    print("16. Fries – ₱80")

    print("\n[0] Cancel Order")
    print("[67] Done - Check out")
    print("=======================================")

items = {
    1: ("Mango Mojito", 180),
    2: ("Calamansi Whisky Sour", 170),
    3: ("Boracay Sunset", 160),

    4: ("San Mig Light", 70),
    5: ("Pale Pilsen", 75),
    6: ("Red Horse", 80),
    7: ("Tanduay Rum (shot)", 60),

    8: ("Margarita", 150),
    9: ("Mojito", 150),
    10: ("Long Island", 220),

    11: ("Fresh Calamansi Juice", 60),
    12: ("Soft Drinks", 35),
    13: ("Bottled Water", 25),

    14: ("Sizzling Sisig", 180),
    15: ("Calamares", 150),
    16: ("Fries", 80)
}

def main():
    balance = 0
    order_history = []

    while True:
        show_menu()
        try:
            user_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number (1-5).")
            continue

        if user_choice == 1:
            print(f"Your current balance is: ₱{balance:.2f}")

        elif user_choice == 2:
            try:
                amount = float(input("Enter amount to deposit: ₱"))
            except ValueError:
                print("Invalid amount.")
                continue

            if amount <= 0:
                print("Invalid amount.")
            else:
                balance += amount
                print("Deposit successful.")
                print(f"Updated balance: ₱{balance:.2f}")

        elif user_choice == 3:
            while True:
                show_order_menu()

                try:
                    order = int(input("Enter the number of the item you want to order: "))
                except ValueError:
                    print("Invalid input.")
                    continue

                if order == 0:
                    print("Order canceled.")
                    break

                if order == 67:
                    print("Order completed. Returning to main menu.")
                    break

                if order not in items:
                    print("Invalid order choice.")
                    continue

                item_name, price = items[order]
                print(f"You selected: {item_name} – ₱{price}")

                if price > balance:
                    print(" ❌ Not enough balance. Please deposit first.")
                    continue 
                else:
                    balance -= price
                    print(f"✅ Order Successful! Enjoy your {item_name}.")
                    print(f"Remaining Balance: ₱{balance:.2f}")

                    order_history.append((item_name, price))


        elif user_choice == 4:
            print("Thank you for visiting CHILLHAUS BAR!")
            break

        elif user_choice == 5:
            print("\n===== ORDER HISTORY =====")
            if not order_history:
                print("No orders yet.")
            else:
                total_spent = 0
                for item, cost in order_history:
                    print(f"- {item} : ₱{cost}")
                    total_spent += cost

                print(f"\nTotal Spent: ₱{total_spent}")
            print("=========================\n")

        else:
            print("Invalid choice. Please select 1-5.")

main()
