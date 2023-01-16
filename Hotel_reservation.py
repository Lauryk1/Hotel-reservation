 from datetime import datetime
import locale

print("The hotel Reservation program\n") 

again = "y"
while again.lower() == "y":
    # get arrival date
    while True:
        date_str = input("Enter arrival date (YYYY-MM-DD): ")
        try:
            arrival_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Try again")
            print()
