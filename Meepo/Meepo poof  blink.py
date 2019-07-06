#config
useItem1 = 1
useItem2 = 0
mouseclick = 0
#hotkeys
blink = "t"
poof = "w"
item1 = "c"
item2 = "4"
atack = "a"
nextUnit = "<tab>"
selectHero = "<f1>"
selectAll = "<f2>"
selectAllNoHero = "z"
#timing
lowDelay = 0.02
midDelay = 0.15
hightDelay = 1.2
#script
keyboard.send_key(selectAllNoHero)
time.sleep(midDelay)
keyboard.send_key(poof)		  #next(2) poof
time.sleep(lowDelay)
keyboard.send_key(nextUnit)	  #select next(3) meepo
time.sleep(lowDelay)
keyboard.send_key(poof)		  #next(3) poof
time.sleep(lowDelay)
keyboard.send_key(nextUnit)   #select next(4) meepo
time.sleep(lowDelay)
keyboard.send_key(poof)		  #next(4) poof
time.sleep(lowDelay)
keyboard.send_key(nextUnit)   #select next(5) meepo
time.sleep(lowDelay)
keyboard.send_key(poof)	      #next(5) poof
time.sleep(lowDelay)
keyboard.send_key(selectHero) #select main meepo
if mouseclick:
    mouse.wait_for_click(1.0)
else:
    time.sleep(hightDelay)  
keyboard.send_key(blink)
time.sleep(lowDelay)
if useItem1:
    keyboard.send_key(item1)
    time.sleep(lowDelay)
if useItem2:  
    time.sleep(midDelay)
    time.sleep(midDelay)  
    keyboard.send_key(item2)
    time.sleep(lowDelay)
    keyboard.send_key(poof)
    time.sleep(lowDelay)
keyboard.send_key(selectAll)  #select all meepo
time.sleep(lowDelay)
keyboard.send_key(atack)
mouse.click_relative_self(0, 0, 1)
time.sleep(lowDelay)
keyboard.send_key(selectHero) #select main meepo
time.sleep(lowDelay)
keyboard.send_key(selectAll)  #select all meepo
