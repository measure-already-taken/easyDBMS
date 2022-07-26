# 该界面注册账号和密码时不能使用纯数字
# 否则会造成该界面判定不成功
# 涉及数据类型转换过程的偷懒

import tkinter as tk
import xlrd


root = tk.Tk()
root.title("log")

xl = xlrd.open_workbook('登录数据.xls')#读取数据文件，并命名
SHEET=xl.sheet_by_name("账号信息")
SHEET_rows=SHEET.nrows#行
SHEET_cols=SHEET.ncols#列

def reg():
    username = str(e_user.get())
    passwd = str(e_pwd.get())
    for i in range(1,SHEET_rows):#令i从1数到指定的数
        if passwd == str(SHEET.cell_value(i, 1)) and username == str(SHEET.cell_value(i, 0)):
            l_msg.configure(text='登录成功,操作中别关界面！', fg='green')
            #登录后运行的程序在此处import即可





# 登录结果提示
l_msg = tk.Label(root, text='')
l_msg.grid(row=0, columnspan=2)  # 跨越两列显示

# 第一行用户名输入框
l_user = tk.Label(root, text='用户名：')
l_user.grid(row=1, sticky=tk.W)
e_user = tk.Entry(root)
e_user.grid(row=1, column=1, sticky=tk.E, padx=3)

# 第二行密码输入框
l_pwd = tk.Label(root, text='密码：')
l_pwd.grid(row=2, sticky=tk.E)
e_pwd = tk.Entry(root)
e_pwd['show'] = '*'  # 隐藏显示
e_pwd.grid(row=2, column=1, sticky=tk.E, padx=3)

# 第三行登录按钮
f_btn = tk.Frame(root)
b_login = tk.Button(f_btn, text='登录', width=6, command=reg)
b_login.grid(row=0, column=0)
b_cancel = tk.Button(f_btn, text='取消', width=6, command=root.quit)
b_cancel.grid(row=0, column=1)
f_btn.grid(row=3, columnspan=2, pady=10)

root.mainloop()