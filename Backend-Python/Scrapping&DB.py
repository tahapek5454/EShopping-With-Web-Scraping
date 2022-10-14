from pyexpat import model
import requests
from bs4 import BeautifulSoup
import getpass



class WebScrapping:

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }

    # where append all all product
    pcN11List=[]
    pcTeknosaList=[]
    pcHepsiBuradaList=[]
    pcTrendyolList=[]
    pcCicekSepetiList=[]


    def __init__(self) -> None:
        pass

    def n11(self):
        
        # n11'de image urlleri çekildi. title çekildi. link çekildi.
        
        
        productLinks = [] # all product link that visited
        productPrice = [] # all product price that visited
        productImageLinks=[] # all product imagelinks that visited
        productTitle=[] # all product prodtitles that visited
        index = 0

        for urlIndex in range(1,2):
            # 
            # https://www.n11.com/bilgisayar/dizustu-bilgisayar
            urlForN11 = f'https://www.n11.com/bilgisayar/dizustu-bilgisayar?pg={urlIndex}'
            response = requests.get(urlForN11)
            html = response.content #response ı html icerigine ceviriyoruz
            soup = BeautifulSoup(html, 'html.parser') #icerigi parse ediyoruz

            

            liste = soup.find('ul', {'class':'list-ul'}).find_all('li', {'class':'column'}, limit=10) #tüm listeyi al
            # n11 page 1 de 24 urun var
            

            for item in liste:
                link = item.find('a', {'class':'plink'}).get('href')
                productLinks.append(link)

                price = item.find('div', {'class':'proDetail'}).find('div', {'class':'priceContainer'})\
                .find('span', {'class':'newPrice cPoint priceEventClick'}).ins.text
                productPrice.append(price)
                
                image = item.find('img',{'class':'lazy cardImage'}).get('data-images')
                productImageLinks.append(image)
                
                title=item.find('h3',{'class':'productName'})
                productTitle.append(title.text)
        
        
        for link in productLinks:
            response2 = requests.get(link, headers=self.headers)
            html2 = response2.content
            soup2 = BeautifulSoup(html2, 'html.parser')

            features = soup2.find_all('li', {'class':'unf-prop-list-item'})
            # feaures has 23 attribute
            raiting = soup2.find('div', {'class':'ratingCont'}).strong.text.strip()      
            # dynamc raiting
                 
            for feaure in features:

                if feaure.p.text == 'Marka':
                    marka = feaure.find_all('p')[1].text.strip()
                
                elif feaure.p.text == 'Model':
                    modelAdi = feaure.find_all('p')[1].text.strip()
                
                elif feaure.p.text == 'İşletim Sistemi':
                    isletimSistemi = feaure.find_all('p')[1].text.strip()

                elif feaure.p.text == 'İşlemci':
                    islemciTipi = feaure.find_all('p')[1].text.strip()
                
                elif feaure.p.text == 'İşlemci Modeli':
                    islemciNesli = feaure.find_all('p')[1].text.strip()
                
                elif feaure.p.text == 'Bellek Kapasitesi':
                    ram = feaure.find_all('p')[1].text.strip()
                
                elif feaure.p.text == 'Disk Kapasitesi':
                    diskBoyutu = feaure.find_all('p')[1].text.strip()
                
                elif feaure.p.text == 'Disk Türü':
                    diskTuru = feaure.find_all('p')[1].text.strip()
                
                elif feaure.p.text == 'Ekran Boyutu':
                    ekranBoyutu = feaure.find_all('p')[1].text.strip()
                  
            puani = raiting     
            fiyat = productPrice[index]
            imageLink=productImageLinks[index]
            prodTitle=productTitle[index]
            index = index + 1
            model_no_list=modelAdi.split(' ')
            if(len(model_no_list)==1):
                if(model_no_list[0].find('-')!=-1):
                    model_list_split=model_no_list[0].split('-')
                    modelAdi=model_list_split[0]
                    model_no=model_list_split[1]
                else:
                    modelAdi='Belirtilmemiş'
                    model_no=model_no_list[0]
            else:
                model_no=model_no_list[len(model_no_list)-1]
                model_name=""
                for x in range(0,len(model_no_list)-1):
                    model_name+=model_no_list[x]
                    model_name+=" "
            site = 'n11'

            productDict = {
                'marka':marka,
                'modelAdi':model_name,
                'modelNo':model_no,
                'isletimSistemi':isletimSistemi,
                'islemciTipi':islemciTipi,
                'islemciNesli':islemciNesli,
                'ram':ram,
                'diskBoyutu':diskBoyutu,
                'diskTuru':diskTuru,
                'ekranBoyu':ekranBoyutu,
                'puani':puani,
                'fiyat':fiyat,
                'site':site,
                'prodLink':link,
                'prodImageLink':imageLink,
                'prodTitle':prodTitle
            }
            self.pcN11List.append(productDict)

