#(2) EXPENCES TRACKER 
# post in linked inkedin and github

expences=[]

while True:
    print("\n ---- Expence tracker ----")
    print("1. Add Expences ")
    print("2. View Expenses ")
    print("3. Show Total expenses ")
    print("4. Exit ")

    choice=int(input("Enter your choice from 1 to 4 :"))

    if choice==1:
        amount=float(input("Enter the expense amount: "))
        category=str(input("Enter the category of the expense :"))

        expences.append ({
            "amount":amount,
            "category":category
        })
        print("Your Expenses added successfully ! ")

    elif choice==2:
        if not expences:
            print(" No expenses to showe ")
        else:
            print("\n Your Expenses are :")
            count=1

            for expense in expences:
                print(f"{count}. Amount:{expense['amount']}, Category:{expense['category']}")
                count += 1

    elif choice==3:
        total=sum(expense['amount'] for expense in expences)
        print(f"\n Total Expenses: {total}")

    elif choice==4:
        print("Exiting from the expense tracker thank you !")
        break 
    else:
        print("Invalid choice please enter a valid choice from 1 to 4 !")

        
            

