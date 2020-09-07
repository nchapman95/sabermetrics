import pybaseball
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import io
import time
import os
class hitter:
    
    def __init__(self):
        self.hitters = pybaseball.batting_stats(2020)
        
    def plot_player_stats(self,player):
        fig,ax = plt.subplots(2,2,figsize=(20,10))

        sns.boxplot(self.hitters["OBP"],ax=ax[0,0])
        ax[0,0].axvline(self.hitters[self.hitters['Name'] == player]['OBP'].unique()[0], c='CRIMSON')

        sns.boxplot(self.hitters["AVG"],ax=ax[0,1],color='blue')
        ax[0,1].axvline(self.hitters[self.hitters['Name'] == player]['AVG'].unique()[0], c='BLUE')

        sns.boxplot(self.hitters["OPS"],ax=ax[1,0],color='green')
        ax[1,0].axvline(self.hitters[self.hitters['Name'] == player]['OPS'].unique()[0], c='GREEN')

        sns.boxplot(self.hitters["BB%"],ax=ax[1,1],color='orange')
        ax[1,1].axvline(self.hitters[self.hitters['Name'] == player]['BB%'].unique()[0], c='ORANGE')
        
        fig.suptitle("Statistics for %s"%player, fontsize=34) 
        # here is the trick save your figure into a bytes object and you can afterwards expose it via flas
        
        for filename in os.listdir('static/'):
            if filename.startswith('graph_'):  # not to remove other images
                os.remove('static/' + filename)
        new_graph_name = "graph" + str(time.time()) + ".png"
        plt.savefig("/home/ec2-user/book_library_app/static/{}".format(new_graph_name),format='png')
        return new_graph_name
