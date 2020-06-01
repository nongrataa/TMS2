string="te4ts@vitebsl.second.mail.gov.com"
string_list = string.split('@')

for i in string_list[0]:
    if i.isalpha() or i.isdigit() or i in '-_.':
        print(i)
    else:
        print("Error")
        break
string_list2=string_list[1]
if string_list2[len(string_list2)] in '-_.':
    print("warning")

for i in range(len(string_list2)):
    if string_list2[i] in '-_.' and string_list2[i+1] in '-_.':
        print("Error222")