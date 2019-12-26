from GPUManager import GPUManager
from SlackAPICaller import send_message
import schedule
from time import sleep
from datetime import datetime

manager = GPUManager()


def app():
    print(str(datetime.utcnow()))
    message = manager.main()
    if message != "":
        send_message(message)


schedule.every(5).seconds.do(app)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        sleep(1)
