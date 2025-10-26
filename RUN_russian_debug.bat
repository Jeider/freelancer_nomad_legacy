powershell -command "Get-ChildItem -Path ($pwd).path -Recurse | Unblock-File"
.\python\python.exe .\install.py ru debug
timeout 5 > NUL
