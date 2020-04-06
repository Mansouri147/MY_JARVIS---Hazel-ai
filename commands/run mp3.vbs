set shell = CreateObject("WScript.Shell")
shell.run "cmd.exe"
WScript.Sleep 2000
shell.SendKeys "nircmd.exe mediaplay 300000 ^v "
WScript.Sleep 100
shell.SendKeys "~"
WScript.Sleep 1000
shell.SendKeys"%{F4}"


