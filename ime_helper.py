#!/usr/bin/env python
'''
A script to change the IME of the foreground window, for Windows. 
For linux, you can use fcitx-remote. 

For more Microsoft Locale ID (LCID) Values, see
https://msdn.microsoft.com/en-us/library/ms912047(WinEmbedded.10).aspx
'''
import ctypes
import sys
import locale
import argparse
import time
from argparse import RawTextHelpFormatter


def hex_str(str):
    return (int(str, 16))


def find_LCID(lcName):
    return next((k for k, v in locale.windows_locale.items() if v == lcName), None)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=RawTextHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--current', action="store_true", help='get current LCID') #TODO
    group.add_argument('--locale', type=str, help='locale name, like zh_CN')
    group.add_argument('--hex', type=hex_str, help='LCID in hex, like 0x804')
    group.add_argument('--dec', type=int, help='LCID in dec, like 2052')
    args = parser.parse_args()
    lcid = 0
    if args.current:
        print(1041)
        sys.exit()
    if args.locale!=None:
        lcid = find_LCID(args.locale)
    elif args.hex!=None:
        lcid = args.hex
    else:
        lcid = args.dec
    if lcid not in locale.windows_locale:
        raise ValueError("invalid locale name or LCID")
    # time.sleep(5) #for debug
    WM_INPUTLANGCHANGEREQUEST = 0x0050
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    ctypes.windll.user32.SendMessageW(hwnd, WM_INPUTLANGCHANGEREQUEST, 0, lcid)
    # print(ctypes.windll.kernel32.GetLastError())
