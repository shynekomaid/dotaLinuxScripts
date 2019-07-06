#config
doHighFive = 1
#hotkeys
poof = "w"
blink = "t"
tp = "3"
stop = "s"
lookAtBase = "0"
nextUnit = "<tab>"
selectHero = "<f1>"
selectAll = "<f2>"
selectAllNoHero = "z"
highFive = "2"
#timing
lowDelay = 0.02
midDelay = 0.15
highDelay = 1.65
#script
time.sleep(midDelay)
keyboard.send_key(selectAll)
time.sleep(lowDelay)
keyboard.send_key(stop)
time.sleep(lowDelay)
keyboard.send_key(selectHero)
time.sleep(lowDelay)
keyboard.press_key("<alt>")
time.sleep(lowDelay)
keyboard.send_key(blink)
time.sleep(lowDelay)
keyboard.send_key(tp)
keyboard.release_key("<alt>")
time.sleep(lowDelay)
keyboard.send_key(selectAllNoHero)
time.sleep(lowDelay)
keyboard.send_key(lookAtBase)
keyboard.press_key("<shift>")
time.sleep(highDelay)
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
time.sleep(midDelay)
keyboard.send_key(selectHero) #select main meepo
time.sleep(lowDelay)
keyboard.release_key("<shift>")
keyboard.send_key(lookAtBase)
time.sleep(2.0)
if doHighFive:
    keyboard.send_key(lookAtBase)
    time.sleep(lowDelay)
    keyboard.send_key(selectAll)
    time.sleep(lowDelay)
    keyboard.press_key("<ctrl>")
    time.sleep(midDelay)
    keyboard.send_key(highFive)
    time.sleep(midDelay)
    keyboard.send_key(nextUnit)
    time.sleep(midDelay)
    keyboard.send_key(highFive)
    time.sleep(midDelay)
    keyboard.send_key(nextUnit)
    time.sleep(midDelay)
    keyboard.send_key(highFive)
    time.sleep(midDelay)
    keyboard.send_key(nextUnit)
    time.sleep(midDelay)
    keyboard.send_key(highFive)
    time.sleep(midDelay)
    keyboard.send_key(nextUnit)
    time.sleep(midDelay)
    keyboard.send_key(highFive)
    time.sleep(midDelay)
    keyboard.send_key(nextUnit)
    time.sleep(midDelay)
    keyboard.send_key(highFive)
    time.sleep(midDelay)
    keyboard.send_key(nextUnit)
    time.sleep(midDelay)
    keyboard.send_key(highFive)
    time.sleep(midDelay)
    keyboard.send_key(nextUnit)
    time.sleep(midDelay)
    keyboard.send_key(highFive)
    time.sleep(midDelay)
    keyboard.send_key(nextUnit)
    time.sleep(midDelay)
    keyboard.send_key(highFive)
    time.sleep(midDelay)
    keyboard.send_key(nextUnit)
    time.sleep(midDelay)
    keyboard.send_key(highFive)
    time.sleep(midDelay)
    keyboard.send_key(nextUnit)
    time.sleep(midDelay)
    keyboard.release_key("<ctrl>")
    time.sleep(midDelay)
    keyboard.send_key(selectHero)
