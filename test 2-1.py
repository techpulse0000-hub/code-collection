import csv
import datetime

# class contact:
#     f = open("contactbook.txt", 'r')
#     contact_list = f.readlines()
#     g = open("contactbook.txt", 'w')
#     h = open("contactbook.txt", 'a')
#     def __init__(self, name, phone, email, address):
#         self.name = name
#         self.phone = phone
#         self.email = email
#         self.address = address

#         a = name, " ", phone, " ", email, " ", address, "\n"

#         # g = open("contactbook.txt", 'r')
#         # contact_list= f.readlines()
#         # g.close()

        
#         if ''.join(a) not in contact.contact_list:
#             # with open("contactbook.txt", 'a') as f:
#             contact.g.writelines(a)

#     def delete(name):
#         # with open("contactbook.txt", 'r') as f:
#         new_list = contact.contact_list
#         # print(new_list)
#         for line in new_list:
#             word = line.split()
#             if name in word:
#                 the_line = line
#                 updated = [n for n in new_list if n != the_line]
#                 # with open("contactbook.txt", 'w') as g:
#                 contact.g.writelines(updated)
#                 break
#             else:
#                 continue
#         print('done')

#     def edit(name, attribute, update):
#         with open("contactbook.txt", 'r') as f:
#             new_list = f.readlines()
#             for line in new_list:
#                 word = line.split()
#                 name, phone, gmail, address = word
#                 if name in word:
#                     if attribute == "name":
#                         name = update
#                     elif attribute == "gmail":
#                         gmail = update
#                     elif attribute == "phone":
#                         phone = update
#                     elif attribute == "address":
#                         address = update
#                     word = name, ' ', phone, ' ', gmail, ' ', address
#                     updated = [n for n in new_list if n != line]
#                     updated += word
#                     with open("contactbook.txt", 'w') as g:
#                         g.writelines(updated)
#                     break
#                 else:
#                     continue
#             print('done')

#     def view(name):
#         with open("contactbook.txt", 'r') as f:
#             new_list = f.readlines()
#             for line in new_list:
#                 word = line.split()
#                 if name in word:
#                     print(line)

#     # f.close()
#     # g.close()
#     # h.close()
   
            
                     


# contact("muhammad", "8088089121", "luku@gmail.com", "eggroll_street")
# contact("habiba", "09049914031", "habibti@gmail.com", "eggroll_street")
# contact("bintu", "8086785345", "egrol@gmail.com", "fishroll_street")
# contact.edit("muhammad", "address", "jin_mu_street")
# contact.delete("muhammad")






# with open("contactbook.txt", "r") as f:
#     info= "muhammad", " ", "8088089121", " ", "luku@gmail.com", " ", "eggroll street", "\n"
#     line = f.readline()
#     word = line.split()
#     name, phone, gmail, address = word
#     print(name, phone, gmail, address)








