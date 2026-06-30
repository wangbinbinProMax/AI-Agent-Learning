# Day 2：Python 基础语法通关

**日期**：2026-06-30
**学习用时**：X 小时
**状态**：✅ 完成

---

## 🎯 今天学了什么

- 函数的定义与调用（`def`、参数、返回值）
- 条件判断（`if / elif / else`）
- 循环（`for`、`while`）
- 列表操作（切片、列表推导式）
- 字典操作（增删改查、`get()` 方法）
- 字符串处理（`split()`、`strip()`、`join()`）

---

## 📝 代码实现：6 个函数

### 1. `greet(name)` — 问候函数
```python
def greet(name):
    return f"你好，{name}！欢迎来到 Python 世界 🐍"

greet("张三")  # → "你好，张三！欢迎来到 Python 世界 🐍"
```

### 2. `is_even(n)` — 判断偶数
```python
def is_even(n):
    return n % 2 == 0

is_even(4)  # → True
is_even(7)  # → False
```

### 3. `fizzbuzz(n)` — FizzBuzz 经典面试题
```python
# 规则：
# - 被 3 整除 → "Fizz"
# - 被 5 整除 → "Buzz"
# - 同时被 3 和 5 整除 → "FizzBuzz"
# - 否则返回数字本身
```

**关键点**：必须先判断 `i % 3 == 0 and i % 5 == 0`（即被 15 整除），否则会先匹配到单独的 3 或 5 的规则。

### 4. `count_words(text)` — 词频统计
```python
def count_words(text):
    words = text.lower().split()          # 转小写 + 按空格分词
    freq = {}
    for word in words:
        word = word.strip(".,!?;:\"'()（）")  # 去掉标点
        if word:
            freq[word] = freq.get(word, 0) + 1   # 计数
    return freq
```

**`dict.get(key, default)`** 是个很实用的方法：key 存在返回对应值，不存在返回默认值 0。

### 5. `reverse_sentence(s)` — 反转单词顺序
```python
def reverse_sentence(s):
    words = s.split()
    return " ".join(words[::-1])   # [::-1] 是列表反转的切片写法

reverse_sentence("我 爱 学习")  # → "学习 爱 我"
```

### 6. `filter_by_length(strings, min_len)` — 按长度过滤
```python
def filter_by_length(strings, min_len):
    return [s for s in strings if len(s) >= min_len]
    #      ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ 这是"列表推导式"

filter_by_length(["a", "ab", "abc"], 2)  # → ["ab", "abc"]
```

---

## 💡 今日重点理解

| 概念 | 一句话解释 | 示例 |
|------|-----------|------|
| `f-string` | 字符串中直接嵌入变量 | `f"你好 {name}"` |
| `[::-1]` | 列表/字符串反转的切片语法 | `[1,2,3][::-1]` → `[3,2,1]` |
| `dict.get(key, default)` | 安全地从字典取值，不存在也不会报错 | `d.get("a", 0)` |
| 列表推导式 | 一行代码生成新列表 | `[x*2 for x in lst if x>0]` |

---

## 🐛 踩坑记录

1. **FizzBuzz 的判定顺序**：如果先判断 `i % 3 == 0`，那 15 会被判成 "Fizz" 而不是 "FizzBuzz"。正确做法是先判断 `i % 3 == 0 and i % 5 == 0`。

---

## ⏭️ 明天计划

- Day 3：数据结构实战（列表/字典/集合/元组）
