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

# print(inc())
# print(inc())
# print(inc())

# Decorators

def require_auth(func):

    def inner(user):
        print("Before function")
        result = func(user)
        print("After function")

        return result

    return inner

@require_auth
def user_call(user):
    print(user)


# new_func = require_auth(user_call)


user_call({'name': 'Max'})