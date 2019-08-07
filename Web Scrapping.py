import requests, json, re


html = requests.get('https://www.daraz.pk/catalog/?q=Bridal%20dress').text


jsonStr = re.search(r'window.pageData=(.*?)</script>', html).group(1)
jsonObject = json.loads(jsonStr)




filename = "Bridal Dress.csv"
f = open(filename, "w")


headers = "product_name, price\n"
f.write(headers)






for item in jsonObject['mods']['listItems']:
         print(item['name'])
         print(item['price'])
         f.write(item['name'].replace(",","") +","+ item['price'].replace(",","") + "\n")


f.close()
