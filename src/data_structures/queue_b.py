class Queue:
    def __init__(self):
        """Создаёт пустую очередь."""
        self._data = []

    def __repr__(self):
        """Возвращает строковое представление очереди."""
        return f"Queue({self._data})"

    def enqueue(self, x: int) -> None:
        """Добавляет элемент x в конец очереди."""
        self._data.append(x)

    # Автокомплит в PyCharm чуть до гроба не довел

    def dequeue(self) -> int:
        """Удаляет и возвращает первый элемент очереди. Ошибка при пустой очереди."""
        if self.is_empty():
            raise IndexError("IndexError: Попытка вызвать 'dequeue' при пустой очереди.")

        return self._data.pop(0)

    def front(self) -> int:
        """Возвращает первый элемент очереди без удаления. Ошибка при пустой очереди."""
        if self.is_empty():
            raise IndexError("IndexError: Попытка вызвать 'front' при пустой очереди.")

        return self._data[0]

    def is_empty(self) -> bool:
        """Возвращает True, если очередь пуста, иначе False."""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Возвращает количество элементов в очереди."""
        return len(self._data)
