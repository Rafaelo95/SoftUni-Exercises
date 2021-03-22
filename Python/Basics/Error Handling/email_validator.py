"""
decided to keep custom exceptions in the same file,
considering the simplicity of the program
"""


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    command = input()
    if command == "End":
        break

    if '@' not in command:
        raise MustContainAtSymbolError("Email must contain @")
    else:
        email_name, site = command.split('@')

    if len(email_name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    site_name, domain = site.split('.', 1)

    if domain != "com" and domain != "bg" and domain != "org" and domain != "net":
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
