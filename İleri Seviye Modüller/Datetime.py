from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL,"")

suan = datetime.now()
saniye = datetime.timestamp(suan)
print(saniye)
ad = datetime.fromtimestamp(saniye)
print(ad)
ad = datetime.fromtimestamp(0)
print(ad)

zaman = datetime(2030,6,18)
suan = datetime.now()
print(zaman - suan)



""""#print(datetime.now())
#şuan ki zmanı gösterir
suan = datetime.now()
"""
"""
print(suan.year)
print(suan.month)
print(suan.second)
"""

"""
#print(datetime.ctime(suan))
#kapsamlı olarak zamanı gösterir
print(datetime.strftime(suan,"%Y %B %A"))
"""

