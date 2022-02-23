#locust -f loc.py --host=http://www.example.com
import time
from locust import HttpUser, task, between
import requests
import json

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")

    # @task(3)
    # def view_items(self):
    #     for item_id in range(10):
    #         self.client.get(f"/item?id={item_id}", name="/item")
    #         time.sleep(1)
    
    def on_start(self):
        path="https://mg-alpha.au66.top/ga/api/admin/v1/manual/withdraw"
        url=path
        headers={
            "accept": "application/json",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            # "content-length": "101",
            "content-type": "application/json",
            "cookie": "gasticky=fa62df5c-ca2f-4c34-96fd-e4562d564750; token_guard=admin; goldenapi_session=ziq0x6PuGECVbWyCe6awxxsxY8mke2vsSxCIOYF2; api_token=9720%7CfkH1rZoYAL2V4wc68tbT2xDQPXtuSodr47ux32F2; IDLE%3ALAST_ACTIVE_TIME_KEY_V2=1641281921",
            "origin": "https://mg-alpha.au66.top",
            "referer": "https://mg-alpha.au66.top/manual/withdraw/create",
            "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": "Android",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36"
        }
        data={
            "cash": "1",
            "deduct_effective_cash_needed": "0.0000",
            "memo": "test",
            "user_id": 363,
            "withdraw_type": "1"
        }
        # print(token)
        # print(headers)
        # print(data)
        for i in range(20000):
            re=requests.post(url,headers=headers,data=json.dumps(data))
            # print(re.json())
            print(re.text)


    