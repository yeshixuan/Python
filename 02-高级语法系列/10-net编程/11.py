import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 构建一个MIMEMultipart邮件
msg = MIMEMultipart("alternative")

# 构建一个HTML邮件内容
mail_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Title</title>
        </head>
        <body>

        <h1> 这是一封HTML格式邮件</h1>

        </body>
        </html>
        """

msg_html = MIMEText(mail_content, "html", "utf-8")
msg.attach(msg_html)

msg_text = MIMEText("just text content ", "plain", "utf-8")
msg.attach(msg_text)

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
    # 加密传输
    #server = smtplib.SMTP_SSL(smtp_srv.encode(), 465) # SMTP协议默认端口是25
    # qq邮箱要求使用 TLS加密传输
    #这里端口必须要用25
    srv = smtplib.SMTP(smtp_srv.encode(), 25) # SMTP协议默认端口25
    srv.starttls()
    # 设置调试级别
    #通过设置调试等级，可以清楚地看到发送邮件的交互步骤
    srv.set_debuglevel(1)
    # 登陆发送优先
    srv.login(from_addr, from_pwd)
    # 发送邮件
    # 三个参数
    # 1. 发送地址
    # 2. 接收地址，必须是list形式
    # 3. 发送内容，作为字符串发送
    srv.sendmail(from_addr, [to_addr], msg.as_string())
    srv.quit()
except Exception as e:
    print(e)