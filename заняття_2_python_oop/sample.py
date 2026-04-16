# closure (замикання)

# global scope
counter = 0

def counter():
    # enclosed, nonlocal
    counter = 0

    def increment():
        # local
        x = 1

        # non local
        nonlocal counter
        counter += 1

        return counter

    return increment

inc = counter()

print(inc())
print(inc())
print(inc())