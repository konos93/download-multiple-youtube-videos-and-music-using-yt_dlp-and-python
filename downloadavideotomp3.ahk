^!s:: ; Ctrl + Alt + S
    WinActivate, ahk_class MozillaWindowClass
    WinWaitActive, ahk_class MozillaWindowClass, , 2
    if !ErrorLevel {
        Send, ^l
        Sleep, 100
        Send, ^c
        ClipWait, 1

        ; Run, %A_ScriptDir%\copytolink.exe
		Run, %ComSpec% /c python3 "C:\Users\konos\Desktop\extension_todownload\copytolink.py", , Hide
		Sleep, 100
        Run, %ComSpec% /c python3 "C:\Users\konos\Desktop\extension_todownload\musicdownloader.py", , Hide
    } else {
        MsgBox, Could not activate Firefox window.
    }
return
