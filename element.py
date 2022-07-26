
def Create(table,rds,msg):#属性添加
    table.write(1,rds.ncols,msg)

def Select(rds,listName,msg):#数据定位
    d,e=[],[]
    for i in range(rds.ncols):#列循环
        if rds.cell_value(1, i)==str(listName):
            for j in range(2,rds.nrows):#行循环
                if rds.cell_value(j, i) == str(msg):
                    d.append(j)#添加j到d列表中
                    e.append(i)#添加i到e列表中
    return d,e



def Insert(table,row,col,msg):
    table.write(row,col, msg)

def Delete(table,row,col):
    table.write(row, col, "")
