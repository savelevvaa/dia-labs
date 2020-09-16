import requests
from LR2.lab_python_oop.rectangle import *
from LR2.lab_python_oop.squad import *
from LR2.lab_python_oop.circle import *

print(requests.__license__ + "\n")

rect = Rectangle(10,15, "Blue")
sqd = Squad(10,"Black")
circ = Circle(5, "Red")

rect.about()
sqd.about()
circ.about()


