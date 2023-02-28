from selenium import webdriver
from bs4 import BeautifulSoup

# 設定WebDriver的路徑，請將路徑替換成您自己的路徑
driver_path = "msedgedriver.exe"

# 設定WebDriver的選項
options = webdriver.EdgeOptions()
options.add_argument("start-maximized") # 啟動瀏覽器時最大化視窗
options.add_argument("disable-infobars") # 禁用瀏覽器資訊列
options.add_argument("--disable-extensions") # 禁用擴展

# 使用WebDriver啟動Edge瀏覽器
driver = webdriver.Edge(executable_path=driver_path, options=options)

# 設定要爬取的網址
url = "https://www.youtube.com/"

# 使用WebDriver打開網頁
driver.get(url)

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(driver.page_source, "html.parser")

# 根據相鄰節點定位元素，以下是一個例子
element = soup.select_one("div > p")

# 關閉瀏覽器
driver.quit()

# 輸出結果
print(element.text)
