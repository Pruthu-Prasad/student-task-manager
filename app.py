from tasks import add_task, list_tasks

tasks = []

print("Student Task Manager")

add_task(tasks, "Learn Git")
add_task(tasks, "Make a Pull Request")

list_tasks(tasks)