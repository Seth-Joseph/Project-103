import pandas
import plotly_express

dataframe = pandas.read_csv('Copy+of+data+-+data.csv')
figure = plotly_express.scatter(dataframe,x = 'date',y = 'cases', title = 'Covid Cases',color = 'country')
figure.show()