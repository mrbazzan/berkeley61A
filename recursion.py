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
