from fact_fibo import fibonacci, fibo_recursive, fact_recursive, factorial
from data_structures.stack_b import Stack
from data_structures.queue_b import Queue
from sort_methods import (
    bubble_sort,
    quick_sort,
    counting_sort,
    bucket_sort,
    radix_sort,
    heap_sort
)
STACK_COMMANDS = {
    "stack_push": Stack.push,
    "stack_pop": Stack.pop,
    "stack_peek": Stack.peek,
    "stack_is_empty": Stack.is_empty,
    "stack_len": Stack.__len__,
    "stack_min": Stack.min
}
QUEUE_COMMANDS = {
    "queue_enqueue": Queue.enqueue,
    "queue_dequeue": Queue.dequeue,
    "queue_front": Queue.front,
    "queue_is_empty": Queue.is_empty,
    "queue_len": Queue.__len__
}
SORT_COMMANDS = {
    "bubble_sort": bubble_sort.bubble_sort,
    "quick_sort": quick_sort.quick_sort,
    "counting_sort": counting_sort.counting_sort,
    "bucket_sort": bucket_sort.bucket_sort,
    "radix_sort": radix_sort.radix_sort,
    "heap_sort": heap_sort.heap_sort
}
MATH_COMMANDS = {
    "fibonacci": fibonacci.fibonacci,
    "fibo_recursive": fibo_recursive.fibonacci_recursive,
    "fact_recursive": fact_recursive.factorial_recursive,
    "factorial": factorial.factorial,
}
SORT_KEYS = {
    "abs": lambda x: abs(x),
    "neg": lambda x: -x,
    "str": lambda x: str(x),
    "len": lambda x: len(str(x)),
}
SORT_COMPARATORS = {
    "desc": lambda a, b: (b > a) - (b < a),
    "abs": lambda a, b: (abs(a) > abs(b)) - (abs(a) < abs(b)),
    "str": lambda a, b: (str(a) > str(b)) - (str(a) < str(b)),
}
HELP_CMD = """
Команды для сортировки:
bubble_sort         - сортировка пузырьком (самая медленная, сравнение 2 чисел)
quick_sort          - быстрая сортировка (относительно pivot)
heap_sort           - пирамидальная сортировка (кучей)
counting_sort       - сортировка подсчетом (*)
bucket_sort         - сортировка ведрами (* **)
radix_sort          - подразрядная сортировка (*)
(*) - не поддерживают строки, (**) - поддерживает только целые числа

Ключи в сортировках:
abs         - сравнение без знака
neg         - сравнение в обратном порядке
str         - сравнение в строковом представлении
len         - сравнение относительно длины

Компараторы в сортировках:
desc        - сравнение по убыванию (в обратном порядке)
abs         - сравнение по модулю (без знака)
str         - сравнение в строковом представлении

Команды для стека:
create_stack      - создать новый пустой стек (заменить текущий)
stack_push X      - добавить элемент X в стек
stack_pop         - удалить верхний элемент стека и вывести его
stack_peek        - вывести элемент на вершине стека без удаления
stack_is_empty    - проверить, пуст ли стек (возвращает True/False)
stack_len         - вывести количество элементов в стеке
stack_min         - вывести минимальный элемент в стеке
create_stack      - создать новый пустой стек

Команды для очереди:
create_queue      - создать новую пустую очередь (заменить текущую)
queue_enqueue X   - добавить элемент X в очередь (в конец)
queue_dequeue     - удалить первый элемент очереди и вывести его
queue_front       - вывести первый элемент без удаления
queue_is_empty    - проверить, пуста ли очередь (возвращает True/False)
queue_len         - вывести количество элементов в очереди
create_queue      - создать новую пустую очередь

Математические функции:
factorial X                 - вычислить факториал от X
factorial_recursive X       - вычислить факториал от X рекурсивным методом
fibonacci X                 - вычислить X-ое число Фибоначчи
factorial_recursive X       - вычислить X-ое число Фибоначчи рекурсивным методом

Дополнительно:
help        - показать эту команду
exit        - выйти из консоли
"""
