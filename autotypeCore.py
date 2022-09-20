import pyautogui as g

import sys, time

if __name__=="__main__":
    fileName = sys.argv[1]
    with open(fileName, encoding="utf-8") as f:
        lines = f.readlines()

    for l in lines:
        g.write(l)
        '''
        for s in l:
            g.typewrite(s)
        '''
