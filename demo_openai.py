from openai import OpenAI
# 获取client对象
client = OpenAI(
    base_url="http://localhost:11434/v1",
)

# 调用模型
response = client.chat.completions.create(
    model = "qwen3-vl:4b",
    # messages = [{"role":"system",  "content" : "你现在是一个编码能力超强的助手"}],
    # 可通过历史记录让模型记住规律并进行预测，以及记住上下文
    messages = [{"role": "system", "content": "你的计算能力很强并且话很简洁"},
                {"role": "user", "content": "有3只狸花猫"},
                {"role": "system", "content": "好的"},
                {"role": "user", "content": "有7只三花猫"},
                {"role": "system", "content": "好的"},
                {"role": "user", "content": "总共有几只猫？"},
                ],
    stream = True  # 流式输出
)

# 处理结果
# print(response.choices[0].message.content)
for chunk in response:
    print(chunk.choices[0].delta.content,
          end=" ",  # 每段之间以空格分隔
          flush=True  # 立即刷新缓冲区
          )

