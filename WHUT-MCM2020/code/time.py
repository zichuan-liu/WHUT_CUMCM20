rating_series = pd.DataFrame(kindle.review_date)
dforms=[]
for x in rating_series.review_date:
    dforms.append((pd.to_datetime(x)).value)
# now we have dforms which has dates transformed to numeric values
rating2 = rating_series.assign(date_min = dforms)
rating2.reset_index(inplace=True)
#rating2.set_index('date_min')
#rating2.columns=['timestamp_string','review_count','date_min']
bins = np.linspace(min(rating2.date_min),max(rating2.date_min),num=50)
rating2.hist(column='date_min', bins=20,figsize=(10,6),)
rating2.hist(column='date_min', bins=30,figsize=(10,6))
rating2.hist(column='date_min', bins=50,figsize=(10,6))

def NPS_eval (A):
    score =0
    for x in A[:]:
        if (x>4) :
            score+=1
        elif (x<3) :
            score-=1
    return 100*score/len(A)    
NPS_overtime = kindle[['temp','star_rating']]
NPS_overtime.groupby(by='temp').agg(NPS_eval).plot(figsize=(15,10))

for i in range(8):
    title = final['product_title'].value_counts().index[i]
    XXXX = final[final['product_title']==title]
    month = XXXX.resample('M').sum()
    month['H/P'] = month['H']/month['P']
    month_dates = month['H/P']
    month_dates.sort_index(inplace=True)
    month_dates.plot(figsize=(12,6))
    plt.legend([title])
    plt.ylabel('Star Rating')
    plt.show()