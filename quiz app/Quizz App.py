import tkinter as tk
from tkinter import ttk
import json
import csv
import random

root = tk.Tk()
root.title("quizing")
root.eval("tk::PlaceWindow . center")
root.geometry("500x200")

###FRAMES
frm1 = ttk.Frame(root)
frm2 = ttk.Frame(root)
frm3 = ttk.Frame(root)

for frm in (frm1, frm2, frm3):
    frm.pack()

###Scrollbar uisng canvas
class scrollable_frame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = tk.Canvas(self)
        self.canvas.pack(side="left", fill="both", expand=1)
        self.scroll_bar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scroll_bar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scroll_bar.set)
        self.canvas.bind('<Configure>', lambda e:self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas_frame2 = ttk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.canvas_frame2, anchor="nw")

###Accessing the Questins from the file
with open("quiz question.json") as f:
    questions = json.load(f)

### Variables for questions, users related stuff
with open("users.csv", 'r', newline="") as f:
    users = list(csv.reader(f))


list_of_q = random.sample(questions, 10)
question = {"id": 11, "question": "ready to see ur reult?", "A": "yes", "B": "no", "answer": "A"}
list_of_q.append(question) 
list_of_user_ans = []
correct = []
wrong = []
i = 0
no = 1

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
        frm_1a.destroy()
        load_frm2()

    def show_context_menu(event):
        context_menu.post(event.x_root, event.y_root)

    def refresh():
        frm1.destroy()
        frm_1a.destroy()
        load_frm1()

    def delete():
        username = show_user.cget("text")
        # del users_names[users_names.index(username)]
        print(username)
        refresh()

    
    frm_1a = scrollable_frame(root)
    frm_1a.pack(fill="both", expand=1, pady=10)
    # frm_1b = ttk.Frame(frm1)
    # frm_1b.pack_propagate(False)
    # frm_1b.pack(pady=10)
    
    # context_menu = tk.Menu(frm_1a, tearoff=0)
    # context_menu.add_command(label="delete", command=delete)

    row = 0
    for i in users[1:]:
        i = i[0]
        users_names.append(i)
        show_user = ttk.Button(frm_1a.canvas_frame2, text=i, command=load_secnd_frm)
        show_user.pack(anchor="center", pady=2)
        
        context_menu = tk.Menu(frm_1a, tearoff=0)
        context_menu.add_command(label="delete", command=delete)
        show_user.bind("<Button-3>", show_context_menu)
        

    msg = ttk.Label(frm_1a, text="select User", font=("Ariel", 10, "bold"))
    msg.pack(pady=10)

    add_user_row = row    
    add_user = ttk.Entry(frm1)
    add_user.grid(row=0, column=0)

    def add_func():
        row = len(users)+1
        text = add_user.get()
        
        if text not in users_names and text != "":
            user(text)
            show_user = ttk.Button(frm_1a.canvas_frame2, text=text, command=load_frm2)
            show_user.grid(row=add_user_row, column=0)
            msg.config(text="")

        else:
            msg.config(text="user already exists")

        add_user.delete(0, tk.END)

    


        

    add_user_btn = ttk.Button(frm1, text="Add User", command=add_func)
    add_user_btn.grid(row=0, column=1)

    


### Post Quiz Page
def load_frm3():
    def load_frst_frm():
        frm_3a.destroy()
        frm3.destroy()
        load_frm1()

    frm_3a = scrollable_frame(root)
    frm_3a.pack(fill="both", expand=1, pady=10)

    text = ttk.Label(frm_3a.canvas_frame2, text=f"you scored {len(correct)} out of 10", font=("Ariel", 10, "bold"))
    text.grid(row=0, column=0)
    row = 1
    for i in range(len(list_of_user_ans)):
        L1 = ttk.Label(frm_3a.canvas_frame2, text=list_of_q[i]["question"], font=("Helvetica", 10))
        L2 = ttk.Label(frm_3a.canvas_frame2, text=f"Your answer: {list_of_user_ans[i]}", font=("Helvetica", 10))
        L3 = ttk.Label(frm_3a.canvas_frame2, text=f"Correct answer: {list_of_q[i]["answer"]}", font=("Helvetica", 10))
        for j in (L1, L2, L3):
            j.grid(row=row, column=0)
            row+=1

    back = ttk.Button(frm3, text="BACK", command=load_frst_frm)
    back.grid(row=row+2, column=3)
        


# ### the quiz page
def load_frm2():
    # no = 1
    global list_of_user_ans
    var = tk.StringVar()
    
    q = no, list_of_q[i]["question"]
    show_q = ttk.Label(frm2, text=q, font=("Helvetica", 10))

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
        global no
        no += 1
        if len(list_of_user_ans)  == 9:
            list_of_user_ans.append(var.get())
            var.set("")

            q = no, list_of_q[i]["question"]
            show_q.config(text=q)
            oa.config(text=list_of_q[i]["A"])
            ob.config(text=list_of_q[i]["B"])
            oc.destroy()
            od.destroy()

            if list_of_user_ans[-1] == list_of_q[i-1]["answer"]:
                correct.append(list_of_q[i-1]["id"])
            else:
                wrong.append(list_of_q[i-1]["id"])
        elif len(list_of_user_ans)  == 10:
            frm2.destroy()
            load_frm3()
        else:
            list_of_user_ans.append(var.get())
            var.set("")

            
            q = no, list_of_q[i]["question"]
            show_q.config(text=q)
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