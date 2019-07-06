blink = "t"
bkb = "c"
eul = "v"
ult = "r"
sb = "4"
discord = "b"
pt = "5"
lowDelay = 0.02
mouse.wait_for_click(1.0)
keyboard.send_key("<shift>")
keyboard.send_key(pt)
time.sleep(lowDelay)
keyboard.send_key(pt)
time.sleep(lowDelay)
keyboard.send_key(blink)
time.sleep(lowDelay)
keyboard.send_key(bkb)
time.sleep(lowDelay)
keyboard.send_key(discord)
time.sleep(lowDelay)
keyboard.send_key(eul)
time.sleep(0.2)
keyboard.send_key(sb)
time.sleep(0.1)
mouse.click_relative_self(0, 0, 3)
time.sleep(0.5)
time.sleep(lowDelay)
keyboard.send_key(ult)
time.sleep(lowDelay)
keyboard.release_key("<shift>")
time.sleep(1.1)
keyboard.send_key(pt)