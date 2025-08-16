'''Beginner Level Coding (Python OOP)-->To-Do list (Task manager)'''

from datetime import datetime as dt

class task:
    def __init__(self,title,due_date,status):
        self.title=title
        self.due_date=due_date
        self.status=status
    def show_info(self):
        print(f"Title: {self.title} || Due date: {self.due_date.strftime('%d.%m.%y')} || Status: {self.status}\n")


tasks=[] 
while True:
    print("\nMenu:\n1.Add a new task\n2.Remove a task\n3.Show all tasks\n4.Change status of a task\n5.Exit\n")
    choice=input("Enter 1,2,3,4 or 5: ")
    if choice=="1":
        while True:
            name=input("Enter task: ").strip()
            d1=input("Enter due_date(date.month.year format): ").strip()
            try:
                date= dt.strptime(d1,"%d.%m.%y")
            except:
                print("Invalid date/format. Please try again with a valid date.(Format: dd.mm.yy)")
                continue
            stat=input("Enter status of task: ").strip()
            if not name or not stat:
                print("All inputs are to be filled. Please try again.")
            else:
                t=task(name,date,stat)
                tasks.append(t)
                print("Task added succesfully.")
                ch=input("Want to continue?y/n: ")
                if ch not in "Yy":
                    break

    elif choice=="2":
        if len(tasks)==0:
            print("No tasks to remove.")
        else:
            num=1
            for x in tasks:
                print(f"{num}.")
                x.show_info()
                num+=1
            t1=input("Enter task number to remove: ")
            if t1.isdigit():
                t1=int(t1)
                if t1 in range(1,len(tasks)+1):
                    task_removed=tasks.pop(t1-1)
                    print(f"Removed: {task_removed.title}")
                else:
                    print("Task number doesnt exist.")
            else:
                print("Invalid input.")
        
    elif choice=="3":
        if len(tasks)==0:
            print("No tasks found.")
        else:
            for x in tasks:
                x.show_info()
    
    elif choice=="4":
        if len(tasks)==0:
            print("No tasks to update.")
        else:
            num=1
            for x in tasks:
                print(f"{num}.")
                x.show_info()
                num+=1
            t1=input("Enter task number to update: ")
            if t1.isdigit():
                t1=int(t1)
                if t1 in range(1,len(tasks)+1):
                    new_stat=input("Enter new status of task: ").strip()
                    tasks[t1-1].status= new_stat
                    print("Status updated.")
                else:
                    print("Task number doesn't exist.")
            else:
                print("Invalid input.")

    elif choice=="5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")


