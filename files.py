#with open ("notes.txt", "a") as file:
    #file.write ("\nanything") 
    #file.write("\nYour age?")


medications = ["Paracetamol 100sh 2mg"
               "\nAspirin 200sh 5mg"
               "\nMetraformin 1000sh 10mg"]

with open("notes.txt" , "w") as file:
    file.writelines(medications)
 