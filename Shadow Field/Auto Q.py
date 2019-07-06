#config
dir_move = "n"
skill = "6"
stop = "s"
pt = "5"
#timing
lowDelay = 0.02
moveDelay = 0.06
#script
time.sleep(0.02)
keyboard.send_key(pt)
time.sleep(lowDelay)
keyboard.send_key(pt)
time.sleep(lowDelay)
keyboard.press_key(dir_move)
time.sleep(lowDelay)
mouse.click_relative_self(0, 0, 3)
time.sleep(moveDelay)
keyboard.send_key(stop)
keyboard.release_key(dir_move)
time.sleep(lowDelay)
keyboard.send_key("<shift>")
time.sleep(lowDelay)
keyboard.send_key(skill)
time.sleep(0.02)
keyboard.send_key(pt)
time.sleep(lowDelay)
keyboard.release_key("<shift>")