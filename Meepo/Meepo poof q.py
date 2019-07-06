#hotkeys
earthbind = "q" 		     #(first skill)
poof = "w"
nextUnit = "<tab>"
selectHero = "<f1>"
selectAll = "<f2>"
lowDelay = 0.02
midDelay = 0.15
#script
time.sleep(midDelay)
keyboard.send_key(poof)		  #main poof
time.sleep(lowDelay)
keyboard.send_key(earthbind)  #main earthbind(first skill)
time.sleep(lowDelay)
keyboard.send_key(nextUnit)   #select next(2) meepo
time.sleep(lowDelay)
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
keyboard.send_key(earthbind)  #next(4) earthbind(first skill)
time.sleep(lowDelay)
keyboard.send_key(nextUnit)   #select next(5) meepo
time.sleep(lowDelay)
keyboard.send_key(poof)	      #next(5) poof
time.sleep(midDelay)
keyboard.send_key(selectHero) #select main meepo
time.sleep(lowDelay)
keyboard.send_key(selectAll)  #select all meepo
