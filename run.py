# -*- coding: utf-8 -*-
import subprocess
import time

def main():
    cmd = ["proxy.exe" ]
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(5)  # 等待5秒，确保脚本执行完成
    
if __name__ == "__main__":
    main()