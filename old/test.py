import socket
import os
# def getIp(self):
# 	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 	s.connect(("8.8.8.8", 80))
# 	ip= s.getsockname()[0]
# 	s.close()
# 	return ip

# import uuid    
# s= uuid.UUID(int=uuid.getnode())
# print(s)

import psutil
if ("ScrapToolUI.exe" in (p.name() for p in psutil.process_iter())):
	print("ok")
else:
	print('no')

# except:
# 	print('false')

print (os.path.basename(__file__))
# from pywin32 import *

# def WindowExists(classname):
#     try:
#         win32ui.FindWindow(classname, None)
#     except win32ui.error:
#         return False
#     else:
#         return True