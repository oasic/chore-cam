

class BaseAction:
    """Any class that exposes a run method that takes an identity as input"""

    def run(self, identity):
      print("BaseAction run called...")

    
class PrintChores:
    """Placeholder for PoC"""

    def run(self, identity):
        print("Chores for ", identity, ":")
        print("* Put away dishes\n* Clean room\n* Homework")


class LogIdentity:

    def run(self, identity):
        print("Running actions for ", identity)


actions = [
    LogIdentity(),
    PrintChores(),
]
