file =open ("notes.txt" , "a")
file.write("\nMy name is lulu")
file.close()


with open ("notes.txt" , "r") as file:
    print(file.read())