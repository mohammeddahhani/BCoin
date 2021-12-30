import time
import random
from pathlib import Path
import pyautogui as pa


for i in range(5):
    e = random.randint(0,5)
    print(e)

sc = pa.screenshot()
curr = str(Path(__file__).parent)#.replace('\\','\\')
curr += "\\screen\\{}.png".format(time.strftime('%d-%m__%H-%M-%S'))
print(curr)
sc.save(curr)