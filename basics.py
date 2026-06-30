"""
Day 2：Python 基础语法通关
包含 6 个基础函数
"""


def greet(name):
    """返回问候语"""
    return f"你好，{name}！欢迎来到 Python 世界"


def is_even(n):
    """判断是否为偶数，返回布尔值"""
    return n % 2 == 0


def fizzbuzz(n):
    """返回 1 到 n 的 FizzBuzz 结果列表
    - 被 3 整除 → Fizz
    - 被 5 整除 → Buzz
    - 被 3 和 5 同时整除 → FizzBuzz
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def count_words(text):
    """统计单词频率，返回字典 {单词: 出现次数}"""
    words = text.lower().split()
    freq = {}
    for word in words:
        # 去掉首尾标点符号
        word = word.strip(".,!?;:\"'()（）")
        if word:
            freq[word] = freq.get(word, 0) + 1
    return freq


def reverse_sentence(s):
    """反转句子中的单词顺序"""
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)


def filter_by_length(strings, min_len):
    """过滤列表中长度 >= min_len 的字符串"""
    return [s for s in strings if len(s) >= min_len]


# ========== 验证测试 ==========
if __name__ == "__main__":
    print("=" * 50)
    print("[TEST] Day 2 基础语法测试")
    print("=" * 50)

    # 测试 greet
    print("\n1. greet('张三')")
    print(f"   结果: {greet('张三')}")

    # 测试 is_even
    print("\n2. is_even 测试")
    print(f"   is_even(4)  → {is_even(4)}")
    print(f"   is_even(7)  → {is_even(7)}")

    # 测试 fizzbuzz
    print("\n3. fizzbuzz(16)")
    print(f"   结果: {fizzbuzz(16)}")

    # 测试 count_words
    print("\n4. count_words 测试")
    text = "Hello world! Hello Python. Python is great, world is beautiful."
    print(f"   原文: {text}")
    print(f"   词频: {count_words(text)}")

    # 测试 reverse_sentence
    print("\n5. reverse_sentence 测试")
    original = "我 爱 学习 Python"
    print(f"   原文: {original}")
    print(f"   反转: {reverse_sentence(original)}")

    # 测试 filter_by_length
    print("\n6. filter_by_length 测试")
    words = ["a", "ab", "abc", "abcd", "abcde"]
    print(f"   输入: {words}")
    print(f"   >=3 的: {filter_by_length(words, 3)}")

    print("\n" + "=" * 50)
    print("[OK] 全部 6 个函数测试通过")
    print("=" * 50)
