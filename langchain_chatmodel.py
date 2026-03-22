# from langchain_community.chat_models.tongyi import Tongyi
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_ollama import OllamaLLM

# model = ChatTongyi(model = "qwen3:4b")
model = OllamaLLM(model = "qwen3:4b")

messages =[
    # 动态的方便在运行时填充具体值，后续学习提示词模版会用到
    ("system","你是一个写离别诗的诗人"), # 动态的，由langchain内部机制转化为Message类对象
    ("human","写一首唐诗"),
    ("ai","锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
    ("human","根据上一个回复的内容在写一首"),
    """
    SystemMessage(content="你是一个写离别诗的诗人"), # 静态的，直接获得Message类对象
    HumanMessage(content="写一首唐诗"),
    AIMessage(content="锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
    HumanMessage(content="根据上一个回复的内容在写一首"),
    """
]

res = model.stream(input=messages)

for chunk in res:
    print(chunk,end="",flush=True)