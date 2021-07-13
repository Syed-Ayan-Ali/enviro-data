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
    return str(emmisions)



def clean_up(data):
    import os
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
    ending= '''     
            </div>
            </aside>
        </div>
        
       <footer id="main-footer">
           <p>Copyright &copy;2021 FORI Interns</p>
       </footer>
     
    </body></html>
'''

    os.remove(name)
    #print("File Removed!")
    f=open('Website\data.html', "w")
    f.write(starting_html +data +ending)
    f.close() 
    #send txt file to website

global data


def process():
    j=0
    data=''
    for i in urls:
        screenshot(i,j)
        j+=1
        green,orange,red=image_annalyser()
        data=data +'<h4>' +  emmisions_calculations(green,orange,red) + '</h4>' +'\n'
    clean_up(data)
process()