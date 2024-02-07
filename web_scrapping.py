import requests
from bs4 import BeautifulSoup

#class="table table-hover live-trading sortable"

html_text = requests.get("https://merolagani.com/LatestMarket.aspx")
soup = BeautifulSoup(html_text.text, "lxml")
table_data = soup.find("table", class_="table table-hover live-trading sortable")

t_body = table_data.find("tbody")
tr_datas = t_body.find_all("tr")
i=1
# tr_data = tr_datas
for tr_data in tr_datas:
    td_datas = tr_data.find_all("td")
    # print(td_company_name.text)
    a = []
    # i=1
    for td_data in td_datas:
        if td_data.text == "":
            continue
        
        a.append(td_data.text)
        # print(td_data.text)
    
    try:
        print(f"{i} \t {a[0]} \t\t {a[1]} \t\t {a[2]} \t\t {a[3]} \t\t {a[4]} \t\t {a[5]} \t\t {a[6]} \t\t {a[7]} \t\t {a[8]} \t\t {a[9]}  ")
    except:
        print(f"{i} \t {a[0]} \t\t {a[1]} \t\t {a[2]} \t\t {a[3]} \t\t {a[4]} \t\t {a[5]} \t\t {a[6]} \t\t   ")
    i=i+1
    a.clear()

# print(table_data)

