from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import MaxNLocator

from parse_names import beautify_string
from matplotlib.axis import Axis
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import pandas as pd

while True:        
    mode = input("Please enter the mode you want to create your graph\n1 for Line Chart\n2 for Stacked Bar Chart\n3 for Pie Chart\nChoice: ")
    #sayı girene kadar tekrar iste

    def my_autopct(pct):
        if pct > 0:
            return '{:.2f}%'.format(pct)
        else:
            return ''


    if mode == "1":
        city_list = []
        fig, ax = plt.subplots()
        while True:
            user_input = input("Which city would you like to see about? ").lower().strip()
            city_list.append(user_input)
            user_input = beautify_string(user_input)
            name = ""
            for i in user_input:
                if ord(i) in range(256):
                    name += i
            user_input = name
            if user_input == "exit":
                break
            infile = "city info/formatted/" + user_input + ".csv"
            

            df = pd.read_csv(infile)
            ax.plot(df['Year'], df['Female MP Count'])
            ax.grid(alpha = 0.8)
            ax.yaxis.set_major_locator(MaxNLocator(integer=True))

            
        plt.title("Female MP's Over Time")
        plt.xlabel("Years")
        plt.ylabel("MP Count")
        plt.legend(city_list, loc = 'upper left', fontsize = 15)
        plt.show()

    elif mode == "2":
        while True:
            user_input = input("Which city would you like to see about? ").lower().strip()
            user_input = beautify_string(user_input)
            name = ""
            for i in user_input:
                if ord(i) in range(256):
                    name += i
            user_input = name
            if user_input == "exit":
                break
            infile = "city info/formatted/" + user_input + ".csv"
            
            try:
                df = pd.read_csv(infile)
                ax = df.plot.bar(x='Year', y = ['Female MP Count', 'Male MP Count'], stacked=True, title='Count of MP\'s Over Time')
                break
            except:
                print("Invalid city name. Please check your input format.")

        ax.grid(axis='y', alpha = 0.8)
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        plt.xlabel("Years")
        plt.ylabel("MP Count")
        plt.show()
    elif mode == "3":
        city_list = []
        fig, ax = plt.subplots()
        while True:
            user_input = input("Which city would you like to see about? ").lower().strip() #sehrin gecerliligini kontrol et
            city_list.append(user_input)
            user_input = beautify_string(user_input)
            name = ""
            for i in user_input:
                if ord(i) in range(256):
                    name += i
            user_input = name
            if user_input == "exit":
                break
            infile = "city info/formatted/" + user_input + ".csv"
            query = int(input("Which assembly would you like to learn about? ")) #sayı girene kadar tekrar iste
            try:
                df = pd.read_csv(infile)
                ax = df.iloc[query-1]
                break
            except:
                print("Invalid city name. Please check your input format.")
        Female = ax['Female MP Count']
        Male = ax['Male MP Count']
        plt.pie([Female, Male], autopct=my_autopct)
        plt.title("Distribution of Male and Female MP's in Assembly No {}".format(query))
        plt.legend(["Female Count", "Male Count"])
        plt.show()



