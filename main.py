from notion_client import Client
import configparser
import scrapper as sc
from datetime import datetime
import pytz

def connect(api_key):
    notion = Client(auth=api_key)
    return notion

def filter_data(api_key, db_id, data, response, impact, currency):
    notion = connect(api_key)
    page_ids = []
    impact_new=[]
    for elem in impact:
        if elem == "yellow":
            impact_new.append("🟡")
        elif elem == "red":
            impact_new.append("🔴")
        elif elem == "orange":
            impact_new.append("🟠")
        else:
            pass
    events=data
    for event in events:
        if event['impact'] in impact_new:
            if event['currency'] in currency:
                date_object = datetime.strptime(event['datetime'], "%Y.%m.%d %H:%M")
                city_timezone = pytz.timezone('Europe/Kiev')
                localized_date_object = city_timezone.localize(date_object)
                iso_date_string = localized_date_object.strftime("%Y-%m-%dT%H:%M%z")
                response = notion.pages.create(
                    parent={
                        "type": "database_id",
                        "database_id": db_id
                    },
                    properties={
                        "Опис": { "type": "title",
                                "title": [{ "type": "text", "text": { "content": event['description'] } }]},
                        "Дата та час": {
                            "date": {
                                "start": iso_date_string
                            }
                        },
                        "Валюта":{
                            "rich_text":[
                                {
                                    "type":"text",
                                    "text":{
                                        "content": event["currency"]
                                    }
                                }
                            ]
                        },
                        "Вплив":{
                            "rich_text":[
                                {
                                    "type":"text",
                                    "text":{
                                        "content": event["impact"]
                                    }
                                }
                            ]
                        },
                        "Фактичний":{
                            "rich_text":[
                                {
                                    "type":"text",
                                    "text":{
                                        "content": event["actual"]
                                    }
                                }
                            ]
                        },
                        "Прогноз":{
                            "rich_text":[
                                {
                                    "type":"text",
                                    "text":{
                                        "content": event["forecast"]
                                    }
                                }
                            ]
                        },
                        "Попередній":{
                            "rich_text":[
                                {
                                    "type":"text",
                                    "text":{
                                        "content": event["previous"]
                                    }
                                }
                            ]
                        }
                    }
                )
        page_ids.append(response['id'])
    return page_ids

def create_pages_and_return_list_of_ids(api_key, db_id, impact, currency):
    notion = connect(api_key)
    response = notion.databases.retrieve(db_id)
    title = response['title'][0]['text']['content']
    page_ids = filter_data(api_key, db_id, sc.fetch_forex_factory_economic_calendar(), response, impact, currency)
    return page_ids

def get_page_name(api_key, id):
    notion = connect(api_key)
    response = notion.databases.retrieve(id)
    title = response['title']
    text = title[0]
    return text['text']['content']
