import tkinter as tk
import shelve
top = tk.Tk()
top.title("SIMPLE PHARMACY MANAGEMENT SYSTEM")
top.geometry("500x500")
top.configure(bg = "white")
global Cid,name,phNumber,medid,quality,price,idEntry,nameEntry,phNumberEntry,medicineEntry,quantityEntry,priceEntry

def register():
    registerWindow = tk.Toplevel()
    registerWindow.title("PHARMACY MANAGEMENT SYSTEM")
    registerWindow.geometry("950x500")
    registerWindow.configure(bg = "white")
    idLabel = tk.Label(registerWindow,text = "Customer ID:",bg = "white").grid(row = 0,column = 0)
    nameLabel = tk.Label(registerWindow,text = "Customer Name:",bg = "white").grid(row = 1,column = 0)
    phNumberLabel = tk.Label(registerWindow,text = "Phone Number:",bg = "white").grid(row = 2,column = 0)
    medicineLabel = tk.Label(registerWindow,text = "medicine ID",bg = "white").grid(row = 3,column = 0)
    quantityLabel = tk.Label(registerWindow,text = "Quantity",bg = "white").grid(row = 4,column = 0)
    priceLabel = tk.Label(registerWindow,text = "Price",bg = "white").grid(row = 5,column = 0)
    listLabel = tk.Label(registerWindow,text = "LIST OF MEDICINES",bg = "white").grid(row = 7,column = 0)
    idEntry = tk.Entry(registerWindow,width = 40)
    idEntry.grid(row = 0,column = 1)
    nameEntry = tk.Entry(registerWindow,width = 40)
    nameEntry.grid(row = 1,column = 1)
    phNumberEntry = tk.Entry(registerWindow,width = 40)
    phNumberEntry.grid(row = 2,column = 1)
    medicineEntry = tk.Entry(registerWindow,width = 40)
    medicineEntry.grid(row = 3,column = 1)
    quantityEntry = tk.Entry(registerWindow,width = 40)
    quantityEntry.grid(row = 4,column = 1)
    priceEntry = tk.Entry(registerWindow,width = 40)
    priceEntry.grid(row = 5,column = 1)
    label1 = tk.Label(registerWindow,text = "\tMED ID   \tMED TYPE   \t\tMED NAME         MED PRICE(RUPEES)",bg = "white").grid(row = 8,column = 0)
    label2 = tk.Label(registerWindow,text = "111   \t   \tOTC   \t\t    Probiotics             RS 25.00",bg = "white").grid(row = 9,column = 0)
    label3 = tk.Label(registerWindow,text = "112   \t    \tOTC   \t\t    Vitamin C(500mg)       RS 25.00",bg = "white").grid(row = 10,column = 0)
    label4 = tk.Label(registerWindow,text = "113   \t    \tOTC   \t\t    Acid Free C(500mg)     RS 35.00",bg = "white").grid(row = 11,column = 0)
    label5 = tk.Label(registerWindow,text = "114   \t    \tOTC   \t\t    Women'S Multivate      RS 50.00",bg = "white").grid(row = 12,column = 0)
    label6 = tk.Label(registerWindow,text = "115   \t    \tOTC   \t\t    Marino Tablet          RS 45.00",bg = "white").grid(row = 13,column = 0)
    label7 = tk.Label(registerWindow,text = "116   \t    \tOTC   \t\t    Crocin                 RS 25.00",bg = "white").grid(row = 14,column = 0)
    label8 = tk.Label(registerWindow,text = "117   \t    \tOTC   \t\t    Maxi Cal Tablet        RS 30.00",bg = "white").grid(row = 15,column = 0)
    label9 = tk.Label(registerWindow,text = "118   \t    \tOTC   \t\t    Dolo 350               RS 25.00",bg = "white").grid(row = 16,column = 0)
    label10 = tk.Label(registerWindow,text = "119   \t   \tOTC   \t\t    Burnex                 RS 30.00",bg = "white").grid(row = 17,column = 0)
    label11 = tk.Label(registerWindow,text = "120   \t   \tOTC   \t\t    Calpol                 RS 15.00",bg = "white").grid(row = 18,column = 0)
    confirmButton = tk.Button(registerWindow ,text="Confirm Order",bg = "white",fg = "black",padx = 20,pady=20,command = lambda: pack(registerWindow,idEntry,nameEntry,phNumberEntry,medicineEntry,quantityEntry,priceEntry)).grid(row=20,column=1)
                                                                                                                             
    registerWindow.mainloop()
