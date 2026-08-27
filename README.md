# Python Todo CLI

这是一个适合 Python 初学者的命令行待办事项项目。它使用 Python 内置的 `argparse` 处理命令，使用 JSON 文件保存数据，并用 `unittest` 编写自动化测试。

## 1. 创建虚拟环境

在项目目录中打开 PowerShell：

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
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

先在 GitHub 网页创建一个名为 `python-todo-cli` 的空仓库，然后在项目目录运行：

```powershell
git init
git add .
git commit -m "初始版本：命令行待办事项程序"
git branch -M main
git remote add origin https://github.com/你的用户名/python-todo-cli.git
git push -u origin main
```

把最后一行中的地址换成你自己的仓库地址。
