import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as soup


class InstaDL:
    def __init__(self, browser="chrome"):
        self.browser = browser

    def _configure_chrome(self) -> webdriver.Chrome:
        chrome_options = Options()
        chrome_options.add_argument("headless")
        chrome_options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        )
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)

        return webdriver.Chrome(options=chrome_options)

    def _get_data(self, url) -> soup:
        try:
            driver = self._configure_chrome()
            driver.get("https://clipdown.app/en")

            time.sleep(1)
            input_element = driver.find_element(By.ID, "s_input")
            input_element.send_keys(url)

            driver.execute_script("document.getElementById('btn_start').click();")

            WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "download-box"))
            )
            html_source = driver.page_source
            parsed_html = soup(html_source, "html.parser")
            result = parsed_html

        except Exception as e:
            driver.quit()
            raise e

        driver.quit()
        return result

    def Reel(self, url) -> dict:
        data = self._get_data(url)
        res = []
        try:
            row = data.find("div", {"id": "download-result"}).find("ul", {"class": "download-box"})
            link = row.find("li")
            link = link.find("a", {"title": "Download Video"})
            res.append(link.get("href"))
            return {"status": True, "url": res}

        except AttributeError:
            return {"status": False, "url": res}
    
    def Photo(self, url) -> dict:
        data = self._get_data(url)
        res = []
        try:
            row = data.find("div", {"id": "download-result"}).find("ul", {"class": "download-box"})
            links = row.find_all("li")
            for link in links:
                link = link.find("a")
                res.append(link.get("href"))
            return {"status": True, "url": res}

        except AttributeError:
            return {"status": False, "url": res}