# TemperatureConvertor Version 1.0
# Very Basic if...elif..else statement to complete the purpose
from unittest import result

UserTemp = input("Enter Temperature: ")
UnitSelection = input("F or C: ")

temp = int(UserTemp)

if UnitSelection == "F":
    celciusConversion = int((temp - 32)*.5556)
    resultC = str(celciusConversion)
    print("The temperature of " + UserTemp + " Fahrenheit would be " + resultC + " Celcius")
elif UnitSelection == "C":
    fahrenheitConversion = int((temp*1.8)+32)
    resultF = str(fahrenheitConversion)
    print("The temperature of " + UserTemp + " Celcius would be " + resultF + " Fahrenheit")
else:
    print("Please make the appropriate selection")