def viewAll():
    dict = shelve.open("medicine")
    viewAllWindow = tk.Toplevel()
    viewAllWindow.configure(bg = "white")
    headerLabel = tk.Label(viewAllWindow,text = "Customer ID:   \t\tCustomer Name:    \t\tPhone No.   \t\tMedcine ID:   \t\tMedicine Name:   \t\tQuantity:  \t\tTotalPrice: ",bg = "white",fg = "black",padx = 5,pady = 5).grid(row = 0,column = 0)
    if len(dict) != 0:
        i = 2
        for key in dict.keys():
            record = dict[key]
            recordsLabel = tk.Label(viewAllWindow,text = record[0]+"\t\t"+record[1]+"\t\t"+record[2]+"\t\t"+record[3]+"\t\t"+record[4]+"\t\t"+record[5]+"\t\t"+record[6],bg = "white",fg = "black",padx = 5,pady = 5).grid(row = i,column = 0)
            i+=1
    else:
        recordsLabel = tk.Label(viewAllWindow,text = "No Records Exists",bg = "white",fg = "black",font = 50,padx = 5,pady = 5).grid(row = 3,column = 0)
    dict.close()
    viewAllWindow.mainloop()
def update():
    rec = ""
    fp = open("medfile.txt","w")
    dict = shelve.open("medicine")
    for key in dict:
        record = dict[key]
        rec = "|".join(record)
        fp.write(rec+"\n")
    dict.close()
    fp.close()
def modifyAndDelete():
    modifyWindow = tk.Toplevel()
    modifyWindow.title("PHARMACY MANAGEMENT SYSTEM")
    modifyWindow.geometry("550x500")
    modifyWindow.configure(bg = "white")
    idLabel = tk.Label(modifyWindow,text = "Enter the Customer ID to modify:",bg = "white",padx = 5,pady=5).grid(row = 2,column = 0,sticky = "W")
    idEntry = tk.Entry(modifyWindow,width = 20)
    idEntry.grid(row = 2,column = 1)
    modifyButton = tk.Button(modifyWindow,text="Modify",padx = 5,pady = 10,width = 10, bg = "white",fg = "black", command = lambda : modify(idEntry,modifyWindow)).grid(sticky = "W",row = 3,column = 2)

def modify(idEntry,modifyWindow):
    dict = shelve.open("medicine")
    number = idEntry.get()
    if number in dict:
        del dict[number]
        update()
        register()
    else:
        errorLabel = tk.Label(modifyWindow,text = "Customer ID doesn't exsit!Please try again.",font = 50).grid(row = 13,column = 0)
    dict.close()

def generateBill(price,userWindow):
    generateBillWindow = tk.Toplevel()
    generateBillWindow.title("PHARMACY MANAGEMENT SYSTEM")
    generateBillWindow.geometry("500x500")
    generateBillWindow.configure(bg = "white")
    gstLevied = "18%"
    costWithoutGST = price
    amountPayable = (price + (gstLeived/100))
    titleLabel = tk.Label(generateBillWindow,text ="BILL"+gstLevied,bg = "white",fg = "black",padx = 5,pady=5,width = 30,font = 65).grid(row = 10,column = 3,sticky = "W")                                                                                                                         
    costWithoutGSTLabel = tk.Label(generateBillWindow,text ="Cost Without GST="+costWithoutGST,bg = "white",fg = "black",padx = 5,pady=5,width = 30,font = 50).grid(row = 12,column = 0,sticky = "W")
    gstLeviedLabel = tk.Label(generateBillWindow,text ="GST(Updated Value)="+gstLevied,bg = "white",fg = "black",padx = 5,pady=5,width = 30,font = 50).grid(row = 13,column = 0,sticky = "W")
    amountPayableLabel = tk.Label(generateBillWindow,text ="Amount Payable="+amountPayable,bg = "white",fg = "black",padx = 5,pady=5,width = 30,font = 50).grid(row = 14,column = 0,sticky = "W")

