
def Operation():
    #-----Menu code-----
    list1=[]
    
    
    def inner_operation():
        print("\n")
        print("*"*15,"Menu lists","*"*15)
        print("Insert: 1 \nUpdate: 2 \nDelete: 3 \nExit : 4")
        option=int(input("Please give me any input data: "))

        #--Insert data
        print("\n \n")
        if(1==option):
            print("-"*10,"insert data","-"*10)
            data=int(input("how manay data you want to insert: "))
            for item in range(data):
                get_data=input("please input string data: ")
                list1.append(get_data)
            print("success full insert data...!","\n",list1)
            inner_operation()
           
        #--Updata data
        elif(2==option):
            print("-"*10,'updata data',"-"*10)
            print("if you want to updata data: ")
            ind=int(input("Please input index: "))
            val=input("enter string values: ")
            list1.insert(ind,val)
            print("update data:\n",list1)
            inner_operation()
        
        #--Delete data
        
        elif(3==option):
            print("-"*10,'Delete data',"-"*10)
            ind1=int(input("enter index no you want to delete data: "))
            list1.pop(ind1)
            print("sucess full delete data...!","\n",list1)
            inner_operation()

        #--Exit
        elif(4==option):
            print("sucess full exit...!")

        else:
            print("Please Enete valid input: ")
            inner_operation()

    inner_operation()
          
Operation()

#QA
#-create dynamic list

    

    
































