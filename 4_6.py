# find_element_by_id => 아이디 속성 사용하여 접근
# find_element_by_name => name 속성
# find_element_by_xpath => xpath 속성
# find_element_by_link_text => 앵커태그(a태그)에 사용되는 텍스트로 접근
# find_element_by_partial_link_text => 앵커태그(a태그)에 사용되는 일부 텍스트로 접근
# find_element_by_tag_name => 태그를 사용해서 접근
# find_element_by_class_name => 클래스 이용해서 접근
 
from selenium import webdriver
chrome_path = r"C:\\py_wj\\chromedriver_win32"
url = 'https://www.naver.com/'
browser = webdriver.Chrome(chrome_path)
browser.get(url)
browser.find_element_by_xpath('//*[@id="account"]/a').click()