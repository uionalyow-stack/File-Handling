def show_medicine():
    print("Paracetamol")
show_medicine()



def patient_name(name):
   print("Hello", name)
patient_name("lulu")



def medicine_price(price, quantity):
    return price * quantity
total_cost = medicine_price(40, 3)
print(total_cost)
