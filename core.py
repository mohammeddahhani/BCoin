import pyautogui as pa
import time
import ctypes
import win32gui, win32con
from pathlib import Path


def sl(i):
    time.sleep(i)

def clickk(x,y):
    pa.click(x,y)# 362,187

def findWin(w,fg=True):
    def myHandler(hwnd, top_windows):
        top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    results = []
    top_windows = []
    win32gui.EnumWindows(myHandler, top_windows)
    for i in top_windows:
        #print(i[1].lower())
        if w in i[1].lower():
            #print(i)
            win32gui.ShowWindow(i[0],win32con.SW_SHOW)
            if fg: win32gui.SetForegroundWindow(i[0])
            break
    #win32gui.EnumWindows(winEnumHandler, None )
    sl(2)

def onStart():
    sl(2)
    clickk(978,785) # connect wallet
    sl(5)
    print("--Trying to access MetaMask")
    findWin("metamask",False)
    #sl(7)          # metamask popup
    clickk(1805,689) # sign 1440,446
    sl(10)           # loading
    findWin("chrome")
    sl(1)

def toMap():
    clickk(985,555) # treasure hunt
    sl(3)
def toGain():
    clickk(1523,232)
    sl(3)
def toHero1():
    clickk(1490,850) # from main
    sl(3)
    screenshot()
def toHero2():
    clickk(975,918) # white arrow
    sl(3)
    clickk(973,884) # hero
    sl(5)             # load
    screenshot()

def backFromMap():
    clickk(430,229) # green arrow
    sl(3)
def backFromGain():
    clickk(1306,334) # gain red cross
    sl(3)
def backFromHero1():
    clickk(1047,329) # hero red cross
    sl(3)
def backFromHero2():
    clickk(1047,331) # hero red cross
    sl(3)
    clickk(974,805) # high white arrow
    sl(3)

def move():
    print("[{}] move()".format(time.strftime('%d/%m %X')))
    clickk(1360,385) # click inside map
    backFromMap()
    toMap()

def bomber(nb = 0, order='work', delay=3):
    dy = 88
    dx = 0
    if order == 'rest': dx= 73

    clickk(872+dx, 430+nb*dy)
    sl(delay)

def screenshot():
    sl(2)
    sc = pa.screenshot()
    scdir = str(Path(__file__).parent)#.replace('\\','\\')
    scdir += "\\screen\\{}.png".format(time.strftime('%d-%m__%H-%M-%S'))
    #print('[{}] screenshot()'.format(time.strftime('%d/%m %X')))
    sc.save(scdir)

def allToWork():
    findWin("bombcrypto")
    screenshot()
    print("[{}] -- AllToWork()".format(time.strftime('%d/%m %X')))
    toHero2()
    sl(3)
    for i in range(5): bomber(4)
    backFromHero2()

def allToRest():
    findWin("bombcrypto")
    screenshot()
    print("[{}] -- AllToRest()".format(time.strftime('%d/%m %X')))
    toHero2()
    sl(3)
    for i in range(5): bomber(0, 'rest') 
    backFromHero2()

def sleepInPeriods(d, p=13):
    assert p != 0 and d != 0
    if d < p: d = p 
    print("[{}] sleep {} min in periods of {} min - ({})".format(time.strftime('%d/%m %X'), d, p, int(d/p)))
    for i in range(int(d/p)):
        screenshot()
        sl(p*60)
        findWin("bombcrypto")
        move()

def nightMode(p=60):
    while(True):
        allToWork()
        sleepInPeriods(p)

def dayMode(w=20, r=30, p=13, wp = 13):
    p = 1
    while(True):
        allToWork()
        sleepInPeriods(w,wp)
        allToRest()
        sleepInPeriods(r,p)
sl(2)
#nightMode(60)
#allToRest()
sleepInPeriods(15,15)
p = 20
wp = 15
dayMode(15,60,p,wp)

def test():
    onStart()
    toHero1()
    #allBomberOn()
    backFromHero1()
    toGain()
    backFromGain()
    toMap()
    toHero2()
    backFromHero2()
    backFromMap()
    toMap()

#test()