powershell -command "Unblock-File -Path (\"{0}{1}\" -f ($pwd).path, \"\python\Lib\site-packages\pythonnet\runtime\Python.Runtime.dll\")"
.\python\python.exe .\install.py ru debug
