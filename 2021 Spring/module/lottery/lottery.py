from random import randint


def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        new_number = randint(1, 45)
        if new_number not in numbers:
            numbers.append(new_number)

    return numbers


def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for num in numbers:
        if num in winning_numbers:
            count = count + 1
    return count


def check(numbers, winning_numbers):
    n = count_matching_numbers(numbers, winning_numbers[:-1])
    bonus = count_matching_numbers(numbers, winning_numbers[-1:])
    if n == 6:
        return 100000000
    elif n == 5 and bonus == 1:
        return 50000000
    elif n == 5:
        return 1000000
    elif n == 4:
        return 50000
    elif n == 3:
        return 5000
    else:
        return 0


# # TEST
# print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
# print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))