from langchain_community.document_loaders.csv_loader import CSVLoader

loader = CSVLoader(
    file_path="./data/stu.csv",
    csv_args={
        "delimiter": ",",       # 指定分隔符
        "quotechar": '"',       # 指定带有分隔符文本的引号包围的是单引号还是双引号
        # 如果原数据有表头，就不要下面的代码，如果眉头就可以使用为数据增添表头
        "fieldnames": ["a", "b", "c", "d"]
    },
    encoding = "utf-8"          # 指定编码为UTF-8
)
# # 批量加载
# documents = loader.load()
#
# for document in documents:
#     print(type(document),document)


# 软加载 .lazy_load()  迭代器[Document]
for document in loader.lazy_load():
    print(document)
