# Day 1：环境搭建与 Hello World

**日期**：2026-06-30
**学习用时**：X 小时
**状态**：✅ 完成

---

## 🎯 今天学了什么

- 安装 Python 3.11
- 创建虚拟环境 `agent_learning/`
- 安装依赖包：`requests`、`python-dotenv`、`black`
- 写了第一个脚本 `hello.py`

---

## 📝 学习笔记

### 1. 虚拟环境

虚拟环境的作用是让每个项目的依赖隔离开，互不干扰。

```bash
# 创建虚拟环境
python -m venv agent_learning

# 激活虚拟环境（Windows）
agent_learning\Scripts\activate

# 激活虚拟环境（Mac/Linux）
source agent_learning/bin/activate
```

### 2. 安装包

```bash
pip install requests python-dotenv black
pip freeze > requirements.txt  # 导出依赖列表
```

### 3. hello.py 代码

```python
import sys
import datetime

print(f"当前时间：{datetime.datetime.now()}")
print(f"Python 版本：{sys.version}")
print("Hello, AI Agent!")
```

---

## 🐛 踩坑记录

1. **问题**：激活虚拟环境时报错 "无法加载文件..."
   **解决**：以管理员身份运行 `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

---

## 💡 今日收获

- 理解了虚拟环境的作用——隔离项目依赖
- 学会了用 `pip freeze > requirements.txt` 导出依赖

---

## ⏭️ 明天计划

- Day 2：基础语法通关（函数、列表、字典）
