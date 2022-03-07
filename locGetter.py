import pyautogui as pag
import time

def constLocating():
    while True:
        time.sleep(0.5)
        print(pag.position())

def locTest():
    out = pag.position()
    print(out[0])
    print(out[1])
    print(out)

if __name__ == "__main__":
    locTest()