#Task 1: Read a File and Handle Errors

try:
    with open('sample.txt','r') as f:
        print("Reading file content: ")
        lines=f.readlines()
        count=1
        for l in lines:
            print(f"Line {count} : {l.strip()}")
            count+=1
except FileNotFoundError:
    print("The file sample.txt not found")    

