import yfinance as stonk
import numpy as numpy
import pandas
import matplotlib.pyplot as plt


class inputstock:
    def __init__(self,stock):
        self.stock = stock ##Input Stock
        self.stockinfo = stonk.Ticker(self.stock) ##Yahoo finance stock
        self.hist_52_weeks = self.stockinfo.history(period="1d")
        self.hist_260_days = self.stockinfo.history(period="1d")
        self.Open = numpy.array(self.hist_52_weeks['Open']) ##OPENINGS FROM YAHOO FINANCE
        self.Close = numpy.array(self.hist_52_weeks['Close'])
        self.High = numpy.array(self.hist_52_weeks['High'])
        self.Low = numpy.array(self.hist_52_weeks['Low'])

        ##for the year
        self.Open_daily =  numpy.array(self.hist_260_days['Open']) ##OPENINGS FROM YAHOO FINANCE
        self.Close_daily = numpy.array(self.hist_260_days['Close'])
        self.High_daily = numpy.array(self.hist_260_days['High'])
        self.Low_daily = numpy.array(self.hist_260_days['Low'])
        self.daily_average = (numpy.average(self.Open_daily) + numpy.average(self.Close_daily) + numpy.average(self.High_daily) + numpy.average(self.Low_daily))/4
        
        


        
                



        
        
    

    def show(self):
        sum_1 = 0;
        sum_2 = 0;
        sum_3 = 0;
        ##global_maximum = numpy.max(numpy.array(self.hist_260_days['High']))
        ##global_minimum = numpy.min(numpy.array(self.hist_260_days['Low']))
        average_open = numpy.average(numpy.array(self.hist_260_days['Open']))
        average_close = numpy.average(numpy.array(self.hist_260_days['Close']))
        


        for i in range(len(self.hist_260_days['Open'])):
                sum_1 += self.hist_260_days['Open'][i]
        for i in range(len(self.hist_260_days['Close'])):
                sum_2 += self.hist_260_days['Close'][i]
        cumulative_average = self.daily_average;

        
        #print(self.hist_260_days['Open'])
        #print(self.hist_260_days['Close'])
        #print(self.hist_260_days['High'])
        #print(self.hist_260_days['Low'])
        Open = numpy.array(self.hist_260_days['Open'])
        Close = numpy.array(self.hist_260_days['Close'])
        High = numpy.array(self.hist_260_days['High'])
        Low = numpy.array(self.hist_260_days['Low'])
        quarterly_data = self.stockinfo.history(period="91d")
        average_daily = []
        for i in range(55):
                average_daily.append((quarterly_data['Close'][i] + quarterly_data['Open'][i] + quarterly_data['High'][i] + quarterly_data['Low'][i]))

       
        for i in range(55):
                sum_3 += (quarterly_data['Close'][i] - quarterly_data['Open'][i])/(average_daily[i])

                

        ##print(Open,Close,High,Low)
        ##x = (numpy.average(Open)+numpy.average(Close)+numpy.average(High)+numpy.average(Low))
        ##print(x/4)
        
        ##t1 = global_maximum/global_minimum
        ##t2 = average_close/average_open
        t3 = (average_close-average_open)/cumulative_average
        ##t4 = global_maximum/cumulative_average
        ##t5 = global_minimum/cumulative_average


#-------------------------------------------------------------------------------

       ## print(self.stock+"\n")
       ## print("Variables")
       ## print("Cumulative Average", cumulative_average)
       ## print("Global Max", global_maximum)
       ## print("Global Min", global_minimum)
       ## print("Average Open", average_open)
       ## print("Average Close",average_close)
       ## print("\n")
        
       ## print("Ratios")
       ## print("Global Max / Global Min =",t1)
       ## print("Average Close / Average Open =",t2)
       ## print("(Average Close - Average Open) / Cumulative Average =",t3)
       ## print("Global Max / Cumulative Average =",t4)
       ## print("Global Min / Cumulative Average =",t5)
       ## print("Updated sum ",sum_1/260)
       ## print("Updated sum ",sum_2/260)
       ## print("Updated Sum",sum_3/91)
       ## print(self.daily_average)
        return t3
        
        
    
#-------------------------------------------------------------------------------
        #print(average_max)
        #print(average_min)
        #print(average_open)
        #print(average_close)
        #print("STANDARD DEV AVG HI")
       #print("STANDARD DEV AVG LOW")
        #print(self.daily_average)

StonkSymbol = inputstock("AA")

StonkSymbol.show()



Russel2000_Tickers = pandas.read_csv('russel_2000.csv')

##print(Russel2000_Tickers)

dataframe = Russel2000_Tickers["AA"]
##print(type(dataframe))


##len(dataframe)




Russel2000_Tickers = pandas.read_csv('russel_2000.csv')

##print(Russel2000_Tickers)

dataframe = Russel2000_Tickers["AA"]
##print(type(dataframe))


len(dataframe)


list = ["AAPL","TSLA","CRM","GE","F","GOOGL","FB","SNAP","AMD","NVDA","ABT","MMM","A","ALB","ALG","BBY","BLK","BA","C","CSCO","KO","AMZN","COST","CBS","FANG","DTE","EQIX","GM","HAL","HPQ","JPM","KEY","LNT","MRO","MGM","MSFT","NSLX","NKE","OXY","PEP","QCOM","RSG","ROL","STE","TXT","TSN","ULTA","VISC","V","WMT","ZION"]
##list = ["AAPL","TSLA","GE","F"]




##plt.plot([1,2,3,4])
##plt.ylabel('some numbers')
##plt.show()


##print(list)
ratio_list = []
for i in range(len(dataframe)):
        list.append(dataframe[i])
        
for i in range(len(list)):
        try:
                stocksymbol = inputstock(list[i])
                g = stocksymbol.show()
                ratio_list.append(g)
        except IndexError:
                continue


x = ratio_list
num_bins = 5
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.show()



#print(g)


