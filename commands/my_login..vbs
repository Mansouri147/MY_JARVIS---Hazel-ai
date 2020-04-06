Set WshShell = WScript.CreateObject("WScript.Shell")
WshShell.SendKeys "ala.man@gmail.com"  
WshShell.SendKeys "{TAB}"
WshShell.SendKeys "password"
WshShell.SendKeys "{Enter}"



