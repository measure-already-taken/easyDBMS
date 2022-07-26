
def Create(wt,name):#创建表
    try:
        wt.add_sheet(name) #在工作簿中新建工作表命名为name
        # wt.save(LibraryName)
    except:
        print("错误:表名重复")


###################################################################
def Select(rd,wt,tableName):#据表名选中列表
    sheets = rd.sheet_names()  # 获取工作簿中的所有工作表名字，形成列表元素
    c = sheets.index(tableName)  # 计算该名字在列表中的位置
    table = wt.get_sheet(c)  # 读取工作表
    rds = rd.sheet_by_index(c)#rd的sheet表
    return table,rds
##################################################################



def SelectAll(rd):#查看所有表名
    note="共"+str(rd.nsheets)+"个表,"+"文件中所含表名如下："+str(rd.sheet_names())#rd.sheet_names()#全部表名# rd.nsheets  # workbook内总的sheet数量
    print(note)
    return note

def Alter(wt,rd,lastName,newName):#修改表名
    try:
        idx = rd.sheet_names().index(lastName)
        wt.get_sheet(idx).name = newName#更改后的表名
        # wt.save(LibraryName)
    except:
        print("错误:Alter的表名不存在")






