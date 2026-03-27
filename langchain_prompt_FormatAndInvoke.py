from langchain_core.prompts import PromptTemplate,FewShotPromptTemplate,ChatPromptTemplate
# 三个方法都继承自BasePromptTemplate

template = PromptTemplate.from_template("我的邻居是:{lastname}")

# format方法返回的是字符串
res = template.format(lastname="宋文莹", hobby=" 看书")
print(res,type(res))

# invoke返回的是PromptValue的对象(langchain的标准接口，支持链式调用)
res2 = template.invoke({"lastname":"宋文莹","hobby":"看书"})
print(res2,type(res2))