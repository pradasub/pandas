import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt


bb = data.DataReader(name='BB',data_source='yahoo', start="2017-01-01", end="2020-12-31")
pd.set_option('max_columns',2)
pd.set_option('precision',0)
pd.set_option('display.max_columns', False)

# line plots
bb.plot(y='Volume'); plt.savefig('./plots/volume.pdf',format='pdf',bbox_inches='tight'); plt.show();
bb.plot(y='High'); plt.savefig('./plots/high.pdf',format='pdf',bbox_inches='tight'); plt.show();
bb[['High','Low']].plot();plt.savefig('./plots/low.pdf',format='pdf',bbox_inches='tight'); plt.show()
print(plt.style.available)
plt.style.use('fivethirtyeight')
plt.style.use('dark_background')
plt.style.use('ggplot')

# bar chart
x = bb['Close'].apply(lambda x: 'poor' if x<= 5 else 'satisfactory' if x<=10 else "Stellar")
x.value_counts().plot(kind='bar'); plt.show()
x.value_counts().plot(kind='barh'); plt.show()

# pie chart
x.value_counts().plot(kind='pie'); plt.show()





