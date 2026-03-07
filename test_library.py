from library import code

def test_code():
  try:
    assert code(1423) == 2846
    
  except AssertionError:
    print("The number is not 2846")

  try:
    assert code(7656) == 15312
    
  except AssertionError:
    print("TThe number is not 15312") 
    

def main():
  code()

if __name__ == "__main__":
  main()
