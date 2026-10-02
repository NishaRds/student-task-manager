tasks = []
def mark_done(number):
    tasks[number - 1]["done"] = True
def add_task(title, subject, deadline):
    tasks.append({"title": title, "subject": subject,
                  "deadline": deadline, "done": False})
def show_tasks():
    for i, t in enumerate(tasks, start=1):
        status = "Done" if t["done"] else "Pending"
        print(i, t["title"], "-", t["subject"], "-", status)

add_task("Finish DBMS assignment", "DBMS", "10 Oct")
show_tasks()