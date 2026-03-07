import csv
import re
import cowsay

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
        File()

        end = input("\nDo you want complete the project? ").lower()

        if end =="yes":
            cowsay.trex("Project complete!")
      
def password():
    passwords = input("Please enter your 6 digits password: ").strip()
    
    if re.search(r"^[0-9][0-9][0-9][0-9][0-9][0-9]$", passwords):
        print("Valid password")

    else:
        print("Invalid password")

def File():
    Name = input("\nPlease enter your name again: ")
    
    with open("file.txt", "a") as file:
        file.write(f"{Name}\n")

    with open("file.txt", "r") as file:
        word = file.readlines()
        
    for words in word:
        print("Nice to meet you,", Name)

    example = []
    
    with open("file.txt") as file:
        for words in file:
            example.append(words.rstrip())
            
    for examples in sorted(example):
        print(f"File I/O is complete, {examples}!")


if __name__ == "__main__":
    main()


















