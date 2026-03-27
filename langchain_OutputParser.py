from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

str_parser = StrOutputParser()
json_parser = JsonOutputParser()

model = ChatTongyi(model="qwen3-max")

#第一个提示词模版
first_prompt = PromptTemplate.from_template(
    "我的邻居姓:{lastname},刚生了{gender},请起名，"
    "并封装为json格式返回。要求key是name，value是你起的名字，请严格遵守要求。"
)

#第二个提示词模版
second_prompt = PromptTemplate.from_template(
    "姓名:{name},请帮我解析含义"
)

# 第一个提示词模版的问题给model，然后让模型返回json格式，json_parser会返回一个字典，再将这个字典写入第二个提示词模版，再将第二个提示词模版注入模型，最后返回字符串
chain = first_prompt | model | json_parser | second_prompt | model | str_parser

for chunk in chain.stream({"lastname": "宋", "gender": "女儿"}):
    print(chunk, end="", flush=True)