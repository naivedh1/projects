import datetime
import random

class Hospital:

    a=datetime.datetime.now()
    def __init__(self,Addmissionfees,Dischargefees):
     self.fees=Addmissionfees
     self.final=Dischargefees

    def admit(self):
        print("Please fill the addmission form =")
        Name=input("Enter Your Name =")
        Age=input("Enter Your Age =")
        Gender=input("Enter Your Gender =")
        Disease=input("Enter Your Disease =")
        Contact_Information=int(input("Enter Your Mobile Number="))
        # ADMIT_FEES=ADMIT_FEES<=1000

        return Name,Age,Gender,Contact_Information
    
    def admitrestriction(self,a):
        a = "Age"
        compulsory_payment = 1000    
        if (a > 17 and a< 60):
            payment = int(input(f"Please pay {self.fees} = "))
        elif(a < 18):
            compulsory_payment = self.Fees - self.Fees/5
            payment = int(input(f"Please pay {compulsory_payment} = ")) 
        else:
            compulsory_payment = self.Fees - self.Fees/2
            payment = int(input(f"Please pay {compulsory_payment} = ")) 
        
        if(payment>= compulsory_payment):
            print("PAYMENT SUCCESFUL !! \n")
            self.admitprocess()
            print(f"The Remaining Rs {self.total} is to be paid before Discharging \n")

        else:
            print(f"Rs {compulsory_payment} is compulsory")
            self.admitrestriction(a)
        return compulsory_payment
    
    def discharge(self,Name,Age,Gender,Contact_Information,ToPay):
     a=datetime.datetime.now

     print(f"Patient name = {Name} \nAge = {Age} \nGender = {Gender} \nContact Info = {Contact_Information} \n")
     print (f"THE PAYMENT RECEIPT \nTotal Amount Paid to The Hospital = {ToPay} \n")


    def Payment(self,Name,Age,Gender,Contact_Information,ToPay,payment) :
       print(f"Before Discharge,{self.Total}Amount Is Due ")
       total_payment = int(input("Please clear the Dues = "))
       ToPay= payment + total_payment
       if(total_payment == self.total):
            
            print("Here is your DISCHARGE SHEET along with the PAYMENT RECEIPT \n")
            self.dischargeform(Age,Name,Gender,Contact_Information,ToPay)
            print("WE, THE OXYGEN FAMILY, ARE READY AT YOUR SERVICE ANYTIME!! ")

       elif(total_payment> self.total):
            print(f"Here is your Remaining change of Rs {total_payment-self.total}")
            self.dischargeform(Age,Name,Gender,Contact_Information,ToPay)
            print("WE, THE OXYGEN FAMILY, ARE READY AT YOUR SERVICE ANYTIME!! ")


       else:
            print(f"Clearing the Due of Rs {self.total} is COMPULSORY")
            self.payment_completion(Age,Name,Gender,Contact_Information,ToPay)
        
        
    def run(self):
        
        Age, Name, Gender, Contact_Information = self.admit()
        # compulsory_payment = self.admitrestriction(Age)
        # self.payment_completion(Age, Name, Gender, Contact_Information)


obj=Hospital(1000,100000)
# obj.admit()
# obj.admitrestriction(18)
# obj.discharge(Name="NONU",Age=21,Gender="M",Contact_Information=1234567899)
obj.run()