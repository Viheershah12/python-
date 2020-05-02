def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    else:
        return "Hello"

print(greet("en"),"Glen")
print(greet("fr"),"Michael")
print(greet("es"),"Sally")

input()