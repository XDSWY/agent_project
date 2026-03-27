from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个诗人，可以作诗"),
        MessagesPlaceholder("history"),
        ("human", "再来一首诗"),
    ]
)

history_data = [
    ("human", "写一首唐诗"),
    ("ai","床前明月光，疑是地上霜，举头望明月，低头思故乡"),
    ("human", "好诗再来一首"),
    ("ai","锄禾日当午，汗滴禾下土，谁知盘中餐，粒粒皆辛苦"),
]

"""
prompt_value = chat_prompt_template.invoke({"history": history_data}).to_string()

print(prompt_value)

model = ChatTongyi(model="qwen3-max")

res = model.invoke(prompt_value)

print(res.content)

"""
model = ChatTongyi(model="qwen3-max")

# 形成一条链，chat_prompt_template的输出作为输入传入到model中去执行
# 组成链，要求每一个组件都是Runnable接口的子类
chain = chat_prompt_template | model

# 通过链去调用invoke或stream（将历史记录返回给聊天模版，聊天模版接收后给model，model接收后给res进行返回）
# res = chain.invoke({"history": history_data})
# print(res.content)

for chunk in chain.stream({"history": history_data}):
    print(chunk.content,end="",flush=True)