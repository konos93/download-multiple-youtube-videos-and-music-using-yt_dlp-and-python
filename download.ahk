; --------------------------------------------
;  Ctrl+Alt+H – Download current page as mp3
; --------------------------------------------
#NoEnv                     ; Skip legacy env-var expansion
SendMode Input             ; Faster, more reliable Send
SetWorkingDir %A_ScriptDir% ; Just in case

^!h::                      ; Ctrl + Alt + H hotkey
{
    ; -------------------------------------------------
    ; 1. Paths
    ; -------------------------------------------------
    downloadDir := "C:\Users\konos\Desktop\extension_todownload"
    if !FileExist(downloadDir)
        FileCreateDir, %downloadDir%

    logFile := downloadDir . "\ctrl_alt_h.log"

    ; -------------------------------------------------
    ; 2. Copy URL from browser address bar
    ; -------------------------------------------------
    Send, ^l               ; Focus address bar
    Sleep, 200
    Send, ^c               ; Copy
    ClipWait, 1
    url := Clipboard

    if (url = "") {
        MsgBox, Failed to get URL from clipboard.
        FileAppend, "[" A_Now "] Failed to get URL from clipboard.`n", %logFile%
        return
    }

    FileAppend, "[" A_Now "] Downloading from URL: " url "`n", %logFile%

    ; -------------------------------------------------
    ; 3. Build yt-dlp command (expression style)
    ; -------------------------------------------------
    command := ComSpec " /c yt-dlp --format bestaudio/best"
    command .= " --output " . """" . downloadDir . "\%(title)s.%(ext)s" . """"
    command .= " --fragment-retries 100000"
    command .= " --min-sleep-interval 0.5"
    command .= " --max-sleep-interval 1"
    command .= " --retry-sleep 1"
    command .= " --extract-audio --audio-format mp3 --audio-quality 64K"
    command .= " --socket-timeout 50 --no-keep-video --concurrent-fragments 1"
    command .= " --cookies-from-browser firefox " . """" . url . """"
    command .= " > " . """" . logFile . """" . " 2>&1"

    ; -------------------------------------------------
    ; 4. Launch yt-dlp
    ; -------------------------------------------------
    Run, % command, , Hide
    FileAppend, "[" A_Now "] yt-dlp command launched.`n", %logFile%
}
return
