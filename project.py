import smtplib
from email.message import EmailMessage
import serial, time

def SendEmail():
    Sender_Email = "anshumanchitkara123@gmail.com"
    Reciever_Email = "anshuman3024.be20@chitkara.edu.in"
    Password = "anshu789"

    newMessage = EmailMessage()                         
    newMessage['Subject'] = "Emergency Message From Home" 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email
    newMessage.set_content('InValid Person Trying To Access The Security System')
                           
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)
        
        
def SerialCommRead():
    global ser
    if ser.in_waiting>0:
        Val=ser.readline().decode("ascii").rstrip()
        return Val
    
    
ser=serial.Serial('/dev/ttyACM0',9600)
ser.flush()

Flag=1
while True:
    Val=SerialCommRead()
    print(Val)
    if Val=="N":
        print("Invalid Person")
        if Flag==1:
            SendEmail()
            print("Email Sent")
            Flag=2
    elif Val=="Y":
        Flag=1
        print("Valid Person")
        
    time.sleep(1)
