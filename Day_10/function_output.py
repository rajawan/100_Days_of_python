def format_name(first_name,last_name):
    if first_name=="" and last_name=="":
        return "Blank Input Not Valid"
    formated_first_name=first_name.title()
    formated_last_name=last_name.title()
    return f"{formated_first_name} {formated_last_name}"
print(format_name("",""))