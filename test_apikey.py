from openai import OpenAI
import os

client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    # api_key="sk-ebe83703548948189e3e4c5c33f9409c",
    # base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",  # 用阿里云的模型
    base_url="http://localhost:11434/v1",  # 改用本地模型
)
# 三个角色：1.system：设定ai行为，规则等 2.assistant：设定ai的回答内容 3.user：代表用户发送问题
messages = [{"role": "user", "content": "你是谁"}]
completion = client.chat.completions.create(
    model="qwen3-vl:4b",  # 您可以按需更换为其它深度思考模型
    messages=messages,
    extra_body={"enable_thinking": True},
    stream=True
)
is_answering = False  # 是否进入回复阶段
print("\n" + "=" * 20 + "思考过程" + "=" * 20)
for chunk in completion:
    delta = chunk.choices[0].delta
    if hasattr(delta, "reasoning_content") and delta.reasoning_content is not None:
        if not is_answering:
            print(delta.reasoning_content, end="", flush=True)
    if hasattr(delta, "content") and delta.content:
        if not is_answering:
            print("\n" + "=" * 20 + "完整回复" + "=" * 20)
            is_answering = True
        print(delta.content, end="", flush=True)