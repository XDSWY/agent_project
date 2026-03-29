from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnableLambda  # 自定义函数注入

model = ChatTongyi(model="qwen3-max")
str_parser = StrOutputParser()

#第一个提示词模版
first_prompt = PromptTemplate.from_template(
    "我的邻居姓:{lastname},刚生了{gender},请起名，仅生成一个名字，并告知我名字，不要额外的信息"
)

#第二个提示词模版
second_prompt = PromptTemplate.from_template(
    "姓名:{name},请帮我解析含义"
)

# 自定义函数，函数的入参：AIMessage -> dict ({"name": "xxx"})
# my_func = RunnableLambda(lambda ai_msg: {"name": ai_msg.content})

# chain = first_prompt | model | my_func | second_prompt | model | str_parser
# 可以直接将函数语句写进链中，直接使用
chain = first_prompt | model | (lambda ai_msg: {"name": ai_msg.content}) | second_prompt | model | str_parser

for chunk in chain.stream({"lastname": "宋", "gender": "女儿"}):
    print(chunk, end="", flush=True)