from tabulate import tabulate
import csv

arr = []
dic = {} 

while 1:
    print("For the given Menu enter the Sno.:")
    print("1. Add participants")
    print("2. Add Expanse")
    print("3. Show all participants")
    print("4. Show expanses")
    print("5. Exit/Export")
    x = input()

    if x == "2":
        print("Enter the following three:")
        admin = input("Paid By: ")
        if admin not in arr:
            print("Not a participant")
            continue
        amt = input("Amount: ")
        Dist = input("Distributed Amongst (Enter names and give ,(comma) between names): ")
        Dist = Dist.split(",")
        for z in Dist:
            if z not in arr:
                print("Not a participant")
                continue
        num = len(Dist)
        if num==0:
            print("Enter a least one name to split the bill")
            continue
        splitAmt = float(amt) / float(num)

        dic[admin] += float(amt)
        for ele in Dist:
            if ele == admin:
                dic[ele] = (dic[ele] - splitAmt)
            else:
                dic[ele] -= splitAmt

    if x == "5":
        with open('expense.csv', 'w', newline='') as csvfile:
            csv_w = csv.writer(csvfile)
            csv_w.writerow(["Participant's Name", "Amount", "Owes/Gets Back"])

            for participant, amount in dic.items():
                abs_a = abs(amount)
                abs_a = round(abs_a,3)
                owes_gets = "Owes" 

                if amount==0:
                    owes_gets = "Cleared"
                elif amount > 0:
                    owes_gets = "Gets Back"
                

                csv_w.writerow([participant, abs_a, owes_gets])
        break

    if x == "1": 
        part = input("Enter all the participants' names with a ,(comma) in between\n")
        part = part.split(",")

        for ele in part:
            if ele not in dic:
                dic[ele] = 0

        for ele in part:
            if ele not in arr:
                arr.append(ele)

    if x == "4":
        table_data = []

        for participant, amount in dic.items():
            abs_a = abs(amount)
            abs_a = round(abs_a,3)
            owes_gets = "Owes" 
            if amount==0:
                owes_gets = "Cleared"
            elif amount > 0:
                owes_gets = "Gets Back"
            table_data.append([participant, abs_a, owes_gets])

        table = tabulate(table_data, headers=["Participant's Name", "Amount", "Owes/Gets Back"], tablefmt="grid")

        print(table)

    if x == "3":
        if len(arr) == 0:
            print("No participants, please add participants")
        else:
            print(arr)

    
