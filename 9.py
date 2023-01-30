#coding=utf-8
import os, sys, platform

os.system('xdg-open https://facebook.com/groups/3017062245271082/')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf Rizwanali.so Rizwan32.so')
except:
    pass
os.system('rm -rf Rizwanali.so Rizwan32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Rizwan.so'):
        os.system('curl -L https://github.com/Rizwan-XD/executables/blob/main/Rizwan.cpython-311.so?raw=true -o Rizwan.so') 
        import Rizwan
    else:
        import Rizwan

elif bit == '32bit':
    if not os.path.isfile('Rizwan32.so'):
        os.system('curl -L https://github.com/Rizwan-XD/executables/blob/main/Rizwan32.cpython-311.so?raw=true -o Rizwan32.so') 
        import Rizwan32
    else:
        import Rizwan32
