Sectors=['E-11','E-9', 'E-8', 'E-7',
'F-5','F-6','F-7','F-8','F-10','F-11',
'G-5','G-6','G-7', 'G-8', 'G-9', 'G-10', 'G-11','G-13', 'G-14',
'H-8','H-9','H-10','H-11', 'H-12',
'I-8','I-9','I-10','I-11' ]

subsectors=[1,6,9,5,4]
sector_emmisions=[]
main_sectors = ['E','F','G','H','I']
startc=[1,7,16,21]
endc=[6,15,21,26]

subsectors=[1,6,9,5,4]
sector_emmisions=[]
main_sectors = ['E','F','G','H','I']


global name

global data

def screenshot(sector, d):

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    
    from time import sleep
    import os

    import pyautogui

    WebDriverWait(d,20).until(EC.visibility_of_element_located((By.ID, "searchboxinput"))).send_keys(sector + ", Islamabad")
    Submit = d.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
    Submit.click()
            
    # if sector != "G-5" and sector != "G-13" and sector != "G-14" and sector != "G-15" and sector != "G-16": 
    #     sleep(3)
    #     Zoom= d.find_element_by_class_name("ujtHqf-zoom-icon")
    #     Zoom.click()
        
    d.fullscreen_window()
  
    global name
    name = sector + '.png'
    print(name)
    sleep(3)
    myScreenshot = pyautogui.screenshot()
    FILE_PATH = "D:\enviro-data-main\screenshots"
    FILE_NAME = sector+".png"
    FILE_INFO = os.path.join(FILE_PATH, FILE_NAME)
    WebDriverWait(d,20).until(EC.visibility_of_element_located((By.ID, "searchboxinput"))).send_keys(Keys.CONTROL + "A")
    WebDriverWait(d,20).until(EC.visibility_of_element_located((By.ID, "searchboxinput"))).send_keys(Keys.BACK_SPACE)
    myScreenshot.save(FILE_INFO)
    print("end...")
   


def image_annalyser(sctr): 
    green,orange,red,black=0,0,0,0
    from PIL import Image
    import os
    FILE_PATH = "D:\enviro-data-main\screenshots"
    FILE_NAME = sctr +".png"
    FILE_INFO = os.path.join(FILE_PATH, FILE_NAME)

    im = Image.open(FILE_INFO, 'r')
    print(im)

    pixel_values = list(im.getdata())
    for i in  pixel_values:  #color has multiple values with small variance, add black color
        if i==(92, 200, 97) or i==(93, 201, 97) or i== (204, 230, 205) or i== (160, 218, 163) :
            green+=1
        elif i==(255, 151, 77)or i==(238, 178, 136):
            orange+=1
        elif i==(242, 77, 68)or i== (227, 77, 69) or i==(229, 97, 90):
            red+=1  
        elif i==(129, 31, 31) or i==(183, 127, 127):
            black+=1 

    return green,red,orange,black



def emmisions_calculations(g,o,r,b):
    formula= (555/700) / 6

    emmisions=((g*formula*0.3)+(o*formula*0.5)+(r*formula*0.8)+(b*formula*0.96))*0.525
    if name[-5]=='5':
        emmisions/=2
    #print(str(emmisions))
    emmisions=int(emmisions)
    return str(emmisions)



