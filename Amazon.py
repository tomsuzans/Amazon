import requests
from bs4 import BeautifulSoup
import smtplib
import time
# pip install requests bs4

URL = 'https://www.amazon.com/ToolKit-15-PCS-Lock-Set/dp/B082K9S9BP/ref=sr_1_2?crid=1ZX9V5G63XQDK&dchild=1&keywords=lock+pick+set&qid=1586439035&sprefix=lock%2Caps%2C222&sr=8-2'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:2])
    if converted_price < 50:
        send_mail()
    print(converted_price)
    print('Price checked')


def send_mail():
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.ehlo()
   server.starttls()
   server.ehlo()
   server.login('divemaster.lv@gmail.com', 'phlseduqqawshrdn')
   subject = 'Price fell down! '
   body = 'Check the link https://www.amazon.com/ToolKit-15-PCS-Lock-Set/dp/B082K9S9BP/ref=sr_1_2?crid=1ZX9V5G63XQDK&dchild=1&keywords=lock+pick+set&qid=1586439035&sprefix=lock%2Caps%2C222&sr=8-2'
   msg = f"Subject: {subject}\n\n{body}"
   server.sendmail('divemaster.lv@gmail.com', 'kristowsky@inbox.lv', msg)
   print('e-mail has been sent')
   server.quit()


# Try:
while True:
    check_price()
    time.sleep(25)

#    except TypeError:
#        check_price()
#    except AttributeError:
#        check_price()
