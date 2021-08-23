# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
print("\n========================\n")
celcius = float(input("Graus celsius: "))

fahrenheit = (celcius * 1.8) + 32
print("")

print("{}°C = {:.1f}°F".format(celcius,fahrenheit))
print("\n========================")
