"""
Day 1 — Hello World
打印当前时间、Python 版本、虚拟环境路径
"""
import sys
import platform
import os
from datetime import datetime


def get_venv_path() -> str:
    """返回当前虚拟环境路径"""
    return sys.prefix


def get_python_info() -> dict:
    """收集 Python 环境信息"""
    return {
        "python_version": sys.version,
        "platform": platform.platform(),
        "venv_path": get_venv_path(),
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "executable": sys.executable,
    }


def main():
    # Windows 终端可能有编码问题，设置 UTF-8
    if sys.platform == "win32":
        os.system("chcp 65001 > nul")

    info = get_python_info()

    print("=" * 50)
    print("[Day 1] Hello, AI Agent Developer!")
    print("=" * 50)
    print(f"  Current Time : {info['current_time']}")
    print(f"  Python       : {info['python_version'].split()[0]}")
    print(f"  Platform     : {info['platform']}")
    print(f"  Virtual Env  : {info['venv_path']}")
    print(f"  Interpreter  : {info['executable']}")
    print("=" * 50)
    print(">> Day 1 complete. Let the AI Agent journey begin!")


if __name__ == "__main__":
    main()
