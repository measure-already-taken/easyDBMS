import xlrd
import xlutils.copy


################################################
def Select(url):
    LibraryName=str(url)+".xls"
    rd = xlrd.open_workbook(LibraryName)  # 读取
    wt = xlutils.copy.copy(rd)  # 复制
    return LibraryName,rd,wt
################################################

def Save(wt,LibraryName):
    wt.save(LibraryName)


