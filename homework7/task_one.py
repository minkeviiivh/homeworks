def number_of_winner(a):
    result_two = []
    while len(result_two) < 3:
        result_two.append(a.index(max(a)) + 1)
        a[a.index(max(a))] = 0
    return result_two


result = number_of_winner([115, 352, 0, 310, 500])
print(result)
