#!/usr/bin/env python
import os
## 從 shell中取得 firefox的執行路徑
firefox_path=os.popen("which firefox").readlines()[0].rstrip("\n")
print(firefox_path)
## 判別所獲得的執行路徑是絕對路徑或是符號連結, 符號連結連至何處
gettype_firefox_path=os.popen("file `which firefox`").readlines()[0].rstrip("\n")
print(gettype_firefox_path.split("symbolic link to "))

## 將判別完成的安裝路徑執行取得其版本, 若為 snap版則待進一步判斷; 若為自行安裝版, 則輸出 (安裝路徑,版本).
firefox_version=os.popen(gettype_firefox_path.split("symbolic link to ")[-1] + " --version").readlines()[0].rstrip("\n").split(" ")
print(firefox_version)
if 'snap' in firefox_version:
    print("The firefox is snap version...")
    print("Waiting for updating new function with snap..., or you can update firefox by manually. ie. \n \
            sudo snap refresh firefox \n")
    pass
else:
    firefox_version=firefox_version[-1]
    real_firefox_path=gettype_firefox_path.split("symbolic link to ")[-1]
    print((real_firefox_path,firefox_version))
    pass
