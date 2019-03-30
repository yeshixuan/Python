import socket

# 理解两个参数的含义
# 理解创建一个socke的过程
# 前者是ipv4, 后者是TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 注意addr的格式tuple
# 以及tuple两个元素的含义
sock.bind(("127.0.0.1", 9495))
print("已经绑定端口........")
# 监听
sock.listen()
print("正在监听...........")
# 接收一个传进起来的socket
print("准备接收socket传入....")
skt, addr = sock.accept()
print("已经接收到传入soket: {0}".format(skt))
# 读取传入消息，实际上是消息
# recv接收对方的消息
# 需要注意读取的信息的长度一定要小于等于实际消息的长度，否则会假死
msg = skt.recv(100)
print(type(msg)) #bytes格式

# decode默认是utf-8
print(msg.decode())

# 给对方一个反馈
msg = "I love only xiaoxue"
skt.send(msg.encode())

skt.close()
sock.close()