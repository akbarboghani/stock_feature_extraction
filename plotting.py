import matplotlib.pyplot as plt
from timaker import TiMaker
import pandas as pd
import numpy as np
import stockstats
from stockstats import StockDataFrame as Sdf
plt.style.use('ggplot')




class IndicatorPlotter:
    def __init__(self, path, to_plot=[]):
        self.path = path
        self.df = None
        self.features = None
        self.to_plot = to_plot

    def get_df(self):
        df = TiMaker(self.path)
        df.run_all()
        self.features = df.features
        self.to_plot = self.features.keys()

        self.df = df.final_data


    def contains(self,subset):
        return [col for col in self.df.columns if subset in col]

    def plotter(self):
        plt.figure(figsize=(15,6))
        for i in self.to_plot:
            if 'macd' not in self.to_plot:
                 tp = self.df[self.contains()]
                 tp.plt()
                 plt.show()
            else:
                tp = self.df[self.contains('macd')]
                tp.drop(self.contains('macdh')[0], axis=1).plot()
                tp[self.contains('macdh')[0]].plot(kind='bar'
                plt.show()

sample = IndicatorPlotter('data.csv')
sample.get_df()
sample.to_plot = 'macd'
sample.plotter()
