def reise_to_the_degrees(number, max_degree):
    i = 0
    for j in range(max_degree):
        yield number ** i
        i += 1

res = reise_to_the_degrees(1234, 20)

for e in res:
    print(e)
print("new")
for e in res:
    print(e)