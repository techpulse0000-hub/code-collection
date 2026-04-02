class contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

        a = name, " ", phone, " ", email, " ", address, "\n"

        g = open("contactbook.txt", 'r')            
        b = g.readlines()
        if b == []:
            with open("contactbook.txt", 'a') as f:
                f.writelines(a)
        else:
            words = ''.join(b).split()
            if name not in words:
                with open("contactbook.txt", 'a') as f:
                    f.writelines(a)
            else:
                print("contact already exists")
                
        
        g.close()


    def delete(name):
        with open("contactbook.txt", 'r') as f:
            new_list = f.readlines()
            for line in new_list:
                word = line.split()
                if name in word:
                    the_line = line
                    updated = [n for n in new_list if n != the_line]
                    with open("contactbook.txt", 'w') as g:
                        g.writelines(updated)
                    break
                else:
                    continue
            print('done')

    def edit(name, attribute, update):
        f = open("contactbook.txt", 'r')
        new_list = f.readlines()
        for line in new_list:
            word = line.split()
            names, phone, gmail, address = word
            if name in word and update not in word:
                if attribute == "name":
                    name = update
                elif attribute == "gmail":
                    gmail = update
                elif attribute == "phone":
                    phone = update
                elif attribute == "address":
                    address = update
                word = names, ' ', phone, ' ', gmail, ' ', address
                updated = [n for n in new_list if n != line]
                print(updated)
                updated += word
                with open("contactbook.txt", 'w') as g:
                    g.writelines(updated)
                break
            else:
                continue
        print('done')
        f.close()

    def view(name):
        with open("contactbook.txt", 'r') as f:
            new_list = f.readlines()
            for line in new_list:
                word = line.split()
                if name in word:
                    print(line)

            
   
            
                     


contact("muhammad", "8088089121", "luku@gmail.com", "eggroll_street")
contact("habiba", "09049914031", "habibti@gmail.com", "eggroll_street")
contact("bintu", "8086785345", "egrol@gmail.com", "fishroll_street")
contact.edit("habiba", "address", "jin_mu_street")
# contact.delete("muhammad")

