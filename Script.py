## ASU Racing Team IT Department
## Automated E-mail Sender 
## Created 24/9/2016
## Use Python shell
## "NOTE THIS PROGRAM SENDS ONLY EMAILS FROM GMAIL" argument1->TextFile  argument2->E-mail
##//  python Script.py emails.txt example@gmail.com  // and then enter 

####NOTE "USE THE RIGHT FORMAT FOR THE E-MAILS SHEET"
##E-mailAddress
##recipantName

import getpass
import sys
import re
import os
import smtplib  ##liberary that will be used to send mails to internet machines 
from smtplib import SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#E-mail address used for sending mails, ##'WILL BE SEEN BY THE RECIPANT' 
fromAddress = sys.argv[2]                   ##Enter a sender MAIL ADDRESS as a SECOND ARGUMENT 
toAddress = 'example@gmail.com'           #E-mail address of the recipant, the example mail will be replaced by different addresses from the mailes file  
username = fromAddress                      #User name used for logging to the Gmail server
password = getpass.getpass('Password:')     #The password related to the username
massage = ' '                               #massage will be sent by the system and will be modefied for each recipant 


##A function sets up the protocole object and sends e-mailes to the server
def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com:587')        #Using Gmail
    server.ehlo()                                      #Our System's object and the server shaking hand 
    server.starttls()                                  #Something to do with encryption 
    server.login(username,password)                    #Logging to the server
    server.sendmail(fromAddress, toAddress, massage)   #Sending e-mail using the information above 
    server.quit()                                      #Stop Communication with the server

try:
    fileName = sys.argv[1]                                      #ENTER the file With the right format as a FIRST ARGUMENT
    emailFile = open(fileName,'r')                             #Creating a file object related to the Emails File
    print "The file :","'",emailFile.name,"'"," is opened"     ####NOTE "USE THE RIGHT FORMAT FOR THE E-MAILS SHEET"  
except:
    print "error can't open the file"
    sys.exit("Error")


try:
    lines = re.split('\n',emailFile.read())                    #Read the file content and split it line by line and put it in a List
    print lines
    emailFile.close()                                          #Close the file
    print "Number of E-mails will be sent: ",str(len(lines)/2)
except:
    print "error can't read from file"
    sys.exit("Error")


try:
    x = 0   #for itteration throw the lines List
    i = 1   #ignore it useless for interface, nothing to do with logic
    numberOfLines = len(lines)
    ##Loop throw each line
    while x < numberOfLines:                                   
        toAddress = lines[x]       #get the e-mail address from the sheet 
        recipantName = lines[x+1]  #get the name related to the e-mail address from the sheet
        
        #START Creating a massage to send
        msg = MIMEMultipart('alternative')      #Choose alternative for the mail extension to mix between html and text
        msg['Subject'] = 'AutoMatedMailSender'  #Set the Subject this method will set it automaticaly to the header
        msg['From'] = 'IT Department ASURT'     #The From attribute will show in the lable of the E-mail
        msg['To'] = toAddress                   #The To attribute will appear to the recipant
        
        #Creating the TEXT and the HTML part of the massage
        text = "Hi this is an Automated mail from ASURT send to %s"%recipantName                   
        html = """                                                                    
        <html>
          <head></head>
          <body>
            <p>Hi! %s<br>
               This is an Automated e-mail<br>
               please don't replay 
            </p>
          </body>
        </html>
        """%(recipantName)
        #Define the type of each part
        part1 = MIMEText(text, 'plain')   
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)
        massage = msg.as_string()
        #FINISH Creating massage to send
        sendEmail()
        print "Mail(",i,")SENT SUCCSSESFULLY to:\n",toAddress,"Recipant name:",recipantName,str((i*2.0/numberOfLines)*100),'%'
        x = x +2
        i = i +1
    print "DONE 100%"
        
except smtplib.SMTPException:
   print "Error: unable to send email ,\n try Access for less secure apps \nfor GMAIL go to:\nhttps://www.google.com/settings/security/lesssecureapps"
   sys.exit("Error")
    

##NOTE THIS PROGRAM WON'T WORKE PROBERLY ON UNIX, BECAUSE THERE IS A DIFFRENCE IN THE .TXT FORMAT 

    
