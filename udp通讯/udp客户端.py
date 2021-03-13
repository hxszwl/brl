#!/usr/bin/python3
# _*_coding:utf-8 _*_
# @Time :2021年3月1日 0001上午 10:13:57
# @Author:zwl(zwlhxs@163.com)
# @File:udp客户端.py
# @Software:PyCharm


import socket
import time

#client 发送端
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
PORT = 8000

while True:
      start = time.time()  #获取当前时间
      print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start)))  #以指定格式显示当前时间
      msg= input("本客户端192.168.43.131，请输入要发送的内容：")
      server_address = ("127.0.0.1", PORT)  # 接收方 服务器的ip地址和端口号
      msg = msg.encode('utf-8')
      client_socket.sendto(msg, server_address) #将msg内容发送给指定接收方
      now = time.time() #获取当前时间
      run_time = now-start #计算时间差，即运行时间
      print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(now)))
      print("run_time: %d seconds\n" %run_time)