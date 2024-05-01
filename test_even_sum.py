def even_sum(numbers: list):
    counter = 0
    for i in range(len(numbers)):
        if isinstance(numbers[i], int):
            if numbers[i] % 2 == 0:
                counter += numbers[i]
        else:
            pass
    if counter == 0:
        print("В списке нет чисел")
    else:
        print(counter)


even_sum([1, 2, 3, 4])
even_sum([4, 4, 4])
even_sum(["j", "j", 4])
even_sum(["j", "j"])
