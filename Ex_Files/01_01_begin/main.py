TIME = "dias"


def saludo():
    message = "Hola"
    return message


def despedida():
    message = "Adios"
    return message


if TIME == "dias":
    print(saludo())
else:
    print(despedida())
