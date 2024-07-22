# Reading alphabets from first file
f = open("D:/UNI/3rd year/2nd term/ISS/project_files/alphabets.txt", "r")
alphabets=[]
for l in f:
  stripped_line = l.replace(" ", "")
  for char in stripped_line:
      alphabets.append(char.lower())
f.close()


# Reading msg from first file
f2 = open("D:/UNI/3rd year/2nd term/ISS/project_files/msg.txt", "r")
msg=""
for l in f2:
  stripped_line = l.replace(" ", "")
  for char in stripped_line:
      msg+=char.lower()
f.close()

print("message = "+msg)


# first step replace each character
shift_number=3
New_msg=""
for i in msg:
    New_msg+=alphabets[(shift_number+alphabets.index(i)) % len(alphabets)]

# second step transposition
Left_msg=""
Right_msg=""
Final_msg=""
for i in range(len(New_msg)):
    if i%2==0:
        Left_msg+=New_msg[i]
    else:
        Right_msg+=New_msg[i]
Final_msg+=Left_msg+Right_msg

print("message after shifting = "+New_msg)
print("message after transpos = "+Final_msg)

file = open("D:/UNI/3rd year/2nd term/ISS/project_files/output.txt", 'a') # Open a file in append mode
file.write("message after shifting = "+New_msg)
file.write("\n")
file.write("message after transpos = "+Final_msg)# Write some text
file.close()