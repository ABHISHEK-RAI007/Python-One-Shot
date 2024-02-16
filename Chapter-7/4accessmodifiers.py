#  Public Modifier
class ABC:
    def __init__(self):
        self.public_attribute = None # This is a public attribute

        def public_function(): # This is a public function
            pass

obj1 = ABC()
obj1.public_attribute
obj1.public_function()

#  Private Modifier
class ABC:
    def __init__(self):
        self._protected_attribute = None # This is a protected attribute

        def __protected_function(): # This is a protectedfunction
            pass

obj1 = ABC()
print(obj1.__private_attribute)

