# Python follows LEGB rules for scoping unlike js usin let, const , var

# Python’s LEGB Rule:
# Python uses the LEGB rule to determine variable scope:

# Local: Variables defined inside a function.

# Enclosing: Variables in the nearest enclosing scope (for example, nested functions).

# Global: Variables defined at the top level of the module.

# Built-in: Predefined names in Python (for example, len, print).

x = "global"

def outer_function():
    x = "enclosing"

    def inner_function():
        x = "local"
        print(x)

    inner_function()

outer_function()  # Output: local
print(x)          # Output: global

