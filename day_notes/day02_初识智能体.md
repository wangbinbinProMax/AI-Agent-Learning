# 智能旅行助手项目学习

## 准备工作：

1. 为了在python里获取网络，我们需要**HTTP库（requests）**

2. `tavily-python`为需要联网获取最新、最实用信息的Agent应用提供支持

   安装命令：`pip install requests tavily-python openai`

3. 指令词设计，告诉LLM它应该以什么身份，用哪些工具实现目标

4. 查询真实天气：`wttr.in`是免费的天气查询服务以json格式返回指定的天气数据

```python
import requests

def get_weather(city:str) -> str:
	"""
	通过调用wttr.in API获取真实的天气信息
	"""
	#API端点，我们请求JSON格式的数据
	url = f"https://wttr.in/{city}?format=j1"
	
	try:
		#发起网络请求
		response = requests.get(url)
		#检查响应状态码是否为200（成功）
		response.raise_for_status()
		#解析返回的JSON数据
		data = response.json()
		#提取当前天气状况
		current_condition = data['current_condition'][0]
		weather_desc = current_condtion['weatherDesc'][0]['value']
		temp_c = current_condition['temp_c']
		
		#格式化成自然语言返回
		return f"{city}当前天气：{weather_desc}，气温{temp_c}摄氏度"
		
	except requests.exceptions.RequestsException as e:
		#处理网络错误
		return f"错误：查询天气时遇到网络问题 - {e}"
	except (Keyerror, IndexError) as e:
		#处理数据解析错误
		return f"错误：解析天气数据失败，可能是城市名称无效 - {e}"
```

5. 搜索并推荐旅游景点，定义新工具`search_attraction`

```python
import os
from tavily import TavilyClient

def get_attraction(city: str, weather: str) -> str:
	"""
	根据城市和天气，使用Tavily Search API搜索并返回优化后的景点推荐
	"""
	#1.从环境变量中读取API密钥
	api_key = os.environ.get("TAVILY_API_KEY")
	if not api_key:
		return f"错误：未配置TAVILY_API_KEY环境变量。"
	
	#2.初始化Tavily客户端
	tavily = TavilyClient(api_key=api_key)
	
	#3.构造一个精确的查询
	query = f"'{city}'在'{weather}'天气下最值得取得旅游景点推荐及理由"
	
	try:
		#4.调用API，include_answer=True会返回一个综合性的回答
		response = tavily.search(query=query, search_depth="basic", include_answer=True)
		
		#5.Tavily返回的结果已经非常干净可以直接使用
		#response['answer']是一个基于所有搜索结果的总结性回答
		#防御性编程，最差也是返回none，程序不会崩溃
		if response.get("answer"):
			return response["answer"]
			
		#如果没有综合性回答，则格式化原始结果
		formatted_results = []
		#response.get("result", [])也是一种防御性编程方法，有result就返回列表，没有result就返回空列表
		for result in response.get("result", []):
			formatted_results.append(f"- {result['title']}:{result['content']}")
			
		if not formatted_results:
			return "抱歉，没有找到相关的旅游景点推荐"
		
		return "根据搜索，为您找到以下信息：\n" + "\n".join(formatted_results)
	
	except Exception as e:
		return f"错误：执行Tavily搜索时出现问题 - {e}"
```

将所有工具放入一个字典，供主循环调用：

```python
#将所有工具函数放入一个字典，方便后面调用
available_tools = {
    "get_weather": get_weather,
    "get_attraction": get_attraction,
}
```

## 接入大语言模型

很多大模型服务提供商都提供了和open AI API相似的接口规范，我们使用一个通用的客户端`openAICompatibleClient`，它可以连接到任何兼容open AI接口规范的大模型服务。

