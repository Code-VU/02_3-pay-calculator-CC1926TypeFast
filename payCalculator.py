def calculatePay():
    # Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
    hrs = input("Enter Hours:")
    rat = input("Enter Rate:")
    gross_pay = int(hrs) * float(rat)
    print(gross_pay)
    # end assignment


## If you want to test locally before you try to sync
## Open your terminal and run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
