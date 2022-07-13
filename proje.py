# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama

""" 
Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak
seviye tabanlı (level based) yeni müşteri tanımları (persona)
oluşturmak ve bu yeni müşteri tanımlarına göre segmentler
oluşturup bu segmentlere göre yeni gelebilecek müşterilerin
şirkete ortalama ne kadar kazandırabileceğini tahmin etmek
istemektedir. 
"""

"""
Örneğin: Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek
kullanıcının ortalama ne kadar kazandırabileceği belirlenmek isteniyor.
"""

"""
Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu
ürünleri satın alan kullanıcıların bazı demografik bilgilerini barındırmaktadır. Veri
seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı
tablo tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir
kullanıcı birden fazla alışveriş yapmış olabilir.
"""

"""
Değişkenler - persona.csv
==========================================
PRICE   – Müşterinin harcama tutarı
SOURCE  – Müşterinin bağlandığı cihaz türü
SEX     – Müşterinin cinsiyeti
COUNTRY – Müşterinin ülkesi
AGE     – Müşterinin yaşı
"""
# Kütüphaneler
import numpy as np
import pandas as pd 
import seaborn as sns 

# Görev 1:
## Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
df = pd.read_csv('data_analysis_with_python\datasets\persona.csv')

def general_information(df):
    print("##### INFO #####")
    print(df.info())
    print("##### DESCRIPTION #####")
    print(df.describe().T)
    print("##### SHAPE #####")
    print(df.shape)
    print("##### MISSING #####")
    print(df.isnull().sum().sort_values(ascending = False))

general_information(df)

## Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?
df.SOURCE.unique()
df.SOURCE.value_counts()

## Soru 3: Kaç unique PRICE vardır?
df.PRICE.unique()

## Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
df.PRICE.value_counts()

## Soru 5: Hangi ülkeden kaçar tane satış olmuş? 
df.COUNTRY.value_counts()

## Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?
df.groupby('COUNTRY')['PRICE'].sum()

## Soru 7: SOURCE türlerine göre satış sayıları nedir?
df.groupby('SOURCE')['PRICE'].count()

## Soru 8: Ülkelere göre PRICE ortalamaları nedir?
df.groupby('COUNTRY')['PRICE'].mean()

## Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
df.groupby('SOURCE')['PRICE'].mean()

## Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
df.groupby(['COUNTRY','SOURCE'])['PRICE'].mean()

#=========================================================================================================================================

# Görev 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
df.groupby(['COUNTRY','SOURCE','SEX','AGE'])['PRICE'].mean().head(15)
# Görev 3: Çıktıyı PRICE’a göre sıralayınız.
agg_df = df.groupby(['COUNTRY','SOURCE','SEX','AGE'])['PRICE'].mean().sort_values(ascending=False)
"""
    • Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE’a göre uygulayınız.
    • Çıktıyı agg_df olarak kaydediniz.
"""

# Görev 4: Indekste yer alan isimleri değişken ismine çeviriniz.
agg_df = agg_df.reset_index()
"""
    • Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir. Bu isimleri değişken isimlerine çeviriniz.
"""

# Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
def new_age(age):
    if 0 < age <= 18:
        return '0_18'
    elif 19 <= age <= 23:
        return '19_23'
    elif 24 <= age <= 30:
        return '24_30'
    elif 31 <= age <= 40:
        return '31_40'
    elif 41 <= age <= 70:
        return '41_70' 

agg_df['CAT_AGE'] = agg_df.AGE.apply(new_age)

"""
    • Age sayısal değişkenini kategorik değişkene çeviriniz.
    • Aralıkları ikna edici şekilde oluşturunuz.
    • Örneğin: ‘0_18', ‘19_23', '24_30', '31_40', '41_70'
"""

# Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
agg_df["customers_level_based"] = (agg_df.COUNTRY + "_" + agg_df.SOURCE + "_" + agg_df.SEX + "_" + (agg_df.CAT_AGE).astype("string"))
agg_df["customers_level_based"] = agg_df["customers_level_based"].apply(lambda x: x.upper())

dff = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"}).reset_index()
"""
    • Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve veri setine değişken olarak ekleyiniz.
    • Yeni eklenecek değişkenin adı: customers_level_based
    • Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek customers_level_based değişkenini oluşturmanız gerekmektedir.
"""

"""  Dikkat! 
List comprehension ile customers_level_based değerleri oluşturulduktan sonra bu değerlerin tekilleştirilmesi gerekmektedir.
Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18. Bunları groupby'a alıp price ortalamalarını almak gerekmektedir.
"""
dff.columns
# Görev 7: Yeni müşterileri (personaları) segmentlere ayırınız.
dff["SEGMENT"] = pd.qcut(dff["PRICE"], 4, labels = ["D", "C", "B", "A"])
dff.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]})

"""
    • Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız.
    • Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
    • Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).
"""
# Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.

"""
    • 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
    • 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
"""

customer1 = "TUR_ANDROID_FEMALE_31_40"
customer2 = "FRA_IOS_FEMALE_31_40"

dff[dff.customers_level_based == customer1]
dff[dff.customers_level_based == customer2]