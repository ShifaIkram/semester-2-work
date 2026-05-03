# Task#3
# To extract only strings from the given list of strings,integers,
# sets & tuples using Recursive Function

# The og function
def only_strings(data):
    if not data:
        return []

    first = data[0]
    rest = data[1:]

    if isinstance(first, str):
        return [first] + only_strings(rest)
    elif isinstance(first, (list, tuple, set)):
        return only_strings(list(first)) + only_strings(rest)
    else:
        return only_strings(rest)

# Mixed Example list
ex_list = [ "I said", 10, [1, "oohh", (2, "I'm blinded")],
    {"by the", 5}, ("lights", 7), 100 ]


# Calling the  function
print(only_strings(ex_list))


