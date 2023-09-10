import json
import requests
from api.dpop import generate_DPOP

class Mercari():
    def __init__(self) -> None:
        self.base_url = 'https://api.mercari.jp/v2'
        session = requests.Session()
        session.headers = {
            'X-Platform': 'web',
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        }
        self.session = session

    def search(self, keyword):
        url = f"{self.base_url}/entities:search"
        self.session.headers['Dpop'] = generate_DPOP(
            uuid="Thungghuan",
            method="POST",
            url=url,
        )

        data = {
            "userId": "",
            "pageSize": 120,
            "pageToken": "",
            "searchSessionId": "5d82adff89abfb66528c31198378d373",
            "indexRouting": "INDEX_ROUTING_UNSPECIFIED",
            "thumbnailTypes": [],
            "searchCondition": {
                "keyword": keyword,
            },
        }
        data = json.dumps(data, ensure_ascii=False).encode('utf-8')

        resp = self.session.post(url, data)
        return resp.json()

