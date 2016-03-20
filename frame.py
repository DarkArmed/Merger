# -*- coding: UTF-8 -*-
from Tkinter import *
import tkFileDialog
from merger import Merger
# from spliter import Spliter
from helper import *


class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        
        self.opend_file = None
        background = 'white'
        text_background = '#EEE'

        master.configure(bg = background)
        master.minsize(600, 600)
        master.title('代码合并器')

        master.rowconfigure(1, weight = 1)
        for col in range(10):
            self.master.columnconfigure(col, weight = 1)
        
        self.label_src = Label(master, text = '原始码', bg = background)
        self.label_src.grid(row = 0, column = 0, rowspan = 1, columnspan = 5, sticky = W+S, padx = 10, pady = 10)

        self.text_src = Text(master, bg = text_background)
        self.text_src.grid(row = 1, column = 0, rowspan = 1, columnspan = 5, sticky = W+E+N+S, padx = (10, 5), pady = 0)

        self.label_dst = Label(master, text = '精简码', bg = background)
        self.label_dst.grid(row = 0, column = 5, rowspan = 1, columnspan = 5, sticky = W+S, padx = 5, pady = 10)

        self.text_dst = Text(master, bg = text_background)
        # self.text_dst.config(state = 'disable')
        self.text_dst.grid(row = 1, column = 5, rowspan = 1, columnspan = 5, sticky = W+E+N+S, padx = (5, 10), pady = 0)

        self.button_open = Button(master, text='导入', width = '10', bg = background, command = self.open)
        self.button_open.grid(row = 2, column = 2, rowspan = 1, columnspan = 2, sticky = N+S, pady = 10)

        self.button_merge = Button(master, text='合并', width = '10', bg = background, command = self.merge)
        self.button_merge.grid(row = 2, column = 4, rowspan = 1, columnspan = 2, sticky = N+S, pady = 10)

        self.button_save = Button(master, text='导出', width = '10', bg = background, command = self.save)
        self.button_save.grid(row = 2, column = 6, rowspan = 1, columnspan = 2, sticky = N+S, pady = 10)

    def open(self):

        self.openfile = tkFileDialog.askopenfile(mode = 'r', defaultextension=".txt")
        text = self.openfile.read()
        print 'File loaded.'
        print text
        self.text_src.delete(0.0, END)
        self.text_src.insert(END, text)

    def merge(self):
        # self.text_dst.config(state = 'normal')

        text = self.text_src.get('1.0', END)
        # print text.encode('utf-8')
        codes2num = decode(text)
        # print codes2num

        self.merger = Merger(codes2num)

        self.text_dst.delete(0.0, END)

        result_text = ''
        for k in range(10, 3, -1):
            result_text += '最大长度' + str(k) + ' '
            result_text += encode(self.merger.merge_result(k))
            # print result_text

        self.text_dst.insert(END, result_text)
        # self.text_dst.config(state = 'disable')

    def save(self):

        self.savefile = tkFileDialog.asksaveasfile(mode = 'w', defaultextension=".txt")
        text = self.text_dst.get(0.0, END)
        # print text.encode('utf-8')
        self.savefile.write(text.encode('utf-8'))
        self.savefile.close()


root = Tk()
app = Application(master = root)
app.mainloop()