from itertools import product, permutations

# res = list(map("".join, product(*[list(str(n))] * len(str(n)))))
# print(res)
def func(n: int):
    w = sorted([''.join(p) for p in permutations(str(n), len(str(n)))])
    try:
        1/w.index(str(n))
    except ZeroDivisionError:
        return (f"Меньше этого числа {n} из комбинаций не бывает")
    return (f"Меньшее число из заданной комбинации :{w[w.index(str(n)) - 1]},"
            f" \nСтолько комбинаций получается :{len(w)}"
            )

n =[12345,135467,2071,2407]
for p in n:
    print(func(p),'\n')

s = 147

res = list(map("".join, product(*[list(str(s))] * len(str(s)))))

print(sorted(res),len(res))