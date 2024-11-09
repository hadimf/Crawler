import random
import string
import os
import requests


class Downloader:
    @staticmethod
    def generateNameRandom():
        length = 10
        characters = string.ascii_lowercase + string.digits + string.ascii_uppercase
        result = ''
        for i in range(length):
            result += random.choice(characters)
        return result

    @staticmethod
    def download_image(image_url, file_dir):
        response = requests.get(image_url)

        if response.status_code == 200:
            directory = os.path.dirname(file_dir)
            if not os.path.exists(directory):
                os.makedirs(directory)

            with open(file_dir, "wb") as fp:
                fp.write(response.content)
        else:
            print(f"Failed to download the image. Status code: {response.status_code}")
