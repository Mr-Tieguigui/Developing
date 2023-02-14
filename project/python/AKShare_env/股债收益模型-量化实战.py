import time
import datetime
import numpy as np
import pandas as pd
# %matplotlib inline
import matplotlib.pyplot as plt
import warnings; warnings.simplefilter('ignore')
import datetime
import akshare as ak
import tushare as ts
ts.set_token('你自己的token')
pro = ts.pro_api()

# 数据从2006年开始
start_date="2006-01-01"
end_date="2022-03-17"
set_date="2022-03-17"

market_code='000300.SH' # 市场组合选取沪深300

market=pro.index_daily(ts_code=market_code, start_date=pd.to_datetime(start_date).strftime('%Y%m%d'), end_date=pd.to_datetime(end_date).strftime('%Y%m%d'))[['trade_date','close','pct_chg']]  # 获取指数收益率数据
market['pct_chg'] = market['pct_chg']/100                       # 收益率去除 %
market['trade_date'] = pd.to_datetime(market['trade_date'])     # 转换成时间格式
market.set_index('trade_date', inplace=True)               # 设置时间索引
market.sort_index(inplace=True)                            # 时间索引从小到大排序

df=ak.index_value_hist_funddb(symbol="沪深300", indicator="股息率")
df1=df[['日期','股息率']]
df1['日期']=pd.to_datetime(df1['日期'])
df1['股息率']=df1['股息率']/100
df1.rename(columns={'日期': 'trade_date'}, inplace=True)
df1.set_index('trade_date',inplace=True)
market=market.join(df1)

info=[]
while pd.to_datetime(start_date)<=pd.to_datetime(set_date):
    time.sleep(1)
    start_date=pd.to_datetime(start_date).strftime('%Y%m%d')
    end_date=(pd.to_datetime(start_date)+datetime.timedelta(days=365)).strftime('%Y%m%d')
    df=ak.bond_china_yield(start_date=start_date,end_date=end_date)
    df1=df.loc[df['曲线名称']=='中债国债收益率曲线'][['日期','10年']] # 曲线名称
    info=df1.append(info)
    start_date=(pd.to_datetime(start_date)+datetime.timedelta(days=366)).strftime('%Y%m%d')

info.sort_values(by=['日期'],inplace=True)
info['日期']=pd.to_datetime(info['日期'])
info['10年']=info['10年']/100
info.rename(columns={'日期': 'trade_date'}, inplace=True)
info.set_index('trade_date',inplace=True)
market=market.join(info).dropna()

market['spread']=market['10年']-market['股息率']
market['mean']=market['spread'].rolling(252*3).mean()
market['std']=market['spread'].rolling(252*3).std()
market['-2 std']=market['mean']-market['std']*2
market['-1 std']=market['mean']-market['std']*1
market['+1 std']=market['mean']+market['std']*1
market['+2 std']=market['mean']+market['std']*2
market.dropna(inplace=True)

#  -----------------------------------------
#  模型可视化          
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig1,ax = plt.subplots(figsize = (20,8))
title='沪深300股债收益模型'
 
plt.grid(True)
ax1 = ax.twinx()       #复制上一张子图的横坐标轴；
plt.title(title)
plt.plot(market['spread'], label='股债收益利差')
plt.plot(market['-2 std'], label='股债收益向下2倍标准差')
plt.plot(market['-1 std'], label='股债收益向下1倍标准差')
plt.plot(market['mean'], label='股债收益均值')
plt.plot(market['+1 std'], label='股债收益向上1倍标准差')
plt.plot(market['+2 std'], label='股债收益向上2倍标准差')
plt.legend(loc='upper left')
 
ax2 = ax.twinx()       #复制上一张子图的横坐标轴；
plt.plot(market['close'],color='k',label='收盘价') 
plt.legend(loc='center left')