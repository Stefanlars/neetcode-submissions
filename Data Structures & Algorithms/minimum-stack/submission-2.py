

class MinStack:

    stack = []

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        prev_min = None

        if len(self.stack):
            prev_min = min(self.stack[-1]["val"], self.stack[-1]["prev_min"] if self.stack[-1]["prev_min"] is not None else self.stack[-1]["val"])

        self.stack.append({"val": val, "prev_min": prev_min})

    def pop(self) -> None:
        self.stack.pop()



    def top(self) -> int:
        return self.stack[-1]["val"]

    def getMin(self) -> int:
        return min(self.stack[-1]["prev_min"] if self.stack[-1]["prev_min"] is not None else self.stack[-1]["val"], self.stack[-1]["val"])
