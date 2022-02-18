def outer_fun():
    #create dictionary
    dict1={}
    
    def inner_fun():
        #--Menu list
        print("*"*20,"Menu List","*"*20)
        print("Insert     : 1\nUpdate     : 2\nDelete     : 3\nExit       : 4\nAll record : 5")
        choice=int(input("Please enter valid input data: "))
        print("\n")

        #--Insert data in the database
        if(1==choice):
            print("-"*15,"Insert data","-"*15)
            no_of_data=int(input("enter no of data you want to insert: "))
            for item in range(no_of_data):
                Id=int(input("please enter your id: "))
                Name=input("please enter your name: ")
                Age=int(input("Please enter your age: "))
                dict1={"id":Id,"name":Name,"age":Age}
                
            print("success full insert data...!")
            print("Id \t  Name  \t age")
            for val in dict1.values():
                print(val,"\t",end=" ")
            print("\n")
            inner_fun()


        #Updata data
        elif(2==choice):
            print("-"*15,"Update data","-"*15)
            key_u=int(input("Enter key you want to update: "))
            if(key_u in dict1):
                val_u=input("pleases insert values: ")
                dict1[key_u]=val_u
                print("success full upadate...!")
                print(key_u,"\t",val_u)
                print("\n")

            else:  
                print("\nPlease Enter Valide key")
                
            inner_fun()

        #Delete data
        elif(3==choice):
            try:
                print("-"*15,"Delete data","-"*15)
                del_d=int(input("Please Enter key you want to delete record: "))
                print(dict1.pop(del_d))
                print("sucess full delete data...!")
                print("\n")
                inner_fun()
            except KeyError:
                print("\nRecord are Empty or Key is not Avilable...?")
                inner_fun()

        
        #Exite
        elif(4==choice):
            print("sucees full Exit...!")
            print("\n")

        elif(5==choice):
            print("-"*15,"Display all Reocord","-"*15)
            print("id\tName")
            for i,j in dict1.items():
                print(i,"\t",j)
            inner_fun()
                 
            
    inner_fun()    
    
outer_fun()


    


































