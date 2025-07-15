from datetime import datetime, timedelta

today = datetime.now()
new_date = today - timedelta(days=5)
print("Current date:", today.strftime("%d-%m-%Y"))
print("Date after subtracting 5 days:", new_date.strftime("%d-%m-%Y"))
