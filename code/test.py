import os
from tavily import TavilyClient
"""
根据城市和天气，使用Tavily Search API搜索并返回优化后的景点推荐。
"""
# 1. 从环境变量中读取API密钥
TAVILY_API_KEY="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"
api_key = TAVILY_API_KEY
if not api_key:
    print("错误:未配置TAVILY_API_KEY环境变量。")

# 2. 初始化Tavily客户端
tavily = TavilyClient(api_key=api_key)

# 3. 构造一个精确的查询
query = f"'杭州' 在'阴雨'天气下最值得去的旅游景点推荐及理由"


# 4. 调用API，include_answer=True会返回一个综合性的回答
response = tavily.search(query=query, search_depth="basic", 
include_answer=True)

print(response)