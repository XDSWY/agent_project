# from langchain_community.llms.tongyi import Tongyi
from langchain_ollama import OllamaLLM

# qwen3-max是聊天模型，qwen-max是大语言模型
# model = Tongyi(model = "qwen-max")
model = OllamaLLM(model = "qwen3:4b")


# 调用invoke向模型询问，一次性返回完整输出
res = model.invoke(input="你是谁会做什么？")
# 逐段流式输出
for chunk in res:
 print(chunk,end='',flush=True)


