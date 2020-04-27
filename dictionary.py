filename=input("Enter the name of the file containing words and their definitions:- ")
dictionary={}
with open(filename,'r') as myfile:
    flag=0
    word=""
    definition=""
    for line in myfile:
        if flag==0:
            word=line.strip()
            flag=-1
        else:
            definition=line.strip()
            dictionary[word]=definition
            flag=0
while 1:
    s=input("Enter the word:- ")
    if s=="":
        break
    s=s.strip()
    if s in dictionary:
        print(dictionary[s])
    else:
        print("The word is not found in the dictionary")
