#Written by Shiven Desai
class Customer:
    def __init__(self, name, address, city, state, zip_code, phone, age): 
        self._name = name
        self._address = address 
        self._city = city
        self._state = state
        self._zip_code = zip_code
        self._phone = phone
        self._age = age
        
    def set_name(self, name): 
        self._name = name
        
    def set_address(self, address): 
        self._address = address
        
    def set_city(self, city):
        self._city = city
        
    def set_state(self, state):
        self._state = state
        
    def set_zip_code(self, zip_code):
        self._zip_code = zip_code
        
    def set_phone(self, phone):
        self._phone = phone
        
    def set_age(self, age):
        self._age = age


import class7

#start the the main function
def main():
    name = input('Enter the name: ')
    address = input('Enter the address: ')
    city = input('Enter the city: ')
    state = input('Enter the state: ')
    zip_code = input('Enter the zip code: ')
    phone = input('Enter the phone: ')
    age = input('Enter the age: ')

    # create a new customer object and set its properties
    customer = class7.Customer(name, address, city, state, zip_code, phone, age)

    # print out a personalized greeting using the customer's information
    print(f"Hello {customer._name}, your address is {customer._address} in {customer._city}, {customer._state} {customer._zip_code}, and your phone number is {customer._phone}. You are {customer._age} years old.")
    
main()
