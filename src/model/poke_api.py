'''
Created on 30 nov. 2019

@author: FLIPE LUNA
'''
import pokepy
import urllib
from requests import get

def obtener_ip_publica():
    ip = 0
    try:    
        ip = get('https://api.ipify.org').text
    except Exception as err:
        print err
    finally:
        return ip


def obtener_img_pokemon(pokemon,ruta=""):
    poke = pokepy.V2Client().get_pokemon(pokemon)
    url = poke.sprites.front_default
    urllib.urlretrieve(url,ruta + str(pokemon) + ".png")
    return url,ruta

if __name__ == "__main__":
    print obtener_img_pokemon("vaporeon")