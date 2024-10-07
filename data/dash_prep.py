import pandas as pd
import numpy as np

df = pd.read_excel('/Users/t0l0bkk/Documents/TTL/github/survey-tool/data/raw_data.xlsx',sheet_name = 'sample')


class metrics_prep(df):
    
    def __init__(self):
        
        # outputs
        self.m1 = self.get_m1()
        self.m2 = self.get_m2()
        self.m3 = self.get_m3()
        self.m4 = self.get_m4()
        
    def get_m1(self):
        
        m1_total_num_issues = df['Issues'].count()
        
        return m1_total_num_issues

    def get_m2(self):
        
        df['Easy_to_Fix'] = ['Yes' if p + h + v + n <= 2 else 'No' for p, h, v, n in zip(df['Physical'], df['Hearing'], df['Vision'], df['Neurodiverse'])]
        m2_easy_to_fix = df.groupby(['Easy_to_Fix'])['Issues'].count().reset_index(drop = False)
        m2_easy_to_fix['Percentage'] = m2_easy_to_fix['Issues'] / m2_easy_to_fix['Issues'].sum()

        return m2_easy_to_fix
    
    def get_m3(self):
        
        m3_types_of_disabilities_affected = df[['Physical', 'Hearing', 'Vision', 'Neurodiverse']].sum().reset_index(drop = False)
        m3_types_of_disabilities_affected.columns = ['Types_of_Disabilities_Affected', 'Issues']

        return m3_types_of_disabilities_affected
    
    def get_m4(self):
        
        m4_issues_per_l2_cat = df.groupby(['L2'])['Issues'].count().reset_index(drop = False)
        
        return m4_issues_per_l2_cat
