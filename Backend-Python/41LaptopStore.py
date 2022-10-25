import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


class LaptopStore41_Database:
    
    client=MongoClient('mongodb://{0}:{0}@localhost:27017'.format('abvag','abvag'))
    db=client["WebScraping"]
    mycol=db["shopping_products"]
    
    def __init__(self) -> None:     
        pass
    
    def add_dict_product(self,prod_dict):
        self.mycol.insert_many(prod_dict)
        
    def add_one_product(self,dict):
        self.mycol.insert_one(dict)
        
    def control_add_product(self,prod_dict):
        
        prod= self.mycol.find()
        if(prod==None):
            
            self.add_dict_product(prod_dict)
            
        else:
            for p in prod_dict:
                    
                    for a in prod:
                        
                        if(a['prodTitle']==p['prodTitle']):
                            
                            self.delete_product(a)
                            break
               
                    self.add_one_product(p)
                  
    def delete_product(self,dict):
        
        self.mycol.delete_one(dict)
            
    def delete_col(self):
        
        self.mycol.delete_many({'site':'41LaptopStore'})


def laptopstore41():
    id= 30000
    for page in range(1,17):
        
        base_url="http://127.0.0.1:8000/?page={}".format(page)
        response=requests.get(base_url)
        soup=BeautifulSoup(response.content,'html.parser')
        products=soup.find_all('div',{'class':'col-sm-3'})
        for prod in products:
            prodTitle=prod.find('h5').text.strip()
            prodLink="127.0.0.1:8000"+prod.find('a').get('href').strip()
            rating_price=prod.find('div',{'class':'card mb-3'}).find('ul',{'class':'list-group list-group-flush'}).find_all('div',{'class':'col'})
            index=0
            for data in rating_price:
                c=data.find_all('p',{'class':'fw-bold'})
                for b in c:
                    if(index==0):
                        prodrating=b.text
                    elif(index==1):
                        prodprice=b.text
                    index=index+1
            productDict = {
                        'marka':"",
                        'modelAdi':"",
                        'modelNo':"",
                        'isletimSistemi':"",
                        'islemciTipi':"",
                        'islemciNesli':"",
                        'ram':"",
                        'diskBoyutu':"",
                        'diskTuru':"",
                        'ekranBoyu':"",
                        'puani':prodrating,
                        'fiyat':prodprice,
                        'site':'41LaptopStore',
                        'prodLink':prodLink,
                        'prodImageLink':"",
                        'prodTitle':prodTitle,
                        'id':id
                    }
            id=id+1   
            print(productDict)
  
db= LaptopStore41_Database()
db.delete_col()