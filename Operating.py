import json
from time import sleep

import requests


class Operating:
    __cats_pages = {}

    @classmethod
    def __cal_pages(cls):
        cats = ["ai-ml", "apache", "databases", "docker", "javascript", "kubernetes", "linux-basics", "mysql", "python",
                "react", "security", "ubuntu"]

        for cat in cats:
            api_pages = (f"https://www.digitalocean.com/api/static-content/v1/search?query=%5B{cat}%5D&type=tutorial&"
                         f"sub_type=-tech-talk&language=en&sort_by=newest&time_range=all&filter=&page=0&hits_per_page=12")

            response_cat = requests.get(api_pages)
            response_dict = json.loads(response_cat.content)
            # print("hits: " + str(len(response_dict['hits'])) + "link: " + str(response_dict['hits'][0]['permalink']))
            total_pages = response_dict["pages"]
            cls.__cats_pages[cat] = total_pages
            sleep(1)
        return cls.__cats_pages

    @staticmethod
    def __get_total_pages():
        total_api = (
            "https://www.digitalocean.com/api/static-content/v1/search?query=&type=tutorial&sub_type=-tech-talk&"
            "language=en&sort_by=newest&time_range=all&filter=&page=0&hits_per_page=12")
        total_response = requests.get(total_api)
        if total_response.status_code == 200:
            total_response_dict = json.loads(total_response.content)
            return total_response_dict["pages"]

    @classmethod
    def get_links(cls):
        for cat, pages in cls.__cal_pages().items():
            for page in range(pages):
                api = (
                    f"https://www.digitalocean.com/api/static-content/v1/search?query=%5B{cat}%5D&type=tutorial&sub_type=-tech-talk&"
                    f"language=en&sort_by=newest&time_range=all&filter=&page={page}&hits_per_page=12")
                res_per_page = requests.get(api)
                if res_per_page.status_code == 200:
                    res_dict = json.loads(res_per_page.content)
                    for size in range(len(res_dict['hits'])):
                        yield str(res_dict['hits'][size]['permalink'])
                sleep(0.4)

    @classmethod
    def get_all_total(cls):
        total_pages = cls.__get_total_pages()
        for page in range(int(total_pages)):
            print("page: " + str(page))
            total_api = f"https://www.digitalocean.com/api/static-content/v1/search?query=&type=tutorial&sub_type=-tech-talk&language=en&sort_by=newest&time_range=all&filter=&page={page}&hits_per_page=12"
            total_response = requests.get(total_api)

            if total_response.status_code == 200:
                total_response_dict = json.loads(total_response.content)
                for size in range(len(total_response_dict['hits'])):
                    yield total_response_dict['hits'][size]['permalink']

            sleep(1.5)
