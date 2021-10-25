# KhushiKhandelwal_python_assign_rpd
Problem Statement 1:
Python script to automate the task of downloading csv from zacks website
By following steps given below
1) go to a url, https://www.zacks.com/screening/stock-screener?icid=screening-screening-nav_tracking-zcom-main_menu_wrapper-stock_screener
2)click "my screens"
3)Click "run" with "Companies All" selected
4) click export to csv

Expected output should be zacks_custom_screen_<current date>.csv
login id: laboc57506@ampswipe.com
pass: msJ$eb8EJu72@Bj

The Python script for this task is zacks.py and csv file that is downloaded is in the same format as mentioned above.
  
Problem Statement 2
https://www.zacks.com/funds/etf/veu/holding
Using the above url , extract all page data for column:date	Security name	Symbol	shares	weight% 52 Change(%).

It shows next page but it does not reload page.Check if page already have all page data so no need of pagination.
The Python script for this task is veu.py and extracted data is stored in VEU.xlsx
  
Problem statement 3  
data.csv contains a ticker name as "veu" so we can replace that name from the ticker name from the following csv to extract data for all so in future more tickers can be added.

Expected output file should have name like (ticker_name.csv)
The python script for this task is ticker.py and final csv is named as ticker_name.csv
  
