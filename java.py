import os, sys
os.system("clear")
file = str(input("[*] Enter Java File Name : "))
clss = str(input("[*] Enter Class Name : "))
out = str(input("[*] Enter Output Name : "))
os.system(f'ecj {file}')
os.system(f'dx --dex --output={out}.dex {clss}.class')
os.system('clear')
os.system(f'dalvikvm -cp {out}.dex {clss}')
