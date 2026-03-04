#Regular Expressions
import csv
import re

def valid_email(email):
    if re.search(r"^\w+@\w.+\.(ac.uk|gov.uk|com)$", email):
        return True
    return False

def main():
    name = input("Enter your name: ").strip()
    email = input("Enter your email: ").strip()
    ids = input("Enter your ID: ").strip()
    
    if valid_email(email):
        print("Valid email")
        
        with open("name1.csv", "a") as file:
          address = csv.DictWriter(file, fieldnames=["name", "email", "ids"])
          address.writerow({"name": name, "email": email, "ids": ids})
        
    else:
        print("Invalid email")


if __name__ == "__main__":
    main()












