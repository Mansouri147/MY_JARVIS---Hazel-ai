'still under development'
set shell = WScript.CreateObject ("WScript.Shell")
shell.run"cmd.exe "
WScript.Sleep 100
shell.SendKeys "nircmd.exe setfiletime "change_dir_cre" "change_date_cre change_time_cre AM_OR_PM_cre" "change_date_modif change_time_modif AM_OR_PM_modif" "
shell.SendKeys"~"
WScript.Sleep 200
'shell.SendKeys"%{F4'