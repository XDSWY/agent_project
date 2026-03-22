from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi
#zero-shot(零提示词)：完全信赖模型

from langchain访问LLM import model

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}，刚生了个{gender}，帮我起个名字，简单回答"
)
model = Tongyi(model = "qwen-max")
# prompt_text = prompt_template.format(lastname="宋", gender="女儿")

# model = Tongyi(model = "qwen-max")
# res = model.invoke(input=prompt_text)
# print(res)

# 把提示词和模型连接成链
chain = prompt_template | model
res = chain.invoke(input={"lastname":"宋","gender":"女儿"})
print(res)