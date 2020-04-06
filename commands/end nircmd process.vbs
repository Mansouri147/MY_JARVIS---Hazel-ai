set shell = CreateObject("WScript.Shell")
shell.run "cmd.exe"
WScript.Sleep 2000
shell.SendKeys "nircmd.exe killprocess nircmd.exe "
WScript.Sleep 100
shell.SendKeys "~"
WScript.Sleep 500
shell.SendKeys"%{F4}"


