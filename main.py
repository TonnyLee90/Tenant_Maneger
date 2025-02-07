def add_my_property():
    print("Property's Information")
    

def get_service_code(max, min = 0):
    while True:
        code = int(input("Enter service code: "))
        if min <= code <= max:
            break
    return code

def is_tenant_exists(tenant):
    for index in range(len(tenents)):
            if tenant == tenents[index]["name"]:
                return True, index
    print(f"No tenant found by the name {tenant}. Please try again.")
    return False

def add_tenent():
    print("Enter tenent's information")
    name = input("Name: ")
    phone = input("Phone: ")
    #rent = input("Rent: ")

    tenent = {
        "name": name,
        "phone": phone,
        "rent": input("Rent: ")
    }

    global tenents
    tenents.append(tenent)

def delete_tenent():
    while True:
        person = input("Who are you gonna delete?: ")
        # search if this tanent exits in the tanents list
        for index in range(len(tenents)):
            if person == tenents[index]["name"]:
                tenents.pop(index)
                print(f"Tenant {person} has been removed!!!")
                # break # only break the for loop so that while loop never end even we enter a existing person
                return # exit the function
        print(f"No tenant found by the name {person}. Please try again.")

def edit_tenant():
    while True:
        person = input("Whose info are you gonna edit?: ")
        exist, index = is_tenant_exists(person)
        if exist == True:
            print("1. name 2. phone 3. rent")
            print("What information should be updated? ")

            code = get_service_code(3)

        match code:
            case 1:
                new_name = input("Name: ")
                tenents[index]["name"] = new_name
            case 2:
                new_phone = input("Phone: ")
                tenents[index]["phone"] = new_phone
            case 3:
                new_rent = input("rent: ")
                tenents[index]["rent"] = new_rent
            case _:
                print("Default option")
        return

    

tenents = [ {
        "name": "tonny",
        "phone": "phone",
        "rent": 321
    }]

print("Welcome to tanents management.")
print("Home Page")


edit_tenant()
print(tenents)
# show all of tanents
# add a tanent
# delete a tanent
# edit a tanent