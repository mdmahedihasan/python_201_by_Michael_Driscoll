from weakref import WeakKeyDictionary


class Drinker:
    def __init__(self):
        self.req_age = 21
        self.age = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.age.get(instance, self.req_age)

    def __set__(self, instance, value):
        if value < 21:
            msg = "{name} is too young"
            raise Exception(msg.format(name=instance.name))
        self.age[instance] = value
        print("{name} is ok".format(name=instance.name))

    def __delete__(self, instance):
        del self.age[instance]


class Person:
    drinker_age = Drinker()

    def __init__(self, name, age):
        self.name = name
        self.drinker_age = age


p = Person("Mike", 44)
p = Person("Mat", 11)