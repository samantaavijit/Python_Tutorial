import requests

r = requests.get("https://financialmodelingprep.com/api/v3/income-statement-as-reported/AAPL?apikey=demo")
print(r.text)
print(r.status_code)

# url = "www.abc.com"
# data = {
#     "p1": 4,
#     "p2": 2
# }
# r2 = requests.post(url=url, data=data)
