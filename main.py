from airtest.core import api as air
from airtest.core.cv import Template, loop_find
from airtest.core.settings import Settings as ST
import time
from random import randint

def main() -> None:
    global cnt
    ST.FIND_TIMEOUT_TMP = 0
    air.init_device()
    cnt = 0
    while True:
        if pos:=air.exists(Template('assets/target.jpg')):
            cnt += 1
            if cnt > times:
                break
            print(f"================The {cnt} times.")
            air.touch(pos)
            begin()
        putCard()
        time.sleep(slp)

def begin() -> None:
    print('^^^^^^^^^^^^^^^')
    loop_find(Template('assets/b.png', rgb=True), timeout=50)
    putCard()
    putCard()
    loop_find(Template('assets/k.png', rgb=True), timeout=50)
    print("kkkkkkkkkkkkkkkkk")
    air.touch(partner)
    time.sleep(sslp)
    air.touch(partnerTo)
    time.sleep(sslp)

'''
def putPartner() -> None:
    time.sleep(bslp)
    putCard()
    putCard()
    time.sleep(slp)
    for i in range(2): # make sure
        air.touch(partner)
        time.sleep(sslp)
        air.touch(partnerTo)
        time.sleep(slp)
'''

def putCard() -> None:
    print("&&&&&&&&&&&&")
    idx = randint(0, 3)
    air.touch(cards[idx])
    time.sleep(sslp)
    #air.touch((randint(field[0], field[2]), randint(field[1], field[3])))
    air.touch(cards[idx])
    time.sleep(sslp)


cnt = int()
times = 5

# ugly bare data
bslp = 22
slp = 1.2
sslp = 0.5

partner = (1067, 1224)
partnerTo = (1446, 766)

cards = [(1400, 1225), (1670, 1225), (1940, 1225), (2310, 1225)]
field = (1220, 322, 1910, 978)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('!!!!!!!!!!!', str(e))
    finally:
        air.home()
