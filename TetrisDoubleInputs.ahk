#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

c & Left:: 
Send {Left down}
sleep, 20
Send {Left up}
sleep, 20
Send {Left down}
sleep, 20
Send {Left up}
return
r & Left:: 
Send {Right down}
sleep, 20
Send {Right up}
sleep, 20
Send {Right down}
sleep, 20
Send {Right up}
return
