import time

while True:
    current_time = time.localtime()
    formatted_time = time.strftime("%H:%M:%S", current_time)
    print("\r" + formatted_time, end="", flush=True)
    time.sleep(1)
