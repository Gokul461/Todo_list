from tkinter import *
import tkinter.messagebox

def enter():
    task="" 
    def add():
        task = entry.get(1.0,"end-1c")
        if task == "":
            tkinter.messagebox.showwarning(title="Warning!",message="The task must not be empty")
        else:
            task = task+' - N'
            box.insert(END,task)
            root1.destroy()
    def high_pri():
        e = entry.get(1.0,"end-1c")
        if e == "":
            tkinter.messagebox.showwarning(title="Warning!",message="First enter any task to set priority")
        else:  
            fin1 = e+' - 1' 
            box.insert(END,fin1)
            root1.destroy() 
    def mod_pri():
        e = entry.get(1.0,"end-1c")  
        if e == "":
            tkinter.messagebox.showwarning(title="Warning!",message="First enter any task to set priority")
              
        else:
            fin2 = e +' - 2' 
            box.insert(END,fin2)
            root1.destroy()
    def low_pri():
        e = entry.get(1.0,"end-1c")  
        if e == "":
            tkinter.messagebox.showwarning(title="Warning!",message="First enter any task to set priority")
        else:    
            fin3 = e+' - 3' 
            box.insert(END,fin3)
            root1.destroy()
    root1 = Tk()
    root1.resizable(False,False)
    root1.title("Add task")
    root1.config(bg='gray')
    f1 = Frame(root1)
    f1.pack(side=LEFT)
    f2 = Frame(root1,bg='gray')
    f2.pack(side=RIGHT)
    root1.geometry("540x220")
    root.resizable(False,False)
    lab = Label(f1,text="Enter the task here",font=('Arial Black',10))
    lab.pack(pady=3)
    entry = Text(f1,width=20,height=7)
    entry.pack(pady=10)
    pri_lab = Label(f2,text='Select priority 1- highest,2- moderate,3- low',bg='gray',font=('Arial Black',10))
    Font=('Aptos Display',10)
    high= Button(f2,text='Add(High-1)',background='red',font=Font,width=9,command=lambda:high_pri())
    mod = Button(f2,text='Add(mod-2)',background='yellow',font=Font,width=9,command=lambda:mod_pri())
    low = Button(f2,text='Add(low-3)',background='green',width=9,font=Font,command=lambda:low_pri())
    pri_lab.pack(padx=3,pady=6)
    high.pack(pady=3)
    mod.pack(pady=3)
    low.pack(pady=3)
    f3 = Frame(root1)
    f3.pack(side=BOTTOM)
    temp = Button(f2,text="Add(n)",command=add,fg='white',width=9,background='black')
    temp.pack(pady=3)
    root1.mainloop()
        
def delete():
    try:
        selection = box.curselection()
        box.delete(selection[0])
    except Exception:
       tkinter.messagebox.showwarning(title="Warning!",message="First enter any task") 
    
        
def mark():
    try:
        selection = box.curselection()
        temp_task = selection[0]
        marked = box.get(selection)
        marked = marked + "✔"
        box.delete(temp_task)
        box.insert(temp_task,marked)
    except Exception:
        tkinter.messagebox.showwarning(title="Warning!",message="First enter task")

root = Tk()
root.config(bg='gray20')
root.title("To-do List")
root.geometry("300x320")
root.resizable(False,False)
top = Frame(root)
top.pack(side=TOP)
label = Label(top,text="To-do List",fg='white',font=("Copperplate Gothic Bold",15),background='dark blue',width=35,height=4)
label.pack(fill=X)
frame = Frame(root)
frame.pack()
box = Listbox(frame,background='pink',fg='black',height=5,width=33,font=('Aptos Display',10))
box.pack(side=LEFT)
scroll_right = Scrollbar(frame)
scroll_right.pack(side=RIGHT,fill=Y)
box.config(yscrollcommand=scroll_right.set)
scroll_right.config(command=box.yview)
Font=('Aptos Display',10)
add_button = Button(root,text="Add task",background='black',font=Font,fg='white',width=30,command=lambda: enter())
delete_button = Button(root,text="Delete task",background='black',font=Font,fg='white',width=30,command= lambda:delete())
mark_button = Button(root,text="Mark as read",background='black',font=Font,fg='white',width=30,command=lambda:mark())
add_button.pack(pady=5)
delete_button.pack(pady=5)
mark_button.pack(pady=5)

root.mainloop()