def clean_up(sctr):
    import os
    FILE_PATH = "D:\enviro-data-main\screenshots"
    FILE_NAME = sctr+".png"
    FILE_INFO = os.path.join(FILE_PATH, FILE_NAME)
    os.remove(FILE_INFO)
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
                <table>    
                        <th>
                            Sector | Emissions
                        </th>
    '''
    ending_html= '''   
                    </table>  
                </div>
            </aside>
        </div>
        
       <footer id="main-footer">
           <p>Copyright &copy;2021 FORI Interns</p>
       </footer>
    </body></html>
    '''

    
    f = open('D:\enviro-data-main\Website\data.html', "w")
    f.write(starting_html + data + ending_html)
    f.close() 
    #send txt file to website



def pie_chart(emmisions):
    import matplotlib.pyplot as plt
    import numpy as np
    end=False
    i=0
    while end==False: 
        total=0
        for j in range(subsectors[i]):
            total+=emmisions[i]
        sector_emmisions.append(total)    
        i+=1
        if i==5:
            end=True


    plt.figure(5)
    plt.pie(np.array(sector_emmisions), labels = main_sectors)
    plt.legend(title = "Sectors:",bbox_to_anchor=(1.15,1))
    plt.savefig('D:\enviro-data-main\Website\images\ ' +'all.png')
    
    for i in range(0,4):
        import matplotlib.pyplot as plt
        import numpy as np
        plt.figure(i)
        y = np.array(emmisions[startc[i]:endc[i]])
        plt.pie(y, labels =Sectors[startc[i]:endc[i]])
        j=i+1
        plt.savefig('D:\enviro-data-main\Website\images\ ' +main_sectors[1+i] +'.png')



def process():
    data=''
    Emissions = []

    from selenium import webdriver
    from time import sleep
    from webdriver_manager.firefox import GeckoDriverManager


    import numpy as np
    from PIL import Image  
    import os
    
    from PIL import Image
    from PIL import ImageFont
    from PIL import ImageDraw 


    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("https://www.google.com/maps/@33.6678654,73.0523224,15z/data=!5m1!1e1")
    sleep(1)
    for sector in Sectors:
        screenshot(sector, driver)
        green,orange,red,black= image_annalyser(sector)
        emission_for_sector = emmisions_calculations(green,orange,red,black)
        
        # colours = ["#95B121", "#AEB91A", "#C6C013","#E3B61C", "#EFB420", "#FAB123", "#FAAA15", "#FAA322",
        #             "#FAA307", "#F48C06", "#F18106","#EB6905", "#E85D04", "#E55204", "#E24603","#DA3B03",
        #             "#D22F03", "#C52A05","#9E1A09","#960E08","#8D0207","#850309","#7C030B","#73040D", "#6A040F"]
        colours = ["#7CA928", "#95B121", "#AEB91A", "#C6C013", "#E3B61C", "#EFB420", "#FAB123", "#FAAA15", "#FAA322",
                    "#FAA307", "#F79807", "#F48C06", "#F18106","#EE7505", "#E85D04", "#E55204", "#E24603","#DA3B03",
                    "#D22F03", "#C52A05", "#B82506","#9E1A09","#960E08","#8D0207","#850309","#7C030B","#73040D", "#6A040F"]
        # #colours = ["#7CA928", "#95B121", "#AEB91A", "#C6C013", "#E3B61C", "#EFB420", "#FAB123", "#FAAA15", "#FAA322",
        #             "#FAA307", "#F79807", "#F48C06", "#F18106","#EE7505","#EB6905", "#E85D04", "#E55204", "#E24603","#DA3B03",
        #             "#D22F03", "#C52A05", "#B82506","#9E1A09","#960E08","#8D0207","#850309","#7C030B","#73040D", "#6A040F"]
        # #Emissions = [23, 24, 29, 29]

        Emissions.append(emission_for_sector)
       
       
        clean_up(sector)

    for i in range(len(Emissions)):
        Emissions[i] = int(Emissions[i])
    print("Emissions before check: "+str(Emissions))
    
    for i in range(len(Emissions)):
        comparable = Emissions[i]
        for j in range(len(Emissions)):
            if i != j:
                if Emissions[j] == comparable:
                    Emissions[j] += 1
    print("Emissions after check: " + str(Emissions))
    no_more_swaps = False
    unsorted_emissions = Emissions
                     #E-11,E-9,E-8,E-7,F-5,F-6,F-7,F-8,F-10,F-11, G-5,G-6,G-7,G-8,G-9 G-10,G-11,G-13,G-14, H-8,H-9,H-10,H-11,H-12, I-8,I-9,I-10,I-11
    start_x_pixels = [290,515, 590,680,865,767,670,575, 378, 288  ,865,767,670,575,472,378, 288,88,   0  , 575,472, 378, 284, 187, 575,472, 378, 285] 
    end_x_pixels =   [370,570, 665,715,910,855,758,663, 465, 370  ,910,855,758,663,565,465, 370,175,  80 , 663,565, 465, 371, 275, 663,565, 465, 371]
    start_y_pixels = [95, 123, 150,170,190,190,190,190, 190, 190  ,285,285,285,285,285,285, 285,285,  285, 375,375, 375, 375, 375, 480,480, 480, 480]
    end_y_pixels =   [180,160, 182,180,275,275,275,275, 275, 275  ,365,365,365,365,365,365, 365,365,  365, 471,468, 468, 468, 468, 565,565, 565, 565]
  
    sorted_x_start_array = [' ' for i in range(len(start_x_pixels))]
    sorted_x_end_array = [' ' for i in range(len(end_x_pixels))]
    sorted_y_start_array = [' ' for i in range(len(start_y_pixels))]
    sorted_y_end_array = [' ' for i in range(len(end_y_pixels))]

    n = len(Emissions) - 1
   
    print("unsorted emissions are: " + str(unsorted_emissions))
    while no_more_swaps == False:
        no_more_swaps = True
        for j in range(0, n):
            if Emissions[j] > Emissions[j+1]:
                Temp = Emissions[j]
                Emissions[j] = Emissions[j + 1]
                Emissions[j + 1] = Temp 
                no_more_swaps = False
        n -= 1  

    sorted_sector_array = [' ' for i in range(len(Emissions))]
    sorted_emissions = Emissions
    print("unsorted emissions are: " + str(unsorted_emissions))
    for emission_num in range(28):
        new_comaparable = unsorted_emissions[emission_num] 
        print("new comparable = " + str( new_comaparable))
        for i in range(28):
            if sorted_emissions[i] == new_comaparable:        
                sorted_sector_array[i] = Sectors[emission_num]
                sorted_x_start_array[i] = start_x_pixels[emission_num]
                sorted_x_end_array[i] = end_x_pixels[emission_num]
                sorted_y_start_array[i] = start_y_pixels[emission_num]
                sorted_y_end_array[i] = end_y_pixels[emission_num]
                print("reached here")
               
    print("Sorted emissiosn are: " + str(sorted_emissions))
    print("Sorted sectors are: " + str(sorted_sector_array))

    print("Sorted start x pixels are: " + str(sorted_x_start_array))
    print("Sorted end x pixels are: " + str(sorted_x_end_array))
    print("Sorted start y pixels are: " + str(sorted_y_start_array))
    print("Sorted end y pixels are: " + str(sorted_y_end_array))

    for i in range(len(Emissions)):
        j = i
        data = data + '<tr><th>' + str(sorted_sector_array[j]) + ': '+ str(sorted_emissions[j]) + ' kg/hour </th></tr>\n'
        send_to_website(data)

    FILE_PATH = "D:\enviro-data-main\Website\images"
    path = os.path.join(FILE_PATH, "Map.png") 
    
    # Open image
    im = Image.open(path)
    draw = ImageDraw.Draw(im)
    from colormap import hex2rgb
    font_path = "D:\enviro-data-main\Fonts"
    font_path =  os.path.join(font_path, "anonoma-mono-less-characters.ttf")
    font = ImageFont.truetype(font_path, 18)
    for i in range(len(colours)):
        print(colours[i])

    for i in range(len(colours)):
        rgb_color = hex2rgb(colours[i])
        if sorted_sector_array[i] == 'E-9':
            x = 515
            x_limit_triangle = x + 5
            for y in range(100, 123):
                while x < (x_limit_triangle):
                    # print("reached here")
                    # here+=1
                    # print(here)
                    im.putpixel((x, y), (rgb_color))
                    x+=1

                x_limit_triangle += 3
                x = 515


            for y in range(123, 160):
                for x in range(515, 570):
                    im.putpixel((x, y), rgb_color)

            SECTOR_WIDTH = 66
            x_initial = 520
            x_limit_parlogram = x_initial + SECTOR_WIDTH
            for y in range(123, 182):
                while x_initial < (x_limit_parlogram):
                    im.putpixel((x_initial, y), rgb_color)
                    x_initial+=1

                x_initial -= SECTOR_WIDTH + 1 
                x_limit_parlogram -= 0.3


        elif sorted_sector_array[i] == 'E-8':
            E_8_start_x = 593
            turn = 0
            x = E_8_start_x
            x_limit_triangle = x + 5
            for y in range(127, 150):
                while x < (x_limit_triangle):
                    # print("reached here")
                    # here+=1
                    # print(here)
                    im.putpixel((x, y), rgb_color)
                    x+=1
                turn += 0.3
                x_limit_triangle += 3
                x = E_8_start_x - int(turn) 
            
            E_8_start_x = 593
            turn = 0
            x = E_8_start_x
            x_limit_triangle = x
            for y in range(127, 182):
                while x < (x_limit_triangle):
                    im.putpixel((x, y), rgb_color)
                    x+=1
                turn += 0.3
                x = E_8_start_x - int(turn)     
                SECTOR_WIDTH = 75
                x_initial = 590
                x_limit_parlogram = x_initial + SECTOR_WIDTH

            for y in range(150, 182):
                while x_initial < (x_limit_parlogram):
                    im.putpixel((x_initial, y), rgb_color)
                    x_initial+=1

                x_initial -= SECTOR_WIDTH + 1 
                x_limit_parlogram -= 0
    
        elif sorted_sector_array[i] == 'E-7':        
            x = 672
            x_limit_triangle = x + 5
            for y in range(153, 182):
                while x < (x_limit_triangle):
                    im.putpixel((x, y), rgb_color)
                    x+=1

                x_limit_triangle += 3
                x = 672
            
        for x in range(sorted_x_start_array[i], sorted_x_end_array[i]):
            for y in range(sorted_y_start_array[i], sorted_y_end_array[i]):
                im.putpixel((x,y), (rgb_color))

        
        middle_x = sorted_x_start_array[i] + (sorted_x_end_array[i] - sorted_x_start_array[i])//2 - 16
        middle_y = sorted_y_start_array[i] + (sorted_y_end_array[i] - sorted_y_start_array[i])//2 - 16
        draw.text((middle_x, middle_y), sorted_sector_array[i], (255,255,255), font = font)

    driver.quit()
    im.show()
    result = os.path.join(FILE_PATH, "result.png")
    im.save(result)
    pie_chart(Emissions)





process()
