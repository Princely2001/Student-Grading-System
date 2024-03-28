#Create variables and lists
pro_count=0
mod_count=0
ex_count=0
ret_count=0
list_pro=[]
list_mod=[]
list_ex=[]
list_ret=[]
i=0
#define functions

def pro_fun(credits_pass,credits_defer,credits_fail):
     if credits_pass==120 and credits_defer==0 and credits_fail==0:
         print("Progress")
         print("Thank you")
         exit()
def pro_mfun(credits_pass,credits_defer,credits_fail):
     if credits_pass==100 and credits_defer==20 and credits_fail==0 or credits_pass==100 and credits_defer==0 and credits_fail==20:
         print("Progress (module trailer)")
         print("Thank you")
         exit()
def Ex_fun(credits_pass,credits_defer,credits_fail):
     if credits_pass in range(0,41,20) and credits_defer in range(0,41,20) and credits_fail in range(80,121,20):
         print("Exclude")
         print("Thank you")
         exit()
def ret_fun(credits_pass,credits_defer,credits_fail):
     if credits_pass in range(0,81,20) and credits_defer in range(0,121,20) and credits_fail in range(0,81,20):
         print("Do not progress – module retriever")
         print("Thank you")
         exit()
#preferred option input ask from user                        
stud_staff = input("if you are student enter stud or if you are staff member enter staff:")
#start Infinite loop
while True:
    if stud_staff == "stud":
        print("Welcome student version")
        #start Infinite loop
        while True:
             print("Would you like to enter another set of data?")
             Option_check = input("Enter 'yes' for yes or 'quit' to quit and view results:")
             if Option_check == "yes":
                try:
                        #student id,credits pass,credits defer,credits_fail inputs ask from user
                        credits_pass=int(input("Please enter your credits at pass:"))
                        credits_defer=int(input("Please enter your credit at defer:"))
                        credits_fail=int(input("Please enter your credit at defer:"))
                        credits_total=credits_pass+credits_defer+credits_fail
                        if credits_pass not in range(0,121,20):
                             print("Out of range")
                        elif credits_defer not in range(0,121,20):
                             print("Out of range")
                        elif credits_fail not in range(0,121,20):
                             print("Out of range")
                        elif credits_total!=120:
                             print("Total incorrect")
                             break
                        
                        pro_fun(credits_pass,credits_defer,credits_fail)
                        pro_mfun(credits_pass,credits_defer,credits_fail)
                        Ex_fun(credits_pass,credits_defer,credits_fail)
                        ret_fun(credits_pass,credits_defer,credits_fail)
                        
                        
                except:
                        print("Integer required")
             elif Option_check == "quit":
                print("Thank you")
                exit()
             else:
                print("Invalid input try again!!!!!")
                continue
    elif stud_staff == "staff":
        print("Welcome staff version")
        print("Would you like to enter another set of data?")
        Option_check = input("Enter 'yes' for yes or 'quit' to quit and view results:")
        if Option_check == "yes":
                try:
                        #student id,credits pass,credits defer,credits_fail inputs ask from user
                        credits_pass=int(input("Please enter your credits at pass:"))
                        credits_defer=int(input("Please enter your credit at defer:"))
                        credits_fail=int(input("Please enter your credit at defer:"))
                        credits_total=credits_pass+credits_defer+credits_fail
                        if credits_pass not in range(0,121,20):
                             print("Out of range")
                        elif credits_defer not in range(0,121,20):
                             print("Out of range")
                        elif credits_fail not in range(0,121,20):
                             print("Out of range")
                        elif credits_total!=120:
                             print("Total incorrect")
                             continue
                        elif credits_pass==120 and credits_defer==0 and credits_fail==0:
                            print("Progress")
                            pro_count = pro_count + 1
                            list_pro.extend([credits_pass,credits_defer,credits_fail])
                        elif credits_pass==100 and credits_defer==20 and credits_fail==0 or credits_pass==100 and credits_defer==0 and credits_fail==20:
                            print("Progress (module trailer)")
                            mod_count = mod_count + 1
                            list_mod.extend([credits_pass,credits_defer,credits_fail])
                        elif credits_pass in range(0,41,20) and credits_defer in range(0,41,20) and credits_fail in range(80,121,20):
                            print("Exclude")
                            ex_count = ex_count + 1
                            list_ex.extend([credits_pass,credits_defer,credits_fail])
                        elif credits_pass in range(0,81,20) and credits_defer in range(0,121,20) and credits_fail in range(0,81,20):
                            print("Do not progress – module retriever")
                            ret_count = ret_count + 1
                            list_ret.extend([credits_pass,credits_defer,credits_fail])
                       
                except:
                        print("Integer required")
        elif Option_check == "quit":
                #output Histogram
                print("Histogram")
                print("Progress",pro_count,":",'*'*pro_count)
                print("Progress (module trailer)",mod_count,":", '*'*mod_count)
                print("Do not progress – module retriever", ret_count,":", '*'*ret_count)
                print("Exclude",ex_count,":",'*'*ex_count)
                full_count=pro_count+mod_count+ex_count+ret_count
                print(full_count,"outcomes in total.")
                max_count=max(pro_count,mod_count,ex_count,ret_count)
                try:
                    
                    while i<=max_count*3:
                        #output lists
                        print("Progress","","-","",list_pro[i:i+3])
                        print("Progress (module trailer)","","-","",list_mod[i:i+3])
                        print("Do not progress – module retriever","","-","",list_ret[i:i+3])
                        print("Exclude","","-","", list_ex[i:i+3])
                        print("")
                        #write studtext text file
                        file1=open('studtext.txt','a')
                        file1.write("Progress"+":"+str(list_pro[i:i+3]))
                        file1.write("Progress (module trailer)"+":"+str(list_mod[i:i+3]))
                        file1.write("Do not progress – module retriever"+":"+str(list_ret[i:i+3]))
                        file1.write("Exclude"+":"+str(list_ex[i:i+3]))
                        file1.close()
                        print("Please open studtext file and see results")
                        i=i+3
                        
                except:
                    print("Others are empty lists")
                break 
        else:
                print("Invalid input try again!!!!!")
                continue
        
                
