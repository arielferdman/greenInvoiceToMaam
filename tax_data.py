import csv

import pandas as pd
from matplotlib import pyplot as plt


class TaxData:
    def __init__(self):
        self.data = []
        self.il_vat_tax = 0.17
        self.load_data_from_csv('income.csv')

    def get_data(self):
        return self.data

    def load_data_from_csv(self, file_name):
        self.data = []
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                self.data.append(row)
        return self.data

    def get_data_as_pandas_df(self):
        return pd.DataFrame(self.data)

    def plot_data(self):
        df = self.get_data_as_pandas_df()
        df.plot(x='day', y='income')
        plt.show()

    def get_total_income(self):
        df = self.get_data_as_pandas_df()
        return df['income'].sum()

    def add_is_taxable_col_to_df(self):
        raise NotImplementedError()

    def add_tax_col_to_df(self):
        df = self.add_is_taxable_col_to_df()
        df['tax'] = (df['income'] / (1 + self.il_vat_tax)) * self.il_vat_tax
        return df

    def add_pre_tax_col_to_df(self):
        df = self.add_tax_col_to_df()
        df['pre_tax'] = df['income'] - df['tax']
        return df

    def get_total_tax(self):
        df = self.add_tax_col_to_df()
        return df['tax'].sum()

    def get_total_pre_tax(self):
        df = self.add_pre_tax_col_to_df()
        return df['pre_tax'].sum()

    def get_total_taxable_income(self):
        df = self.add_is_taxable_col_to_df()
        return df['income'][df['is_taxable']].sum()

    def split_df_by_month(self):
        df = self.add_is_taxable_col_to_df()
        df['month'] = df['day'].apply(lambda x: x[:7])
        return df.groupby('month')

    def get_total_tax_by_month(self):
        df = self.split_df_by_month()
        return df['tax'].sum()

    def get_total_pre_tax_by_month(self):
        df = self.split_df_by_month()
        return df['pre_tax'].sum()

    def get_total_income_by_month(self):
        df = self.split_df_by_month()
        return df['income'].sum()

    def get_total_taxable_income_by_month(self):
        df = self.split_df_by_month()
        return df['income'][df['is_taxable']].sum()

    def show_gui_with_input_dialog(self):
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename
        Tk().withdraw()
        file_name = askopenfilename()
        self.load_data_from_csv(file_name)
        self.plot_data()


