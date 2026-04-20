from datetime import datetime


class LogUtility:

    def __init__(self):
        self.GREEN = "\033[92m"
        self.YELLOW = "\033[93m"
        self.RED = "\033[91m"
        self.RESET = "\033[0m"

        self.date_format = "%Y-%m-%d %H:%M:%S"

    def debug(self, msg):
        print(f"{self.GREEN} {self.__now()} [INFO]{msg} {self.RESET}")

    def error(self, msg):
        print(f"{self.GREEN} {self.__now()} [INFO]{msg} {self.RESET}")

    def info(self, msg):
        print(f"{self.GREEN} {self.__now()} [INFO]{msg} {self.RESET}")

    def __now(self):
        return datetime.now().strftime(self.date_format)
