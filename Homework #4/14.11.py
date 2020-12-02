""""Ricky Tran - 1832920"""


def selection_sort_descend_trace(numbers):
    for i in range(len(numbers)-1):
        a = i
        for j in range(i + 1, len(numbers)):
            if numbers[a] < numbers[j]:
                a = j
        numbers[i], numbers[a] = numbers[a], numbers[i]
        for x in numbers:
            print(x, end=" ")
        print()
    return numbers

if __name__ == "__main__":
    numbers = [int(x) for x in input("").split()]
    selection_sort_descend_trace(numbers)