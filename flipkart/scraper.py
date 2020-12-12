import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL='https://www.flipkart.com/moto-g8-plus-cosmic-blue-64-gb/p/itm1b6ec61647f7a'
TPRICE=13200

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'}

def checkprice():
    page=requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')

    tittle = soup.find(class_='_35KyD6').get_text()
    price = float(soup.find(class_='_1vC4OE _3qQ9m1').get_text()[1:].replace(',',''))

    #check the targeted price
    if(price<TPRICE):
        send_mail()

def send_mail():
    #start server
    server=smtplib.SMTP('host_name',587)
    server.ehlo()
    server.starttls() #encryption our connection
    server.ehlo()
    server.login('username','password')

    #email message
    subject='Hurry! price fell down'
    body='Check the link'.URL
    msg=f"Subject: {subject}\n\n\n{body}"

    server.sendmail(
        'from email',
        'to email',
        msg
    )

    print("Mail sent")

    #close the connection
    server.quit()
while True:
    print("Checking...")
    checkprice()
    time.sleep(3600)

