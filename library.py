def main():
  number = int(input("Please enter a 4 digits number: "))
  print("Your verification code is", code(number))

def code(numbers):
  return numbers * 2

if __name__ == "__main__":
  main()
  