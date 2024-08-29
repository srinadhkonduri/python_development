# function with outputs

def formated_name(first_name, last_name):
    name = first_name.title()
    names = last_name.title()
    return f"{name} {names}"


print(formated_name("konduri", "srinadh"))

# multiple return statements

def my_name(f_name,l_name):
    if f_name == "" or l_name == "":
        return "you do not entered a valid inputs"
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name}  {last_name}"


print(formated_name(input("first name = "),input("last name = ")))