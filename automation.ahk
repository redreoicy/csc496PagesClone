#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

^j::
Send #{PrintScreen}
Send #+s
sleep, 2000
Click, 10 10 Down
sleep, 2000
Click, 500 500 Up
sleep, 2000
Click, 1700 1000
sleep, 2000
Send ^s
sleep, 2000
Send ^l
Send C:\Users\Admin\Desktop\CSC496Git\csc496work
Send {Enter}
Send {Enter}
return