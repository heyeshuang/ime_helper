import sys

def find_LCID(lcName):
    return next((k for k, v in locale.windows_locale.items() if v == lcName), None)

if len(sys.argv)<2:
    print("You need to assign a locale")
    sys.exit()

arg = sys.argv[1]
if arg == "--help"or"-h":
    print(__doc__)
    sys.exit()


if find_LCID(sys.argv[1])==None:
    print("Locale not found. ")