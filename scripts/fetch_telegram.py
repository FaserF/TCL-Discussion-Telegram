import requests
from bs4 import BeautifulSoup
import json
import sys
import re

def fetch_latest_post(channel="tclupdates"):
    url = f"https://t.me/s/{channel}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get all messages
        messages = soup.find_all('div', class_='tgme_widget_message_wrap')
        if not messages:
            return None

        # Get last message
        last_msg = messages[-1]

        # Extract text
        text_div = last_msg.find('div', class_='tgme_widget_message_text')
        text = text_div.get_text(separator=' ').strip() if text_div else "Latest updates on Telegram!"

        # Clean up text (limit length)
        text = (text[:120] + '...') if len(text) > 120 else text

        # Extract link
        link_tag = last_msg.find('a', class_='tgme_widget_message_date')
        link = link_tag['href'] if link_tag else f"https://t.me/{channel}"

        return {
            "text": text,
            "link": link
        }
    except Exception as e:
        print(f"Error fetching telegram: {e}")
        return None

if __name__ == "__main__":
    data = fetch_latest_post()
    if data:
        print(json.dumps(data))
    else:
        sys.exit(1)
