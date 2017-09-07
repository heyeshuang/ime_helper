# Command line input source switcher for Windows

## About

The script could change the IME of the foreground window for Windows. It is proposed to work with [atom-vim-mode-plus-auto-ime](https://github.com/xream/atom-vim-mode-plus-auto-ime). Tested in Windows 10 (15063) and Python 3.6.

For linux, `fcitx-remote` provides the similar function.

For OS X, you may want to look at [input-source-switcher](https://github.com/vovkasm/input-source-switcher), and I stole its README. Thanks Vovkasm! 

## Usage

    python ime_helper.py (--current | --locale LOCALE | --hex HEX | --dec DEC)

    Or you could use the [pre-built EXE releases](https://github.com/heyeshuang/ime_helper/releases).

Arguments:

    --current        get current LCID

    --locale LOCALE  locale name, like zh_CN

    --hex HEX        LCID in hex, like 0x804

    --dec DEC        LCID in dec, like 2052

For more Microsoft Locale ID (LCID) Values, see
https://msdn.microsoft.com/en-us/library/ms912047(WinEmbedded.10).aspx

## Known issue

Doesn't work on CMD or powershell, however, if you set a delay time you will see it works on other softwares:
```powershell
# powershell
sleep 5|python ime_helper.py --locale zh_CN
# then switch to another window
```
I'm new to Windows APIs. Any help would be appreciated.