# sıkıntılı
    def hepsiBurada(self):
        productLinks = []
        productTitles=[]
        index=0
        # sayfaki genel tum urunlerin linkini alma kısmı
        for urlIndex in range(1,2):
            urlForHepsiBurada = f'https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98?sayfa={urlIndex}'
            # first page
            response = requests.get(urlForHepsiBurada, headers=self.headers)
            html = response.content
            soup = BeautifulSoup(html, 'html.parser')

            products = soup.find('ul', {'class':'productListContent-frGrtf5XrVXRwJ05HUfU productListContent-rEYj2_8SETJUeqNhyzSm'})\
                        .find_all('li', {'class':'productListContent-zAP0Y5msy8OHn5z7T_K_'}, limit=1)
            
            for item in products:
                #print(item)
                link = item.a.get('href')
                productLinks.append('https://www.hepsiburada.com'+link)
                
                title=item.h3.text
                productTitles.append(title)
                
                image=item.find('div',{'class':'moria-ProductCard-dhSYSm iVMOsM sip5m7paym9'})
                
                # all link
            
        # print(len(productLinks))
        # print(productLinks)
        
        for link in productLinks:
            # icerde gezip ozellikleri alıcaz
            response2 = requests.get(link, headers=self.headers)          
            html2 = response2.content #response ı html icerigine ceviriyoruz
            soup2 = BeautifulSoup(html2, 'html.parser') #icerigi parse ediyoruz

            price = soup2.find('span', {"data-bind":"markupText:'currentPriceBeforePoint'"}).text.strip()
            # tam kismi
            price += ','+soup2.find('span', {'data-bind':"markupText:'currentPriceAfterPoint'"}).text.strip()
            # kurus kismi

            try:
                # bazı ürünlerde rating olmuyor exception fırlatıyor otomatik sıfır atarız
                rating = soup2.find('span', {'class':'rating-star'}).text.strip()
            except Exception as ex:
                rating = str(0)

            name = soup2.find('h2', {'class':'product-features-text'}).text.strip().split(' ')[0]
                    #bu sekilde texte ilk basta marka ismi oluyor onu cektik
            
            print(name)
            print("")
            
            features = soup2.find('table', {'class':'data-list tech-spec'}).find_all('tr')

            for feaure in features:
                
                if feaure.th.text == 'İşletim Sistemi':
                    
                    if feaure.td.span == None:
                        isletimSistemi = feaure.td.a.text.strip()
                    else:
                        isletimSistemi = feaure.td.span.text.strip()

                elif feaure.th.text == 'İşlemci Tipi':
                    
                    if feaure.td.span == None:
                        islemciTipi = feaure.td.a.text.strip()
                    else:
                        islemciTipi = feaure.td.span.text.strip()
                
                elif feaure.th.text == 'İşlemci Nesli':
                   
                    if feaure.td.span == None:
                        islemciNesli = feaure.td.a.text.strip()
                    else:
                        islemciNesli = feaure.td.span.text.strip()
                
                elif feaure.th.text == 'Ram (Sistem Belleği)':
                    if feaure.td.span == None:
                        ram = feaure.td.a.text.strip()
                    else:
                        ram = feaure.td.span.text.strip()
                
                elif feaure.th.text == 'SSD Kapasitesi':
                    # if feaure.get('a').text.strip() != 'Yok':
                    #     try:
                    #         diskBoyutu = feaure.span.text.strip()
                    #     except:
                    #         diskboyutu=feaure.get('a').text.strip()
                    #     diskTuru='SSD'
                    
                    if feaure.td.span == None:
                        if feaure.td.a.text.strip() != "Yok":
                            diskBoyutu = feaure.td.a.text.strip()
                            diskTuru='SSD'
                    else:
                        if feaure.td.span.text.strip() != "Yok":
                            diskBoyutu = feaure.td.span.text.strip()
                            diskTuru='SSD'


                
                elif feaure.th.text == 'Harddisk Kapasitesi':
                    if feaure.td.span == None:
                        if feaure.td.a.text.strip() != "Yok":
                            diskBoyutu = feaure.td.a.text.strip()
                            diskTuru='HDD'
                    else:
                        if feaure.td.span.text.strip() != "Yok":
                            diskBoyutu = feaure.td.span.text.strip()
                            diskTuru='HDD'
       
                elif feaure.th.text == 'Ekran Boyutu':
                    if feaure.td.span == None:
                        ekranBoyutu = feaure.td.a.text.strip()
                        
                    else:
                        ekranBoyutu = feaure.td.span.text.strip()
                    

                        
                    
            
            puani = rating
            fiyat = price
            title= productTitles[index]
            site="hepsiburada"
            modelNo=""
            modelAdi=""
            marka = name
            index=index+1
            


            productDict = {
                'marka':marka,
                'modelAdi':modelAdi,
                'modelNo':modelNo,
                'isletimSistemi':isletimSistemi,
                'islemciTipi':islemciTipi,
                'islemciNesli':islemciNesli,
                'ram':ram,
                'diskBoyutu':diskBoyutu,
                'diskTuru':diskTuru,
                'ekranBoyu':ekranBoyutu,
                'puani':puani,
                'fiyat':fiyat,
                'site':site,
                'prodLink': link,
                'prodTitle':title,
                'imageLink':"",      
            }


            print(productDict)
            print('*'*100)

            # eksikler - modelNo - modelAdi

    def trendyol(self):
        
        product_urls=[]
        product_names=[]
        product_prices=[]
        product_modal_names=[]
        product_ratings=[]
        product_image_urls=[]
        product_titles=[]
        index2=0
        for page in range(1,2):
            base_url="https://www.trendyol.com/laptop-x-c103108?pi={0}".format(page)
            response=requests.get(base_url)
            soup=BeautifulSoup(response.content,'html.parser')
            products=soup.find('div',{'class':'prdct-cntnr-wrppr'}).find_all('div',{'class':'p-card-wrppr'},limit=2)
            for product in products:
                url=product.find('a').get('href')
                product_url="https://www.trendyol.com"+url
                product_urls.append(product_url)
                product_name=product.find('span',{'class':'prdct-desc-cntnr-ttl'}).text
                product_names.append(product_name)
                product_price=product.find('div',{'class':'prc-box-dscntd'}).text.split(' ')[0]
                product_prices.append(product_price)
                product_modal_name=product.find('div',{'class':'prdct-desc-cntnr-ttl-w two-line-text'}).find('span',{'class':'prdct-desc-cntnr-name'}).text.split(' ')[0]
                product_modal_names.append(product_modal_name)
                product_title=product.find('span',{'class':'prdct-desc-cntnr-name'})
                product_titles.append(product_name+" "+product_title.text)
              
                try:
                    puan = product.find('div',{'class':'product-down'}).find('div',{'class':'ratings-container'}).find('div',{'class':'ratings'}).find_all('div',{'class':'star-w'})
                except:
                    puan=None
                    
                index=0
                toplam=0
                if(puan is not None):
                        for x in puan:
                                m=str(x.find('div',{'class':'full'},{'style':'width'})).split(':')
                                if(m[1].split('%')[0]!='0;max-width'):
                                    toplam+=int(m[1].split('%')[0])
                                    index+=1
                                else:
                                    str2=str(m[1].split('%')[0]).split(';')[0]
                                    toplam+=int(str2)
                                    index+=1   
                                if(index==5):
                                    rating=toplam/100.0
                                    product_ratings.append(rating)
                                    toplam=0
                                    index=0     
                else:
                    product_ratings.append('Puanlanmamış')    
        for url in product_urls:
            response2=requests.get(url)
            soup2=BeautifulSoup(response2.content,'html.parser')
            features=soup2.find('div',{'class':'detail-border'}).find('ul',{'class':'detail-attr-container'}).find_all('li')
            image_url=soup2.find('main',{'id':'product-detail-app'}).find('img')
            product_image_urls.append(image_url['src'])
            disk_tipi=""
            toplam_kapasite=""
            for feature in features:
                if(feature.span.text=='İşlemci Tipi'):
                    islemci_tipi=feature.find_all('span')[1].text
                elif(feature.span.text=='İşletim Sistemi'):
                    isletim_sistemi=feature.find_all('span')[1].text
                elif(feature.span.text=='İşlemci Nesli'):
                    islemci_nesli=feature.find_all('span')[1].text
                elif(feature.span.text=='SSD Kapasitesi'):
                    ssd_kapasitesi=feature.find_all('span')[1].text
                    disk_tipi="SSD"
                elif(feature.span.text=='Ekran Boyutu'):
                    ekran_boyutu=feature.find_all('span')[1].text
                elif(feature.span.text=='Ram (Sistem Belleği)'):
                    ram=feature.find_all('span')[1].text
                elif(feature.span.text=='Hard Disk Kapasitesi'):
                    hdd_kapasitesi=feature.find_all('span')[1].text
            
            if(hdd_kapasitesi=="Yok" or hdd_kapasitesi=='HDD Yok'):
                disk_tipi="SSD"
                toplam_kapasite=ssd_kapasitesi
            elif(ssd_kapasitesi=="Yok" or ssd_kapasitesi=='SSD Yok'):
                disk_tipi="HDD"
                toplam_kapasite=hdd_kapasitesi
            elif((ssd_kapasitesi!="Yok" or ssd_kapasitesi!="SSD Yok") and (hdd_kapasitesi!="Yok" or hdd_kapasitesi!='HDD Yok')):
                disk_tipi='SSD+HDD'
                toplam_kapasite=ssd_kapasitesi+"/"+hdd_kapasitesi   
                
            model_no=""
            pro_price=product_prices[index2]
            pro_name=product_names[index2]
            pro_modal_name=product_modal_names[index2]
            pro_rating=product_ratings[index2]
            pro_url=product_urls[index2]
            pro_image_url=product_image_urls[index2]
            pro_title=product_titles[index2]
            index2=index2+1
            pro_site="Trendyol"
            
            productDict = {
                        'marka':pro_name,
                        'modelAdi':pro_modal_name,
                        'modelNo':model_no,
                        'isletimSistemi':isletim_sistemi,
                        'islemciTipi':islemci_tipi,
                        'islemciNesli':islemci_nesli,
                        'ram':ram,
                        'diskBoyutu':toplam_kapasite,
                        'diskTuru':disk_tipi,
                        'ekranBoyu':ekran_boyutu,
                        'puani':pro_rating,
                        'fiyat':pro_price,
                        'imageLink':pro_image_url,
                        'prodLink':url,
                        'prodTitle':pro_title,
                        'site':pro_site
                    }
  
            self.pcTrendyolList.append(productDict)
                
            
    def teknosa(self):
        for page in range(1,2):
            base_url="https://www.teknosa.com/laptop-notebook-c-116004?s=%3Arelevance&page={0}".format(page)
            headers={
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
            }

            response=requests.get(base_url,headers=self.headers)
            soup=BeautifulSoup(response.content,'html.parser')

            products=soup.find('div',{'class':'products'}).find_all('div',{'id':'product-item'})

            product_links=[]
            product_titles=[]
            product_prices=[]
            product_marka_names=[]
            product_base_image_urls=[]
            index2=0

            for product in products:
                product_url=product.find('a',{'class':'prd-link'}).get('href')
                product_base_url="https://www.teknosa.com"+product_url
                product_links.append(product_base_url)
                product_title=product.find('div',{'class':'prd-body'}).h3.text.strip()
                product_titles.append(product_title)
                product_price=product.find('div',{'class':'prd-amount'}).find('div',{'class':'prd-prc2'}).span.text
                product_prices.append(product_price.strip())
                product_marka_names.append(product_title.split(' ')[0])
                product_base_image_url=product.find('div',{'class':'prd-media'}).find('figure',{'class':'responsive'}).find('img').get('data-srcset')
                if product_base_image_url is None:
                    product_base_image_url=product.find('div',{'class':'prd-media'}).find('figure',{'class':'responsive'}).find('img').get('src')
                    product_base_image_urls.append(product_base_image_url)
                else:
                    product_base_image_urls.append(product_base_image_url)

        for pr_link in product_links:
            
            response2=requests.get(pr_link,headers=self.headers)
            soup2=BeautifulSoup(response2.content,'html.parser')
            
            product_rating=soup2.find('div',{'class':'bv-flex-container-column'})
            features=(soup2.find('div',{'class':'pdp-accordion'}).find('div',{'class':'pdp-acc pdp-section'}).find('div',{'class':'ptf-body'}).find_all('table'))
            nammes=[]
            fss=[] 
            for m in features:
                names=m.find_all('th')
                for name in names:
                    nammes.append(name.text)
                fs=m.find_all('td')
                for fsss in fs:
                    fss.append(fsss.text) 
            
            for i in range(0,len(nammes)):
                
                if(nammes[i]=='SSD Kapasitesi'):
                    ssd_kapasitesi=fss[i]
                elif(nammes[i]=='Ekran Boyutu'):
                    ekran_boyutu=fss[i]
                elif(nammes[i]=='Model Kodu'):
                    model_kodu=fss[i]
                elif(nammes[i]=='HDD Kapasitesi'):
                    hdd_kapasitesi=fss[i]
                elif(nammes[i]=='Disk Türü'):
                    disk_turu=fss[i]
                elif(nammes[i]=='İşlemci'):
                    islemci=fss[i]
                elif(nammes[i]=='İşlemci Nesli'):
                    islemci_nesli=fss[i]
                elif(nammes[i]=='İşletim Sistemi Yazılımı'):
                    isletim_sistemi=fss[i]
                elif(nammes[i]=='Ram'):
                    ram=fss[i]
            
            pro_title=product_titles[index2]
            pro_price=product_prices[index2]
            pro_name=product_marka_names[index2]
            pro_modal_name=product_titles[index2].split(' ')[1]
            pro_url=product_links[index2]
            pro_image_url=product_base_image_urls[index2]
            index2=index2+1
            pro_site="Trendyol"
            
            if(hdd_kapasitesi!='Yok' and ssd_kapasitesi!='Yok'):
                kapasite=(hdd_kapasitesi)+(ssd_kapasitesi)
                disk_turu='SSD+HDD'
            elif(hdd_kapasitesi=='Yok' and ssd_kapasitesi!='Yok'):
                kapasite=ssd_kapasitesi
                disk_turu='SSD'
            elif(ssd_kapasitesi=='Yok' and hdd_kapasitesi!='Yok'):
                kapasite=hdd_kapasitesi
                disk_turu='HDD'
            
            
            productDict = {
                            'marka':pro_name,
                            'modelAdi':pro_modal_name,
                            'modelNo':model_kodu,
                            'isletimSistemi':isletim_sistemi,
                            'islemciTipi':islemci,
                            'islemciNesli':islemci_nesli,
                            'ram':ram,
                            'diskBoyutu':kapasite,
                            'diskTuru':disk_turu,
                            'ekranBoyu':ekran_boyutu,
                            'puani':'0',
                            'fiyat':pro_price,
                            'prodLink':pr_link,
                            'imageLink':pro_image_url,
                            'prodtitle':pro_title,
                            'site':pro_site
            }
            
            print(productDict)
            print('*'*100)

    def ciceksepeti(self):
        product_links = []
        product_prices = []
        product_disc_types = []
        product_image_links=[]
        product_titles=[]
        index = 0
        for aa in range(1,3):
            urlForCicekSepeti = "https://www.ciceksepeti.com/dizustu-bilgisayar-laptop?page={0}".format(aa)
            print("Processing for {0}".format(urlForCicekSepeti))
            response=requests.get(urlForCicekSepeti)
            html=response.content
            soup=BeautifulSoup(html,'html.parser')
            isletimsistemi='Freedos'
            product_list=soup.find('div',{'class':'products'}).find_all('div',{'class':'products__item'},limit=5)


            for item in product_list:
                  
                    link=item.find('a',{'class':'products__item-link'}).get('href')
                    product_url='https://www.ciceksepeti.com'+link
                    product_links.append(product_url)
                    
                    product_price=item.find('div',{'class':'price price--now'}).find('div',{'class':'price__left'}).find('span',{'class':'price__integer-value'}).text
                    product_prices.append(product_price)
                    
                    prod_image_link=item.find('img',{'class':'products__item-img lazyload'}).get('data-src')
                    product_image_links.append(prod_image_link)
                    
                    prod_title=item.find('p',{'class':'products__item-title'}).text
                    product_titles.append(prod_title)

        for url in product_links:
            response2 = requests.get(url)
            soup2=BeautifulSoup(response2.content,'html.parser')
            marka3=soup2.find('h1',{'class':'product__info__title'}).find('span',{'class':'js-product-title'}).text
            if(marka3.find('SSD')!=-1):
                product_disc_types.append('SSD')
            elif(marka3.find('HDD')!=-1):
                product_disc_types.append(('HDD'))
            else:
                product_disc_types.append(('Belirtilmemiş'))
            table=soup2.find_all('div',{'class':'product__specifications__table-row'})
            islemcinesli=""
            kapasite=""
            for feature in table:
                x=feature.find('div',{'class':'product__specifications__table-cell'}).text
                if(x=='Renk'):
                    renk=feature.find_all('div',{'class':'product__specifications__table-cell'})[1].text.strip()
                elif(x=='Ekran Boyutu'):
                    ekran_boyutu = feature.find_all('div', {'class': 'product__specifications__table-cell'})[1].text.strip()
                elif (x == 'Kapasite'):
                    kapasite = feature.find_all('div', {'class': 'product__specifications__table-cell'})[1].text.strip()
                elif (x == 'Ram (Sistem Belleği)'):
                    ram = feature.find_all('div', {'class': 'product__specifications__table-cell'})[1].text.strip()
                elif (x == 'İşlemci Tipi'):
                    islemci_tipi = feature.find_all('div', {'class': 'product__specifications__table-cell'})[1].text.strip()
                elif (x == 'İşlemci Çekirdek Sayısı'):
                    islemci_cekirdek_sayisi = feature.find_all('div', {'class': 'product__specifications__table-cell'})[1].text.strip()
                elif(x=='İşletim Sistemi'):
                    isletimsistemi= feature.find_all('div', {'class': 'product__specifications__table-cell'})[1].text.strip()
                elif(x=='İşlemci Nesli'):
                    islemcinesli= feature.find_all('div', {'class': 'product__specifications__table-cell'})[1].text.strip()
            if(islemcinesli==""):
                nesil=soup2.find('div',{'class':'product__description-text--left'}).find('div',{'class':'product__recipe-body'}).find('div',{'class':'product__description-text'}).find('div',{'class':'js-clear-inline-styles'}).find_all('tr')
                for x in nesil:
                    try:
                        if(x.find('td').text=='İşlemci' or x.find('td').text=='İşlemci Nesli'):
                            islemcinesli=x.find('tr')
                    except:
                            islemcinesli='Belirtilmemiş'
            if(kapasite=="" or kapasite=="Yok"):
                try:
                    nesil = soup2.find('div', {'class': 'product__description-text--left'}).find('div', { 'class': 'product__recipe-body'}).find('div', {'class': 'product__description-text'}).find('div', {'class': 'js-clear-inline-styles'}).find_all('tr')
                    for x in nesil:
                        try:
                            if(x.find('td').text=='SSD Kapasitesi' or x.find('td').text=='Kapasite'):
                                kapasite=x.find('tr')
                            else:
                                kapasite='Belirtilmemiş'
                        except:
                            kapasite='Belirtilmemiş'
                except:
                    kapasite='Belirtilmemiş'
            if(kapasite=='Yok'):
                kapasite='Belirtilmemiş'
            print(index)
            fiyat=product_prices[index]
            disk_tipi=product_disc_types[index]
            imageLink=product_image_links[index]
            prodTitle=product_titles[index]
            index=index+1
            model_no="Belirtilmemiş"
            model_adi=prodTitle.split(" ")[1]
            title_split=prodTitle.split(' ')
            marka=title_split[0]
            model_no=self.cs_modalnoshaper(prodTitle)
            site='Çiçek Sepeti'
            puani='0'
            

            productDict = {
                        'marka':marka,
                        'modelAdi':model_adi,
                        'modelNo':model_no,
                        'isletimSistemi':isletimsistemi,
                        'islemciTipi':islemci_tipi,
                        'islemciNesli':islemcinesli,
                        'ram':ram,
                        'diskBoyutu':kapasite,
                        'diskTuru':disk_tipi,
                        'ekranBoyu':ekran_boyutu,
                        'puani':puani,
                        'fiyat':fiyat,
                        'prodLink':url,
                        'imageLink':imageLink,
                        'prodTitle':prodTitle,
                        'site':site
                    }

            print(productDict)
            print('*'*100)
            self.pcCicekSepetiList.append(productDict)
        

