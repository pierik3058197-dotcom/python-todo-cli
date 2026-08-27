"""一个使用 JSON 文件保存数据的命令行待办事项程序。"""

import argparse
import json
import os
from pathlib import Path


# 数据文件放在项目根目录，便于初学者直接找到它。
DEFAULT_FILE = Path(os.environ.get("TODO_FILE", Path(__file__).parent / "todos.json"))


def load_todos(file_path: Path = DEFAULT_FILE) -> list[dict]:
    """读取待办事项；文件不存在时返回空列表。"""
    if not file_path.exists():
        return []
    return json.loads(file_path.read_text(encoding="utf-8"))


def save_todos(todos: list[dict], file_path: Path = DEFAULT_FILE) -> None:
    """把待办事项写入 JSON 文件。"""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(
        json.dumps(todos, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def add_todo(title: str, file_path: Path = DEFAULT_FILE) -> dict:
    """新增一条待办事项并返回它。"""
    todos = load_todos(file_path)
    next_id = max((todo["id"] for todo in todos), default=0) + 1
    todo = {"id": next_id, "title": title, "completed": False}
    todos.append(todo)
    save_todos(todos, file_path)
    return todo


def complete_todo(todo_id: int, file_path: Path = DEFAULT_FILE) -> bool:
    """完成指定待办；找到并修改时返回 True。"""
    todos = load_todos(file_path)
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = True
            save_todos(todos, file_path)
            return True
    return False


def delete_todo(todo_id: int, file_path: Path = DEFAULT_FILE) -> bool:
    """删除指定待办；找到并删除时返回 True。"""
    todos = load_todos(file_path)
    remaining = [todo for todo in todos if todo["id"] != todo_id]
    if len(remaining) == len(todos):
        return False
    save_todos(remaining, file_path)
    return True


def print_todos(file_path: Path = DEFAULT_FILE) -> None:
    """在终端打印所有待办事项。"""
    todos = load_todos(file_path)
    if not todos:
        print("还没有待办事项。")
        return
    for todo in todos:
        mark = "x" if todo["completed"] else " "
        print(f"{todo['id']}. [{mark}] {todo['title']}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="一个简单的命令行待办事项程序")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="新增待办事项")
    add_parser.add_argument("title", help="待办事项的内容")

    subparsers.add_parser("list", help="列出所有待办事项")

    complete_parser = subparsers.add_parser("complete", help="完成待办事项")
    complete_parser.add_argument("id", type=int, help="待办事项编号")

    delete_parser = subparsers.add_parser("delete", help="删除待办事项")
    delete_parser.add_argument("id", type=int, help="待办事项编号")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "add":
        todo = add_todo(args.title)
        print(f"已添加：{todo['id']}. {todo['title']}")
    elif args.command == "list":
        print_todos()
    elif args.command == "complete":
        print("已完成。" if complete_todo(args.id) else "找不到这个编号。")
    elif args.command == "delete":
        print("已删除。" if delete_todo(args.id) else "找不到这个编号。")


if __name__ == "__main__":
    main()
