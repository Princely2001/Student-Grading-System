#create variable and dictonary
stud_dic={}
option=0
#Define Functions
def range_fun(credits_pass,credits_defer,credits_fail):
     credits_total=credits_pass+credits_defer+credits_fail
     if credits_pass not in range(0,121,20):
         print("Out of range")
     elif credits_defer not in range(0,121,20):
         print("Out of range")
     elif credits_fail not in range(0,121,20):
         print("Out of range")
     elif credits_total!=120:
         print("Total incorrect")

def pro_fun(credits_pass,credits_defer,credits_fail):
     if credits_pass==120 and credits_defer==0 and credits_fail==0:
         print("Progress")
         stud_dic[stud_id] = "Progress"+":"+str(credits_pass)+","+str(credits_defer)+","+str(credits_fail)
         print("Thank you")
         
         
def pro_mfun(credits_pass,credits_defer,credits_fail):
     if credits_pass==100 and credits_defer==20 and credits_fail==0 or credits_pass==100 and credits_defer==0 and credits_fail==20:
         print("Progress (module trailer)")
         stud_dic[stud_id] = "Do not progress – module retriever"+":"+str(credits_pass)+","+str(credits_defer)+","+str(credits_fail)
         print("Thank you")
         
         
def Ex_fun(credits_pass,credits_defer,credits_fail):
     if credits_pass in range(0,41,20) and credits_defer in range(0,41,20) and credits_fail in range(80,121,20):
         print("Exclude")
         stud_dic[stud_id] = "Exclude"+","+str(credits_pass)+":"+str(credits_defer)+","+str(credits_fail)
         print("Thank you")
         
         
def ret_fun(credits_pass,credits_defer,credits_fail):
     if credits_pass in range(0,81,20) and credits_defer in range(0,121,20) and credits_fail in range(0,81,20):
         print("Do not progress – module retriever")
         stud_dic[stud_id] = "Do not progress – module retriever"+":"+str(credits_pass)+","+str(credits_defer)+","+str(credits_fail)
         print("\n")
         print("Thank you")
         
#start infinite loop         
while True:
    #preferred option input ask from user 
    option = input("If you want to enter another set of data enter Y else enter N:")
    if option == "Y":
        #start infinite loop
        while True:
            #student id,credits pass,credits defer,credits_fail inputs ask from user
            stud_id = str(input("Please enter your student id:"))
            credits_pass=int(input("Please enter your credits at pass:"))
            credits_defer=int(input("Please enter your credit at defer:"))
            credits_fail=int(input("Please enter your credit at defer:"))
            credits_total=credits_pass+credits_defer+credits_fail
            range_fun(credits_pass,credits_defer,credits_fail)
            pro_fun(credits_pass,credits_defer,credits_fail)
            pro_mfun(credits_pass,credits_defer,credits_fail)
            ret_fun(credits_pass,credits_defer,credits_fail)
            Ex_fun(credits_pass,credits_defer,credits_fail)
            break
            
            
    
    elif option == "N":
        #output dictonary keys with values
        for k,v in stud_dic.items():
             print(k,v)
             
    else:
        print("Invalid input try again")
   
       
