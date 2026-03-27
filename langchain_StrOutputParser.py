from langchain_core.messages import AIMessage
from langchain_core.output_parsers import StrOutputParser
# StrOutputParser可将AI message的格式转化为字符串
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

parser = StrOutputParser()
model = ChatTongyi(model="qwen3-max")
prompt = PromptTemplate.from_template(
    "我的邻居姓:{lastname},刚生了{gender},请起名，无需告诉我别的内容。"
)

chain = prompt | model | parser | model | parser
res: str = chain.invoke({"lastname": "宋", "gender": "女儿"})
print(res)
print(type(res))

# 因为模型的调用，parser将原本的模型输出问题作为输入传入给大模型，导致生成的内容为二次给模型之后的结果

# **整体风格**：这组名字统一采用“宋”姓，搭配双字名，用字多取自自然意象（溪、夏）、美德象征（瑾、婉）或文化元素（书、知），体现出温婉、知性、清雅的审美倾向，适合文艺、古风或现代简约风格的角色设定。
#
# 如果这是用于小说、角色设定或起名参考，可以根据人物性格进一步匹配：
# - 温柔内敛 → 宋婉清
# - 才女气质 → 宋书瑶
# - 灵动自然 → 宋若溪
# - 贤淑坚韧 → 宋瑾萱
# - 明朗聪慧 → 宋知夏
