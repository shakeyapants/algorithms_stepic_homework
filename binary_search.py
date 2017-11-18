"""
В первой строке даны целое число 1≤n≤10^5 и массив A[1…n] из n различных натуральных чисел, не превышающих 10&9,
в порядке возрастания, во второй — целое число 1≤k≤10^5 и k натуральных чисел b1,…,bk, не превышающих 10^9.
Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n, для которого A[j]=bi, или −1, если такого j нет.
"""

sequence_1 = [int(num) for num in input().split()]
sequence_2 = [int(num) for num in input().split()]


def find_num(sequence_1, sequence_2):
    answer = []

    for num in sequence_2[1:]:
        left = 1
        right = sequence_1[0]
        while left <= right:
            m = int((left + right) / 2)
            if sequence_1[m] == num:
                answer.append(m)
                break
            elif sequence_1[m] > num:
                right = m - 1
            else:
                left = m + 1
        if left > right:
            answer.append(-1)
    return ' '.join([str(item) for item in answer])

if __name__ == '__main__':
    print(find_num(sequence_1, sequence_2))
