import ctypes
import sys, locale
'''
A script to change the IME of the foreground window.
Usage:
ime_helper.py zh_CN

For more Language Identifier Constants, see
https://msdn.microsoft.com/en-us/library/ms912047(WinEmbedded.10).aspx
'''

def find_LCID(lcName):
    return next((k for k, v in locale.windows_locale.items() if v == lcName), None)

if __name__ == '__main__':
    time.sleep(5)
    WM_INPUTLANGCHANGEREQUEST=0x0050
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    print(hwnd)
    wnd_title=ctypes.create_unicode_buffer(256)
    ctypes.windll.user32.GetWindowTextW(hwnd,wnd_title,256)
    print(wnd_title.value)
    SendMessage = ctypes.windll.user32.SendMessageW
    SendMessage(hwnd,WM_INPUTLANGCHANGEREQUEST,0,find_LCID("zh_CN"))

