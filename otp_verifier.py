import random
import smtplib

server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login('mmkg0504@gmail.com',password="aftn eumt mxvo uyei")
otp=''.join([str(random.randint(0,9))for i in range(6)])
msg='Hello, Your OTP is '+str(otp)
server.sendmail('mmkg0504@gmail.com','mmkgandhi5@gmail.com',msg)
server.quit()
otp1=input('Enter your otp')
if(otp1==otp):
    print('OTP verification succesful')
else:
    print('Please enter CORRECT otp')
