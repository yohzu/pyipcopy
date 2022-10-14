import urllib.request
import sys
import pyperclip

if "6" in sys.argv or "v6" in sys.argv or "ipv6" in sys.argv:
    ip = urllib.request.urlopen('https://v6.ident.me').read().decode('utf8')
else:
    ip = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')

pyperclip.copy(ip)
print(ip)