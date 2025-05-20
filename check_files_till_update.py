import time

keyword = input("Enter the Keyword to search for: ")
while True:
    with open("data.txt", "r") as f:
        lines = f.readlines()

        print("Reading file...")
    
        if keyword in "".join(lines):
            print("Found the keyword!")
        
            break
    time.sleep(1) 
