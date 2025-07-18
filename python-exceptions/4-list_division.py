#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            num1 = my_list_1[i]
            num2 = my_list_2[i]

            if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
                print("wrong type")
                result.append(0)
                continue

            result.append(num1 / num2)

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass

    return result
