# 🧠 AI Agent 应用开发 — 8周学习计划（每日产出版）

---

## 📅 第1周：Python 基础与开发环境

> **整体目标**：能独立写出与 API 交互的 Python 脚本，掌握 virtualenv/pip/Git 工作流

---

### Day 1：环境搭建与 Hello World

**产出**：
- [x] 安装 Python 3.10+，执行 `python --version` 截图
- [x] 创建并激活虚拟环境 `agent_learning/`，执行 `pip list` 截图
- [x] 安装 `requests`、`python-dotenv`、`black`，生成 `requirements.txt`
- [x] Hello World 脚本 `hello.py` 打印当前时间、Python 版本、虚拟环境路径

### Day 2：基础语法通关

**产出**：
- `basics.py`，包含以下 6 个函数并通过打印验证：
  - `greet(name)` → 返回问候语
  - `is_even(n)` → 返回布尔值
  - `fizzbuzz(n)` → 返回 1 到 n 的 FizzBuzz 结果列表
  - `count_words(text)` → 返回单词频率字典
  - `reverse_sentence(s)` → 反转句子中的单词顺序
  - `filter_by_length(strings, min_len)` → 过滤列表中长度 ≥ min_len 的字符串

### Day 3：数据结构实战

**产出**：
- `data_structures.py`，完成以下 4 个练习：
  - **列表**：实现学生成绩管理器（增删改查排序），输出成绩分布（优/良/中/及格）
  - **字典**：电话簿应用（按姓名存/查/删/列），处理同名冲突（用列表存多个号码）
  - **集合**：两篇英文文章的共同词汇统计
  - **元组**：存储不可变的地理坐标，计算两点距离

### Day 4：文件读写与异常处理

**产出**：
- `file_handler.py`，实现 3 个功能：
  - `read_config(path)` → 读取 JSON 配置文件，处理 FileNotFoundError
  - `append_log(path, message)` → 追加日志，自动加时间戳
  - `safe_divide(a, b)` → 安全除法，捕获 ZeroDivisionError 和 TypeError
- 一个 `test_config.json` 测试文件
- 一次"故意犯错"的记录（如读不存在的文件），截图异常输出

### Day 5：面向对象入门

**产出**：
- `oo_basics.py`，定义以下类并实例化测试：
  - `Tool` 基类：属性 `name`, `description`；方法 `execute(**kwargs)` → 抛出 NotImplementedError
  - `CalculatorTool(Tool)`：实现四则运算，重写 `execute()`
  - `ToolRegistry`：管理多个 Tool 实例，方法 `register(tool)`、`list_tools()`、`find(name)`
- 打印输出展示 3 个类的使用

### Day 6：HTTP 请求与 JSON 处理

