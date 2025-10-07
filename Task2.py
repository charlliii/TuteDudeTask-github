# Task 2: Write and Append Data to a File
file = open ('Output.txt','w')
fl=file.write(input("Enter text to write to the file: "))
print("Data successfully written to output.txt.")
file.close()

file=open('Output.txt','a')
fl=file.write("\n"+ input("Enter additional text to append: "))
print("data successfully appended.")
file.close()


print("Final contant of output.txt: ")
file=open('Output.txt','r')
f=file.read()
print(f)
file.close()

