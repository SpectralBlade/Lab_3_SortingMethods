class Stack:
    def __init__(self):
        self.items = []
        self.min_stack = []

    def __repr__(self):
        return f"Stack({self.items})"

    def push(self, x: int) -> None:
        self.items.append(x)

        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> int | ValueError:
        if self.is_empty():
            raise ValueError("ValueError: Попытка вызвать 'pop' при пустом стеке.")

        popped = self.items.pop()

        if popped == self.min_stack[-1]:
            self.min_stack.pop()

        return popped

    def peek(self) -> int | ValueError:
        if self.is_empty():
            raise ValueError("ValueError: Попытка вызвать 'peek' при пустом стеке.")

        return self.items[-1]

    def is_empty(self) -> bool:
        return self.__len__() == 0

    def __len__(self) -> int:
        return len(self.items)

    def min(self) -> int | ValueError:
        if self.is_empty():
            raise ValueError("ValueError: Попытка вызвать 'min' при пустом стеке.")

        return self.min_stack[-1]