**产出**：
- `api_caller.py`，实现：
  - `fetch_json(url, params=None)` → 发 GET 请求，返回 dict，处理 timeout/HTTPError
  - `post_json(url, data)` → 发 POST 请求，返回 dict
  - 使用 [JSONPlaceholder](https://jsonplaceholder.typicode.com/) 假接口测试
- 完成以下调用并打印结果：
  - 获取一篇假文章（GET /posts/1）
  - 创建一篇文章（POST /posts）
  - 用 `.env` 文件管理一个假 API Key

### Day 7：综合练习 — 天气小助手

**产出**：
- `weather_app.py`，完整功能：
  - 从 `.env` 读取 OpenWeatherMap API Key
  - 用户输入城市名 → 获取天气
  - 输出格式：`🌍 城市 | 🌡️ 温度 | 💧 湿度 | ☁️ 天气描述 | 🌬️ 风速`
  - 完整的异常处理（网络错误、城市不存在、API Key 未设置）
  - 支持 `--city CityName` 命令行参数

📦 **第1周交付物清单**：
```
agent_learning/
├── requirements.txt
├── .env.example
├── hello.py
├── basics.py
├── data_structures.py
├── file_handler.py
├── oo_basics.py
├── api_caller.py
└── weather_app.py
```

---

## 📅 第2周：AI/ML 基础概念 + API 初体验

> **整体目标**：理解 AI 核心概念，能调用 LLM API 完成多轮对话

---

### Day 8：AI 概念扫盲

**产出**：
- `concepts.md`，用自己的话写出以下 10 个术语的解释（每个 ≤3 句话，有类比）：
  - LLM / Token / Embedding / Fine-tuning / RAG / Context Window
  - System Prompt / Temperature / Hallucination / Agent
- 画一张"LLM 工作流程"简图（拍照或 draw.io 导出）

### Day 9：Transformer 通俗理解

**产出**：
- `transformer_notes.md`，包含：
  - 用大白话解释"注意力机制"（给朋友能讲懂的程度）
  - Transformer 的 Encoder-Decoder 结构简图
  - Token → Embedding → 多层处理 → 输出 Token 的完整流程（用 5 步概述）

### Day 10：API 密钥与计费

**产出**：
- `api_setup.md`，记录：
  - 在至少一个平台注册并获取 API Key（Anthropic / OpenAI / 国内大模型平台）
  - 各平台的主要模型名称、价格表（每 1K Token 的价格）
  - 在 `.env` 文件中正确配置（API Key + Base URL），输出 `print(os.getenv("API_KEY")[:8] + "***")` 验证
- 设置好 API 消费限额/警报

### Day 11：第一个 API 调用

**产出**：
- `first_chat.py`，实现：
  - 调用 LLM API，发送"你好，请用三句话介绍你自己"
  - 打印完整响应，包括：模型名、Token 用量（prompt_tokens / completion_tokens）、响应内容
  - 用 `python-dotenv` 加载密钥，不在代码中硬编码
  - 打印格式：
    ```
    🤖 模型: claude-sonnet-4-6
    📊 Token: 输入=12, 输出=45, 总计=57
    💬 回复: ...
    ```

### Day 12：控制生成参数

**产出**：
- `param_experiments.py` 或一个 Jupyter Notebook `param_lab.ipynb`：
  - 同一问题"写一首关于秋天的五言绝句"，测试以下参数组合：
    - temperature: [0, 0.3, 0.7, 1.0]
    - max_tokens: [50, 200]
  - 输出每个组合的结果 + 你的观察笔记（哪个组合最有创意/最稳定）
- `param_guide.md`：记录你对 temperature / top_p / max_tokens 的理解

### Day 13：System Prompt 实战

**产出**：
- `system_prompt_lab.py`，完成 3 个实验：
  - **实验①**：同一个问题"解释量子计算"，用 3 种 System Prompt 风格（教授/小学生/脱口秀演员）分别回答
  - **实验②**：设计一个"代码审查助手"的 System Prompt，测试它对一段有 bug 代码的审查效果
  - **实验③**：写一个 JSON 输出的 System Prompt，测试输出格式稳定性
- `system_prompt_notes.md`：总结 System Prompt 的 5 条设计原则

### Day 14：周末总结 — 知识卡片

**产出**：
- `week2_summary.md`：
  - 画出 LLM API 调用的完整流程图（参数准备 → 请求 → 响应解析 → Token 统计）
  - 列出你学到的 3 个最重要的经验和 2 个踩过的坑
  - 写出下周想深入探索的 3 个问题

📦 **第2周交付物清单**：
```
agent_learning/
├── concepts.md
├── transformer_notes.md
├── api_setup.md
├── first_chat.py
├── param_experiments.py / param_lab.ipynb
├── param_guide.md
├── system_prompt_lab.py
├── system_prompt_notes.md
└── week2_summary.md
```

---

## 📅 第3周：Prompt Engineering（提示词工程）

> **整体目标**：掌握与 LLM 高效沟通的系统方法，能设计可靠的结构化 Prompt

---

### Day 15：Prompt 基本原则

**产出**：
- `prompt_principles.md`：总结 7 条 Prompt 设计原则（清晰/上下文/角色/格式/示例/约束/迭代）
- `prompt_before_after.py`：选 3 个你之前写的不够好的 Prompt，逐一优化，每个展示：
  - ❌ 优化前的 Prompt + LLM 回复
  - ✅ 优化后的 Prompt + LLM 回复
  - 📝 改进了什么地方

### Day 16：Few-shot Prompting

**产出**：
- `few_shot_lab.py`，完成 3 个实验：
  - **零样本**：让 LLM 判断 5 条电影评论的情感（正面/负面），记录正确率
  - **少样本（3 个示例）**：同样的 5 条评论，记录正确率
  - **少样本（5 个示例 + 风格要求）**：要求按特定格式输出，记录输出格式符合率
- `few_shot_notes.md`：总结何时需要用 Few-shot，何时不需要

### Day 17：Chain of Thought（思维链）

**产出**：
- `cot_lab.py`，设计 5 道需要推理的题目（数学、逻辑、规划各 1-2 道），每题测试：
  - 直接回答（不加 CoT 引导）
  - 加上"让我们一步步思考"/"请先分析再给答案"
- `cot_results.md`：对比表格（题目 | 直接回答正确? | CoT 正确? | 分析），总结 CoT 在什么类型的任务上最有效

### Day 18：结构化输出

**产出**：
- `structured_output.py`，实现：
  - **新闻解析器**：输入新闻文本 → 输出严格 JSON `{"title": "", "summary": "", "keywords": [], "sentiment": "positive/neutral/negative", "entities": [{"name": "", "type": ""}]}`
  - 测试至少 3 篇不同领域的新闻
  - 用 `json.loads()` 验证输出格式，解析失败则记录并重试
- `json_schema_guide.md`：写 JSON Schema 约束的 5 个要点

### Day 19：Prompt 模板化

**产出**：
- `prompt_templates.py`，创建一个模板库，至少 8 个模板：
  - `SUMMARIZE` / `TRANSLATE` / `CODE_EXPLAIN` / `CLASSIFY`
  - `BRAINSTORM` / `EMAIL_REPLY` / `OUTLINE_GENERATE` / `QA_PAIR_GENERATE`
- 每个模板支持 `{variable}` 参数替换
- `template_demo.py`：展示所有模板的使用示例

### Day 20：Prompt 调试技巧

**产出**：
- `prompt_debug_log.md`：记录本周遇到的所有 LLM 输出问题，每个问题包含：
  - 原始 Prompt + 错误输出
  - 问题分类（输出截断/格式错误/幻觉/跑题/太啰嗦）
  - 修复方法 + 修复后 Prompt + 正确输出
- 至少 5 个调试案例

### Day 21：综合练习 — AI 读书笔记生成器

**产出**：
- `reading_notes_bot.py`，完整功能：
  - 用户粘贴文章链接或文本 → LLM 生成结构化读书笔记
  - 笔记包含：核心观点、关键论据、个人可行动项、3 个延伸问题
  - 支持 3 种输出风格：精炼版（200字内）/ 详细版 / 思维导图大纲版
  - 测试 3 篇不同类型的内容（技术文章、新闻、散文）

📦 **第3周交付物清单**：
```
agent_learning/
├── prompt_principles.md
├── prompt_before_after.py
├── few_shot_lab.py
├── few_shot_notes.md
├── cot_lab.py
├── cot_results.md
├── structured_output.py
├── json_schema_guide.md
├── prompt_templates.py
├── template_demo.py
├── prompt_debug_log.md
└── reading_notes_bot.py
```

---

## 📅 第4周：Function Calling / Tool Use

> **整体目标**：这是 Agent 开发核心周 — 掌握 LLM 调用工具的完整循环

---

### Day 22：Tool Use 概念理解

**产出**：
- `tool_use_notes.md`：
  - 画出"LLM 调用工具"的时序图（Mermaid 或手绘）
  - 解释：如果 LLM 不能调用工具，Agent 为什么做不了？
  - 列出真实 Agent 产品中会用到的 10 种工具（如搜索、计算、发邮件、查数据库…）
- 阅读 Anthropic/OpenAI 的 Tool Use 官方文档，摘录关键 API 格式

### Day 23：定义 Tool Schema

**产出**：
- `tool_schemas.py`，定义 5 个工具的 JSON Schema：
  - `get_weather(city: str)` → `{temperature, humidity, condition}`
  - `calculator(expression: str)` → `{result: float}`
  - `search_web(query: str)` → `{results: [{title, url, snippet}]}`
  - `send_email(to: str, subject: str, body: str)` → `{success: bool}`
  - `get_stock_price(symbol: str)` → `{symbol, price, change_percent}`
- 打印完整的 tools 数组，确认格式与 API 文档一致

### Day 24：单工具调用

**产出**：
- `single_tool_agent.py`，实现：
  - 定义一个真正的 `calculator` 工具（用 Python `eval`，做好安全过滤）
  - LLM 收到数学问题 → 返回 tool_call → 执行计算 → 结果送回 → 最终回复
  - 打印每一步的完整信息：
    ```
    [Step 1] 用户: 23 * 45 + 678 = ?
    [Step 2] LLM 决定调用: calculator(expression="23*45+678")
    [Step 3] 工具返回: {"result": 1713}
    [Step 4] LLM 最终回复: 23 × 45 + 678 = 1713
    ```
  - 测试 5 个不同难度的数学题

### Day 25：多工具调用

**产出**：
- `multi_tool_agent.py`，在 Day 24 基础上：
  - 增加 `get_current_time()` 和 `get_date_after_days(days: int)` 两个工具
  - 实现：用户问"现在是几点？180 天前是什么日期？" → LLM 连续调用 2 个工具 → 给出完整回答
  - 特别验证：当用户问题需要调用 2 个以上工具时，LLM 是否做出了正确选择
  - 记录至少 1 个 LLM 选错工具或漏掉工具的失败案例

### Day 26：处理 Tool 结果

**产出**：
- `tool_result_handler.py`，重点解决：
  - **结果裁剪**：工具返回了 5000 字，如何压缩到 500 字送回 LLM
  - **结果格式化**：将工具返回的 dict 转成 LLM 容易理解的文本描述
  - **错误结果**：工具执行失败时，返回 `{"error": "..."}`，LLM 正确理解并告知用户
  - 写 `format_tool_result(tool_name, raw_result)` 通用函数
- 测试：搜索工具返回超长结果 → 裁剪后 LLM 能否正常总结

### Day 27：错误处理与边界情况

**产出**：
- `tool_error_handling.py`，实现：
  - 工具超时（2 秒未返回则中断）
  - 工具返回格式不符合 Schema
  - 工具抛出未预期的异常
  - LLM 调用了不存在的工具（幻觉）
  - 每种情况都有对应的降级策略 + 用户友好提示
- `error_cases.md`：记录你设计的 5 种错误场景和处理方式

### Day 28：小项目 — AI 个人助理

**产出**：
- `personal_assistant.py`，完整功能：
  - 🔧 至少 4 个工具：查天气 / 计算器 / 当前时间 / 记录备忘录
  - 💬 支持多轮对话，直到用户说"再见"
  - 📝 备忘录存到 JSON 文件，下次启动能加载
  - 🛡️ 完整的错误处理
  - 📊 每次对话结束打印 Token 用量汇总
- 和助理做一段至少 10 轮的真实对话，记录完整日志

📦 **第4周交付物清单**：
```
agent_learning/
├── tool_use_notes.md
├── tool_schemas.py
├── single_tool_agent.py
├── multi_tool_agent.py
├── tool_result_handler.py
├── tool_error_handling.py
├── error_cases.md
└── personal_assistant.py  ← 本周重点
```

---

## 📅 第5周：Agent 核心架构

> **整体目标**：手写完整 ReAct Agent、实现记忆系统、建立可观测性

---

### Day 29：Agent 架构总览

**产出**：
- `agent_architecture.md`：
  - 画出 Agent 三大组件的交互图（感知 → 规划 → 执行 → 观察 → 循环）
  - 对比表格：普通 Chatbot vs Tool-using Agent vs Autonomous Agent 的 5 个维度差异
  - 代码层面画出 Agent 的类设计图（Agent / Memory / Tool / Planner 各有什么属性和方法）

### Day 30：短期记忆 — 对话历史管理

**产出**：
- `short_term_memory.py`，实现 `ConversationMemory` 类：
  - `add_message(role, content)` → 添加消息
  - `get_messages()` → 获取完整历史
  - `trim_to_token_limit(max_tokens)` → 保留最近 N 条消息使总 Token ≤ 上限
  - `summarize_old(llm)` → 将超出窗口的旧消息交给 LLM 生成摘要
  - `clear()` → 清空记忆
- 测试：模拟 50 轮对话，验证裁剪和摘要功能

### Day 31：长期记忆 — 向量存储

**产出**：
- `long_term_memory.py`，实现：
  - 安装并使用 ChromaDB
  - `LongTermMemory` 类：
    - `store(topic, content)` → 将一段对话摘要存为向量
    - `search(query, k=5)` → 语义搜索最相关的 k 条记忆
    - `get_context(query)` → 返回可作为 LLM 上下文的格式化记忆文本
  - 集成到 ConversationMemory 中：收到新消息 → 自动存储关键信息
- 测试：存 20 条不同主题的对话 → 搜索"旅行" → 验证返回相关记忆（不是关键词匹配，是语义匹配）

### Day 32：规划能力 — 任务分解

**产出**：
- `task_planner.py`，实现：
  - 给定一个复杂任务（如"规划一次出差行程"），让 LLM 分解为子任务列表
  - 每个子任务包含：`{id, description, depends_on[], estimated_tool}`
  - `TaskPlanner` 类：
    - `decompose(complex_task)` → 返回子任务列表（JSON 格式）
    - `get_next_task(completed_ids)` → 返回下一个可执行的子任务（依赖已满足）
  - 测试 3 个不同类型的复杂任务，验证分解合理性

### Day 33：ReAct Agent — 完整手写实现

**产出**：
- `react_agent.py`，**不依赖任何 Agent 框架**，完整实现：
  ```
  while 未完成:
    1. LLM 思考 → 产出 Thought + Action
    2. 如果需要工具 → 执行 Action → 得到 Observation
    3. Observation 加入上下文 → 回到步骤 1
    4. 如果不需要工具 → 产出最终回答 → 结束
  ```
  - 类结构：
    ```python
    class ReActAgent:
        def __init__(self, llm, tools, memory, max_steps=10)
        def run(self, user_input) -> str  # 返回最终回答
        def _think(self, messages) -> Thought     # LLM 推理
        def _act(self, action) -> Observation     # 执行工具
        def _should_stop(self, thought) -> bool   # 判断是否结束
    ```
  - 每步打印：`🤔 Thought → 🔧 Action → 👁️ Observation`
  - 至少 3 个工具，测试 5 个不同场景

### Day 34：安全与护栏

**产出**：
- `safety_guard.py`，实现：
  - **输入检查**：检测危险关键词（SQL 注入、系统命令、prompt 注入），返回风险等级
  - **输出过滤**：用正则过滤手机号/身份证/邮箱等隐私信息
  - **循环限制**：Agent 最多执行 10 步，超时则强制终止
  - **工具权限**：每个工具标注风险等级（safe/medium/dangerous），dangerous 工具需用户确认
  - `SafetyGuard` 类集成到 ReActAgent 中
- 测试：尝试 3 种攻击场景，验证护栏是否生效

### Day 35：调试与可观测性

**产出**：
- `agent_logger.py`，实现完整的日志系统：
  - 每一步的 Thought / Action / Observation 都写日志
  - 记录 Token 用量（每步 + 累计）
  - 记录耗时（每步 + 总计）
  - `AgentLogger` 类：
    - `log_step(step_num, thought, action, observation)`
    - `log_token_usage(prompt_tokens, completion_tokens)`
    - `save_session(path)` → 保存完整会话记录为 JSON
    - `generate_report()` → 生成可读的会话报告
- 用 ReActAgent 跑一次完整会话 → 生成报告

📦 **第5周交付物清单**：
```
agent_learning/
├── agent_architecture.md
├── short_term_memory.py
├── long_term_memory.py
├── task_planner.py
├── react_agent.py          ← 本周核心：完全手写的 ReAct Agent
├── safety_guard.py
└── agent_logger.py
```

---

## 📅 第6周：RAG + 框架入门

> **整体目标**：搭建知识库问答系统，初步使用 LangChain 等框架

---

### Day 36：RAG 原理与 Embedding

**产出**：
- `rag_notes.md`：画出 RAG 的完整流程图（文档→分块→Embedding→存储→检索→增强→生成）
- `embedding_demo.py`：
  - 调用 Embedding API（如 text-embedding-3-small），对 10 句话生成向量
  - 计算任意两句之间的余弦相似度
  - 验证：语义相近的句子相似度高，不相关的句子相似度低
  - 打印相似度矩阵

### Day 37：向量数据库入门

**产出**：
- `vectordb_demo.py`，使用 ChromaDB：
  - 创建一个 collection
  - 添加 20 条"文档片段"（可用维基百科摘要或自编内容）
  - 实现 `search(query, k=3)` → 返回最相关的 3 条，并显示相似度分数
  - 对比实验：关键词检索 vs 语义检索，对于模糊问题"怎么提高记忆力"，分别返回什么结果
- `chunking_strategies.md`：文档分块的 4 种策略（固定大小/按句子/按段落/语义分块），各自的优劣

### Day 38：搭建完整 RAG 系统

**产出**：
- `rag_qa_system.py`，完整流程：
  ```
  1. 加载文档（支持 .txt / .md / .pdf 至少两种格式）
  2. 文档分块（可配置 chunk_size 和 overlap）
  3. 生成 Embedding 存入 ChromaDB
  4. 用户提问 → 检索相关块 → 拼成 Context → 送 LLM 回答（要求引用来源）
  ```
  - 测试：准备一份至少 3000 字的中文文档 → 问 5 个问题 → 验证回答是否正确引用了文档内容
  - 对比实验：同样的 5 个问题，用 RAG 和不用的结果对比（RAG 用基础 LLM，不用 RAG 时 LLM 只能靠自身知识）

### Day 39：LangChain 入门

**产出**：
- `langchain_hello.py`：
  - 用 LangChain 的 ChatModel 封装 LLM
  - 实现一个简单的 Chain：`PromptTemplate → LLM → StrOutputParser`
  - 实现一个 Tool：用 `@tool` 装饰器定义一个计算器
  - 实现 Agent：用 `create_tool_calling_agent` + `AgentExecutor` 跑一个带工具的 Agent
- `langchain_vs_raw.md`：对比 Day 33 手写版，LangChain 帮你省了多少代码？又带来了什么限制？

### Day 40：其他框架概览

**产出**：
- `framework_survey.py` 或笔记，至少调研并记录：
  - **LangChain**：最流行，抽象多，适合快速原型
  - **AutoGPT**：自主 Agent 先驱，适合长时自主任务
  - **CrewAI**：角色扮演式多 Agent 协作
  - **Dify**：低代码 Agent 平台，适合非程序员
  - **Semantic Kernel**：微软出品，适合 .NET 生态
- 每个框架记录：一句话概括 / 最适合场景 / 一个不足
- 对至少 2 个框架写 "Hello World" 级别的 Demo

### Day 41：LangChain Agent 实战

**产出**：
- `langchain_agent.py`，用 LangChain 实现一个功能完整的 Agent：
  - 至少 3 个工具（搜索/计算/查天气）
  - 包含记忆（ConversationBufferMemory）
  - 与 Day 33 手写版做相同的 5 个测试场景
- `langchain_vs_handwritten.md`：详细的对比分析表，包括：代码行数、灵活性、调试难度、性能、学习曲线

### Day 42：反思与选型

**产出**：
- `framework_decision_guide.md`：
  - 画一个决策树/流程图："我应该用什么方式构建 Agent？"
  - 4 种路径：纯 API 手写 / LangChain / CrewAI / Dify
  - 每种路径的启动条件（项目规模/团队技能/时间约束）
- 为你的最终项目选择一条路径，并写 100 字说明理由

📦 **第6周交付物清单**：
```
agent_learning/
├── rag_notes.md
├── embedding_demo.py
├── vectordb_demo.py
├── chunking_strategies.md
├── rag_qa_system.py        ← 本周重点
├── langchain_hello.py
├── langchain_vs_raw.md
├── framework_survey.py / framework_survey.md
├── langchain_agent.py
├── langchain_vs_handwritten.md
└── framework_decision_guide.md
```

---

## 📅 第7周：多 Agent 系统 + 综合项目

> **整体目标**：理解多 Agent 协作模式，启动最终项目

---

### Day 43：多 Agent 概念与协作模式

**产出**：
- `multi_agent_notes.md`：
  - 多 Agent 的 4 种协作模式（画图）：
    1. **流水线**（Pipeline）：A→B→C 顺序传递
    2. **辩论**（Debate）：多个 Agent 讨论后达成共识
    3. **分层**（Hierarchical）：一个指挥 Agent 分配任务给执行 Agent
    4. **并行**（Parallel）：各自独立完成，合并结果
  - 每种模式的适用场景 + 优缺点
- `pipeline_demo.py`：用 Day 33 的 ReActAgent，实现两个 Agent 串联
  - Agent1（研究员）：根据主题搜索资料 → 输出研究发现
  - Agent2（撰稿人）：根据研究发现 → 写一篇短文

### Day 44：CrewAI 入门

**产出**：
- `crewai_demo.py`，用 CrewAI 创建 3 个 Agent：
  - **需求分析师**：理解用户需求，输出功能清单
  - **架构师**：根据功能清单，设计系统架构
  - **开发者**：根据架构，输出伪代码实现
  - 定义一个 Task 流水线，观察 3 个 Agent 如何协作
- `crewai_notes.md`：CrewAI 的核心概念（Agent/Task/Crew/Tool）、优点和坑

### Day 45：Agent 与外部系统集成

**产出**：
- `external_integrations.py`，实现至少 3 种外部集成：
  - **数据库**：Agent 能查询 SQLite 数据库（根据自然语言问题生成 SQL）
  - **文件系统**：Agent 能读取目录、搜索文件内容
  - **REST API**：Agent 能调用第三方 API（如 GitHub API 查仓库信息）
- 每种集成写一个测试用例

### Day 46：项目选题与设计

**产出**：
- `final_project_plan.md`，包含：
  - **项目名称 + 一句话描述**
  - **用户故事**：3 个典型使用场景
  - **架构图**：Agent / Tool / Memory / UI 的关系
  - **技术选型**：用什么框架、什么模型、什么向量库
  - **工具清单**：Agent 需要哪些工具（至少 4 个）
  - **开发计划**：Day 47-49 的分工

🎯 **项目选题参考**：
1. **智能客服 Agent** — 查知识库 → 解答 → 不能解答则转人工 → 记录工单
2. **代码助手 Agent** — 读 GitHub 仓库 → 回答技术问题 → 生成单元测试
3. **个人学习助手** — 上传学习资料 → 自动出题 → 批改 → 给学习建议
4. **数据分析助手** — 上传 CSV → 理解数据 → 自动写分析代码 → 生成报告
5. **旅行规划 Agent** — 根据预算和偏好 → 搜索景点/酒店 → 生成行程 → 导出 PDF

### Day 47：项目骨架搭建

**产出**：
- 项目仓库初始化：
  - `README.md`（项目介绍 + 使用说明草稿）
  - `requirements.txt`（所有依赖）
  - `.env.example`
  - `src/` 目录结构
  - `main.py`（入口文件）
- 核心 Agent 循环能跑通（哪怕工具都是 mock 的，返回假数据）
- 第一段成功的对话日志

### Day 48：项目功能完善

**产出**：
- 所有工具实现完毕（非 mock）
- 记忆系统集成完毕
- 错误处理覆盖所有工具
- 日志/可观测性系统就绪
- 跑通 3 个完整的用户场景

### Day 49：项目打磨

**产出**：
- 边界情况处理完成（空输入、超长输入、恶意输入）
- 回复质量优化（调整 System Prompt、工具描述、few-shot 示例）
- 至少 5 个端到端测试用例全部通过
- `PROJECT_LOG.md`：项目开发日志，记录了 Day 46-49 的关键决定和踩坑

📦 **第7周交付物清单**：
```
agent_learning/
├── multi_agent_notes.md
├── pipeline_demo.py
├── crewai_demo.py
├── crewai_notes.md
├── external_integrations.py
├── final_project_plan.md
└── final_project/           ← 从 Day 47 开始
    ├── README.md
    ├── requirements.txt
    ├── .env.example
    ├── src/
    │   ├── __init__.py
    │   ├── agent.py
    │   ├── tools.py
    │   ├── memory.py
    │   └── config.py
    ├── main.py
    ├── PROJECT_LOG.md
    └── tests/
        └── test_scenarios.py
```

---

## 📅 第8周：完善 + 部署 + 展示

> **整体目标**：项目上线、作品展示、规划下一步

---

### Day 50：UI 界面开发

**产出**：
- 用 **Streamlit** 或 **Gradio** 搭建 Web 界面：
  - 聊天输入框 + 历史对话展示
  - 工具调用的可视化（展示 Agent 调用了哪个工具、返回了什么）
  - Token 用量实时显示
  - 设置面板（temperature、max_tokens 可调）
- 界面截图（至少 3 张，覆盖不同功能）

### Day 51：测试与评估

**产出**：
- `evaluation.py`，实现：
  - 至少 **15 个测试用例**，覆盖正常/边界/异常场景
  - 对每个用例，记录：正确性（人工评分 1-5）、响应时间、Token 用量
  - 生成评估报告：平均分、最低分场景、Token 效率
- `test_results.md`：评估结果汇总 + 发现的 3 个待改进点

### Day 52：部署准备

**产出**：
- `Dockerfile` + `docker-compose.yml`（容器化）
- 用 Docker 在本地成功运行
- `deployment_guide.md`：部署文档（环境变量配置、启动命令、健康检查）

### Day 53：上线部署

**产出**：
- 部署到以下平台之一（按推荐优先级）：
  1. **HuggingFace Spaces**（免费，最简单）
  2. **Railway / Render**（有免费额度）
  3. **Streamlit Cloud**（如果是 Streamlit 应用）
- 生成一个可分享的公开链接
- 让至少 1 个朋友访问测试，收集反馈

### Day 54：作品展示

**产出**：
- 完善 `README.md`：
  - 项目简介 + GIF/视频 Demo
  - 架构图（用 draw.io 或 Mermaid）
  - 功能列表（带截图）
  - 安装与运行方法（5 分钟内能跑起来）
  - 技术栈说明
  - 未来改进方向
- 将项目 Push 到 GitHub（Public 仓库）
- 在社交媒体/技术社区分享（optional）

### Day 55：进阶方向探索

**产出**：
- `advanced_roadmap.md`，调研并记录以下进阶方向：
  - **Agent 评估体系**：如何系统评估 Agent 质量（AgentBench / 人工评估 / 自动评估）
  - **Agentic RAG**：让 Agent 决定何时检索、检索什么、检索几次
  - **Multi-Agent 编排**：复杂的多 Agent 协作框架（AutoGen / CrewAI 进阶）
  - **Agent 调优**：Prompt 自动优化 / DSPy / RLHF for Agents
  - **生产级 Agent**：流式输出 / 限流 / 缓存 / 降级 / A/B 测试
- 为每个方向标注：学习优先级（高/中/低）+ 推荐学习资源

### Day 56：复盘与总结

**产出**：
- `learning_journey.md`（旅程总结）：
  - **8 周时间线**：每周的核心收获
  - **项目展示**：最终项目的亮点 + 技术难点回顾
  - **技能清单**：列出你现在掌握的所有技能（30+ 项）
  - **踩坑 Top 10**：学习过程中最大的 10 个教训
  - **下一步**：未来 3 个月的学习计划（具体到每个月要达成什么）
- 🎉 **庆祝！你完成了 8 周 AI Agent 开发学习之旅**

📦 **第8周 + 最终交付物清单**：
```
final_project/
├── README.md (完善版)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── deployment_guide.md
├── evaluation.py
├── test_results.md
├── src/
├── main.py (或 app.py)
├── PROJECT_LOG.md
├── screenshots/
│   ├── ui_chat.png
│   ├── ui_tools.png
│   └── ui_settings.png
└── demo.mp4 (可选)

agent_learning/
├── advanced_roadmap.md
└── learning_journey.md
```

---

## 📊 8 周产出总览

| 周 | 主题 | 核心产出 | 代码文件数 |
|----|------|----------|-----------|
| 1 | Python 基础 | 天气脚本 + 基础练习 | 8 个 |
| 2 | AI 概念 + API | 首次 LLM 调用 + 参数实验 | 6 个 + 笔记 |
| 3 | Prompt 工程 | 模板库 + 结构化输出 + 笔记机器人 | 8 个 + 笔记 |
| 4 | Tool Use 🔴 | **个人助理 Agent**（多工具 + 多轮） | 7 个 + 笔记 |
| 5 | Agent 架构 🔴 | **手写 ReAct Agent** + 记忆 + 安全 | 7 个 + 笔记 |
| 6 | RAG + 框架 | 知识库问答 + LangChain 对比 | 9 个 + 笔记 |
| 7 | 多 Agent + 项目 | CrewAI 实验 + **最终项目 MVP** | 5 个 + 项目 |
| 8 | 部署 + 展示 | **可访问的线上应用** + 作品集 | 项目完成 |

**总计**：约 **50+ 个代码文件** + **20+ 份笔记** + **1 个线上应用** + **1 个 GitHub 仓库**

---

## 💡 使用建议

1. **每天打卡**：在每项产出前打勾 `[x]`，保持成就感
2. **遇到阻塞**：一个问题超过 30 分钟没解决就搜/问，不要死磕
3. **周末弹性**：如果工作日落下了，周末补，但尽量不要连续落 3 天
4. **笔记即财富**：每份 `.md` 笔记都是你未来的面试素材和参考手册
5. **Git 记录成长**：从 Day 1 就用 Git，每天 commit，8 周后看 Contribution 绿格子会很有成就感
