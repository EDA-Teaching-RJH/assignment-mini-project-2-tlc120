#Libraries
import csv
import re
import random
import cowsay

#Object-Oriented Programming (OOP) 
class project:
    def __init__(self, name, email, ids):
        self.name = name
        self.email = email
        self.ids = ids


code_a = random.randint(10000,99999)
code_b = random.randint(10000,99999)

#Regular Expressions(1)
def valid_email(email):
    if re.search(r"^\w+@\w.+\.(ac\.uk|com)$", email):
        return True
    return False

#File I/O (1)
def listss():
    
    lists = open("name1.csv", newline='')

    list = csv.DictReader(lists)

    for i in list:
        print(i["name"] + "," + i["email"]+ "," + i["ids"])

    lists.close()

#Regular Expressions(2)
def valid_password(passwords):
    if re.search(r"^[0-9][0-9][0-9][0-9][0-9][0-9]$", passwords):
        return True
    return False


def password():
    passwords = input("Please enter your 6 digits password: ").strip()
    
    if valid_password(passwords):
        print("Valid password")

    else:
        print("Invalid password")

#File I/O (2)
def File():

    Name = input("Please enter anything in the txt file: ")

    with open("file.txt", "a") as file:
        file.write(f"{Name}\n")

    with open("file.txt", "r") as file:
        word = file.readlines()
        
    for words in word:
        print("\nYou have entered:", Name)

    example = []
    
    with open("file.txt") as file:
        for words in file:
            example.append(words.rstrip())
            
    for examples in sorted(example):
        print(f"\nThe words that stored in the txt file are: {examples}!")

#File I/O (3)
def main():
    name = input("Enter your name: ").strip()
    password()
    email = input("Enter your email: ").strip()
    
    if valid_email(email):
        print("Valid email\n")

        ids = input("Enter your ID: ").strip()
        
        with open("name1.csv", "a") as file:
          address = csv.DictWriter(file, fieldnames=["name", "email", "ids"])
          address.writerow({"name": name, "email": email, "ids": ids})

        

    else:
        print("Invalid email")
        
    print("Your verification code is", code_a + code_b)
    full = input("Do you want to see the name1 list? ").strip().lower()

    if full == "yes":
        print("")
        listss()
        File()      
        
        end = input("\nDo you want complete the project? ").lower()

        if end =="yes":
            cowsay.fox("Project complete!")

            additions()
            return project(name, email, ids)

#Above and Beyond (Extension)
def addition_decorator(add):
    def addition():
        add()
        print(f"Well done!")
    return addition

@addition_decorator
def additions():
    print("Good job!")


if __name__ == "__main__":
    main()
