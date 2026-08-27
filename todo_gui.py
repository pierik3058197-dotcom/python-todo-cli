"""使用 tkinter 的待办事项窗口界面。"""

import tkinter as tk
from tkinter import messagebox

from todo_app import add_todo, complete_todo, delete_todo, load_todos


class TodoWindow:
    """待办事项窗口。"""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("我的待办事项")
        self.root.geometry("500x420")

        title_label = tk.Label(root, text="待办事项", font=("Microsoft YaHei", 18))
        title_label.pack(pady=(15, 8))

        input_frame = tk.Frame(root)
        input_frame.pack(fill="x", padx=20)

        self.title_entry = tk.Entry(input_frame, font=("Microsoft YaHei", 12))
        self.title_entry.pack(side="left", fill="x", expand=True)
        self.title_entry.bind("<Return>", self.add_button_clicked)

        add_button = tk.Button(
            input_frame, text="添加", width=8, command=self.add_button_clicked
        )
        add_button.pack(side="left", padx=(8, 0))

        self.todo_list = tk.Listbox(
            root, height=12, font=("Microsoft YaHei", 12),
            selectmode=tk.SINGLE
        )
        self.todo_list.pack(fill="both", expand=True, padx=20, pady=15)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=(0, 15))

        tk.Button(
            button_frame, text="完成选中项目", width=14,
            command=self.complete_button_clicked
        ).pack(side="left", padx=5)
        tk.Button(
            button_frame, text="删除选中项目", width=14,
            command=self.delete_button_clicked
        ).pack(side="left", padx=5)
        tk.Button(
            button_frame, text="刷新", width=8,
            command=self.refresh_list
        ).pack(side="left", padx=5)

        self.refresh_list()
        self.title_entry.focus_set()

    def refresh_list(self):
        """从 todos.json 重新读取并显示任务。"""
        self.todo_list.delete(0, tk.END)
        for todo in load_todos():
            mark = "x" if todo["completed"] else " "
            self.todo_list.insert(
                tk.END, f"{todo['id']}. [{mark}] {todo['title']}"
            )

    def get_selected_id(self):
        """返回当前选中任务的编号；没有选中时返回 None。"""
        selection = self.todo_list.curselection()
        if not selection:
            return None
        todos = load_todos()
        index = selection[0]
        if index >= len(todos):
            return None
        return todos[index]["id"]

    def add_button_clicked(self, event=None):
        title = self.title_entry.get().strip()
        if not title:
            messagebox.showwarning("提示", "请先输入待办事项内容。")
            return
        add_todo(title)
        self.title_entry.delete(0, tk.END)
        self.refresh_list()

    def complete_button_clicked(self):
        todo_id = self.get_selected_id()
        if todo_id is None:
            messagebox.showwarning("提示", "请先选中一个待办事项。")
            return
        complete_todo(todo_id)
        self.refresh_list()

    def delete_button_clicked(self):
        todo_id = self.get_selected_id()
        if todo_id is None:
            messagebox.showwarning("提示", "请先选中一个待办事项。")
            return
        if messagebox.askyesno("确认删除", "确定要删除选中的待办事项吗？"):
            delete_todo(todo_id)
            self.refresh_list()


def main():
    root = tk.Tk()
    TodoWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
