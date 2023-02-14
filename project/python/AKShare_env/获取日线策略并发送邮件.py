import akshare as ak
import time
# import datetime
import numpy as np
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.message import EmailMessage
import logging
import os
 
nowtime = datetime.now()
 
 
day_nums = 1  # 使用前一天的收盘价数据做信号判断
stock_num = 1  # 买入评分最高的前stock_num只股票 可以修改
momentum_day = 20  # 最新动量参考最近momentum_day的
ref_stock = 'sh000300'  # 用ref_stock做择时计算的基础数据
N = 18  # 计算最新斜率slope，拟合度r2参考最近N天
M = 600  # 计算最新标准分zscore，rsrs_score参考最近M天
score_threshold = 0.7  # rsrs标准分指标阈值
 
 
 
def get_index_list(index_symbol='sh000068'):
    stocks2 = []
    stocks = ak.index_stock_hist(index_symbol).stock_code
    for stock in stocks[:]:
        if int(stock) < 100000:
            stock = 'sz' + stock
        else:
            stock = 'sh' + stock
        stocks2.append(stock)
    return stocks2
 
 
stock_pool = get_index_list()
 
 
# 找到有交易信号的股票，为之后交易进行准备
 
 
# 动量因子：由收益率动量改为相对MA90均线的乖离动量
def get_rank(stock_pool):
    rank, biasN = [], 90
    for stock in stock_pool:
        # print(stock)
        from_date = '2010-01-01'
        from_date = datetime.strptime(from_date, "%Y-%m-%d")
        day_nums = 1
        current_dt = time.strftime("%Y-%m-%d", time.localtime())
        current_dt = datetime.strptime(current_dt, '%Y-%m-%d')
        previous_date = current_dt - timedelta(days=day_nums)
        #         data = jq.get_price(stock, end_date=previous_date, count=biasN +
        #                             momentum_day, frequency='daily', fields=['close'])
        try:
            data = ak.stock_zh_a_daily(symbol=stock, start_date=from_date, end_date=previous_date)
        except:
            pass
        # print('2222',data.head())
        bias = np.array((data.close / data.close.rolling(biasN).mean())[-momentum_day:])  # 乖离因子
        #         print(bias)
        #         print(bias[0])
        score = np.polyfit(np.arange(momentum_day), bias / bias[0], 1)[0].real  # 乖离动量拟合
        rank.append([stock, score])
    rank.sort(key=lambda x: x[-1], reverse=True)
    return rank[0]
 
 
# 线性回归：复现statsmodels的get_OLS函数
def get_ols(x, y):
    slope, intercept = np.polyfit(x, y, 1)
    r2 = 1 - (sum((y - (slope * x + intercept)) ** 2) / ((len(y) - 1) * np.var(y, ddof=1)))
    return (intercept, slope, r2)
 
 
def get_zscore(slope_series):
    mean = np.mean(slope_series)
    std = np.std(slope_series)
    return (slope_series[-1] - mean) / std
 
 
# 择时过程 ----->--------------------------------------------
def initial_slope_series():
    current_dt = time.strftime("%Y-%m-%d", time.localtime())
    current_dt = datetime.strptime(current_dt, '%Y-%m-%d')
    from_date = '2010-01-01'
    from_date = datetime.strptime(from_date, "%Y-%m-%d")
    previous_date = current_dt - timedelta(days=day_nums)
    data = ak.stock_zh_index_daily(symbol=ref_stock)
    data['date'] = data['date'].apply(lambda x: str(x))
    data['date'] = data['date'].apply(lambda x: datetime.strptime(str(x), '%Y-%m-%d'))
    data = data[(data['date'] >= from_date) & (data['date'] <= previous_date)]
    return [get_ols(data.low[i:i + N], data.high[i:i + N])[1] for i in range(M)]
 
 
