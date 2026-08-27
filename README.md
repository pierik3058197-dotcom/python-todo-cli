# Python Todo

一个使用 Python 标准库编写的简单待办事项应用，提供 tkinter 窗口界面和命令行界面。

这个项目适合 Python 初学者学习窗口界面、文件读写、模块拆分、自动化测试和 Git 项目结构。

## 功能

- 添加、查看、完成和删除待办事项
- 使用 `todos.json` 保存数据
- 提供 tkinter 窗口界面
- 同时保留命令行界面
- 支持固定编号和重新编号两种模式
- 使用 Python 内置 `unittest` 编写测试
- 不依赖第三方 Python 库

## 环境要求

- Python 3.9 或更高版本
- Windows 和 macOS 通常已自带 tkinter

## 快速开始

在项目目录中运行窗口版：

```powershell
python todo_gui.py
```

窗口打开后：

1. 输入任务，点击“添加”，或按 Enter。
2. 选中任务，点击“完成选中项目”。
3. 选中任务，点击“删除选中项目”。
4. 使用顶部的“固定编号”或“重新编号”切换编号规则。

## 命令行用法

```powershell
python todo_app.py add "学习 Python"
python todo_app.py add "上传 GitHub"
python todo_app.py list
python todo_app.py complete 1
python todo_app.py delete 2
```

## 编号模式

固定编号模式下，删除任务不会改变其他任务的编号，新任务会使用更大的编号。

重新编号模式下，任务会按照当前顺序整理为 `1、2、3……`。切换到该模式或删除任务时，程序会更新 `todos.json` 中保存的编号。

## 数据保存

任务保存在项目目录中的 `todos.json`。这个文件属于运行时数据，已加入 `.gitignore`，不会被提交到 Git。

## 项目结构

    python-todo-cli/
    ├── todo_app.py       # 核心功能和命令行界面
    ├── todo_gui.py       # tkinter 窗口界面
    ├── test_todo_app.py  # 自动化测试
    ├── README.md         # 项目说明
    └── .gitignore        # Git 忽略规则

## 运行测试

```powershell
python -m unittest -v
```

如果看到 `OK`，说明测试通过。
