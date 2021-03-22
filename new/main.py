from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import wx

from urllib.request import urlopen
import datetime
import sys
import os
import os.path
from os import path
from pathlib import Path
import win32api, win32con
import shutil
import time
import psutil
import random
import string


from win32com.client import Dispatch

# allow time
deadline = datetime.datetime(2021, 1, 6)
top_label = 'Please press decode button to show files and double click on file\'s name of application'
bottom_label = 'Application Expiration Date: '

# password
allowPassword = True
password = 'I am password'

folder_access_time = datetime.datetime(random.randint(2018, 2019), random.randint(1, 12), random.randint(1, 28), random.randint(1, 23), random.randint(1, 59), random.randint(1, 59))
folder_modify_time = datetime.datetime(random.randint(2018, 2019), random.randint(1, 12), random.randint(1, 28), random.randint(1, 23), random.randint(1, 59), random.randint(1, 59))

class RealTimer(object):
    """docstring for RealTimer"""
    def __init__(self):
        super().__init__()


    def getRealTime(self):
        datetime_now = datetime.datetime.now()
        try:
            res = urlopen('http://worldtimeapi.org/api/timezone/Europe/London.txt')
            result = res.read().strip()
            result_str = result.decode('utf-8')
            liststr = result_str.split('\n')
            timestr = ''
            for item in liststr:
                if item[:8] == 'datetime':
                    timestr = item[10:29]
            datetime_now = datetime.datetime.strptime(timestr, '%Y-%m-%dT%H:%M:%S')
        except:
            pass
        
        return datetime_now

def killExcelProc(func, path, _):
    for proc in psutil.process_iter():
        if proc.name().lower() == 'excel.exe':
            try:
                proc.kill()
            except:
                pass
        pass

