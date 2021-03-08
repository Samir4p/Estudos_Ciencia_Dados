import urllib
import urllib.request

try:
    site = urllib.request.urlopen("https://supercentral.com.br/")
except urllib.error.URLError:
    print('Deu erro')
else:
    print('Tudo ok')
    print(site.read())      # comando para acessar o site e ver seu codigo
    