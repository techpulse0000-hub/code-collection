import csv
import datetime

class finance:
    def __init__(self, category, item, amount, date, description):
        self.category = category
        self.item = item
        self.amount = amount
        self.date = date
        self.description = description

        transaction = date, category, item, amount, description
        rows = list(transaction)
        with open("finance_tracker.csv", "a", newline="") as f:
            write = csv.writer(f)
            write.writerow(rows)

    def edit():
        f = open("finance_tracker.csv", "r", newline="")
        reader = csv.reader(f)
        history = list(reader)
        a = 0
        for h in history:
            print(a, h)
            a+=1
        to_edit = input("choose the transaction by its no.")
        edit = history[int(to_edit)]
        print(','.join(edit))
        print("rewrite the transaction. you can copy, paste and edit it")
        editing = input("--")
        edited = editing.split(",")
        history[int(to_edit)] = edited
        with open("finance_tracker.csv", "w", newline='') as write:
            writer = csv.writer(write)
            writer.writerows(history)
        print('done')
        f.close()

    def total_spent():
        a = "a: total money spent"
        b = "b: total money spent by category"
        c = "c: spendding by date"
        d = "d: spendding by month"
        with open("finance_tracker.csv", "r", newline='') as file:
            reader = csv.reader(file)
            next(reader)
            total_money_spent = 0
            categories = {}
            by_month = {}
            by_date = {}
            for r in reader:
                total_money_spent += int(r[3])
                if r[1] not in categories:
                    categories[r[1]] = 0
                categories[r[1]] += int(r[3])
                d = r[0]
                dd, mm, yy = d.split("-")
                dt = datetime.date(int(yy), int(mm), int(dd))
                month = dt.strftime("%B") + f", {yy}"
                if  month not in by_month:
                    by_month[month] = 0
                by_month[month] += int(r[3])
                day = dt.strftime("%B %d, %Y")
                if day not in by_date:
                    by_date[day] = 0
                by_date[day] += int(r[3])

        print(a, "\n", b, "\n", c, "\n", d)
        calculate = input("choose yor option: ")
        if calculate.lower() == "a":
            print(f"the total money you have spent is {total_money_spent}")
        elif calculate.lower() == "b":
            print(f"the total money you have spent per category is {categories}")
        elif calculate.lower() == "c":
            print("remeber, the format for writing date is: dd-mm-yy")
            frome = input("from(date) separated by dash only): ")
            dd, mm, yy = frome.split("-")
            frome = datetime.datetime(int(yy), int(mm), int(dd))
            to = input("to(date) separated by dash only): ")
            dd, mm, yy = to.split("-")
            to = datetime.datetime(int(yy), int(mm), int(dd))  
            b = {k:v for k,v in by_date.items() if datetime.datetime.strptime(k, "%B %d, %Y") >= frome and datetime.datetime.strptime(k, "%B %d, %Y") <= to}
            print(b)
        elif calculate.lower() == "d":
            print(f"the total money you have spent per category is {by_month}")




print("Hi MUHAMMAD")
a = "a= new transaction"
b = "b= edit old transaction"
c = "c= money spent"
end = "end: to end the program"

print(a, "\n", b, "\n", c, "\n", end)
while True:
    command = input("What operation will u like to perform ")
    if command.lower() == "end":
        break
    
    a = "a= new transaction"
    b = "b= edit old transaction"
    c = "c= money spent"
    end = "end: to end the program"

    print(a, "\n", b, "\n", c, "\n", end)

    if command.lower() == "a":
        print("write the transaction in this order: category, item, amount, date, description each sepatared by a comma ONLY")
        print("remeber, the format for writing date is: dd-mm-yy")
        new = input("--")
        category, item, amount, date, description = new.split(",")
        finance(category, item, amount, date, description)
    elif command.lower() == "b":
        finance.edit()
    elif command.lower() == "c":
        finance.total_spent()



        