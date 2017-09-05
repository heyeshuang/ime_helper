#!/usr/bin/env python
'''
A script to change the IME of the foreground window, for Windows.
'''
import argparse
def hex_str(str):
    return (int(str,16))
parser = argparse.ArgumentParser(description=__doc__)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--locale', type=str, help='locale name, like zh_CN')
group.add_argument('--hex', type=hex_str, help='LCID in hex, like 0x804')
group.add_argument('--dec', type=int, help='LCID in dec, like 2052')
args=parser.parse_args()
