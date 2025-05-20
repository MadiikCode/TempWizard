def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

print("Выберите исходную единицу:")
print("1. Цельсий")
print("2. Фаренгейт")
print("3. Кельвин")

choice = input("> ")

temperature = float(input("Введите значение температуры:\n> "))

if choice == "1":
    f = celsius_to_fahrenheit(temperature)
    k = celsius_to_kelvin(temperature)
    print(f"{temperature}°C = {f:.2f}°F = {k:.2f}K")
elif choice == "2":
    c = fahrenheit_to_celsius(temperature)
    k = fahrenheit_to_kelvin(temperature)
    print(f"{temperature}°F = {c:.2f}°C = {k:.2f}K")
elif choice == "3":
    c = kelvin_to_celsius(temperature)
    f = kelvin_to_fahrenheit(temperature)
    print(f"{temperature}K = {c:.2f}°C = {f:.2f}°F")
else:
    print("Неверный выбор. Попробуйте снова.")