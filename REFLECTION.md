# Developer Journal

1. Regular Expressions

I used the REGEX by importing the "re" library that referred to the examples from Workshop 8. This function allows the program to check that if the users' input is valid or not when they enter their email address and password. For example: 123@kent.ac.uk is valid but 123@kent.ac@uk is invalid.

2.Testing

I used the "pytest" function to test different functions in project_2.py and check if the code can pass the pytest. I also made two function which are "Valid" and "Invalid" to check the code if ir can work correctly.It referred to the examples from lecture 8.

3. Libraries

I used different libraries such as "random" and "cowsay" in the code. I used random library to create two sets of random numbers between 10000 and 99999 and add them together. Also I used the cowsay library to create a fox image. In addition I also used my own libraries in the test_project.py for testing my code. 

4. File I/O

I created a csv file for the program to input user's name, email, id to them by using the "append" function. The list in the csv file can be printed out using the "address = csv.DictWriter" and "address.writerow" function. I also created a txt file for the users to input any words if they want by using the "append" and "read" fuction.

5. Object-Oriented Programming (OOP)

I used a class for the users to store their name, email and id. This function can helps me more easier to write and test the code. It can also make me easier to extend my code if I need to add more fuctions.

6.Above and Beyond (Extension)

In addition, I used the decorator function that I learnt in lecture 9 to prints the "Good job!" message when the program is complete. It allows me to add new function to the code without changing the original functions.
