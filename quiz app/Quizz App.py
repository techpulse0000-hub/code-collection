import tkinter as tk
from tkinter import ttk
import json
import csv
import random

root = tk.Tk()
root.title("quizing")
root.eval("tk::PlaceWindow . center")

###FRAMES
frm1 = ttk.Frame(root)
frm2 = ttk.Frame(root)
frm3 = ttk.Frame(root)
for frm in (frm1, frm2, frm3):
    frm.grid(row=0, column=0)



###Accessing the Questins from the file
with open("quiz question.json") as f:
    questions = json.load(f)

### Variables for questions, users related stuff
# users = {}
with open("users.csv", 'r', newline="") as f:
    users = list(csv.reader(f))

list_of_q = random.sample(questions, 11)

list_of_user_ans = []
correct = []
wrong = []
i = 0


## user info
class user:
    def __init__(self, username):
        self.username = username
        with open("users.csv", 'a', newline="") as f:
            users = csv.writer(f)
            rows = [username,0,0,0]
            users.writerow(rows)
        # users[username] = {"no_of_games": 0, "highest":0, "lowest":0}
        
    def player_history(self, no_of_games, highest, lowest):
        # self.username = username
        self.no_of_games = no_of_games
        self.highest = highest
        self.lowest = lowest
        

### Users page
def load_frm1():
    users_names = []
    def load_secnd_frm():
        frm1.destroy()
        load_frm2()

    frm_1a = ttk.Frame(frm1, width=400, height=600)
    frm_1b = ttk.Frame(frm1, width=400, height=35)

    # r=0
    for i in (frm_1a, frm_1b):
        i.pack_propagate(False)
        i.pack(pady=10)
        # r+1
    
    row = 0
    for i in users[1:]:
        i = i[0]
        users_names.append(i)
        show_user = ttk.Button(frm_1a, text=i, command=load_secnd_frm)
        show_user.grid(row=row, column=0)
        row+=1

    msg = ttk.Label(frm_1a, text="select User", font=("Ariel", 10, "bold"))
    msg.grid(row=row+1, column=1)

    add_user_row = row    
    add_user = ttk.Entry(frm_1b)
    add_user.grid(row=0, column=0)

    def add_func():
        row = len(users)+1
        text = add_user.get()
        
        if text not in users_names and text != "":
            user(text)
            show_user = ttk.Button(frm_1a, text=text, command=load_frm2)
            show_user.grid(row=add_user_row-1, column=0)
            msg.config(text="")

        else:
            msg.config(text="user already exists")

        add_user.delete(0, tk.END)

        

    add_user_btn = ttk.Button(frm_1b, text="Add User", command=add_func)
    add_user_btn.grid(row=0, column=1)

    


### Post Quiz Page
def load_frm3():
    def load_frst_frm():
        frm3.destroy()
        load_frm1()

    text = ttk.Label(frm3, text=f"you scored {len(correct)} out of 10", font=("Ariel", 10, "bold"))
    text.grid(row=0, column=0)
    row = 1
    for i in range(len(list_of_user_ans)):
        L1 = ttk.Label(frm3, text=list_of_q[i]["question"], font=("Helvetica", 10))
        L2 = ttk.Label(frm3, text=f"Your answer: {list_of_user_ans[i]}", font=("Helvetica", 10))
        L3 = ttk.Label(frm3, text=f"Correct answer: {list_of_q[i]["answer"]}", font=("Helvetica", 10))
        for j in (L1, L2, L3):
            j.grid(row=row, column=0)
            row+=1

    back = ttk.Button(frm3, text="BACK", command=load_frst_frm)
    back.grid(row=row+2, column=3)
        


# ### the quiz page
def load_frm2():
    global list_of_user_ans
    var = tk.StringVar()
    
    show_q = ttk.Label(frm2, text=list_of_q[i]["question"], font=("Helvetica", 10))

    list_of_user_ans.append(var.get())
    var.set("")
    
    oa = ttk.Radiobutton(frm2, text=list_of_q[i]["A"], variable=var, value="A")  
    ob = ttk.Radiobutton(frm2, text=list_of_q[i]["B"], variable=var, value="B")
    oc = ttk.Radiobutton(frm2, text=list_of_q[i]["C"], variable=var, value="C")  
    od = ttk.Radiobutton(frm2, text=list_of_q[i]["D"], variable=var, value="D")
    row = 0
    for j in (show_q, oa, ob, oc, od):
        j.grid(row=row, column=0)
        row+=1
    
    list_of_user_ans = [i for i in list_of_user_ans if i != ""]

    def next_Q():
        global i
        i+=1
        if len(list_of_user_ans)  == 10:
            frm2.destroy()
            load_frm3()
        else:
            list_of_user_ans.append(var.get())
            var.set("")

            show_q.config(text=list_of_q[i]["question"])
            oa.config(text=list_of_q[i]["A"])
            ob.config(text=list_of_q[i]["B"])
            oc.config(text=list_of_q[i]["C"])
            od.config(text=list_of_q[i]["D"])

            if list_of_user_ans[-1] == list_of_q[i-1]["answer"]:
                correct.append(list_of_q[i-1]["id"])
            else:
                wrong.append(list_of_q[i-1]["id"])
            
        print("question no. ", list_of_q[i]["id"], list_of_q[i]["question"])
        print("correct: ", correct)
        print("wrong: ", wrong)
        print(list_of_user_ans)


    next_btn = ttk.Button(frm2, text="Next Question", command=next_Q)
    next_btn.grid(row=4, column=1)





load_frm1()
root.mainloop()