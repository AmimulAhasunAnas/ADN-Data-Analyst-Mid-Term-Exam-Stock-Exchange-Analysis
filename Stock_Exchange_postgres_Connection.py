import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

conn = psycopg2.connect(database="companydata",
                        host="localhost",
                        user="postgres",
                        password="Anas907",
                        port="5432")
data1=pd.read_csv('company_data.csv')
rows1=data1.shape[0]

data2=pd.read_csv('Holding_data.csv')
rows2=data2.shape[0]

cur=conn.cursor()

cur.execute('create table company_data(Company_ID varchar(100),Company_Name varchar(150),Sectors varchar(100),Trading_Codes varchar(100),Scrip_Codes varchar(100),Websites varchar(200),Urls varchar(200),primary key(Company_ID));')
cur.execute('create table other_info_data(Company_ID varchar(100),Date_ varchar(100),Sponsor float,Govt float,Institute float ,Foreign_ float,Public_ float);')

for i in range(0,rows1):
    cur.execute('insert into company_data values(%s,%s,%s,%s,%s,%s,%s)',(data1['Company_ID'][i],data1['Company_Name'][i],data1['Sectors'][i],data1['Trading_Codes'][i],str(data1['Scrip_Codes'][i]),data1['Websites'][i],data1['Urls'][i]))
conn.commit()

for i in range(0,rows2):
    cur.execute('insert into holding_data values(%s,%s,%s,%s,%s,%s,%s)',(data2['Company_ID'][i],data2['Date'][i],float(data2['Sponsor'][i]),float(data2['Govt'][i]),float(data2['Institute'][i]),float(data2['Foreign'][i]),float(data2['Public'][i])))
conn.commit()