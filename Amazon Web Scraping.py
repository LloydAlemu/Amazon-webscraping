{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 123,
   "id": "a1f011c7-206d-435d-bc27-c1daa897a01e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup \n",
    "import requests \n",
    "import smtplib\n",
    "import time\n",
    "import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "id": "47d6c7be-9a87-49da-bfe7-b32af9631ba5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "                     Got Data Funny Business Data Analyst T-Shirt\n",
      "                    \n",
      "Price: $19.99\n"
     ]
    }
   ],
   "source": [
    "URL = ' https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_5?crid=2KY5C1Q0MLAE8&dib=eyJ2IjoiMSJ9.PM2zhQFx_lfPnddZwr05Dr8MgvuqgncumkkGSNGClexIhzJnz_UO7GIaZd1tCeojtqixplEB_myQHR6h1CXFNh-ntzT93diukU7NtGXijqqCDhcZmxRh9tcMT_ffYGkDNkjk1iOk1wmQH0v0gB8eKASI5S1G3v2Ji9AlMGmveErxWFWEYEtxs9a03oOPecDRZSz6edskmBRSTrpKm_adX66kjq_kqF2pWSzupB0WrUtHprsaLmqPs9hzjVEE_a6teQ-IwnZ4fOW24yzow-j3f4pJ_mgFTwJ-9H1omeA6RJXtN6gRy22jAmlbaTFJCmIrrrHwv8mG4XLQid6mo77IlCQrXrB9ADySHgUuA8s_qr7IT47jrHXSNo1HFbU4InQo2EVh2m9R_2U0T7u5g8t3D_nG7kWS4CV0FFILKH7bYrDBlanDGZPTFdTCjadd0EJx.pFJWEmhSlv-EHInTFDXyGtG8imrEopdyLi3pu71yuUU&dib_tag=se&keywords=data%2Banalyst%2Btshirt&qid=1738452406&sprefix=data%2Banalyst%2Btshirt%2Caps%2C154&sr=8-5'\n",
    "\n",
    "headers = { \"User-Agent\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36\"}\n",
    "\n",
    "page = requests.get(URL, headers == headers)\n",
    "\n",
    "Soup1 = BeautifulSoup(page.content, \"html.parser\")\n",
    "\n",
    "Soup2 = BeautifulSoup(Soup1.prettify(), \"html.parser\")\n",
    "\n",
    "product = Soup2.find(id='productTitle').get_text()\n",
    "\n",
    "symbol = Soup2.find('span', class_='a-price-symbol')\n",
    "\n",
    "whole = Soup2.find('span', class_='a-price-whole')\n",
    "\n",
    "fraction = Soup2.find('span', class_='a-price-fraction')\n",
    "\n",
    "price = symbol.get_text(strip=True) + whole.get_text(strip=True) + fraction.get_text(strip=True)\n",
    "\n",
    "\n",
    "print(product)\n",
    "print(\"Price:\", price.strip())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "9fb061b8-b50b-47fe-b230-adb4783f4b5a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Got Data Funny Business Data Analyst T-Shirt\n",
      "19.99\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "price = price.strip()[1:]\n",
    "product = product.strip()\n",
    "\n",
    "print(product)\n",
    "print(price)\n",
    "type(price)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "e77d9f5a-4f36-4ce5-aaec-1c993617f7f0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2025-02-02\n"
     ]
    }
   ],
   "source": [
    "import datetime\n",
    "\n",
    "today = datetime.date.today()\n",
    "\n",
    "print(today)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "1bf4d162-4ec6-4e89-a8b7-9768e26ef88c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "\n",
    "header = ['product', 'price', 'Data']\n",
    "data =[title, price,today]\n",
    "\n",
    "\n",
    "with open('AmazonwebScraperDataset.csv' , 'w' ,newline= '', encoding= 'UTF8') as f:\n",
    "    writer = csv.writer(f)\n",
    "    writer.writerow(header)\n",
    "    writer.writerow(data)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "id": "e2d287d1-78e9-420e-b7dc-a62b1f3ba06d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                         product  price        Data\n",
      "0   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "1   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "2   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "3   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "4   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "5   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "6   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "7   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "8   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "9   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "10  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "11  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "12  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "13  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "14  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "15  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "16  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "17  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "18  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "19  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "20  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv(r'/Users/lloydalemu/AmazonwebScraperDataset.csv')\n",
    "\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "id": "dfd6a089-ce94-4ffd-99f6-d6fa3b3845be",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('AmazonwebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:\n",
    "    writer = csv.writer(f)\n",
    "    writer.writerow(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "id": "576ad739-705c-4108-b0c3-b6b8ce261637",
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_price():\n",
    "    URL = ' https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_5?crid=2KY5C1Q0MLAE8&dib=eyJ2IjoiMSJ9.PM2zhQFx_lfPnddZwr05Dr8MgvuqgncumkkGSNGClexIhzJnz_UO7GIaZd1tCeojtqixplEB_myQHR6h1CXFNh-ntzT93diukU7NtGXijqqCDhcZmxRh9tcMT_ffYGkDNkjk1iOk1wmQH0v0gB8eKASI5S1G3v2Ji9AlMGmveErxWFWEYEtxs9a03oOPecDRZSz6edskmBRSTrpKm_adX66kjq_kqF2pWSzupB0WrUtHprsaLmqPs9hzjVEE_a6teQ-IwnZ4fOW24yzow-j3f4pJ_mgFTwJ-9H1omeA6RJXtN6gRy22jAmlbaTFJCmIrrrHwv8mG4XLQid6mo77IlCQrXrB9ADySHgUuA8s_qr7IT47jrHXSNo1HFbU4InQo2EVh2m9R_2U0T7u5g8t3D_nG7kWS4CV0FFILKH7bYrDBlanDGZPTFdTCjadd0EJx.pFJWEmhSlv-EHInTFDXyGtG8imrEopdyLi3pu71yuUU&dib_tag=se&keywords=data%2Banalyst%2Btshirt&qid=1738452406&sprefix=data%2Banalyst%2Btshirt%2Caps%2C154&sr=8-5'\n",
    "\n",
    "    headers = { \"User-Agent\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36\"}\n",
    "\n",
    "    page = requests.get(URL, headers == headers)\n",
    "\n",
    "    Soup1 = BeautifulSoup(page.content, \"html.parser\")\n",
    "\n",
    "    Soup2 = BeautifulSoup(Soup1.prettify(), \"html.parser\")\n",
    "\n",
    "    product = Soup2.find(id='productTitle').get_text()\n",
    "\n",
    "    symbol = Soup2.find('span', class_='a-price-symbol')\n",
    "\n",
    "    whole = Soup2.find('span', class_='a-price-whole')\n",
    "\n",
    "    fraction = Soup2.find('span', class_='a-price-fraction')\n",
    "\n",
    "    price = symbol.get_text(strip=True) + whole.get_text(strip=True) + fraction.get_text(strip=True)\n",
    "\n",
    "    price = price.strip()[1:]\n",
    "    product = product.strip()\n",
    "    \n",
    "    import datetime\n",
    "\n",
    "    today = datetime.date.today()\n",
    "    \n",
    "    import csv\n",
    "\n",
    "    header = ['product', 'price', 'Data']\n",
    "    data =[title, price,today]\n",
    "\n",
    "    with open('AmazonwebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:\n",
    "        writer = csv.writer(f)\n",
    "        writer.writerow(data)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8123d907-5acd-481a-bdb9-7c349e94299e",
   "metadata": {},
   "outputs": [],
   "source": [
    "while(True):\n",
    "    check_price()\n",
    "    time.sleep(86400)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "id": "8719bba9-225d-4212-9f3e-04fe45927017",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                         product  price        Data\n",
      "0   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "1   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "2   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "3   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "4   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "5   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "6   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "7   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "8   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "9   Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "10  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "11  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "12  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "13  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "14  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "15  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "16  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "17  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "18  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "19  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "20  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "21  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n",
      "22  Got Data Funny Business Data Analyst T-Shirt  19.99  2025-02-02\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "df = pd.read_csv(r'/Users/lloydalemu/AmazonwebScraperDataset.csv')\n",
    "\n",
    "print(df)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
