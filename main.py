import math


def find_sum_of_two_primes(number: int) -> list[tuple[int, int]]:
    """Finding 2 prime numbers that sum of them = number.
     Returning list of tuples,each tuple is 2 prime numbers"""
    list_of_tuples_for_return = []
    half_of_number = int(number/2) + 1  # to prevent repeating same result

    # finding two prime numbers that sum of them is the number we are checking
    for first_num in range(2, half_of_number):
        if is_num_prime(first_num):
            second_num = number - first_num
            if is_num_prime(number - first_num):
                list_of_tuples_for_return.append((first_num, second_num))

    return list_of_tuples_for_return


def is_num_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    boundary = int(math.floor(math.sqrt(number)))

    for i in range(3, boundary + 1, 2):
        if number % i == 0:
            return False

    return True


def get_int_natural_number_from_user() -> int:
    """Getting natural even number > 2 from user. return: int"""
    while True:
        try:
            user_input = int(input("Enter a number:"))
            if user_input < 1 or user_input % 2 == 1:
                raise ValueError
            return user_input
        except ValueError:
            print("Please enter a natural even number greater than 2")


def printing_result(number: int, results: list[tuple[int, int]]):
    for result in results:
        print(f"The number {number} equals to the sum of {result[0]} and {result[1]}")


def main():
    input_number = get_int_natural_number_from_user()
    result_list = find_sum_of_two_primes(input_number)
    printing_result(input_number, result_list)


if __name__ == "__main__":
    main()
