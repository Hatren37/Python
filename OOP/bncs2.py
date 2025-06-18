class isbat:
    a = 'hello' #class attribute

    def __init__(self, name):
        self.name = name # instance attribute

    @classmethod
    def sample(cls):
        return cls.a  # class method accessing class attribute
print(isbat.sample())  # Output: hello