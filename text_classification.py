from tkinter.scrolledtext import example

from openai import OpenAI
# 获取client对象
client = OpenAI(
    base_url="http://localhost:11434/v1",
)
example_data = [
    "今天天气真好，心情都变好了！",
    "这电影太难看了，浪费我两个小时。",
    "刚看到一只小猫在路边，好可爱！",
    "早饭随便吃了点，没啥感觉。",
    "地铁又挤又慢，真是受够了。",
    "这个博主讲得挺有道理的，支持一下。",
]

examle_types = [
    "积极",
    "消极",
    "中立"
]

message = [
    "今天加班到十点，累死了。",
    "午饭吃了碗面，一般般吧。",
    "终于周末了，可以好好休息了！",
    "看到新闻说又要降温，真烦。"]

# 调用模型
for i in message:
    response = client.chat.completions.create(
        model="qwen3-vl:4b",
        # messages = [{"role":"system",  "content" : "你现在是一个编码能力超强的助手"}],
        # 可通过历史记录让模型记住规律并进行预测，以及记住上下文
        messages=[{"role": "system", "content": "现在有很多评论需要你做情感分析，情感分别有积极，消极和中立"},
                  {"role": "user", "content": "今天天气真好，心情都变好了！"},
                  {"role": "system", "content": "积极"},
                  {"role": "user", "content": "这电影太难看了，浪费我两个小时。"},
                  {"role": "system", "content": "消极"},
                  {"role": "user", "content": "刚看到一只小猫在路边，好可爱！"},
                  {"role": "system", "content": "积极"},
                  {"role": "user", "content": "早饭随便吃了点，没啥感觉。"},
                  {"role": "system", "content": "中立"},
                  {"role": "user", "content": "地铁又挤又慢，真是受够了。"},
                  {"role": "system", "content": "消极"},
                  {"role": "user", "content": "这个博主讲得挺有道理的，支持一下。"},
                  {"role": "system", "content": "积极"},
                  {"role": "user", "content": f"按照历史记录，回答这几段文本的情感倾向{i}"},
                  ],
        stream=True  # 流式输出
    )

    # 处理结果
    (response.choices[0].message.content)
