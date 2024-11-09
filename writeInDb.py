import sqlite3
from ctypes.wintypes import DWORD

from bs4 import BeautifulSoup
import requests
import os
from ImageDownloader import Downloader


class WriteInDb:

    @staticmethod
    def __imageBin(soup):
        imgs = soup.select_one('img[class^="TutorialTemplateStyles__StyledRecordHeaderImage"]')
        resImg = requests.get(imgs.attrs['src'])
        if resImg.status_code == 200:
            return imgs.attrs['src']

    @classmethod
    def writingInDbPerLink(cls, dbName, tableName, path, link):
        connection = sqlite3.connect(dbName)
        cursor = connection.cursor()

        cursor.execute(f"SELECT url FROM '{tableName}' WHERE url=?", (link,))
        data = cursor.fetchall()

        if not data:
            response = requests.get(link)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                url = link
                titles = soup.title.string if soup.title else "No Title"
                body = soup.select_one('div[class^="ContainerStyles__StyledContainer"]')
                navigation = soup.select_one(
                    'div[class^="QuestionAndTutorialLeftContainerStyles__StyledColumnContainer"]')
                imageUrl = cls.__imageBin(soup)

                if imageUrl:
                    name = Downloader.generateNameRandom()
                    file_dir = os.path.join(path, name + '.jpg')
                    photoPath = file_dir
                    Downloader.download_image(imageUrl, file_dir)

                    cursor.execute(
                        f"INSERT INTO '{tableName}' (url, titles, body, navigation, photoPath) VALUES (?, ?, ?, ?, ?)",
                        (url, titles, str(body), str(navigation), str(photoPath))
                    )

        connection.commit()
        connection.close()

    @staticmethod
    def writingInDbLinksByLink(dbName, tableName, url):
        with sqlite3.connect(dbName) as connection:
            cursor = connection.cursor()

            cursor.execute(f"SELECT url FROM '{tableName}' WHERE url = ?", (url,))
            data = cursor.fetchall()

            if not data:
                cursor.execute(f"INSERT INTO '{tableName}' (url) VALUES (?)", (url,))

            connection.commit()
