class Stack:
    def __init__(self):
        """Создаёт два стека - основной и вспомогательный для минимальных значений."""
        self.items = []
        self.min_stack = []

    def __repr__(self):
        """Возвращает строковое представление стека."""
        return f"Stack({self.items})"

    def push(self, x: int) -> None:
        """Добавляет элемент x на вершину стека."""
        self.items.append(x)

        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> int:
        """Удаляет и возвращает верхний элемент стека. Ошибка при пустом стеке."""
        if self.is_empty():
            raise IndexError("IndexError: Попытка вызвать 'pop' при пустом стеке.")

        popped = self.items.pop()

        if popped == self.min_stack[-1]:
            self.min_stack.pop()

        return popped

    def peek(self) -> int:
        """Возвращает верхний элемент стека без удаления. Ошибка при пустом стеке."""
        if self.is_empty():
            raise IndexError("IndexError: Попытка вызвать 'peek' при пустом стеке.")

        return self.items[-1]

    def is_empty(self) -> bool:
        """Возвращает True, если стек пуст, иначе False."""
        return not self.items

    def __len__(self) -> int:
        """Возвращает количество элементов в стеке."""
        return len(self.items)

    def min(self) -> int:
        """Возвращает минимальный элемент в стеке. Ошибка при пустом стеке."""
        if self.is_empty():
            raise IndexError("IndexError: Попытка вызвать 'min' при пустом стеке.")

        return self.min_stack[-1]