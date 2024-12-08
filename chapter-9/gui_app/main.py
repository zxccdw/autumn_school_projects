import dearpygui.dearpygui as dpg

tasks = []

def add_task_callback(sender, app_data, user_data):
    task_text = dpg.get_value("input_task") # сюда можно пихнуть бд
    if task_text:
        task_id = len(tasks)
        tasks.append({"id": task_id, "text": task_text, "completed": False})
        with dpg.table_row(parent="task_table", tag=f"task_row_{task_id}"):
            dpg.add_text(task_text, tag=f"task_text_{task_id}")
            dpg.add_text("No", tag=f"task_completed_{task_id}")
            dpg.add_button(label="Mark Completed", tag=f"btn_complete_{task_id}", 
                           callback=mark_completed_callback, user_data=task_id)
            dpg.add_button(label="Delete", tag=f"btn_delete_{task_id}", 
                           callback=delete_task_callback, user_data=task_id)
        dpg.set_value("input_task", "")

def mark_completed_callback(sender, app_data, user_data):
    task_id = user_data
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            dpg.set_value(f"task_completed_{task_id}", "Yes")
            break

def delete_task_callback(sender, app_data, user_data):
    """Удалить задачу."""
    task_id = user_data
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]  # Удаление задачи из списка
    dpg.delete_item(f"task_row_{task_id}")  # Удаление строки из таблицы

# Создание интерфейса
dpg.create_context()

with dpg.window(label="To-Do Application", width=600, height=400):
    dpg.add_text("To-Do List Application", color=[0, 128, 255])
    
    # Поле для ввода задачи
    dpg.add_input_text(label="New Task", hint="Enter a new task", tag="input_task", width=300)
    dpg.add_button(label="Add Task", callback=add_task_callback)
    
    # Таблица для отображения задач
    with dpg.table(header_row=True, tag="task_table", borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True):
        dpg.add_table_column(label="Task")
        dpg.add_table_column(label="Completed")
        dpg.add_table_column(label="Actions")
        dpg.add_table_column(label="Actions")

dpg.create_viewport(title="To-Do List", width=700, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
