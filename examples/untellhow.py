from maspy import *

class Sample(Agent):
    @pl(gain, Goal("delete_plan_from_receiver"))
    def delete_plan_from_receiver(self, src):
        # Initial state of the receiver.
        self.send("Receiver", achieve, Goal("debug", "INITIAL"))

        # Attempt to remove the hello plan from the receiver.
        hello_plan = self.get(Plan, Goal("hello"))
        self.send("Receiver", untellHow, hello_plan)

        # Final state of the receiver.
        self.print("Final state of the receiver")
        self.send("Receiver", achieve, Goal("debug", "FINAL"))

        # The hello goal still executes because the plan was not removed.
        self.send("Receiver", achieve, Goal("hello"))
        self.stop_cycle()

    @pl(gain, Goal("debug", Any))
    def report(self,src, state):
        plans = self._plans
        self.print(f"[{state}] Plans in the agent library: {plans}")
        indexed_plans = self._plan_index.values()
        self.print(f"[{state}] Plans indexed to be used: {indexed_plans}")

    @pl(gain, Goal("hello"))
    def hello(self, src):
        self.print("Hello!")
        self.stop_cycle()

if __name__ == "__main__":
    print("Untell example!")
    Channel().show_exec = True
    Sample("Receiver")
    Sample("Orchestrator", goals=Goal("delete_plan_from_receiver"))
    Admin().start_system()