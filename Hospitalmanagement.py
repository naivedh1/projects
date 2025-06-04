import datetime as dt
import random as rd

class Hospital:

    a = dt.datetime.now()
    
    doctors = {"Amit Gupta": 45, "Hitesh Sharma": 74, "Deepak Khandelwal": 38, "Rajesh Mehta": 60, "Gunjan Agarwal":59}
    nurses = {"Nurse 1": 234, "Nurse 2" : 355, "Nurse 3": 123, "Nurse 4": 789, "Nurse 5": 602}
    wardboys = {"Wardboy 1" : 324,"Wardboy2": 687, "Wardboy 3" : 169, "Wardboy 4" : 902, "Wardboy 5" : 290}

    Rooms = {100 : True, 101 : True, 102 : True, 103 : True, 104 : True, 105 : True, 106 : True, 107 : True }
    
    
    def __init__(self,TokenAmount,Finalamount):
        self.Fees = TokenAmount
        self.total = Finalamount

    
    def admitform(self):
        print("Please fill this Admit Form \n")
        Patient_name = input("Please Enter Name = ")
        Age = int(input("Enter Age = "))
        Gender = input("Enter Gender = ")
        Contact_info = int(input("Enter Mobile No = "))
        Date_time = self.a.strftime("Date = %d/%m/%Y Time = %H:%M:%S")
        file = open("Hospital Register.txt","a")
        file = file.write(f"\n Patient Name = {Patient_name}, Age = {Age}, Gender = {Gender}, Contact = {Contact_info}, {Date_time}")
        
        return Age,Patient_name,Gender,Contact_info
    

    def admitprocess(self):
        b = rd.choice(list(self.Rooms.keys()))  
        c = rd.choice(list(self.doctors.keys()))
        d = rd.choice(list(self.nurses.keys()))
        e = rd.choice(list(self.wardboys.keys()))

                
        file = open("Hospital Register.txt","a")
        file = file.write(f"\n Admitted Under Dr.{c} in Room Number {b} with Nurse = {d} and Wardboy = {e}")
        
        if (b in self.Rooms):
            print(f"You have been assigned Dr.{c} in Room Number {b} with Nurse = {d} and Wardboy = {e}") 
            if True :
                self.Rooms[b] = False
                print(f"Room {b} is now occupied \n")
        return b
     
    def admitrestriction(self,Age):
        compulsory_payment = 0    
        if (Age > 17 and Age< 60):
            payment = int(input(f"Please pay {self.Fees} = "))
        elif(Age < 18):
            print("The Hospital waivers off 20% Discount for Children")
            compulsory_payment = self.Fees - self.Fees/5
            payment = int(input(f"Please pay {compulsory_payment} = ")) 
        else:
            print("The Hospital waivers off 50% Discount to Senior Citizens")
            compulsory_payment = self.Fees - self.Fees/2
            payment = int(input(f"Please pay {compulsory_payment} = ")) 
        
        if(payment >= compulsory_payment):
            print("PAYMENT SUCCESFUL !! \n")
            self.admitprocess()
            print(f"The Remaining Rs {self.total} is to be paid before Discharging \n")

        else:
            print(f"Rs {compulsory_payment} is compulsory")
            self.admitrestriction(Age)
        return compulsory_payment
    

    def dischargeform(self,Age,Patient_name,Gender,Contact_info,t):
        dnt = dt.datetime.now()
        Date_time1 = dnt.strftime("Date = %d/%m/%Y Time = %H:%M:%S")

        print(f"Patient name = {Patient_name} \nAge = {Age} \nGender = {Gender} \nContact Info = {Contact_info} \n")
        print (f"THE PAYMENT RECEIPT \nTotal Amount Paid to The Hospital = {t} \n")
        file1 = open("Discharge Register.txt","a")
        file1 = file1.write(f"Patient name = {Patient_name}, Age = {Age}, Gender = {Gender}, Contact Info = {Contact_info}, FEES PAID = {t}, {Date_time1}")




    def payment_completion(self,Age,payment,Patient_name,Gender,Contact_info):
        
        print(f"Before recieving the Discharge Sheet, {self.total} amount is due")
        total_payment = int(input("Please clear the Dues = "))
        t = payment + total_payment

        if(total_payment == self.total):
            
            print("Here is your DISCHARGE SHEET along with the PAYMENT RECEIPT \n")
            self.dischargeform(Age,Patient_name,Gender,Contact_info,t)
            print("WE, THE OXYGEN FAMILY, ARE READY AT YOUR SERVICE ANYTIME!! ")

        elif(total_payment> self.total):
            print(f"Here is your Remaining change of Rs {total_payment-self.total}")
            self.dischargeform(Age,Patient_name,Gender,Contact_info,t)
            print("WE, THE OXYGEN FAMILY, ARE READY AT YOUR SERVICE ANYTIME!! ")


        else:
            print(f"Clearing the Due of Rs {self.total} is COMPULSORY")
            self.payment_completion(Age,Patient_name,Gender,Contact_info,t)
        
       
        
    def run(self):
        
        Age, Patient_name, Gender, Contact_info = self.admitform()
        compulsory_payment = self.admitrestriction(Age)
        self.payment_completion(Age, compulsory_payment, Patient_name, Gender, Contact_info)

    
obj = Hospital(2000,10000)
# obj.run()

class Emergency(Hospital):

    def __init__(self,emergency):
        self.emergency_payment = emergency
        
        
    def e_payment(self, Age, Patient_name, Gender, Contact_info):
        pay = int(input(f"WE HAVE ADMITTED THE PATIENT IN THE EMERGENCY WARD \n Please clear the payment of Rs{self.emergency_payment} = "))
        if (pay == self.emergency_payment):
            print("PAYMENT SUCCESSFUL")
            self.dischargeform(Age, Patient_name, Gender, Contact_info,self.emergency_payment)
        elif(pay > self.emergency_payment):
            print(f"Here is Your Remaining change of Rs {pay - self.emergency_payment}")
            self.dischargeform(Age, Patient_name, Gender, Contact_info,self.emergency_payment)

        else:
            print(f"Payment of Rs {self.emergency_payment} is Compulsory")
            self.e_payment()
        return Age, Patient_name, Gender, Contact_info,self.emergency_payment

    def dischargeform(self, Age, Patient_name, Gender, Contact_info, emergency_payment):
        return super().dischargeform(Age, Patient_name, Gender, Contact_info, emergency_payment)
    
    def run_emergency(self):
        self.admitprocess()
        age, patientname, g, contactinfo = self.admitform()
        self.e_payment(age, patientname, g, contactinfo)

obj1 = Emergency(12000)
# obj1.run_emergency()

def task_manager():
    print("******** THE OXYGEN HOSPITAL AT YOUR SERVICE ******** \n")
    task = int(input("1 for EMERGENCY SERVICES \n2 for REGULAR CHECKUPS AND ADMITS \n3 to EXIT THE HOSPITAL \nINPUT = "))
    if(task==1):
        obj1.run_emergency()

    elif(task==2):
        obj.run()

    elif(task==3):
        print("WE THE OXYGEN FAMILY ARE READY AT YOUR SERVICE ANYTIME")

task_manager()
