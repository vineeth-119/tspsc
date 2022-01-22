from bs4 import BeautifulSoup
import requests
from datetime import datetime
from email.mime.text import MIMEText
import smtplib
def tspsc():
    data=[]
    page="https://tspsc.gov.in/notifications"
    text = requests.get(url=page).text
    soup = BeautifulSoup(text, 'html.parser')
    my_table = soup.find_all('table',{'class':'table _table-hover table-light table-striped table-responsive'})  
    for tag in my_table:
        heading = tag.tbody.find_all('tr')
        for i in heading:
            temp=i.find_all('td')
            for j in temp:
                temp1=j.find_all('a')
                for k in temp1: 
                    data.append(k.get_text())
                    #print(k.get_text())
    # print(data)
    return data
    
def sendmail():
    s=smtplib.SMTP("smtp.gmail.com",587)
    smtpu="weconnectpublicpoliceproject@gmail.com"
    smtpp="ImIronMan@2021"
    subj="\n\n\n\n\n Todays Notifications from vineeth for TSPSC \n\n\n\n\n\n"
    fromadd=smtpu
    recipients = ['vineethsharma30@gmail.com', 'sahithigundi92@gmail.com']
    data=tspsc()
    header=""
    for i in data:
        header+=i+"\n"
        header+="--------------------------------------------------------------------------------------------------------------------------------------"
    msg=MIMEText(header)
    msg['Subject']="Todays Notifications from vineeth for TSPSC"
    msg['From'] = fromadd
    msg['To'] = ", ".join(recipients)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(smtpu,smtpp)
    #header['Subject']="Todays Notifications from vineeth for TSPSC"
    s.sendmail(fromadd,recipients,msg.as_string())
    print( "mail sent")

sendmail()