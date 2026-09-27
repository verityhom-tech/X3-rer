def  reise_to_the_degrees(number):
    i = 0
    while True:
        result = number ** i
        yield result
        if result > 200 ** 20:
            return
        i += 1

res = reise_to_the_degrees(1234)

for e in res:
    print(e)
    print()
