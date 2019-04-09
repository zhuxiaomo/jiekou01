#coding:utf-8
import unittest
import os
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from com import HTMLTestRunner
def all_case():
    #加载测试用例
    a=unittest.defaultTestLoader.discover(case_path,
                                          pattern="test*.py",
                                          top_level_dir=None)
    return a
def run_case():
    '执行测试用例，生成测试报告'
    now = time.strftime("%Y_%m_%d %H_%M_%S")
    htmlreport_path = os.path.join(reportpath, now+"result.html")
    fp = open(htmlreport_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="自动化测试报告",
                                           description="测试用例执行情况")
    # 调用allcase函数返回值
    runner.run(all_case())
    fp.close()
def get_report_file(report_path):
    '获取最新的测试报告'
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print('最新的测试报告:'+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file
def send_mail(sender, psw, receiver, smtpserver,report_file, port=465):
    '发送最新的测试报告内容'
    #打开测试报告
    with open(report_file, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')# 定义邮件正文为html格式
    msg['Subject'] = "自动化测试报告"#主题
    msg["from"] = sender   #发件人
    msg["to"] = ";".join(receiver)    #收件人
    msg.attach(body)#msg时发送消息
    # 添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")#附件编码为utf-8
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'#附件起名为report.html
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)#连接服务器
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver,port)
    # 用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
if __name__ == '__main__':
    case_path = os.path.join(os.getcwd(),"case") #测试用例存放路径
    reportpath = os.path.join(os.getcwd(),"report") #测试报告存放路径
    run_case() #执行测试用例
    report_file = get_report_file(reportpath)
    smtpserver = "smtp.163.com"#发件服务器
    sender = "zxm17521041689@163.com" # 自己的账号
    psw = "zhu13839483971" #自己的密码
    receiver=["515228611@qq.com"]
    #receiver = ["1161804812@qq.com","13588241650@163.com","wjx573263521@163.com"] #对方的账号
    send_mail(sender, psw, receiver, smtpserver,report_file)#使用 sendmail 方法发送邮件
    print("发送成功")
else:
    print("发送失败")






