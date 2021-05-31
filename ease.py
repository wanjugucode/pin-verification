secret_pin=0000
pin = ""
pin_count=0
pin_limit=3
out_of_inputs=False



while pin!=secret_pin and not(out_of_inputs):
    if pin_count<pin_limit:
        guess = input("Enter pin ")
        pin_count+=1
    else:
        out_of_inputs=True

if out_of_inputs:
    print("pin blocked")
else:
    print("loged in successfully")







