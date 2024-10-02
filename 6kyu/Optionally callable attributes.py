class MyClass:
    def __init__(self, values):
        # Define the default values as 0
        default_values = [0, 0, 0]

        # Unpack the values or use defaults if the list is shorter than 3
        self.prop1, self.prop2, self.prop3 = (values + default_values)[:3]

# Example usage
obj1 = MyClass([10, 20, 30])
print(obj1.prop1, obj1.prop2, obj1.prop3)  # Output: 10 20 30

obj2 = MyClass([10])  # Only one value provided
print(obj2.prop1, obj2.prop2, obj2.prop3)  # Output: 10 0 0

obj3 = MyClass([])  # Empty list
print(obj3.prop1, obj3.prop2, obj3.prop3)  # Output: 0 0 0