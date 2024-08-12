import requests
from lxml import html

RequestDataBase = 'https://ipspeed.info/freevpn_l2tpipsec.php?language=en'

respone_block = requests.get(RequestDataBase)
byte_string = respone_block.content
source_code = html.fromstring(byte_string)

def xpatch_country():
    xpatch_list = list() 

    for i in range(6, 36):
        xpatch_list.append( f"/html/body/center/div[6]/div[3]/div[{ i + 3 }]" )

    return xpatch_list


def xpatch_ip(): 
    xpatch_list = list() 
    
    for i in range(7, 17):
        xpatch_list.append( f"/html/body/center/div[6]/div[3]/div[{i + 6}]" )
    
    return xpatch_list


def getter_data():
    country_list = xpatch_country()
    ip_list = xpatch_ip()
    tree_list_country = list()
    tree_list_ip = list()

    for i in range( 0, len(country_list) ):
        tempary = source_code.xpath(country_list[i])
        data = tempary[0].text_content()
        tree_list_country.append(data)

    for i in range( 0, len(ip_list) ):
        tree_list_ip.append(  )

    return tree_list_country

