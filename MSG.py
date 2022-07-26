import time
import Table



def log(rd,wt,msg):#此处msg为要传入日志的信息
    table,rds=Table.Select(rd, wt, "系统日志")
    a=int(rds.cell_value(0, 0))+1#行数自加1
    table.write(0,0,a)#将下次的行数写入（0,0）格
    b = int(rds.cell_value(0, 1))
    if a==65535:
        b=int(rds.cell_value(0, 1))+1#列数自加1
        table.write(0, 1, b)
        table.write(0, 0, 1)
        if b == 256:
            table.write(0, 1, 0)
    d=time.strftime('%Y/%m/%d/%H:%M：')+str(msg)
    table.write(a-1, b, d)


