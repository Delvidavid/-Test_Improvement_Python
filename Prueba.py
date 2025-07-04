import time
# Dictionary for books
books = {

    "cien años de soledad" : {

        "author" : "gabriel garcia marquez",
        "category" : "ficcion",
        "price": 350000,
        "stock": 3,
        },

    "cronica de una muerte anunciada" : {

        "author" : "gabriel garcia marquez",
        "category" : "novela",
        "price": 200000,
        "stock": 2,
        },

    "el ultimo secreto" : {

        "author" : "dan brown",
        "category" : "literatura",
        "price": 100000,
        "stock": 4,
        },

    "la voragine" : {

        "author" : "jose eustasio",
        "category" : "ficcion",
        "price": 120000,
        "stock": 7,
        },

    "ahora" : {
        #hector abad - y en la hora
        "author" : "d",
        "category" : "literatura",
        "price": 70000,
        "stock": 5,
        },

}

# Dictionary for sale
sale = {}

flag = True

#------------------- Inventary-----------------------

# validations of entered data
def ValidateName(messeges):

     while flag:
        nameInput = input(messeges).strip().lower()

        if not nameInput:
            print("❌ The name can't be empty.")
        elif nameInput.isdigit():
            print("❌ numbers are not accepted")
        else:
            return nameInput

def ValidateNumber(messages):
    while flag:
        number = input(messages).strip()
        if number.isdigit() and float(number) >= 0:
            return float(number)
        print("❌ Please enter a valid age greater than 0.")


# add books with their characteristics
def AddBook():

    while flag:

        cantBook = ValidateNumber("How many books do you want to enter in the invetory: ")
        cont = 1

        while cont <= int(cantBook):
            print(f"Book #{cont}")
            title = input("Enter title:")
            author =  ValidateName("Enter author: ")
            category = ValidateName("Enter category: ")
            price = ValidateNumber("Enter price: ")
            cant = ValidateNumber("Enter cant: ")
            books[title] = {"author":author,"category":category,"price":price,"stock":cant}
            print(f"Book {title} add with success")
            cont +=1

        break


# consult books already entered
def ConsultBook():

    consult = input("Enter Book to consult: ")

    if consult in books:
        print(f"books information found:{books[consult]} ")
    else:
        print("book not found")

# update books already entered
def UpdateBook():

    update = input("Enter book to update: ").strip()

    if update in books:

        author =  ValidateName("Enter new author: ")
        category = ValidateName("Enter new category: ")
        price = ValidateNumber("Enter new price: ")
        cant = ValidateNumber("Enter new cant: ")

        books[update]={"author":author,"category":category,"price":price,"stock":cant}

    else:
        print("book not found")

# delete books already entered
def DeleteBook():

    delete = input("Enter book to delete: ").strip()

    if delete in books:

        del books[delete]
        print("book delete success")
    else:
        print("book not found")



# ----------------- Sale ---------------------


# record invoice data
def RegisterSale():

    while flag:

        cantbooks = ValidateNumber("How many book will the customer buy?: ")
        cont = 1

        while cont <= int(cantbooks):

            namebook = ValidateName("Enter book sold: ")

            if namebook in books:

                idsale = input("Enter id of the sale: ").strip()

                if idsale in sale:
                    print("the id exists")

                else:

                    nameCustomer = ValidateName("Enter name of customer: ")
                    soldDate = input("Enter data of tha sale: ")
                    soldCant = ValidateNumber("Enter cant: ")
                    soldDiscount = ValidateNumber("Enter discount: ")

                    if soldCant <= books[namebook]["stock"] and soldCant > 0:

                        subTotal = (books[namebook]["price"]*soldCant)

                        # add data to the sales dictionary
                        sale[idsale] = {"customer": nameCustomer,"nameBook":namebook,"author":books[namebook]["author"],"date":soldDate,"soldCant":soldCant,"discount":soldDiscount,"subTotal":subTotal,"priceTotal": (subTotal- (subTotal*soldDiscount/100)) }

                        books[namebook]["stock"] -= soldCant

                        print("Register sucess")
                        cont +=1

                    else:
                        print(f"there is not enough books {namebook}")

            else    :
                print("Product not found")
        break

# consult registered invoices
def ConsultSale():

    consult = input("Enter Id of the record to be consulted: ").strip()

    if consult in sale:
        print(f"information found:{sale[consult]} ")
    else:
        print("Product not found")

# report of each author (quantity and price)
def Report():

    author =  ValidateName("Enter author: ").lower().strip()
    cantReport = 0
    saleReport = 0

    for x in sale:
        
        if sale[x]["author"] == author:

            cantReport += sale[x]["soldCant"]
            saleReport += sale[x]["priceTotal"]
        

    print(f'''Report the author {author}
        Cant of books sold: {cantReport}
        Price total sold: {saleReport}
          ''')
    
# total report
def Income():

    subTotal = 0
    Total = 0
    for x in sale:

        subTotal += sale[x]["subTotal"]
        Total += sale[x]["priceTotal"]        


    print(f"The income neto is: {subTotal} ")
    print(f"The income bruto is: {Total} ")

def printLate(text, delay=0.08):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay)

# Main menu
def menu():
    while flag:
        print("===== MAIN MENÚ =====")
        print("1. Register Books")
        print("2. consult Books")
        print("3. Update Books")
        print("4. Delete Books")
        print("5. Register Sale")
        print("6. Consult Register Sale")
        print("7. Report Sale")
        print("8. Incomes")
        print("9. Exit")
        print("====================")

        option = input("Enter an option: ").strip()

        match option:

            case "1":
                AddBook()

            case "2":
                ConsultBook()

            case "3":
                UpdateBook()

            case "4":
                DeleteBook()

            case "5":
                RegisterSale()

            case "6":
                ConsultSale()

            case "7":
                Report()

            case "8":
                Income()

            case "9":
                printLate("👋 ¡Thanks for using the system! See you soon!.....")
                break

            case _:
                print("❌ Option invalidates. try again.\n")

# run program
menu()
