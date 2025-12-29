class Person():
    def __init__(self,first_name,last_name):
        self.__first=first_name
        self.last=last_name

    @property
    def fullname(self):
        return self.__first+ ' '+self.last

    # @fullname.setter
    # def fullname(self,name):
    #
    #     first_name,last_name=name.split()
    #     self.__first=first_name
    #     self.last=last_name
    # @fullname.deleter
    # def fullname(self):
    #     self.first=None
    #     self.last=None

    def a(self):
        print(self)

    @classmethod
    def b(cls):
        print(cls)



person=Person('jia','yifei')
# print(person.__first)
print(person.a)
print(Person.b)
# print(person.fullname,person.last,person.first)
# person.fullname='li si'
# print(person.fullname,person.last,person.first)
# del person.fullname
# print(person.last,person.first)






