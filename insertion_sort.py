def insertion_sort(numbers):
    n = len(numbers)
    for i in range(n):
        element = numbers[i]
        j = i - 1
        while j >= 0 and element < numbers[j] : #j >= 0 1st coz when j=0 next it will be -1, so danger
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = element