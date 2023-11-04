import logging

import requests
import xml.etree.ElementTree as ET

from apps.currency.models import Currency

from django.db import connection


def currency_update_task():
    with connection.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE currency_currency")
    url = 'https://www.nationalbank.kz/rss/rates_all.xml'
    response = requests.get(url)
    if response.status_code == 200:
        xml_content = response.content
        try:
            root = ET.fromstring(xml_content)
            items = []
            for item_elem in root.findall('.//item'):
                item = Currency(name=item_elem.find('title').text,
                                rate=item_elem.find('description').text)
                items.append(item)
            Currency.objects.bulk_create(items)
        except ET.ParseError as e:
            logging.error(f"XML parsing error: {e}")
    else:
        logging.error(f"Request failed with status code {response.status_code}")
