# coding:utf-8
import unittest
# 从工程下面的第一层开始导入
from common.HtmlRunner import HTMLTestRunner
import os
# 用例存放的路径
# strtdir = r'D:\ke4Project\case'  # 写文档


# 获取当前脚本的路径
curPath = os.path.dirname(os.path.realpath(__file__))
# 用例的路径
strtdir = os.path.join(curPath, "case")
reportPath = os.path.join(curPath, "report", "report.html")

rule = "test*.py"
discover = unittest.defaultTestLoader.discover(strtdir,rule)
print(discover)

# 生成高级的HTML报告
fp = open(reportPath, "wb")
runner = HTMLTestRunner(fp,
                        title="报告的标题：这个是我的接口项目",
                        description="报告如下：",
                        verbosity=2,
                        retry=2)
runner.run(discover)
fp.close()

# 这个报告太低级了
# runner = unittest.TextTestRunner()
# runner.run(discover)

