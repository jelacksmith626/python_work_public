import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT",
            message = "Go to bed!",
            timeout = 10
            )
        time.sleep(86400)
    