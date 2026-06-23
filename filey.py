file =open ("notes.txt" , "a")  #not preferred way
file.write("\nMy name is lulu") #changess the file to append mode
file.close()


with open ("notes.txt" , "r") as file:
    print(file.read())