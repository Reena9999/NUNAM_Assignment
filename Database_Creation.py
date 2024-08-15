from mysql.connector import Error
import pandas as pd
from sqlalchemy import create_engine

def insert_data():
    xls_5308 = pd.ExcelFile(r'C:\Users\HP\Downloads\Assignment\5308.xls')
    df_5308 = pd.read_excel(xls_5308, sheet_name=xls_5308.sheet_names[3])
    df2= pd.read_excel(xls_5308, sheet_name=xls_5308.sheet_names[4])
    df3= pd.read_excel(xls_5308, sheet_name=xls_5308.sheet_names[5])

    df_5308=pd.concat([df_5308,df2.iloc[:,[4,5]],df3.iloc[:,[4,5]]],axis=1)
    df_5308.insert(loc=0, column='cell id', value=5308)

    xls_5329 = pd.ExcelFile(r'C:\Users\HP\Downloads\Assignment\5329.xls')
    df_5329 = pd.read_excel(xls_5329, sheet_name=xls_5329.sheet_names[3])
    df2= pd.read_excel(xls_5329, sheet_name=xls_5329.sheet_names[4])
    df3= pd.read_excel(xls_5329, sheet_name=xls_5329.sheet_names[5])

    df_5329=pd.concat([df_5329,df2.iloc[:,[4,5]],df3.iloc[:,[4,5]]],axis=1)
    df_5329.insert(loc=0, column='cell id', value=5329)

    df= pd.concat([df_5308,df_5329])
    df.columns = ['cell_ID','record_index','status','jump_to','cycle','step','curent_mA','voltage_v','capacity_mAh','energy_mWh','relative_time', 'absolute_time','auxilary_channel_TU1_voltage','gap_voltage','auxilary_channel_TU1_temperature','gap_temperature']

    engine = create_engine(f"mysql+pymysql://root:94807279@localhost/nunam")
    df.to_sql('_cell_monitor_', con=engine, if_exists='append', index=False)


def main():
    insert_data()


if __name__=="__main__":
    main()