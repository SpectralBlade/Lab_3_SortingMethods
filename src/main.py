from constants import (
    STACK_COMMANDS,
    QUEUE_COMMANDS,
    MATH_COMMANDS,
    SORT_COMMANDS,
    SORT_KEYS,
    SORT_COMPARATORS,
    HELP_CMD
)
from Lab_3_SortingMethods.src.data_structures.queue_b import Queue
from Lab_3_SortingMethods.src.data_structures.stack_b import Stack
from parse_array import parse_array

def main() -> None:
    """
    Функция, являющаяся точкой входа в приложение и взаимодействующая с пользователем.
    :return: Данная функция ничего не возвращает
    """
    queue = None
    stack = None
    print("Для подсказки по командам введите 'help'.")
    try:
        while (input_str := input("Введите желаемую функцию/команду для запуска: \n")) != "exit":
            user_input = input_str.split()
            cmd = user_input[0]
            args = user_input[1:]
            match cmd:
                case cmd if cmd in SORT_COMMANDS:
                    match cmd:
                        case "bucket_sort":
                            x = [float(k) for k in input("Введите массив для сортировки: ").split()]
                            y = int(input("Введите количество 'ведер': "))
                            print(SORT_COMMANDS[cmd](x, y))
                        case "bubble_sort" | "quick_sort" | "heap_sort":
                            try:
                                x = parse_array(input("Введите массив для сортировки: "))
                            except ValueError as e:
                                print(e)
                                continue
                            y = input("Введите ключ из списка (abs, neg, str, len) или none: ")
                            match y:
                                case "none":
                                    print(SORT_COMMANDS[cmd](x, None, SORT_COMPARATORS[input("Введите "
                                            "компаратор из списка (asc, desc, abs, str) или none: ")]))
                                case _:
                                    print(SORT_COMMANDS[cmd](x, SORT_KEYS[y], None))
                        case _:
                            try:
                                x = parse_array(input("Введите массив для сортировки: "))
                            except ValueError as e:
                                print(e)
                                continue
                            try:
                                print(SORT_COMMANDS[cmd](x))
                            except ValueError as e:
                                print(e)
                                continue
                case cmd if cmd in MATH_COMMANDS:
                    if args:
                        print(MATH_COMMANDS[cmd](args[0]))
                    else:
                        print(MATH_COMMANDS[cmd](int(input("Введите целое число для подсчета "
                                                       "значения выбранной функции: "))))
                case cmd if cmd == "create_queue":
                    queue = Queue()
                    print("Очередь создана.")
                case cmd if cmd == "create_stack":
                    stack = Stack()
                    print("Стек создан.")
                case cmd if cmd in QUEUE_COMMANDS:
                    if queue is None:
                        print("ValueError: Очередь не создана")
                    else:
                        try:
                            before = repr(queue)
                            if args:
                                arg = int(args)
                                result = QUEUE_COMMANDS[cmd](queue, arg)
                            else:
                                result = QUEUE_COMMANDS[cmd](queue)

                            print("Команда выполнена.")
                            print("Очередь до:", before)

                            if result is not None:
                                print("Результат команды:", result)

                            print("Очередь после:", queue)
                        except (OverflowError, ValueError, IndexError, TypeError) as e:
                            print(e)
                case cmd if cmd in STACK_COMMANDS:
                    if stack is None:
                        print("ValueError: Стек не создан")
                    else:
                        try:
                            before = repr(stack)
                            if args:
                                arg = int(args)
                                result = QUEUE_COMMANDS[cmd](queue, arg)
                            else:
                                result = QUEUE_COMMANDS[cmd](queue)

                            print("Команда выполнена.")
                            print("Стек до:", before)

                            if result is not None:
                                print("Результат команды:", result)

                            print("Стек после:", stack)
                        except (OverflowError, ValueError, IndexError, TypeError) as e:
                            print(e)
                case "help":
                    print(HELP_CMD)
                case _:
                    print("SyntaxError: Неизвестная функция для подсчета")
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
