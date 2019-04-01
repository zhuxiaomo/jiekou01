import os
# 用例存放的路径
# strtdir = r'D:\ke4Project\case'  # 写文档

# 获取当前脚本的路径
print(__file__)

curPath = os.path.realpath(__file__)
print(curPath)

filePath = os.path.dirname(curPath)
print(filePath)

reportPath = os.path.join(filePath, "report", "report.html")
print(reportPath)