def getData():
    getWindow = tk.Toplevel()
    getWindow.title("PHARMACY MANAGEMENT SYSTEM")
    getWindow.geometry("600x500")
    getWindow.configure(bg = "white")
    dict = shelve.open("medicine")
    idLabel = tk.Label(getWindow,text = "Enter the Customer ID to search:",bg = "white",padx = 5,pady=5).grid(row = 2,column = 0,sticky = "W")
    idEntry = tk.Entry(getWindow,width = 20)
    idEntry.grid(row = 2,column = 1)
    searchButton = tk.Button(getWindow,text="Search",padx = 15,pady = 10,width = 20,bg = "white",fg = "black",command = lambda: search(idEntry,getWindow)).grid(sticky = "W",row = 2,column = 2)

def search(idEntry,getWindow) :
    dict = shelve.open("medicine")
    number = idEntry.get()
    if number in dict :
        record = dict[number]
        idLabel = tk.Label(getWindow,text = "Customer ID:",bg = "white",font = 50,padx = 5,pady=5).grid(row = 3,column = 0,sticky = "W")
        idOutputLabel = tk.Label(getWindow,text = record[0],bg = "white",font = 50,padx = 5,pady=5).grid(row = 3,column = 1,sticky = "W")
        nameLabel = tk.Label(getWindow,text = "Customer Name:",bg = "white",font = 50,padx = 5,pady=5).grid(row = 4,column = 0,sticky = "W")
        nameOutputLabel = tk.Label(getWindow,text = record[1],bg = "white",font = 50,padx = 5,pady=5).grid(row = 4,column = 1,sticky = "W")
        phNumberLabel = tk.Label(getWindow,text = "Phone Number:",bg = "white",font = 50,padx = 5,pady=5).grid(row = 5,column = 0,sticky = "W")
        phNumberOutputLabel = tk.Label(getWindow,text = record[2],bg = "white",font = 50,padx = 5,pady=5).grid(row = 5,column = 1,sticky = "W")
        medicineLabel = tk.Label(getWindow,text = "medicine ID:",bg = "white",font = 50,padx = 5,pady=5).grid(row = 6,column = 0,sticky = "W")
        medicineOutputLabel = tk.Label(getWindow,text = record[3],bg = "white",font = 50,padx = 5,pady=5).grid(row = 6,column = 1,sticky = "W")
        medNameLabel = tk.Label(getWindow,text = "medicine Name:"+record[4],bg = "white",font = 50,padx = 5,pady=5).grid(row = 7,column = 1,sticky = "W")
        quantityLabel = tk.Label(getWindow,text = "Quantity:",bg = "white",font = 50,padx = 5,pady=5).grid(row = 8,column = 0,sticky = "W")
        quantityOutputLabel = tk.Label(getWindow,text = record[5],bg = "white",font = 50,padx = 5,pady=5).grid(row = 8,column = 1,sticky = "W")
        priceLabel = tk.Label(getWindow,text = "Total Price:",bg = "white",font = 50,padx = 5,pady=5).grid(row = 9,column = 0,sticky = "W")
        priceOutputLabel = tk.Label(getWindow,text = record[6],bg = "white",font = 50,padx = 5,pady=5).grid(row = 9,column = 1,sticky = "W")
    else:
        errorLabel = tk.Label(getWindow,text = "Customer ID doesn't exist!Please try again.",bg = "white",font = 50).grid(row = 13,column = 0)
    dict.close()

