def format_name(f_name, l_name):
    formated_f_name = (f_name.title())
    formated_l_name = (l_name.title())
    return f"Result: {formated_f_name} {formated_l_name}"

formatted_name = format_name(f_name="Ilias", l_name="Sari")

length = len(formatted_name)

print(length)


#Other lesson!


def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)