import socket
"""
- Server端的编写流程
         1. 建立socket负责具体通信，这个socket其实只负责接受对方的请求，真正通信的是链接后从新建立的socket
         2. 绑定端口和地址
         3. 监听接入的访问socket
         4. 接受访问的socket，可以理解接受访问即建立了一个通讯的链接通路
         5. 接受对方的发送内容，利用接收到的socket接收内容
         6. 如果有必要，给对方发送反馈信息
         7. 关闭链接通路
"""
def tcp_srv():
    # 1. 建立socket负责具体通行，这个socket其实值负责接收对方的请求，真正通行的是链接后重新建立的socket
    # 需要用到两个参数
    # AF_INIT:含义同udp一致
    # SOCK_STREAM: 表明是使用的tcp进行通行
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定端口和地址
    # 此地址信息是一个元组内容，元组分为两部分，第一部分为字符串，代表ip,第二部分代表端口，是个整数，推荐大于10000
    addr = ("127.0.0.1", 9495)
    sock.bind(addr)

    # 3. 监听介入的范文socket
    sock.listen()

    while True:
        # 4. j接收访问的socket, 可以理解接收访问即建立了一个通讯的链接
        # accept返回的是元组的第一个元素赋值给skt, 第二个赋值给addr
        skt, addr = sock.accept()

        # 5. 接收对方的发送内容，利用接收到的socket接收内容
        # 500代表接收使用的buffersize
        msg = skt.recv(500)

        rst = "Received msg:{} from {}".format(msg, addr)
        print(rst)

        # 6. 如果有必要，给对方发送反馈消息
        skt.send(rst.encode())

        # 7. 关闭链接通路


if __name__ == '__main__':
    print("starting................")
    tcp_srv()
    print("Ending...................")


