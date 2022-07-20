## Pandas Alıştırmalar
from itertools import groupby
import seaborn as sns
import pandas as pd
import numpy as np

# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
df = sns.load_dataset('titanic')
df.columns

# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
df.sex.value_counts()

# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
df.nunique()

# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
df.pclass.value_counts()

# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
df.pclass.value_counts()
df.parch.value_counts()

# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
df.embarked.dtype
df.embarked = df.embarked.astype('category') 

# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
df[df.embarked == 'C']

# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
df[df.embarked != 'S']

# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
df[(df.age < 30) & (df.sex == 'female')]

# Görev 10: Fare'i 500'den büyük veya yaşı 70’den büyük yolcuların bilgilerini gösteriniz.
df[(df["fare"] > 500) | (df["age"] > 70)]

# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
df.isnull().sum()

# Görev 12: who değişkenini dataframe’den çıkarınız.
df.drop('who', axis=1, inplace=True)

# Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
df.deck.fillna(df.deck.mode()[0], inplace=True)

# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
df.age.fillna(df.age.median(), inplace=True)

# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
df.groupby(['pclass','sex']).agg({'survived': ["sum","count", "mean"]})

# Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 verecek bir fonksiyon yazın. 
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. 
# (apply ve lambda yapılarını kullanınız)

df['age_flag'] = df.age.apply(lambda x: x if x<30 else 0)

# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
df1 = sns.load_dataset('tips')

# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerinin sum, min, max ve mean değerlerini bulunuz.
df1.groupby('time').agg({'total_bill': ["sum","min", "max", "mean"]})

# Görev 19: Day ve time’a göre total_bill değerlerinin sum, min, max ve mean değerlerini bulunuz.
df1.groupby(['day','time']).agg({'total_bill': ["sum","min", "max", "mean"]})

# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre sum, min, max ve mean değerlerini bulunuz.
(df1[(df1.time == 'Lunch') & (df1.sex == 'Female')]).groupby(['day']).agg({'total_bill':["sum", "min", "max", "mean"],
                                                                            'tip':["sum", "min", "max", "mean"]})

# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
df1.loc[(df1["size"] < 3) & (df1["total_bill"] > 10), 'total_bill'].mean()

# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
df1["total_bill_tip_sum"] = df1.total_bill + df1.tip

# Görev 23: Total_bill değişkeninin kadın ve erkek için ayrı ayrı ortalamasını bulunuz. 
# Bulduğunuz ortalamaların altında olanlara 0, üstünde ve eşit olanlara 1 verildiği yeni bir total_bill_flag değişkeni oluşturunuz.
# Kadınlar için Female olanlarının ortalamaları, erkekler için ise Male olanların ortalamaları dikkate alınacaktır. 
# Parametre olarak cinsiyet ve total_bill alan bir fonksiyon yazarak başlayınız. (If-else koşulları içerecek)

f_avg = df1[df1["sex"] == "Female"]["total_bill"].mean() 
m_avg = df1[df1["sex"] == "Male"]["total_bill"].mean() 

def flag(sex, total_bill):
    if sex == "Female":
        if total_bill < f_avg:
            return 0
        else:
            return 1
    else:
        if total_bill < m_avg:
            return 0
        else:
            return 1

df1["total_bill_flag"] = df1[["sex","total_bill"]].apply(lambda x: flag(x["sex"],x["total_bill"]),axis=1)

# Görev 24: total_bill_flag değişkenini kullanarak cinsiyetlere göre ortalamanın altında ve üstünde olanların sayısını gözlemleyiniz.
df1.groupby(['total_bill_flag','sex'])['sex'].count()

# Görev 25: Veriyi total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
new_df = df1.sort_values(by='total_bill_tip_sum', ascending=False).head(30)
