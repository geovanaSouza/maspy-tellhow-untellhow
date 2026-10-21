from maspy import *
from maspy.agent import Plan


class Sender(Agent):
    @pl(gain, Goal("hello"))
    def hello(self, src):
        self.print("Hello!")

    @pl(gain, Goal("send_plan"))
    def send_plan(self, src):
        plan = self.get(Plan, Goal("hello"))
        self.send("Receiver", tellHow, plan)
        self.send("Receiver", achieve, Goal("hello"))
        self.send("Receiver", achieve, Goal("debug"))
        self.stop_cycle()

class Receiver(Agent):
    # def add(self, data_type, instant=False, no_lock=False):
    #     super().add(data_type, instant, no_lock)

    #     # MASPY 2026.5.13 does not rebuild the plan index when a Plan is added through tellHow.
    #     if isinstance(data_type, Plan):
    #         self._build_plan_index()

    @pl(gain, Goal("debug"))
    def report(self, src):
        plans = self._plans
        self.print(f"Plans added to agent library: {plans}")
        indexed_plans = self._plan_index.values()
        self.print(f"Plans indexed to be used: {indexed_plans}")
        self.stop_cycle()

if __name__ == "__main__":
    Channel().show_exec = True
    Receiver("Receiver")
    Sender("Source", goals=Goal("send_plan"))
    Admin().start_system()
