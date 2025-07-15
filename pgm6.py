from datetime import datetime

def earlier_date(date1_str, date2_str):
    date_format = "%d-%m-%Y"  # Assuming date format as DD-MM-YYYY
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)

    if date1 < date2:
        print(f"{date1_str} is earlier.")
    elif date2 < date1:
        print(f"{date2_str} is earlier.")
    else:
        print("Both dates are the same.")

# Example usage
d1 = input("Enter first date (DD-MM-YYYY): ")
d2 = input("Enter second date (DD-MM-YYYY): ")
earlier_date(d1, d2)
