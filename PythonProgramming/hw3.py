## PYTHON ALISTIRMALAR ## 
# =========================================================================================================================================================================
# * **Görev 1:** Verilen değerlerin veri yapılarını inceleyiniz.

x = 8                                                 #int
y = 3.2                                               #float
z = 8j + 18                                           #complex
a = "Hello World"                                     #str
b = True                                              #bool
c = 23 < 22                                           #bool
l = [1,2,3,4]                                         #list
d = {"Name": "Jake",                                  #dict
    "Age": "27",
    "Adress": "Downtown"}
t = ("Machine Learning", "Data Science")              #tuple
s = {"Python", "Machine Learning", "Data Science"}    #set

liste = [x, y, z, a, b, c, l, d, t, s]
[type(i) for i in liste]
# =========================================================================================================================================================================


# =========================================================================================================================================================================
# * **Görev 2:** Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.

text = "The goal is to turn data into information, and information into insight."
text = text.upper()
text = text.replace(",", " ").replace(".", " ").split()
text
# =========================================================================================================================================================================


# =========================================================================================================================================================================
# * **Görev 3:** Verilen listeye aşağıdaki adımları uygulayınız:
lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Adım1: Verilen listenin eleman sayısına bakınız.
len(lst)

# Adım2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
lst[0], lst[1]

# Adım3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
lst[0:4]

# Adım4: Sekizinci indeksteki elemanı siliniz.
lst.pop(8)

# Adım5: Yeni bir eleman ekleyiniz.
lst.append("X")

# Adım6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.
lst.insert(8, "N")
# =========================================================================================================================================================================


# =========================================================================================================================================================================
# **Görev 4:** Verilen sözlük yapısına aşağıdaki adımları uygulayınız:
dict  = {'Christian': ["America", 18],
         'Daisy': ["England", 12],
         'Antonio': ["Spain", 22],
         'Dante': ["Italy", 25]}

# Adım1: Key değerlerine erişiniz.
dict.keys()
# Adım2: Value'lara erişiniz.
dict.values()
# Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict['Daisy'][1] = 13
# Adım4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict['Ahmet'] = ["Turkey", 24]
# Adım5: Antonio'yu dictionary'den siliniz.
dict.pop('Antonio')
# =========================================================================================================================================================================


# =========================================================================================================================================================================
# **Görev 5:** Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.

l = [2, 13, 18, 93, 22]

def func(l):
    even_list, odd_list = [], []
    [even_list.append(i) if i % 2 == 0 else odd_list.append(i) for i in l]
    return even_list, odd_list

even_list, odd_list = func(l)

# Liste elemanlarına tek tek erişmeniz gerekmektedir.
# Her bir elemanın çift veya tek olma durumunu kontrol etmek için % yapısını kullanabilirsiniz.
# =========================================================================================================================================================================


# =========================================================================================================================================================================
# **Görev 6:** List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
import seaborn as sns 
df = sns.load_dataset("car_crashes")
df.columns

df.columns = ["NUM_" + i.upper() if df[i].dtype != 'O' else i.upper() for i in df.columns]

# Numeric olmayan değişkenlerin de isimleri büyümeli.
# Tek bir list comprehension yapısı kullanılmalı.
# =========================================================================================================================================================================


# =========================================================================================================================================================================
# **Görev 7:** List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.
df = sns.load_dataset("car_crashes")
df.columns = [i.upper()+ "_FLAG" if "no" not in i else i.upper() for i in df.columns]

# Tüm değişkenlerin isimleri büyük harf olmalı.
# Tek bir list comprehension yapısı ile yapılmalı.
# =========================================================================================================================================================================


# =========================================================================================================================================================================
# **Görev 8:** List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir data frame oluşturunuz.
df = sns.load_dataset("car_crashes")
og_list = ["abbrev", "no_previous"]

# Önce verilen listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz ve adını new_df olarak isimlendiriniz.

new_cols = [i for i in df.columns if i not in og_list]
new_df = df[new_cols]
new_df.head()
# =========================================================================================================================================================================