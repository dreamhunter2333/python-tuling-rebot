# -*- coding: utf-8 -*-

__author__ = 'jinmu333'

from tkinter import *
from multiprocessing import Process
import tkinter.messagebox as messagebox
import urllib,hashlib
import random
import requests,sys
import requests


print("你好，我是图灵机器人")

root = Tk()
root.title("聊天机器人 by jinmu333")
root.geometry('400x500')                 #是x 不是*
root.resizable(width=True, height=True) #宽不可变, 高可变,默认为True
l = Label(root, text="邮件反馈idl253841@gmail.com", font=("Arial", 9), width=20)
l.pack(side=BOTTOM)    
t = Text()
t.pack()
t.insert('1.0', "此处显示历史聊天记录\n")
var = StringVar()
e = Entry(root, textvariable = var)
var.set('此处显示最新输入内容')
e.pack()
class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.bind('<Key-Return>',self. qqq)
		self.nameInput.pack()
		self.alertButton = Button(self, text='发送消息', command=self.hello,width = 20,height = 2,bd = 2)
		self.alertButton.pack()
		
	def qqq(self,event):
		s = self.nameInput.get() or '请输入聊天内容'
		
		
		resp = requests.post("http://www.tuling123.com/openapi/api", data={
        "key": "f96464f031c64ce2b98bd21e8a6d0964",
        "info": s,
        "userid": "123456"
		})
		resp = resp.json()
		print(resp['text'])
		
		data=resp['text']
		print (s +'  =  '+data)
		var.set(data)
		t.insert('1.0', "-------------------------------------------------------\n")
		t.insert('1.0', "机器人: %s\n" %data)
		t.insert('1.0', "##我##: %s\n" %s)
    
	def hello(self):
		s = self.nameInput.get() or '请输入聊天内容'
		
		
		resp = requests.post("http://www.tuling123.com/openapi/api", data={
        "key": "f96464f031c64ce2b98bd21e8a6d0964",
        "info": s,
        "userid": "123456"
		})
		resp = resp.json()
		print(resp['text'])
		
		data=resp['text']
		print (s +'  =  '+data)
		var.set(data)
		t.insert('1.0', "-------------------------------------------------------\n")
		t.insert('1.0', "机器人: %s\n" %data)
		t.insert('1.0', "##我##: %s\n" %s)
app = Application()
    
# 主消息循环:
app.mainloop()