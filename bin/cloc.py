import os
import platform
os_type = platform.system()
if os_type == 'Linux':
    os.system("sudo apt install cloc")
    os.system("echo '==============================================================================='")
    os.system("echo 'TOTAL'")
    os.system("cloc project2")
    os.system("echo '==============================================================================='")
    os.system("echo 'STATS OF SRC'")
    os.system("cloc project2/project2/src")
    os.system("echo '==============================================================================='")
    os.system("echo 'STATS OF TEST'")
    os.system("cloc project2/project2/test")
    os.system("echo '==============================================================================='")
elif os_type == 'Windows':
    os.system("""@powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('http://bit.ly/psChocInstall'))""")
    # os.system("""runas /user:Administrator "choco install cloc""")
    os.system("choco install cloc")
    os.system("cloc project2")
    os.system("echo 1234")

else:
    print('os not recognized')
