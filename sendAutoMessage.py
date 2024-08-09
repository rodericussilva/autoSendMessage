from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta
import time
import urllib.parse
import pandas as pd
import requests

def shorten_url(long_url, access_token):
    url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "long_url": long_url
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code in [200, 201]:
        shortened_url = response.json().get("link")
        #print(f"Original URL: {long_url} -> Shortened URL: {shortened_url}")
        return shortened_url
    else:
        print(f"Erro ao encurtar URL: {response.status_code}, Response: {response.text}")
        return long_url

contact_df = pd.DataFrame({
    'name': ['User'],
    'number': ['999999999'],
    'text': [
        "Enviado"
    ]
})

BITLY_ACCESS_TOKEN = 'YOUR TOKEN' 

for i, row in contact_df.iterrows():
    parts = row['text'].split(" ")
    new_parts = []
    for part in parts:
        if part.startswith("https://"):
            new_parts.append(shorten_url(part, BITLY_ACCESS_TOKEN))
        else:
            new_parts.append(part)
    contact_df.at[i, 'text'] = " ".join(new_parts)
    print(f"Updated text for {row['name']}: {contact_df.at[i, 'text']}")

options = Options()
service = Service(ChromeDriverManager().install())

def send_messages(browser):
    try:
        WebDriverWait(browser, 40).until(EC.presence_of_element_located((By.ID, "side")))
        for i, row in contact_df.iterrows():
            name = row['name']
            number = row['number']
            message = f"Olá {name}, segue o link do seu dashboard atualizado: {row['text']} Favor, acessar!"
            print(f"Sending message: {message}")
            quote = urllib.parse.quote_plus(message)
            url = f'https://web.whatsapp.com/send?phone={number}&text={quote}'

            browser.get(url)
            WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]')))
            time.sleep(20)
            browser.find_element(By.XPATH, '//span[@data-icon="send"]').click()
            time.sleep(20)
            
    except Exception as e:
        print(f"Erro durante o envio das mensagens: {e}")

def until_next_schedule(restart_times):
    now = datetime.now()
    today = now.date()
    for time_str in restart_times:
        scheduled_time = datetime.strptime(time_str, '%H:%M').time()
        scheduled_datetime = datetime.combine(today, scheduled_time)
        if scheduled_datetime > now:
            return (scheduled_datetime - now).total_seconds(), scheduled_datetime   
    first_time_tomorrow = datetime.combine(today + timedelta(days=1), datetime.strptime(restart_times[0], '%H:%M').time())
    return (first_time_tomorrow - now).total_seconds(), first_time_tomorrow

def main():
    browser = webdriver.Chrome(service=service, options=options)
    
    restart_times = ['07:30', '09:30', '12:30', '16:30', '22:00']
    
    try:
        browser.get('https://web.whatsapp.com/')
        while True:
            time_until_next, next_schedule_time = until_next_schedule(restart_times)
            if time_until_next > 0:
                time.sleep(time_until_next)
            send_messages(browser)
            print(f"O horário do próximo envio será às {next_schedule_time.strftime('%H:%M')}")
            time_until_next, next_schedule_time = until_next_schedule(restart_times)
            
    finally:
        browser.quit()

if __name__ == "__main__":
    main()
