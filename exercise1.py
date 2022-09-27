class Person:
    def __init__(self,name,address,phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

        def get_name(self):
            return self.__name
        
        def get_address(self):
            return self.__address

        def get_number(self):
            return self.__phone_number

        def print_person(self):
            print('Name: ', self.__name)


class Customer(Person):
    def __init__(self,name, address, phone_number, customerNumber,mail_list):
        