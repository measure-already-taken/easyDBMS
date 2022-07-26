import Table
import MSG
import PRIMARYKEY
import DB
import element



#########################################
url="仓库DB"
LibraryName,rd,wt=DB.Select(url)#库地址说明
#########################################

######################
name="仓库物资"
newName="仓库物资名单2"

tableName="仓库物资名单"
msg="物资编号"
listName="物资编号"
######################



Table.Create(wt,name)#创建表
note=Table.SelectAll(rd)#查看所有表名

#############################################
table,rds=Table.Select(rd,wt,tableName)#选中表
#############################################


Table.Alter(wt,rd,name,newName)#修改表名

#######################################################################
element.Create(table,rds,msg)#创建列名
row,col=element.Select(rds,listName,msg)#输出程序可以直接利用的（行，列）坐标值
element.Insert(table,row[0],col[0],"msg")#根据行列定点写入数据
element.Delete(table,row[0],col[0])#根据行列删除数据
#######################################################################


########################################################################################################################
MSG.log(rd,wt, msg)#使用此句前请先确定LibraryName中有无名为“系统日志”的sheet，以及第一行第一个单元格是否填1，第二个单元格是否填0，否则会报错
########################################################################################################################

##################################################
PRIMARYKEY.PrimaryKey(rd,wt,tableName,msg)#主键设置
PRIMARYKEY.PrimaryKeyFind(rd,tableName)#主键查询
##################################################

#################################
DB.Save(wt,LibraryName)#保存全体数据
#################################


PRIMARYKEY.PrimaryKeyDelete(rd,wt,tableName,msg)#主键删除
DB.Save(wt,"1.xls")
