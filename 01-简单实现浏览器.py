import socket

# 创建套接字    IPv4            流式报文<面向连接 消息边界>
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 用户输入网址-域名 DNS域名-------》IP----链接服务器
tcp_socket.connect(("tlias-stu.boxuegu.com", 80))

# 拼接HTTP请求报文
# 请求行
request_line = "GET / HTTP/1.1\r\n"

# 请求头
request_header = "Host:tlias-stu.boxuegu.com\r\n"

request_data = request_line + request_header + "\r\n"

# 发送HTTP请求报文--HTTP请求报文格式
tcp_socket.send(request_data.encode())

# 会送HTTP响应数据--HTTP响应报文格式  浏览器接收到数据 解析——显示
recv_data = tcp_socket.recv(4096)
recv_date = recv_data.decode()
print(recv_date)
# print(recv_date[recv_date.find("\r\n\r\n")+4:])
# 断开连接
tcp_socket.close()