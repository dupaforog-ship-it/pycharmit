import colorama
from colorama import Fore, Back, Style

print("=== Інтроспекція бібліотеки colorama ===")

print("\nАтрибути:")
for name in dir(colorama):
    if not name.startswith("_"):
        print(name)

print("\nНайважливіші атрибути:")
print("Fore — кольори тексту")
print("Back — кольори фону")
print("Style — стилі тексту")
print("init — налаштування colorama")

print("\nМетоди та функції:")
for name in dir(colorama):
    obj = getattr(colorama, name)
    if callable(obj) and not name.startswith("_"):
        print(name)

print("\nПриклад використання:")
print(Fore.RED + "Це червоний текст")
print(Fore.GREEN + "Це зелений текст")
print(Fore.BLUE + "Це синій текст")
print(Back.YELLOW + "Жовтий фон")
print(Style.RESET_ALL + "Звичайний текст")