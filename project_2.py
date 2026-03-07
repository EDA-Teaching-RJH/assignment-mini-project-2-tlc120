#Regular Expressions
import csv
import re

def valid_email(email):
    if re.search(r"^\w+@\w.+\.(ac.uk|gov.uk|com)$", email):
        return True
    return False

def listss():
    
    lists = open("name1.csv", newline='')

    list = csv.DictReader(lists)

    for i in list:
        print(i["name"] + "," + i["email"]+ "," + i["ids"])

    lists.close()

def main():
    name = input("Enter your name: ").strip()
    password()
    
    email = input("Enter your email: ").strip()
    ids = input("Enter your ID: ").strip()
    
    if valid_email(email):
        print("Valid email\n")
        
        with open("name1.csv", "a") as file:
          address = csv.DictWriter(file, fieldnames=["name", "email", "ids"])
          address.writerow({"name": name, "email": email, "ids": ids})
        
    else:
        print("Invalid email")

    full = input("Do you want to see the name1 list? ").strip().lower()

    if full == "yes":
        listss()
    
    
        
def password():
    passwords = input("\nPlease enter your 6 digits password: ").strip()
    
    if re.search(r"^[0-9][0-9][0-9][0-9][0-9][0-9]$", passwords):
        print("Valid password")

    else:
        print("Invalid password")


if __name__ == "__main__":
    main()












