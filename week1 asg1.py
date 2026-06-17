def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit

celsius=float(input("Enter temperature in celsius: "))
print("Temperature in fahrenheit will be: ",celsius_to_fahrenheit(celsius))
