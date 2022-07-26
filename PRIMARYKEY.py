
def PrimaryKey(rd,wt,tableName,msg):#主键设置
    sheets = rd.sheet_names()  # 获取工作簿中的所有工作表名字，形成列表元素
    c = sheets.index(tableName)  # 计算该名字在列表中的位置
    table = wt.get_sheet(c)  # 读取工作表
    rds = rd.sheet_by_index(c)#rd的sheet表
    a=rds.ncols
    for i in range(a):
        if msg==rds.cell_value(1, i):
            table.write(0, i,"PrimaryKey")

def PrimaryKeyFind(rd,tableName):#主键查询
    sheets = rd.sheet_names()  # 获取工作簿中的所有工作表名字，形成列表元素
    c = sheets.index(tableName)  # 计算该名字在列表中的位置
    rds = rd.sheet_by_index(c)#rd的sheet表
    a=rds.ncols
    for i in range(a):
        if rds.cell_value(0, i)=="PrimaryKey":
            print(rds.cell_value(1, i))

def PrimaryKeyDelete(rd,wt,tableName,msg):#主键删除
    sheets = rd.sheet_names()  # 获取工作簿中的所有工作表名字，形成列表元素
    c = sheets.index(tableName)  # 计算该名字在列表中的位置
    table = wt.get_sheet(c)  # 读取工作表
    rds = rd.sheet_by_index(c)#rd的sheet表
    a=rds.ncols
    for i in range(a):
        if msg==rds.cell_value(1, i):
            table.write(0, i,"")

