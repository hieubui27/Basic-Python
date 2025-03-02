time = int(input( "Enter hours worked: "))
rate = int(input("Enter hourly rate: "))

if(time<=40):
    pay=time*rate
 
else:
    pay =(40*rate)+(time-40)*(3/2)*rate

print("Pay: ",pay)
 
