from gpiozero import Button

# create a button connected to gpio 26
button = Button('gpio26', pull_up=False)

while True:
    print('waiting')
    button.wait_for_press()
    print("The button was pressed!")
    button.wait_for_release()
    print("The button was realeased!")
