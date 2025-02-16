import requests
url='https://pypi.org/simple/'
def getpackages(url):
    r=requests.get(url)
    if r.status_code==200:
        with open('packages.txt','w+') as f:
            for pkg in r.text.split('\n'):
                f.write(str(pkg)+'\n') 
            f.close()
    else:
        print('Error:',r.status_code)        