# 只看RSRS因子值作为买入、持有和清仓依据，前版本还加入了移动均线的上行作为条件
def get_timing_signal(stock):
    current_dt = time.strftime("%Y-%m-%d", time.localtime())
    current_dt = datetime.strptime(current_dt, '%Y-%m-%d')
    previous_date = current_dt - timedelta(days=day_nums)
    from_date = '2010-01-01'
    from_date = datetime.strptime(from_date, "%Y-%m-%d")
    data = ak.stock_zh_index_daily(symbol=ref_stock)
    data['date'] = data['date'].apply(lambda x: str(x))
    data['date'] = data['date'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    data['date'] = data['date'].apply(lambda x: x.to_pydatetime())
    # data = data[data['date']>=from_date & data['date']<= previous_date]
    data = data[(data['date'] >= from_date) & (data['date'] <= previous_date)]
    intercept, slope, r2 = get_ols(data.low, data.high)
    slope_series.append(slope)
    rsrs_score = get_zscore(slope_series[-M:]) * r2
    print('rsrs_score {:.3f}'.format(rsrs_score))
    if (rsrs_score > score_threshold):
        return "BUY"
    elif (rsrs_score < -score_threshold):
        return "SELL"
    else:
        return "KEEP"
 
 
# slope_series = initial_slope_series()[:-1]  # 除去回测第一天的 slope ，避免运行时重复加入
slope_series = initial_slope_series()[:-1]
 
 
def my_trade():
    # print(stock_pool)
    # print(get_rank(stock_pool))
    check_out_list = get_rank(stock_pool)
    timing_signal = get_timing_signal(ref_stock)
    message = ""
    if len(check_out_list) > 0:
        each_check_out = check_out_list[0]
        #         security_info = jq.get_security_info(each_check_out)
        #         stock_name = security_info.display_name
        #         stock_code = each_check_out
        print('今日自选股:{}({})'.format(each_check_out, each_check_out))
        if timing_signal == 'SELL':
            #             for stock in list(positions.keys()):
            #                 close_position(stock)
            #                 message = '清仓！卖卖卖！'
            #                 message += "\r\n\r\n".join(positions.keys())
            #                 positions.clear()
            #                 print('今日择时信号:{}'.format(timing_signal))
            pass
        else:
            message = "今日自选股:{}({})".format(each_check_out, each_check_out)
            # adjust_position([each_check_out])
        print(message)
        sendMail(message)
 
 
def mail(message):
    ret = True
 
    try:
 
        # 定义SMTP邮件服务器地址
        smtp_server = 'smtp.qq.com'
        # 邮件发送人邮箱
        from_addr = '876506966@qq.com'  # 自己的邮想
        # 邮件发送人邮箱密码
        password = 'vhfzjjvkgbhebahi'  # 邮箱密码
        # 邮件接收人
        to_addr = '2669746433@qq.com'  # 测试接收邮件地址邮箱
 
        # 创建SMTP连接
        conn = smtplib.SMTP_SSL(smtp_server, 465)
        # 设计调试级别
        conn.set_debuglevel(1)
        # 登录邮箱
        conn.login(from_addr, password)
        # 创建邮件内容对象
        msg = EmailMessage()
        # 设置邮件内容
        msg.set_content('{}'.format(message), 'plain', 'utf-8')
        msg['Subject'] = '现在时间为：{}'.format(nowtime)
        msg['From'] = '星涅'
        msg['To'] = '我挚爱的朋友'
        # 发送邮件
        conn.sendmail(from_addr, [to_addr], msg.as_string())
        # 退出连接
        conn.quit()
 
 
 
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret = False
        ret = False
        print(e)
 
    return ret
 
 
def sendMail(message):
    ret = 0
    for _ in range(10):
        if ret:
            # 邮件发送成功推出
            break
        else:
            # 没有发送成功或失败继续
            ret = mail(message)
            time.sleep(1)
 
 
if __name__ == '__main__':
    # positions["159928.XSHE"] = 100
    my_trade()