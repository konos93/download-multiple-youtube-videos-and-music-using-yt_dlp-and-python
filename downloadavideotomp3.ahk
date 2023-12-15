^!s:: ; This defines the hotkey as Ctrl+Alt+S
    WinActivate, ahk_class MozillaWindowClass
    Send, ^l
    Send, ^c
    ClipWait, 1
    Run, copytolink.exe ; Assuming copytolink.exe is in the same folder as the script
    Run, music-download-hide.exe ; Assuming music-download-hide.exe is in the same folder as the script
return
