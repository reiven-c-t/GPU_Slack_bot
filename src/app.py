from GPUManager import GPUManager
from SlackAPICaller import send_message
import schedule
from time import sleep

manager = GPUManager()


def app():
    message = manager.main()
    if message != "":
        send_message(message)


schedule.every(5).seconds.do(app)

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        sleep(1)
