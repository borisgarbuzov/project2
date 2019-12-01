import os
import platform
os_type = platform.system()
if os_type == 'Linux':
    os.system("sudo apt install cloc")
    os.system("cloc project2")
elif os_type == 'Windows':
    os.system("""@powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('http://bit.ly/psChocInstall'))""")
    # os.system("""runas /user:Administrator "choco install cloc""")
    os.system("choco install cloc")
    os.system("cloc project2")
else:
    print('os not recognized')
    
