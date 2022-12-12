#Docstrings
def format_name(f_name, l_name):
  #validation of empty values
  if f_name=="" and l_name=="":
    return ""
  else:
    formated_f_name=f_name.title()
    formated_l_name=l_name.title()
    #returning a concatenation
    return formated_f_name+" "+formated_l_name
#setting inputs
f_name = input("Tell your first name: ")
l_name = input("Tell your last name: ")
#output
print(format_name(f_name=f_name, l_name=l_name))
