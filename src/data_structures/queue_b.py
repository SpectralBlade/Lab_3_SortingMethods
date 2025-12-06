class Queue:
    def __init__(self):
        self._data = []

    def __repr__(self):
        return f"Queue({self._data})"

    def enqueue(self, x: int) -> None:
        self._data.append(x)

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        return self._data.pop(0)

    def front(self) -> int:
        if self.is_empty():
            raise IndexError("front from empty queue")

        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)
