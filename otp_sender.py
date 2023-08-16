import smtplib
import random
def otp_sender(user_id):
     s= smtplib.SMTP('smtp.gmail.com', 587)
     s.starttls()
     s.login('group4@apsjorhat.org', 'apsj#12345678')
     otp= random.randint(111111,999999)
     message= str(otp)
     s.sendmail("group4@apsjorhat.org",user_id,message)
     s.quit()
     print("Enter the otp: ")
     val= int(input())
     if val==otp:
         print("Verifing the OTP...")
         print("Login successful...")

     else:
         print("Incorrect OTP...")