# AMD Kontrol et 
    def shapeIslemciNesli(self, item):
        
        # bu metod 11 - 12 - 10 tarzı yazar
        # bulunamadi veya yok tarzı yazılara yok yazar
        # amd ryzen gibi seylerde yok yazıyor
        # simdilik sadece printletiyorum deger dondurmuyorum
        if item.find('.') != -1:
            # nokta bulundu
            item = item[:item.find('.')].strip()
        elif item.find('-') != -1:
            item = item[item.find('-')+1:item.find('-')+3].strip()
        else:
            item = 'yok'
    
    def shapeFiyat(self, item):
        
        if item.find('T') !=-1 :
            item = item[:item.find('T')].strip()

        
        if item.find('.') != -1 :
            item = item.replace('.','')
         
        
        if item.find(',') != -1:
            item = item.replace(',','.')
         

        # finish cleaning

        # str to float

        item = float(item)
        print(item, type(item))

        # format tam.kurus
    
    def shapeEkranBoyutu(self, item):

        if item.find('"') != -1:
            item = item[:item.find('"')].strip()
        
        elif item.find('i') != -1:
            item = item[:item.find('i')].strip()

        if item.find('.') != -1:
            item = item.replace('.',',')
        

        # string tipinde 14,6 ya da 14 seklinde dondurur
    
    def shapeIsletimSistemi(self, item):

        if item.find('Free') != -1:
            item = 'Freedos'
        
        # cogunluk zaten free dos ya da windows 11 home falan
        # bazı kıl adamlar sadece window yazmıs hic onu kurcalamadım kalsın öyle ugrasılmaz
        # sorguda gelmez olur biter zaten cok pc olucak
        # freedosların yazımı farkılı geliyor sitelerde Free yi gordu mu kod otomatik Freedos yazıypr
     
    # Çiçeksepeti sitesindeki Asus,Lenovo,Msi markalarının model numaralarını çekmeyi sağlayan fonksiyondur  
    def cs_modalnoshaper(self,title):
        
        title_split=title.split(' ')
        marka=title_split[0]
        print(marka)
        if(marka=="Lenovo" or marka=="LENOVO"):
            if((title_split[-1]).startswith('20') or (title_split[-1]).startswith('82') or title_split[-1].startswith('21')):
                return title_split[-1]
            else:
                for m in title_split:
                    if(m.startswith('20') or m.startswith('82')):
                        if(m.startswith('20GB')==False):
                            return m
                return 'Belirtilmemiş'
        elif((marka=="Asus" or marka=="ASUS") or (marka=='Msi' or marka=='MSI')):
            for title in title_split:
                if(title.find('-')!=-1):
                    array=title.split('-')
                    array[0]=str(array[0])
                    if(array[0]!='i3' and array[0]!='i5' and array[0]!='i7' and array[0]!='i9' and array[0]!='I3' and array[0]!='I5' and array[0]!='I7' and array[0]!='I9'):
                        return title
                    else:
                        continue
            return 'Belirtilmemiş'
        else:
            return 'Belirtilmemiş'


    def hb_modalnoshaper(self,title):
        return 1
deneme = WebScrapping()
deneme.hepsiBurada()
# Tüm sitelerin scraping kodlarının fonksiyonları eklendi.
# Database class'ı oluşturuldu. Class içerisinde database işlemlerinin fonksiyonlarını tanımlarız.(append,list eklendi)
# Shape tarafı 11.10.2022 incelenecek.
