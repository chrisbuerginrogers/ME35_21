import hub

while True:
    if hub.button.left.is_pressed():
        hub.display.show(hub.Image.YES)
    elif hub.button.right.is_pressed():
        hub.display.show(hub.Image.NO)
        