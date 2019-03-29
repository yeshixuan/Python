# 导入相应的包
from email.mime.multipart import MIMEMultipart # 构建基础邮件使用
from email.mime.text import MIMEText #构建附件使用

mail_mul = MIMEMultipart()
# 构建邮件正文
mail_text = MIMEText("Hello, i am yeshixuan", "plain", "utf-8")
# 把构建好的邮件正文附加入邮件中
mail_mul.attach(mail_text)

# 构建附加
# 构建附件，需要从本地读入附件
# 打开一个本地文件
# 以rb格式打开
with open("01.html", "rb") as f:
    s = f.read()
    # 设置附件的MIME和文件名
    m = MIMEText(s, "base64", "utf-8")
    m["Content-Type"] = "application/octet-stream"
    # 需要注意
    # 1. attachment后分号为英文状态
    # 2. filename 后面需要用引号包裹，注意与外面引号错开
    m["Content-Disposition"] = "attachment; filename='01.html'"
    # 添加到MIMEMultipart
    mail_mul.attach(m)


# 发送email地址，此处地址直接使用我的qq邮箱，闭包一般需要临时输入
from_addr = "@qq.com"
# 此处密码是经过申请设置后的授权码，不是邮箱秘密
from_pwd = ""

# 收件人信息
# 此处使用qq邮箱
to_addr = "@qq.com"


# 输入SMTP服务器地址
# 此处根据不同的邮件服务商有不同的值
# 现在基本任何一家邮件服务商，如果采用第三方发邮件，都需要开启授权选择
# 腾讯qq邮箱锁在的stmp地址是 smtp.qq.com

smtp_srv = "smtp.qq.com"

try:
    import smtplib
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465) # SMTP协议默认端口25
    # 登陆邮箱发送
    srv.login(from_addr, from_pwd)
    # 发送邮件
    # 三个参数
    # 1. 发送地址
    # 2. 接收地址，必须是list形式
    # 3. 发送内容，作为字符串发送
    srv.sendmail(from_addr, [to_addr], mail_mul.as_string())
    srv.quit()
except Exception as e:
    print(e)