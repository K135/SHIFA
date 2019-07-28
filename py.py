# Ask the user to enter the names of files to compare
fname1 = input("Enter the Blue print name: ")
fname2 = input("Enter the Source name: ")
print("-----------------------------------------------------------")
print("Enter below question numbers in accordance with blue print")
print("------------------------------------------------------------")
PartAquestions = int (input("Enter the last question number of part A : "))
PartBquestions = int (input("Enter the last question number of part B : "))
PartCquestions = int (input("Enter the last question number of part C : "))


# Open file for reading in text mode (default mode)
f1 = open(fname1)
f2 = open(fname2)

# Print confirmation
print("-----------------------------------")
print("Comparing files ", " BP " + fname1, " SRC " +fname2, sep='\n')
print("-----------------------------------")

# Read the first line from the files
f1_line = f1.readline()
f2_line = f2.readline()

# Initialize counter for line number
line_no = 1
NoError=True
# Loop if either file1 or file2 has not reached EOF
while f1_line != '' or f2_line != '':

    # Strip the leading whitespaces
    f1_line = f1_line.rstrip()
    f2_line = f2_line.rstrip()
    
    # Compare the lines from both file
    if f1_line != f2_line:
        
        # If a line does not exist on file2 then mark the output with + sign
        if f2_line == '' and f1_line != '':
            NoError=False
            print("Additional line found in BP", "Line-%d" % line_no, f1_line)
        # otherwise output the line on file1 and mark it with > sign
        elif f1_line != '':
            print("Please check BP", "Line-%d" % line_no, f1_line)
            NoError=False
        # If a line does not exist on file1 then mark the output with + sign
        if f1_line == '' and f2_line != '':
            print("Additional line found in SRC ", "Line-%d" % line_no, f2_line)
            NoError=False
        # otherwise output the line on file2 and mark it with < sign
        elif f2_line != '':
            print("Please check SRC", "Line-%d" %  line_no, f2_line)
            NoError=False

      
        

    #Read the next line from the file
    f1_line = f1.readline()
    f2_line = f2.readline()


    #Increment line counter
    line_no += 1
if NoError:
    print("Both files are same")


print("\n---------------------------------------------------------------------")
print("-------------------------Checking for parts-----------------------------\n")
print("")


#Checking for parts
#Put the parts in as p1 for part A, p2 for part b etc.....
p1 = "Part A"
p2 = "Part B"
p3 = "PART C"
MissPart= True
PartCheck= False
NoMissPart= True
#Checking parts condition in Source file
if p1.lower() in open(fname1).read().lower():
    if p1.lower() in open(fname2).read().lower():
      NoMissPart= True
    else:
     print("Part A not found in SOURCE or spelling missplaced")
     PartCheck= True
     MissPart= False
     

if p2.lower() in open(fname1).read().lower():
    if p2.lower() in open(fname2).read().lower():
      NoMissPart= True
    else:
     print("Part B not found in SOURCE or spelling missplaced") 
     PartCheck= True
     MissPart= False
     
 

if p3.lower() in open(fname1).read().lower():
    if p3.lower() in open(fname2).read().lower():
      NoMissPart= True
    else:
     print("Part C not found in SOURCE or spelling missplaced")
     PartCheck= True
     MissPart= False
     
if MissPart:
    print("all parts found in Source.")
    

if PartCheck:
     import sys
     print("\n--------------------------------------------------------------------------------")
     print("Note: This may effect the question count, Please Correct it and Check further!!")
     print("_________________________________________________________________________________")
     input("\nPress Enter to close")
     sys.exit("Error message")
    





print("\n---------------------------------------------------------------------")
print("-----------------------Checking for questions----------------------")


print("PART A")

parta = ["{}.".format(i+1) for i in range(PartAquestions)]
found_alla = True
with open(fname2) as file:
    text = file.read().lower().split("part a")[1].split("part b")[0].strip()
    for word in parta: 
        if word not in text:
            found_alla= False
            print(" Question {} not found\n".format(word))
            
if found_alla:
    print("all questions found in Part A of Source\n") 

    #---
print("------------------")
print("PART B")
    

partb = ["{}.".format(i+1) for i in range(PartAquestions, PartBquestions)]
found_allb = True
with open(fname2) as file:
    text = file.read().lower().split("part b")[1].split("part c")[0].strip()
    for word in partb: 
        if word not in text:
            found_allb= False
            print(" Question {} not found\n".format(word))
            
if found_allb:
    print("all questions found in Part B of Source")     

print("------------------")
print("PART C")
    

partc = ["{}.".format(i+1) for i in range(PartBquestions, PartCquestions)]
found_allc = True
with open(fname2) as file:
    text = " ".join(file.read().lower().split("part c")[1:]).strip()
    for word in partc: 
        if word not in text:
            found_allc= False
            print(" Question {} not found\n".format(word))
            
if found_allc:
    print("all questions found in Part C of Source")                         

f1.close()
f2.close()

input("Press Enter to close")