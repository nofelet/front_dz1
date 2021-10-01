import pandas as pd

df = pd.read_csv('data.csv', delimiter=';')

def record(firstname='', middlename='', lastname='', birthdate=''):
    return (lastname + firstname + middlename + birthdate).upper()

def number_of_records(record, df=df):
    filtered = df.loc[df['brand_sort'] == record]
    return(filtered.shape[0])
