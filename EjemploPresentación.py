import pyautogui as pg
import time as t

distance = 200

pg.hotkey('win','r')
t.sleep(.3)
pg.typewrite('cmd\n',0.1)
t.sleep(.5)
pg.typewrite('mspaint\n',0.1)
t.sleep(3)
pg.moveTo(500,400,duration=0.2)
while distance > 0:
    pg.drag(distance, 0, duration=0.01)   # move right
    distance -= 5
    pg.drag(0, distance, duration=0.01)   # move down
    pg.drag(-distance, 0, duration=0.01)  # move left
    distance -= 5
    pg.drag(0, -distance, duration=0.01)  # move up