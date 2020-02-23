import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.ae/Black-Decker-VM1200-B5-Bagged-Cleaner/dp/B071WM22H7/ref=sr_1_3?keywords=vaccum&qid=1582471174&sr=8-3'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}



def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price_raw = soup.find(id="priceblock_ourprice").get_text()
    price = float(price_raw[3:])

    if (price < 200.0):
        send_mail()   


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('hamad.altamimi97@gmail.com', 'dvqhoxxfjkyxqkiy')


    msg = 'The Vacum price is lower Now !!, Check the price of the vacum price is lower now https://www.amazon.ae/Black-Decker-VM1200-B5-Bagged-Cleaner/dp/B071WM22H7/ref=sr_1_3?keywords=vaccum&qid=1582471174&sr=8-3'

    server.sendmail(
        'hamad.altamimi97@gmail.com',
        'hamad-altamimi@live.com', msg
    )

    print('The Massage has been sent !!!')

    server.quit()

check_price()    

   





