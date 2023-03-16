import time, _thread, machine

def task(n, delay):
    led = machine.Pin(6, machine.Pin.OUT)
    for i in range(n):
        led.high()
        time.sleep(delay)
        led.low()
        time.sleep(delay)
    print('done')

_thread.start_new_thread(task, (1000, 0.5))
