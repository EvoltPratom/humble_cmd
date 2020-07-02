from winreg import *
a = OpenKey(HKEY_CURRENT_USER,
            "Software\\Microsoft\\Command Processor", 0, KEY_WRITE)
DeleteValue(a, 'Autorun')
CloseKey(a)

#test