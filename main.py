from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

URL = "https://www.amazon.in/Titan-Analog-Blue-Dial-Watch-1769SM01/dp/B0792KQMC5/ref=sr_1_43_mod_primary_new?crid=32J1VBISPQC0K&keywords=titan+watches+for+men&qid=1675522061&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=titan+%2Caps%2C816&sr=8-43"
ACCEPT_LANGUAGE = "en-GB,en;q=0.9,bn-IN;q=0.8,bn;q=0.7,el-GR;q=0.6,el;q=0.5,en-US;q=0.4"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
headers = {'Accept-Language': ACCEPT_LANGUAGE, 'User-Agent': USER_AGENT}
response = requests.get(URL, headers=headers)
website_html = response.text
# print(website_html)
soup = BeautifulSoup(website_html, "lxml")
price = soup.find(class_="a-price-whole").getText()
price_without_dot = price.split(".")[0]
price_without_comma = price_without_dot.split(",")
price_concat = price_without_comma[0] + price_without_comma[1]
price_int = int(price_concat)
title = soup.find(class_="a-size-large product-title-word-break").getText()
print(title)
print(price_int)

BUY_PRICE = 2000

if price_int < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("soutrikroy1382002@gmail.com", "ulvpykpydczbwqvm")
        connection.sendmail(
                            from_addr="soutrikroy1382002@gmail.com",
                            to_addrs="soutrikroy1382002@gmail.com",
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )



