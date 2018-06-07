'''
Created on Jun 7, 2018

@author: hari
'''
from pandas_datareader import data
import pandas as pd
from bokeh.plotting import figure, output_file, show
from datetime import datetime


class MI:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    
    def getMI_C(self, companyname, startdate, enddate):
                
        '''
                
                Pyhton code to access MI date for a company
        
        '''
        MIC_DataReader = data.DataReader('NVDA', 'yahoo', startdate, enddate)
        MIC_DataReader.to_csv('NVDA1'+'.csv')

        MIC_DataReader.index = pd.to_datetime(MIC_DataReader.index)
        MIC_DataReader['Date'] = MIC_DataReader.index
        
        print(MIC_DataReader)
        
    def accessMI_C_Date(self,sp,ep,rs,rm,rf):
        
        
        '''
            
            Python code to access each of the csv data obtained from yahoo finance
        
        '''
    
