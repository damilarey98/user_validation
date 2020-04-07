import random
value = "abcdefghijklmnopqrstuvwxyz1234567890"

client_info = {}
n = int(input("How many number of users?: "))
#since range begins from 1, when n=2, it request only one value
for i in range(1, n):
    new_client = {}
    
    print("Enter first name of user", i, ":")
    fname = input()
    print("Enter last name of user", i, ":")
    lname = input()
    print("Enter email of user", i, ":")
    email = input()

    new_client["FirstName"] = fname
    new_client["LastName"] = lname
    new_client["Email"] = email

    #comb is the combination of strings to form password
    comb1 = fname[0:2]
    comb2 = lname[-2:]
    comb3 = random.sample(value, 5)

    comb3_str = ''.join([str(elem) for elem in comb3])
    password = str(fname[0:2] + lname[-2:] + comb3_str)
    print("Your password is", password)
    new_client["Password"] = password

#adds new clients to the main container which is printed out at the end of program.
    new_client_id = len(client_info) + 1
    client_info[new_client_id] = new_client
    

    like = input("Do you like the password? [y/n]: ")

    if like == "y".lower():
        print("Password is secure.")
        print("Details of user", i, ":" , new_client)
    elif like == "n".lower():
        while True:
            new_password = input("Enter preffered password: ")
            new_client["Password"] = new_password 
            if len(new_password) < 7:
                print("Your password is not strong. Try again")
            elif len(new_password) == 7:
                print("Still not strong enough, length should be more than 7.")
            else:
                print("Your new password", new_password)
                print("Details of user", i, ":", new_client)
                break;
print("Clients added, client infos are now", client_info)