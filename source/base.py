import requests
import pandas as pd

class Base:
    
    def __init__(self):
        self.api_url1 = "https://eldenring.fanapis.com/api/weapons?limit=400&page=0"
        self.api_url2 = "https://eldenring.fanapis.com/api/weapons?limit=400&page=1"
        self.api_url3 = "https://eldenring.fanapis.com/api/weapons?limit=400&page=2"
        self.api_url4 = "https://eldenring.fanapis.com/api/weapons?limit=400&page=3"
        self.get_data()
        self.clean_data()
    
    def return_url(self):
        return self.api_url1, self.api_url2, self.api_url3, self.api_url4
    
    def get_data(self):
        weapons= []
        response_1 = requests.get(self.api_url1).json()['data']
        response_2 = requests.get(self.api_url2).json()['data']
        response_3 = requests.get(self.api_url3).json()['data']
        response_4 = requests.get(self.api_url4).json()['data']
        weapons = response_1 + response_2 + response_3 + response_4
        self.df = pd.DataFrame(weapons)
        return(self.df)
    def clean_data(self):
        keys_to_extract = ['Str', 'Dex', 'Int', 'Fai', 'Arc']
        for key in keys_to_extract:
            new_column_name = f'req_{key}'
            self.df[new_column_name] = self.df['requiredAttributes'].apply(
                lambda lst: next((item['amount'] for item in lst if item['name'] == key), None)
            )
        keys_to_extract = ['Str', 'Dex', 'Int', 'Fai', 'Arc']
        for key in keys_to_extract:
            new_column_name = f'scl_{key}'
            
            self.df[new_column_name] = self.df['scalesWith'].apply(
                lambda lst: next((item.get('scaling', None) for item in lst if item['name'] == key), None)
            )

        key_to_column = {
            'Phy': 'phys_attack',
            'Mag': 'magic_attack',
            'Fire': 'fire_attack',
            'Ligt': 'light_attack',
            'Holy': 'holy_attack',
            'Crit': 'crit_attack',
        }

        for key, column_name in key_to_column.items():
            self.df[column_name] = self.df['attack'].apply(
                lambda lst: next((item['amount'] for item in lst if item['name'] == key), None)
            )

        key_to_column = {
            'Phy': 'phys_defence',
            'Mag': 'magic_defence',
            'Fire': 'fire_defence',
            'Ligt': 'light_defence',
            'Holy': 'holy_defence',
            'Boost': 'boost_defence',
        }

        for key, column_name in key_to_column.items():
            self.df[column_name] = self.df['defence'].apply(
                lambda lst: next((item['amount'] for item in lst if item['name'] == key), None)
            )
        ctd = ['defence','attack','scalesWith','requiredAttributes']
        self.df.drop(columns = ctd,axis= 0,inplace = True)
        self.df.columns = self.df.columns.str.lower()
        
        return(self.df)
        
if __name__ == '__main__':
    c = Base()
    c.clean_data()
    c.df.to_csv('source/data/weapons_list.csv', index = True)
