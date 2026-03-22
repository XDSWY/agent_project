from langchain_community.embeddings import DashScopeEmbeddings
# from langchain_ollama import OllamaEmbeddings

# 不传model默认用的是text-embeddings-v1
model = DashScopeEmbeddings()

# model = OllamaEmbeddings(model = "qwen3-embedding:4b")

print(model.embed_query("我喜欢你"))  # 单次转化为向量
print(model.embed_documents(["早上吃啥","中午吃啥","晚上吃啥"]))  # 批量转换