def fact(n):
    """Find factorial of a number.

    >>> fact(5)
    120
    >>> fact(4)
    24
    >>> fact(3)
    6
    """
    if n == 0:
        return 1
    return n * fact(n-1)

def num_sevens(n):
    """Returns the number of times 7 appears as a digit of n.

    >>> num_sevens(3)
    0
    >>> num_sevens(7)
    1
    >>> num_sevens(7777777)
    7
    >>> num_sevens(2637)
    1
    >>> num_sevens(76370)
    2
    >>> num_sevens(12345)
    0
    """
    if n == 0:
        return 0
    elif n % 10 == 7:
        return 1 + num_sevens(n // 10)
    else:
        return num_sevens(n // 10)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """

    def helper(count, index, updater):
        if index == n:  # if index > n: return count
            return count + updater
        elif (index%7==0) or num_sevens(index)>0:
            return helper(count+updater, index+1, -updater)
        else:
            return helper(count+updater, index+1, updater)

    return helper(0, 1, 1)

"""1) The number of partitions of a positive integer n is the number of ways in
which n can be expressed as the sum of positive integers in increasing order.
For example, the number 5 has 7 partitions:

    5 = 5
    5 = 1 + 4
    5 = 2 + 3
    5 = 1 + 1 + 3
    5 = 1 + 2 + 2
    5 = 1 + 1 + 1 + 2
    5 = 1 + 1 + 1 + 1 + 1

Write a tree-recursive function part(n) that returns the number of partitions
of n.

Hint: Introduce a locally defined function that computes partitions of n using only
a subset of the integers less than or equal to n.  Once you have done so, you
can use very similar logic to the count_change function from lecture.
"""

def part(n):
    """Return the number of partitions of positive integer n.

    >>> part(5)
    7
    """

    def helper(count, partition):
        if count < 0:
            return 0
        if count == 0 or partition == 1:
            return 1
        return helper(count-partition, partition) + helper(count, partition-1)

    return helper(n, n)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    >>> count_change(16)
    36
    """

    # for 7
    #      (7, 7)
    #  (0, 7)  (7, 6)
    #       (1, 6) (7, 5)
    #            (2, 5) (7, 4)
    #                  (3, 4) (7, 3)
    #              (-1, 4) (3, 3)      (4, 3)               (7, 2)
    #                    (0, 3) (3, 2)   x               (5, 2) (7, 1)
    #                         (1, 2) (3, 1)           (3, 2) (5, 1)
    #                          (-1, 2) (1, 1)      (1, 2) (3, 1)
    #                                           (-1, 2) (1, 1)
    # 1 2 4
    # 1 1 1 4
    # 1 2 2 2
    # 1 1 1 2 2
    # 1 1 1 1 1 2
    # 1 1 1 1 1 1 1

    # find the highest power of two in amount
    def max_power_of_two(amount):
        def index(number):
            if number == 1:
                return 0
            return 1 + index(number >> 1)
        return 1 << index(amount)

    def helper(amount, cent):
        if amount < 0:
            return 0
        elif amount == 0 or cent == 1:
            return 1
        return helper(amount-cent, cent) + helper(amount, max_power_of_two(cent-1))

    return helper(amount, max_power_of_two(amount))

"""TOWER OF HANOI"""

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"

    def get_free_pole(start, end):
        # basically during movement, move n-1 to the other pole
        # so if we are moving from 1 to 2, move n-1 to the 3rd pole
        # or moving from 3 to 2, move n=1 to the 1st pole

        if end == 1:
            return 3 if start == 2 else 2
        if end == 2:
            return 3 if start == 1 else 1
        if end == 3:
            return 2 if start == 1 else 1

    if n == 1:
        print_move(start, end)
    else:
        move_stack(n-1, start, get_free_pole(start, end))
        move_stack(n-n+1, start, end)
        move_stack(n-1, get_free_pole(start, end), end)


"""3) A perfect number is defined as a positive integer equal to the sum of all
its factors less than itself. For example, the first perfect number is 6,
because its factors are 1, 2, 3, and 6, and 1+2+3=6. The second perfect number
is 28, because 1+2+4+7+14=28.

Write a function next_perfect(n) that tests numbers starting with n and
continuing with n+1, n+2, etc. until a perfect number is found. You will need
to implement sum_of_factors as well.
"""

def sum_of_factors(n):
    """Return the sum of the factors of n less than n. A factor of a positive
    integer n is a positive integer that divides n evenly.

    >>> sum_of_factors(21)
    11
    >>> sum_of_factors(28)
    28
    """
    def helper(i):
        if i == n:
            return 0
        elif (n%(n-i)) == 0:
            return n-i + helper(i+1)
        else:
            return helper(i+1)
    return helper(1)


def next_perfect(n):
    """Return the smallest perfect number greater than or equal to n.

    >>> next_perfect(7)
    28
    """
    if sum_of_factors(n) == n:
        return n
    return next_perfect(n+1)
