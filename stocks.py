# Program name: stocks.py
# Your Name: Aerin Schmall
# Python Version: 3.7.8
# Date Started - Date Finished: 9/14/2020 - 9/14/2020
# Description: takes data from file-1.csv and prints out average stocks for each month in a table.

data_list = {'2008':{}, '2007':{},'2006':{},'2005':{},'2004':{}}
file = open('table-1.csv', 'r')
line = file.read().split('\n')
def get_data_list (line):
      line.pop(0)
      line.remove('')
      for i in line:
            g = str(i).split(',')
            if g[0][5:7] not in data_list[g[0][:4]]:
                  data_list[g[0][:4]][g[0][5:7]] = [g[6]]
            else:
                  data_list[g[0][:4]][g[0][5:7]].append(g[6])
            
      get_monthly_averages(data_list) # just nested the functions instead of returning and then calling outside
            
def get_monthly_averages (line):
      
      for i in line:
            for j in line[i]:
                  aver = 0
                  for k in line[i][j]:
                        aver += float(k)
                  line[i][j] = aver / len(line[i][j])
      print_info(line)
                  

def print_info (line):
      count = 1
      
      print("                           'Month' | 'Year' | 'Average'")
      print('                           --------|--------|----------')
      for i in line:
            for j in line[i]:
                  if count < 10:
                        print(f"monthly_average_list[0{count}]  =  '{j}'  | '{i}' | '%.2f'" %line[i][j])
                  else:
                        print(f"monthly_average_list[{count}]  =  '{j}'  | '{i}' | '%.2f'" %line[i][j])
                  count+=1 # sorry that it's a dictionary that data is pulled from and not a printed list

get_data_list(line)            
file.close()
# this is to make up for using a dictionary instead of list
def stock():
      import urllib3
      print('\nthe current price of alphabet inc.(google\'s parent company) stock is $', end='')
      http = urllib3.PoolManager()
      url = "https://markets.businessinsider.com/stocks/googl-stock"
      page = http.request('POST', url)
      html_binary = page.data
      html = html_binary.decode("utf-8")
      title_index = html.find('<span class="price-section__current-value">')
      new_page = html[title_index:]
      start_index = len('<span class="price-section__current-value">')
      end_index = new_page.find("</span>")
      title = new_page[start_index:end_index]
      print(title)
stock()
'''
============= RESTART: C:\\Users\\aerin\\Documents\\Python\\stocks.py ==============
                           'Month' | 'Year' | 'Average'
                           --------|--------|----------
monthly_average_list[01]  =  '09'  | '2008' | '437.70'
monthly_average_list[02]  =  '08'  | '2008' | '485.91'
monthly_average_list[03]  =  '07'  | '2008' | '510.03'
monthly_average_list[04]  =  '06'  | '2008' | '556.32'
monthly_average_list[05]  =  '05'  | '2008' | '575.92'
monthly_average_list[06]  =  '04'  | '2008' | '497.58'
monthly_average_list[07]  =  '03'  | '2008' | '440.33'
monthly_average_list[08]  =  '02'  | '2008' | '503.80'
monthly_average_list[09]  =  '01'  | '2008' | '611.81'
monthly_average_list[10]  =  '12'  | '2007' | '695.40'
monthly_average_list[11]  =  '11'  | '2007' | '676.37'
monthly_average_list[12]  =  '10'  | '2007' | '635.39'
monthly_average_list[13]  =  '09'  | '2007' | '540.43'
monthly_average_list[14]  =  '08'  | '2007' | '509.83'
monthly_average_list[15]  =  '07'  | '2007' | '532.48'
monthly_average_list[16]  =  '06'  | '2007' | '515.02'
monthly_average_list[17]  =  '05'  | '2007' | '473.01'
monthly_average_list[18]  =  '04'  | '2007' | '472.50'
monthly_average_list[19]  =  '03'  | '2007' | '452.91'
monthly_average_list[20]  =  '02'  | '2007' | '467.22'
monthly_average_list[21]  =  '01'  | '2007' | '490.58'
monthly_average_list[22]  =  '12'  | '2006' | '473.50'
monthly_average_list[23]  =  '11'  | '2006' | '485.63'
monthly_average_list[24]  =  '10'  | '2006' | '440.53'
monthly_average_list[25]  =  '09'  | '2006' | '397.06'
monthly_average_list[26]  =  '08'  | '2006' | '377.09'
monthly_average_list[27]  =  '07'  | '2006' | '403.53'
monthly_average_list[28]  =  '06'  | '2006' | '393.59'
monthly_average_list[29]  =  '05'  | '2006' | '383.80'
monthly_average_list[30]  =  '04'  | '2006' | '413.78'
monthly_average_list[31]  =  '03'  | '2006' | '358.87'
monthly_average_list[32]  =  '02'  | '2006' | '370.00'
monthly_average_list[33]  =  '01'  | '2006' | '445.71'
monthly_average_list[34]  =  '12'  | '2005' | '418.95'
monthly_average_list[35]  =  '11'  | '2005' | '399.14'
monthly_average_list[36]  =  '10'  | '2005' | '322.47'
monthly_average_list[37]  =  '09'  | '2005' | '304.24'
monthly_average_list[38]  =  '08'  | '2005' | '286.92'
monthly_average_list[39]  =  '07'  | '2005' | '298.21'
monthly_average_list[40]  =  '06'  | '2005' | '287.55'
monthly_average_list[41]  =  '05'  | '2005' | '239.71'
monthly_average_list[42]  =  '04'  | '2005' | '199.21'
monthly_average_list[43]  =  '03'  | '2005' | '181.16'
monthly_average_list[44]  =  '02'  | '2005' | '195.01'
monthly_average_list[45]  =  '01'  | '2005' | '192.85'
monthly_average_list[46]  =  '12'  | '2004' | '181.77'
monthly_average_list[47]  =  '11'  | '2004' | '177.50'
monthly_average_list[48]  =  '10'  | '2004' | '153.23'
monthly_average_list[49]  =  '09'  | '2004' | '113.23'
monthly_average_list[50]  =  '08'  | '2004' | '105.26'

the current price of alphabet inc.(google's parent company) stock is $1,763.93
'''
