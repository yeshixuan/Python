from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText("Hello, i am haha", "plain", "utf-8")
# 下面代码故意写错，说明，所谓的发送者的地址，只是从一个Header的第一个参数作为字符串构建的内容
# 用utf8编码是因为很可能内容包含非英文字母
header_from = Header("从yeshixuan出发送出去的<sfsfsfsf@qq.com>", "utf-8")
msg["From"] = header_from

# 填写接受者的信息
header_to = Header("去yebiyun的地方<sfwr89i00@qq.com>", "utf-8")
msg["To"] = header_to

header_sub = Header("这是我自己测试的主题", "utf-8")
msg["Subject"] = header_sub

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
    # 两个参数
    # 第一个是服务器地址，但一定shibytes格式，所以需要编码
    # 第二个参数是服务器的接受范文端口
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465) # SMTP协议默认端口25
    # 登陆邮箱发送
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