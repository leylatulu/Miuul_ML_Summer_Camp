## Fonksiyonlara Özellik ve Docstring Ekleme

# Görev : Fonksiyonlara özellik eklemek
# cat_summary() fonksiyonuna 1 özellik ekleyiniz. Bu özellik argümanla biçimlendirilebilir olsun. Var olan özelliği de argümanla kontrol edilebilir hale getirebilirsiniz.

import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset('tips')

def cat_summary(df, sample = 10, missing = False):
    print()
    print("#################################### INFO ###################################")
    print(df.info())
    print()
    print("################################ DESCRIPTION ################################")
    print(df.describe().T)
    print()
    print("################################### SHAPE ###################################")
    print(df.shape)
    print()
    if missing:
        print("################################## MISSING ##################################")
        print(df.isnull().sum())
        print()
    print("################################### SAMPLE ##################################")
    print(df.head(sample))
    print()
    print("################################# Quantiles #################################")
    print(df.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]). T)
    print()

cat_summary(df, sample = 3, missing = False)


# Görev : Docstring Yazımı
# check_df(), cat_summary() fonksiyonlarına 4 bilgi (uygunsa) barındıran numpy tarzı docstring yazınız. (task, params, return, example)

df1 = sns.load_dataset('car_crashes')

def check_df(df, sample = 5, missing = False, quan = False, desc = False):
    """
    Task
    ----
    This function shows one example and statistical information about the dataframe.

    Parameters
    ----------
    df : DataFrame
    sample : int
    missing : bool
    quan : bool
    desc : bool

    Examples
    --------
    >>> check_df(df, sample = 5, missing = False, quan = False, desc = False)

    Notes
    -----
    If this parameters is True, then all information will be shown.
    """
    
    print()
    print("########################################### TYPES #########################################")
    print(df.dtypes)
    print()
    print("########################################### INFO ##########################################")
    print(df.info())
    print()
    print("########################################## SHAPE ###########################################")
    print(df.shape)
    print()
    if missing:
        print("######################################### MISSING ##########################################")
        print(df.isnull().sum())
        print()
    print("########################################## SAMPLE ##########################################")
    print(df.head(sample))
    print()
    if quan:
        print("######################################## Quantiles ##########################################")
        print(df.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]). T)
        print()
    if desc:
        print("######################################## DESCRIPTION ########################################")
        print(df.describe().T)
        print()  

check_df(df1, sample = 3, missing = True, quan = True, desc = True)

def cat_summary(df, information = False, num_cols = False, cat_cols  = False, cat_th = 12, car_th = 25):
    """
    Task
    ----
    This definition shows the summary of the dataframe.

    Parameters
    ----------
    df : DataFrame
    information : bool
    num_cols : bool
    cat_cols : bool
    cat_th : int
    car_th : int

    Examples
    --------
    >>> cat_summary(df1, information = True, num_cols = True, cat_cols  = False, cat_th = 6, car_th = 15)

    Notes
    -----
    If this parameters is True, then all information will be shown.
    """
    
    num_cols = [i for i in df.columns if str(df[i].dtype) in ['int64', 'float64']]
    cat_cols = [i for i in df.columns if str(df[i].dtype) in ['object', 'category', 'bool']]
    num_but_cat = [i for i in df.columns if str(df[i].dtype) in ['int', 'float'] and df[i].nunique() < cat_th]
    cat_but_car = [i for i in df.columns if str(df[i].dtype) in ['object', 'category'] and df[i].nunique() > car_th]
    print()
    if information:
        print("############################################## INFO #############################################")
        print(df.info())
        print()
    if num_cols:
        print("######################################## NUMERICAL COLUMNS #######################################")
        print(num_cols)
        print()
    if cat_cols:
        print("######################################## CATEGORICAL COLUMNS #####################################")
        print(cat_cols)
        print()
    if num_but_cat:
        print("######################################## NUMERICAL BUT CATEGORICAL COLUMNS #######################################")
        print(num_but_cat)
        print()
    if cat_but_car:
        print("############################### CATEGORICAL BUT CARDINALITY COLUMNS ##############################")
        print(cat_but_car)
        print()
    return num_but_cat, cat_but_car

cat_summary(df1, information = True, num_cols = True, cat_cols  = True, cat_th = 12, car_th = 25)

