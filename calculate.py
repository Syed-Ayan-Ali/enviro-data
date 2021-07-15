urls=['https://bit.ly/3eeuGuv','https://bit.ly/36B3GkG','https://bit.ly/3rcdkU7','https://bit.ly/36FZWy1','https://bit.ly/3ebFUzK','https://bit.ly/3xQucSM','https://bit.ly/3wAuWdr','https://bit.ly/3B4f3PO','https://bit.ly/36ARfoM','https://bit.ly/3r6TGsN','https://bit.ly/3i6adJf','https://bit.ly/3AWYAx7'
,'https://bit.ly/3AXec3v','https://bit.ly/3efzuiW','https://bit.ly/3AVz23r','https://bit.ly/3efEx2Y','https://bit.ly/3xHQk1Y','https://bit.ly/2T9i0xD'] 


Sector=['G-5','G-6','G-7','G-8','G-9','G-10','G-11','G-12','G-13','G-14','G-15','G-16'
,'F-5','F-6','F-7','F-8','F-10','F-11']





global name

global data



def screenshot(url,sectorInitall):
    from selenium import webdriver
    from time import sleep
    from webdriver_manager.firefox import GeckoDriverManager

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(url)
    driver.fullscreen_window
    sleep(0.35)
    global name
    
    name=Sector[sectorInitall] + '.png'
    driver.get_screenshot_as_file(name)
    driver.quit()
    print("end...")



def image_annalyser(): 
    green,orange,red,black=0,0,0,0
    from PIL import Image
    im = Image.open(name, 'r')
    width, height = im.size
    pixel_values = list(im.getdata())
    for i in  pixel_values:  #color has multiple values with small variance, add black color
        if i==(92, 200, 97, 255)or i== (173, 220, 175, 255):
            green+=1
        elif i==(238, 141, 72, 255)or i==(238, 178, 136, 255):
            orange+=1
        elif i==(226, 56, 46, 255)or i== (227, 77, 69, 255) or i==(229, 97, 90, 255):
            red+=1  
        elif i==(183, 127, 127, 255) or i==(129, 31, 31, 255):
            black+=1
    return green,red,orange,black



def emmisions_calculations(g,o,r,b):
    formula= (555/700) / 6

    emmisions=((g*formula*0.2)+(o*formula*0.5)+(r*formula*0.8)+(b*formula*0.96))*0.525*0.2
    if name[-5]=='5':
        emmisions/=2
    #print(str(emmisions))
    emmisions=int(emmisions)
    return str(emmisions)



def clean_up():
    import os
    os.remove(name)
    print("File Removed!")


    
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



def process():
    j=0
    data=''
    for i in urls:
        screenshot(i,j)
        green,orange,red,black=image_annalyser()
        data=data +'<h4>' + Sector[j] + ': '+ emmisions_calculations(green,orange,red,black) + ' kg/hour </h4>\n'
        j+=1
        clean_up()
    send_to_website(data)



process()