def modifyFileDatetime(path_to_file):
    mod_access_Time = time.mktime(folder_access_time.timetuple())
    mod_modification_time = time.mktime(folder_modify_time.timetuple())
    try:
        os.utime(path_to_file, (mod_access_Time, mod_modification_time))
    except:
        pass
    pass

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class DecodeDlg(QWidget):
    """docstring for DecodeDlg"""
    def __init__(self, leftDays):
        super().__init__()
        self.list_files = []
        self.tmpPath = resource_path('data')
        self.excelProcess = None
        self.workbook = None
        self.realPath = None
        self.baseDir = None
        self.initFiles()
        self.initUI(leftDays)

    def initUI(self, leftDays):
        grid = QGridLayout()
        grid.setSpacing(10)
        
        self.top_label = QLabel(top_label, self)
        grid.addWidget(self.top_label, 0, 1, 1, 15)

        self.files_list_widget =  QListWidget(self)
        grid.addWidget(self.files_list_widget, 1, 1, 15, 15)
        self.files_list_widget.itemDoubleClicked.connect(self.handleListDoubleClick)

        self.btn_decode = QPushButton('Decode', self)
        self.btn_decode.clicked.connect(self.decodeFiles)
        grid.addWidget(self.btn_decode, 16, 1, 1, 1)

        self.bottom_label1 = QLabel(bottom_label + str(deadline.year) + '/' + str(deadline.month) + '/' + str(deadline.day), self)
        grid.addWidget(self.bottom_label1, 17, 1, 1, 12)

        self.bottom_label2 = QLabel('Days left: ' + str(leftDays), self)
        grid.addWidget(self.bottom_label2, 17, 13, 1, 3)

        self.setLayout(grid)
        self.setContentsMargins(2, 20, 2, 20)
        self.setGeometry(300, 300, 450, 360)

        self.setWindowIcon(QIcon(self.tmpPath+'\\logo.ico'))
        self.setWindowTitle('WI-FROM Studio Ballarini')

    def initFiles(self):

        letters = string.ascii_uppercase
        homeDir = str(Path.home())

        baseDir = homeDir + '\\sysdir'
        if path.isdir(baseDir):
            try:
                shutil.rmtree(baseDir)
            except:
                pass
            else:
                os.mkdir(baseDir)
            time.sleep(2)
        else:
            try:
                os.mkdir(baseDir)
            except:
                pass

        self.baseDir = baseDir
        subDir = baseDir + '\\sysadd'
        dirArray = [ baseDir + '\\sysadd' ]
        try:
            os.mkdir(subDir)
        except:
            pass
        for i in range(5):
            tmpDirArray = []

            for subDir in dirArray:
                for i in range(3):
                    randTmp = ''.join(random.choice(letters) for i in range(20))
                    strTmp =subDir + '\\' + randTmp
                    try:
                        os.mkdir(strTmp)
                        time.sleep(0.1)
                        modifyFileDatetime(strTmp)
                        tmpDirArray.append(strTmp)
                    except:
                        pass
            dirArray = tmpDirArray
            # try:
            #     os.mkdir(subDir + '\\' + randTmp)
            #     subDir = subDir + '\\' + randTmp
            # except:
            #     pass
            # time.sleep(0.1)
        # randStr = ''.join(random.choice(letters) for i in range(20))
        # rp = subDir + '\\' + randStr

        
        # if path.isdir(rp):
        #     try:
        #         shutil.rmtree(rp)
        #     except:
        #         pass
        #     time.sleep(1)

        # try:
        #     os.mkdir(rp)
            
        # except:
        #     pass
        # else:
        rp = dirArray[0]
            
        files = os.listdir(self.tmpPath)

        for f in files:
            srcFile = self.tmpPath + '\\' + f
            distFile = rp + '\\' + f
            try:
                shutil.copy(srcFile, distFile)
            except:
                pass
            else:
                time.sleep(0.05)
                modifyFileDatetime(distFile)
            pass

        for dirTmp in dirArray:
            strTmp = dirTmp
            for i in range(7):
                strTmp = os.path.dirname(strTmp)
                modifyFileDatetime(strTmp)
        modifyFileDatetime(baseDir)
        win32api.SetFileAttributes(baseDir,win32con.FILE_ATTRIBUTE_HIDDEN)
        self.realPath = rp
        return True

    def decodeFiles(self):
        if self.realPath:
            self.files_list_widget.clear()
            try:
                files = os.listdir(self.realPath)
                for f in files:
                    if f.split('.')[-1] == 'xlsm' and f[0] != '~':
                        self.files_list_widget.addItem(f)
                pass
            except:
                pass
        else:
            pass

    def delFolder(self, folderpath):
        try:
            shutil.rmtree(folderpath)
        except:
            pass
        pass

    def handleListDoubleClick(self, item):

        value = item.text()
        filePath =  self.realPath + '\\' + value 
        
        xl = Dispatch('Excel.Application')
        if self.excelProcess:
            self.excelProcess.Quit()
        self.excelProcess = xl

        workbook= None
        xl.Visible = True
        workbook = xl.Workbooks.Open (filePath, readonly = True)
        self.workbook = workbook

    def closeEvent(self, event):
        close = QMessageBox()
        close.setText("You sure? All xls* files will be CLOSED!")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            
            if self.excelProcess:

                self.excelProcess.Quit()
                del self.excelProcess
                self.excelProcess = None
                time.sleep(2)

            try:
                # shutil.rmtree(self.realPath)
                shutil.rmtree(self.baseDir, onerror = killExcelProc)
                time.sleep(1)
            except os.error:
                killExcelProc()
                time.sleep(1)
                try:
                    shutil.rmtree(self.baseDir)
                except:
                    pass
            except:
                pass
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    realTimer = RealTimer()
    datetime = realTimer.getRealTime()

    if datetime < deadline:
        leftDays = (deadline-datetime).days
        decodeDialog = DecodeDlg(leftDays)
        decodeDialog.show()
        sys.exit(app.exec_())
    else:
        app = wx.App()
        title = 'error'
        message = 'Expired date'
        msg_dlg = wx.MessageDialog(None, message, title, wx.OK | wx.ICON_ERROR)
        val = msg_dlg.ShowModal()
        msg_dlg.Show()
        msg_dlg.Destroy()    