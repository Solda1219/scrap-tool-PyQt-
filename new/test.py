from win32com.client import Dispatch

if __name__ == '__main__':
    filePath = 'E:\\python_work\\alfrad\\test files\\TemplateA.csv'
    xl = Dispatch('Excel.Application')
    workbook= None
    xl.Visible = True
    workbook = xl.Workbooks.Open (filePath, ReadOnly = True)
    pass
    
