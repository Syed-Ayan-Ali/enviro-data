Sectors=['G-5','G-6','G-7', 'G-8', 'G-9', 'G-10', 'G-11','G-12','G-13', 'G-14', 'G-15', 'G-16'
,'F-5','F-6','F-7','F-8','F-10','F-11'
,'E-7','E-8','E-9','E-11'
,'I-8','I-9','I-10','I-11'
,'H-8','H-9','H-10','H-11']



def website_opener():
    data=''    
    global sector,name
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from time import sleep
    from webdriver_manager.firefox import GeckoDriverManager



    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("https://www.google.com/maps/place/G-5,+Islamabad,+Islamabad+Capital+Territory/@33.72064,73.0929157,16z/data=!4m5!3m4!1s0x38dfc07b1b153ac9:0x7a6fc13096543e55!8m2!3d33.7218048!4d73.0980773!5m2!1e4!1e1")
    driver.maximize_window() 
    # Inital google maps window --- opens with Traffic data already on
    sleep(0.22)
    for sector in Sectors: 
        name=sector + '.png'

        if sector != 'G-5':
            WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, "searchboxinput"))).send_keys(sector + ", Islamabad")
            Submit = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
            Submit.click()
            sleep(2)
            Zoom= driver.find_element_by_class_name("ujtHqf-zoom-icon")
            Zoom.click()
        
        
                      
        

        if sector== 'G-6':
            sleep(0.6)

        sleep(0.35)   

        screenshot()
        green,orange,red,black=image_annalyser()
        data=data + '<H4>' + emmisions_calculations(green,orange,red,black) + '<H/4> \n'
        clean_up()
    
     
        WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, "searchboxinput"))).send_keys(Keys.CONTROL + "A")
        WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID, "searchboxinput"))).send_keys(Keys.BACK_SPACE)

    driver.quit()
    print(data)
    return data



def emmisions_calculations(g,o,r,b):
    formula= (555/700) / 6

    emmisions=((g*formula*0.2)+(o*formula*0.5)+(r*formula*0.8)+(b*formula*0.96))*0.525*0.2
    emmisions=int(emmisions)
    return str(emmisions)



def clean_up():
    import os
    os.remove(name)
    print("File Removed!")



def screenshot():
    import pyautogui
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(name)



def image_annalyser(): 
    green,orange,red,black=0,0,0,0
    from PIL import Image
    im = Image.open(name, 'r')
    pixel_values = list(im.getdata())
    for i in  pixel_values:  #color has multiple values with small variance, add black color
        if i==(93, 201, 97) or i== (204, 230, 205) or i== (160, 218, 163):
           green+=1
        elif i==(255, 151, 77)or i==(238, 178, 136):
           orange+=1
        elif i==(242, 77, 68)or i== (227, 77, 69) or i==(229, 97, 90):
           red+=1  
        elif i==(183, 127, 127) or i==(129, 31, 31):
           black+=1
    print(green,red,black,orange)
    return green,red,orange,black



def send_to_website(data):
    
    starting_html='''
    <html><head><meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
        <title>CSS Website</title>
        <link rel="stylesheet" href="Website.css">
    </head>
    <body>
        <header id="main-header">
            <div class="main-container">
                <h1>
                    CO<sub>2</sub> Emissions in Islamabad
                </h1>
            </div>
        </header>

        <nav id="navbar">
            <div class="container">
                <ul>
                    <li><a href="" > Home</a></li>
                    <li><a href="" > About</a></li>
                    <li><a href="" > The Team</a></li>
                    <li><a href="" > Contact</a></li>
                </ul>
            </div>
        </nav>
        <div class="container">
            <section id="image-showcase">
                <div class="container">
                </div>
            </section>

            <aside id="showcase">
                <div class="container">
    '''
    ending_html= '''     
            </div>
            </aside>
        </div>
        
       <footer id="main-footer">
           <p>Copyright &copy;2021 FORI Interns</p>
       </footer>
    </body></html>
    '''

    
    f=open('Website\data.html', "w")
    f.write(starting_html +data +ending_html)
    f.close() 
    #send txt file to website



send_to_website=website_opener()


