from maspy import *


class TellHowUntellHow(Agent):
    @pl(gain, Goal("hello"))
    def say_hello(self, src):
        self.print("Hello, world!")
        self.stop_cycle()


if __name__ == "__main__":
    TellHowUntellHow(goals=[Goal("hello")])
    Admin().start_system()
