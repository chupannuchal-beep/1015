import csv
import os
import random
import time

def make_headings() -> list[str]:
    headings = [
        "transaction_id", "timestamp", "store_id", "product_id",
        "quantity", "unit_price", "total_amount", "payment_method"
    ]
    return headings

def make_row() -> list:
    random.seed()
    
    transaction_id = random.randint(100000, 999999)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    store_id = random.randint(1, 20)
    product_id = random.randint(1000, 9999)
    quantity = random.randint(1, 50)
    unit_price = round(random.uniform(5.0, 299.99), 2)
    total_amount = round(quantity * unit_price, 2)
    payment_method = random.choice(["cash", "credit_card", "debit_card", "mobile_pay", "online"])
    
    return [
        transaction_id,
        timestamp,
        store_id,
        product_id,
        quantity,
        unit_price,
        total_amount,
        payment_method
    ]

def make_data(rows: int = 10) -> list[list]:
    my_data = [make_row() for _ in range(rows)]
    return my_data

def make_file(pathname: str, headings: list[str], my_data: list[list]) -> bool:
    if not os.path.exists(pathname):
        with open(pathname, 'w', newline='') as newCSV:
            writer = csv.writer(newCSV, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(headings)
            writer.writerows(my_data)
        print(f"SALES data written to {pathname}.")
        return True
    else:
        print(f"Sorry, a sales data file called '{pathname}' already exists, aborting!")
        return False

def build_me() -> None:
    print("Making headings")
    headings = make_headings()
    print("Making data")
    my_data = make_data(15)  # Generate 15 sample transactions per file
    print("Creating filename")
    pathname = "SALES_DATA_" + time.strftime("%Y%m%d%H%M%S") + ".csv"
    
    print("Attempting to build the CSV sales data file")
    result = make_file(pathname, headings, my_data)
    print(f"Written successfully: {result}")

# Generate 5 sample sales data files (with small delays)
for counter in range(5):
    print(f"\nProcessing #{counter:03d}...")
    time.sleep(random.randint(1, 3))
    build_me()