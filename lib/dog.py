#!/usr/bin/env python3

class Dog:
    
    def bark(self):
        print("Woof!")

    #Instance method definition
    def sit(self):
        print("The dog is sitting.")

fido = Dog()
# fido.bark()
fido.sit()

snoopy = Dog()
snoopy.bark()

# fido.__dir__()