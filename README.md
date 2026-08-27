# Python Todo

这是一个适合 Python 初学者的待办事项项目。

它同时提供窗口版和命令行版：窗口版使用 Python 自带的 `tkinter`，命令行版用于学习 Python 基础。项目不使用第三方库，使用 JSON 文件保存数据，并用 `unittest` 编写自动化测试。

## 项目结构

    python-todo-cli/
    ├── todo_app.py       # 核心功能和命令行版本
    ├── todo_gui.py       # tkinter 窗口界面
    ├── test_todo_app.py  # 自动化测试
    ├── README.md         # 项目说明
    └── .gitignore        # Git 忽略规则

## 窗口版：推荐初学者使用

在项目目录中运行：

```powershell
python todo_gui.py
```

窗口打开后：

1. 在输入框输入任务，点击“添加”，或按 Enter。
2. 在列表中点击一个任务，再点击“完成选中项目”。
3. 点击一个任务，再点击“删除选中项目”。
4. “刷新”会重新读取 `todos.json`。

窗口版和命令行版使用同一个 `todos.json`，两边的数据会同步。

窗口中还可以切换编号模式：

- `固定编号`：删除任务后，其他任务的编号不变；新任务使用更大的编号。
- `重新编号`：切换后会把当前任务整理成 1、2、3……；之后删除任务也会自动重新编号。

重新编号会修改 `todos.json` 中保存的 `id`。如果你希望任务编号永远不变，请使用“固定编号”。

## 1. 创建虚拟环境

在项目目录中打开 PowerShell：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

如果 PowerShell 阻止脚本运行，可以执行一次：

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## 2. 运行程序

```powershell
python todo_app.py add "学习 Python"
python todo_app.py add "上传 GitHub"
python todo_app.py list
python todo_app.py complete 1
python todo_app.py delete 2
```

数据会保存在项目根目录的 `todos.json`。这个文件被 `.gitignore` 忽略，不会上传个人待办内容。

如果运行环境不允许程序写入项目目录，可以临时指定保存位置：

```powershell
$env:TODO_FILE = "$env:TEMP\todos.json"
python todo_app.py add "测试环境"
python todo_app.py list
```

## 3. 运行测试

```powershell
python -m unittest -v
```

## 4. 上传 GitHub

先在 GitHub 网页创建一个名为 `python-todo-cli` 的空仓库。新仓库不要预先创建 README、`.gitignore` 或 License 文件。然后在项目目录运行：

```powershell
git remote add origin https://github.com/你的用户名/python-todo-cli.git
git push -u origin main
```

把命令中的地址换成你自己的仓库地址。

以后修改代码后，使用下面三条命令提交并上传新版本：

```powershell
git add .
git commit -m "说明这次修改了什么"
git push
```
