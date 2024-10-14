import requests
class Dota2Market:
    
    def __init__(self,key = None):
        self._key = key

    def set_key(self, x):
        self._key = x
    
    def get_key(self):
        self._key

    def get_min_price_item(self,name_item):
        """
        
        """
        url = f"https://market.dota2.net/api/SearchItemByName/{name_item}/?key={self._key}"
        response = requests.request("POST", url)
        price = response.text.split(',')[7]
        price = price.split(':')[1]
        full_price = list(str(price))
        end = ''.join(full_price[-2:])
        full_price = ''.join(full_price[:-2])  + '.' + end
        return full_price
    

