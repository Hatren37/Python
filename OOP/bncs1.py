"""Syntax of a class in Python
A class is a blueprint for creating objects. Objects are instances of classes.
A class can contain attributes (variables) and methods (functions).
class class_name:
    variables
    methods"""
class car:
    def start(self):
        print("Car start...")
    def stop(self):
        print("Car stop...")

a = car()  # Creating an instance of the class
a.start()  # Calling the start method
a.stop()   # Calling the stop method
# The above code defines a class named 'car' with two methods: start and stop.
