# import ipdb

# ipdb.set_trace()

# FUNCTIONS

def whatever_name_we_want(param1, param2="g'day"):
    # new_var = f"hello {param1} {param2}"
    new_var = "hello" + param1 + param2 # concatenation
    return new_var

result = whatever_name_we_want(param2=12, param1=True)

print(result)

def is_it_true(item="howdy"):
    # i want to return "yes" if something is truthy
    if item:
        return "yes"
    # return "no" if something is falsey
    return "no"
    
empty_list = []
empty_list.append("hello")

my_tuple = (1,2,3,4,5,6)
# a tuple is immutable

result = is_it_true( [] )
print(result)

# [] ===> list

# list comprehension

greetings = ["hello", "howdy", "g'day", "bonjour", "top o the morning"]

result = [ item.title() for item in greetings ]

print( result )

# SCOPE

basketball = 'Shaq'

def add_last_name():
    global basketball # tells the function to get the global variable
    basketball += " O'Neil"

# DICTIONARIES

my_dictionary = { 
    'key': 'value', 
    "key_two": "value two", 
    'key3': "value 3" 
}

def make_error():
    try:
        raise TypeError('I am a type error!')
    except ZeroDivisionError:
        print("You may not do this")
    except TypeError:
        print("Got a type error")


make_error()

print("Hello Flatiron! Class is in session!")