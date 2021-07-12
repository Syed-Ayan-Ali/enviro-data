urls=['https://bit.ly/3e4Sh0C','https://bit.ly/3yFAiFD'] #urls are temporary, will add better urls soon/potentially a html file to avoid side menu
global name


def screenshot(url,sectorinitall):
    from selenium import webdriver
    from time import sleep
    from webdriver_manager.firefox import GeckoDriverManager

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(url)
    sleep(0.35)

    Sector=['A','B','C','E','F','G','H','I']
    global name
    name=Sector[sectorinitall] + '.png'
    driver.get_screenshot_as_file(name)
    driver.quit()
    print("end...")



def image_annalyser(): 
    green,orange,red=0,0,0
    from PIL import Image
    im = Image.open(name, 'r')
    width, height = im.size
    pixel_values = list(im.getdata())
    for i in  pixel_values:  #color has multiple values with small variance, add black color
        if i==(92, 200, 97, 255):
            green+=1
        elif i==(238, 141, 72, 255):
            orange+=1
        elif i==(226, 56, 46, 255):
            red+=1      
    return green,red,orange



def emmisions_calculations(g,o,r):
    emmisions=(g*1+o*2+r*3)/5000 * .5 # replace 5000 with acurate number for scale and give each color accurate waitage, formula not final
    #print(str(emmisions))
    return emmisions



def clean_up(data):
    import os
    os.remove(name)
    #print("File Removed!")
    f=open('data.txt', "a")
    f.write(str(data) +' Kg/hour\n')
    f.close() 
    #send txt file to website



def process():
    j=0
    for i in urls:
        screenshot(i,j)
        j+=1
        green,orange,red=image_annalyser()
        clean_up(emmisions_calculations(green,orange,red))

process()