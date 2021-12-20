from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://www.theneedledrop.com/')

content = browser.find_element_by_class_name('summary-title-link').text
print(f'Álbum semanal: {content}')


browser.close()
