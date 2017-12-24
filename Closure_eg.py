def outer_function():
    message="hi"

    def inner_function():
        print (message)
    return inner_function

my_func=outer_function()
my_func()