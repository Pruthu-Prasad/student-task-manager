def add_task(tasks, task):
    if task.strip():
        tasks.append(task)


def list_tasks(tasks):
    print("\nTasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")