```python
form openai import OpenAI

class OpenAICompatibleClient:
    """
    一个用于调用任何兼容OpenAI接口的LLM服务的客户端
    """
    #__init__是类的构造函数，当我创建一个对象时，自动设置它的初始状态
    def __init__(self, model: str, api_key: str, base_url: str):
        self.model = model
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        
    def generate(self, prompt: str, system_prompt: str) -> str:
    	"""调用LLM API来生成回应"""
    	print("正在调用大语言模型...")
    	try:
    		#这是OpenAI API的标准格式，'system'表示AI，'user'表示用户，system_prompt是为了约束AI的行为，prompt是用户的提问
    		messages = [
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': prompt}
    		]
    		response = self.client.chat.completions.create(
    			model = self.model,
    			messages = messages,
    			stream = false
    		)
    		answer = response.choices[0].message.content
    		print("大语言模型响应成功。")
    		return answer
    	except Exception as e:
    		print(f"调用LLM API时发生错误：{e}")
    		return "错误：调用语言模型服务时出错。"
```

我们已经创建了一个客户端类，为了实例化此类，我们还需要三个信息：`API_KEY`、`BASE_URL`和`MODEL_ID`。

## 主循环

整合所有组件，通过格式化后的Prompt驱动大模型进行决策。

```python
import re

#--- 1.配置LLM客户端 ---
#根据你日常使用的服务，将这里替换成对应的凭证和地址
API_KEY = "..."
BASE_URL = "..."
MODEL_ID = "..."
TAVILY_API_KEY = "..."
os.environ['TAVILY_API_KEY'] = "..."

llm = OpenAICompatibleClient(
	model = MODEL_ID,
	api_key = API_KEY,
	base_url = BASE_URL
)

# --- 2. 初始化 ---
user_prompt = "你好，请帮我查询一下今天杭州的天气，然后根据天气推荐一个合适的旅游景点。"
prompt_history = [f"用户请求：{user_prompt}"]

print(f"用户输入：{user_prompt}\n" + "="*40)

# --- 3. 运行主循环 ---
for i in range(5): #设置最大循环次数
	print(f"--- 循环 {i+1} ---\n")
	
	# 3.1. 构建Prompt
	full_prompt = "\n".join(prompt_history)
	
	# 3.2. 调用LLM进行思考
	llm_output = llm.generate(full_prompt, system_prompt=AGENT_SYSTEM_PROMPT)
	# 模型可能会输出多余的Thought-Action，需要截断
	match = re.search(r'(Thought:.*?Action:.*?)(?=\n\s*(?:Thought:|Action:|Observation:)|\Z)', llm_output, re.DOTALL)
	if match:
	truncated = match.group(1).strip()
	if truncated != llm_output.strip():
		llm_output = truncated
		print("已截断多余的Thought-Action对")
	print(f"模型输出：\n{llm_output}\n")
	prompt_history.append(llm_output)
	
	# 3.3. 解析并执行行动
	action_match = re.search(r"Action:(.*)", llm_output, re.DOTALL)
	if not action_match:
		observation = "错误：未能解析到Action字段。请确保你的回复严格遵循'Thought:...Action:...'的格式。"
		observation_str = f"observation: {observation}"
		print(f"{observation_str}\n" + "="*40)
		prompt_history.append(observation_str)
		continue
	action_str = action_match.group(1).strip()
	
	if action_str.startswitch("Finish"):
		final_answer = re.match(r"Finish\[(.*)\]", action_str).group(1)
		print(f"任务完成，最终答案：{final_answer}")
		break
	
	tool_name = re.search(r"(\w+)\(", action_str).group(1)
	args_str = re.search(r"\((.*)\)", action_str).group(1)
	kwargs = dict(re.findall(r'(\w+)="([^"]*)"', args_str))
	
	if tool_name in available_tools:
        # 假设 kwargs = {"query": "杭州天气", "city": "杭州"}
        # 正常调用 search_function(query="杭州天气", city="杭州")
        # 使用 **kwargs 解包 search_function(**kwargs)  # 等价于上面的调用
		observation = available_tools[tool_name](**kwargs)
	else:
		observation = f"错误：未定义的工具 '{tool_name}'"
	
	# 3.4. 记录观察结果
	observation_str = f"observation: {observation}"
	print(f"{observation_str}\n" + "="*40)
	prompt_history.append(observation_str)
```

