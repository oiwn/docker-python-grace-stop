"""Example of how to gracefully stop python sccipt inside docker container"""
# pylint: disable=too-few-public-methods,missing-function-docstring
import sys
import signal
import time
import logging


class GracefulKiller:
    """Finish pything app on SIGINT/SIGTERM"""

    gracefully_exit = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        logging.info("Exiting from app... %s %s", signum, frame)
        self.gracefully_exit = True


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    killer = GracefulKiller()
    while True:
        time.sleep(1)
        logging.info("doing something in a loop ...")
        if killer.gracefully_exit:
            break

    logging.info("End of the program. I was killed gracefully :)")
    time.sleep(3)