def user():
    userWindow = tk.Toplevel()
    userWindow.title("PHARMACY MANAGEMENT SYSTEM")
    userWindow.geometry("500x500")
    userWindow.configure(bg = "white")
    idLabel = tk.Label(userWindow,text = "Enter Customer ID:",bg = "white").grid(row = 0,column = 0)
    idEntry = tk.Entry(userWindow,width = 20)
    idEntry.grid(row = 0,column = 1)
    submitButton = tk.Button(userWindow,text = "Submit",bg = "white",fg = "black",padx = 5,pady=5,command = lambda: generateBill(idLabel,userWindow)).grid(row = 0,column = 2)
    
    userWindow.mainloop()

def pack(registerWindow,idEntry,nameEntry,phNumberEntry,medicineEntry,quantityEntry,priceEntry):
    dict = shelve.open("medicine")
    record = []
    number = int(medicineEntry.get())
    print(number, type(number))
    if number == 111:
        medName = "Probiotics"
    elif number == 112:
        medName = "Vitamin C(500mg)"
    elif number == 113:
        medName = "Acid Free C(500mg)"
    elif number == 114:
        medName = "Women'S Multivate"
    elif number == 115:
        medName = "Marino Tablet"
    elif number == 116:
        medName = "Crocin"
    elif number == 117:
        medName = "Maxi Cal Tablet"
    elif number == 118:
        medName = "Dolo 350"
    elif number == 119:
        medName = "Burnex"
    elif number == 120:
        medName = "Calpol"
    else :
        medName = "error"
        
    Cid = idEntry.get()
    name = nameEntry.get()
    phNumber = phNumberEntry.get()
    medid = medicineEntry.get()
    quantity = quantityEntry.get()
    price = priceEntry.get()
    print(Cid, " ", name, " ", phNumber, " ", medid, " " ,quantity, " ", price)
    if len(Cid)!=0 and len(medid)!=0 and len(name)!=0 and len(quantity)!=0 and len(price)!=0:
        if phNumber.isnumeric() and len(phNumber) == 10:
        
            # record.append(medName)
            # record.insert(1,Cid)
            # record.insert(2,name)
            # record.insert(3,phNumber)
            # record.insert(4,medid)
            # record.insert(5,quantity)
            # record.insert(6,price)

            record.append(Cid)
            record.append(name)
            record.append(phNumber)
            record.append(medid)
            record.append(medName)
            record.append(quantity)
            record.append(price)

            key = Cid
            if str(key) not in dict:
                dict[str(key)] = record
                registerWindow.destroy()
                update()
            else:
                registerWindow.destroy()
                register()
        else:
            registerWindow.destroy()
            register()
    else:
        registerWindow.destroy()
        register()
    dict.close()
welcomeLabel = tk.Label(text = "PHARMACY MANAGEMENT SYSTEM",font = 50,bg = "white",fg = "black").pack()
buttonFrame = tk.Frame().pack()
orderButton = tk.Button(buttonFrame,text="NEW ORDER",padx = 30,pady = 10,width = 50,bg = "white",fg = "black",command = register).pack(side = "top")
updateButton = tk.Button(buttonFrame,text="MODIFY YOUR ORDER",padx = 30,pady = 10,width = 50,bg = "white",fg = "black",command = modifyAndDelete).pack(side = "top")
searchButton = tk.Button(buttonFrame,text="SEARCH YOUR ORDER",padx = 30,pady = 10,width = 50,bg = "white",fg = "black",command = getData).pack(side = "top")
billButton = tk.Button(buttonFrame,text="GENERATE BILL",padx = 30,pady = 10,width = 50, bg = "white",fg = "black",command = user).pack(side = "top")
viewButton = tk.Button(buttonFrame,text="VIEW ALL RECORDS",padx = 30,pady = 10,width = 50, bg = "white",fg = "black",command = viewAll).pack(side = "top")
top.mainloop()
