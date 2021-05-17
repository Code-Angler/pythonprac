from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/seong gyeong/Desktop/SPARTA/pythonprac/chromedriver.exe')
driver.get("https://shoppinglive.naver.com/home?category=46")
time.sleep(5) # 5초 동안 페이지 로딩 기다리기(이미지가 자꾸 바뀌는 페이지는 필요)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
trs = soup.select("#wa-main-46 > div > section > div")
for tr in trs:
    div = tr.select_one('a.VideoCard_link_3x4f- > span.VideoCard_video_wrap_2as3m > span.VideoCard_item_wrap_eQfmS')
    a_tag = div.select_one('span.VideoCard_item_title_2yVNl')
    discount_a = div.select_one(
        'span.VideoCard_discount_2fhhu')
    title = a_tag.text
    if discount_a is None:
        discount_a = "할인 없음" # text 파일을 출력할시 오류가 발생하므로, none 값은 이렇게 확인한다
        print(title, discount_a)
    else:
        discount_a = discount_a
        print(title, discount_a.text) # 여기서 출력할때는 결과적으로 원하는 값인 .text를 한 값을 출력한다.


\


driver.quit() # 끝나면 닫아주기

