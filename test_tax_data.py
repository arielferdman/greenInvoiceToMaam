from tax_data import TaxData


class TestTaxData:
    def __init__(self):
        self.test_data = TaxData()
        self.test_data.load_data_from_csv('income.csv')
        self.test_data.add_is_taxable_col_to_df()
        self.test_data.add_tax_col_to_df()
        self.test_data.add_pre_tax_col_to_df()
        self.passed_tests = 0
        self.failed_tests = 0

    # a decorator that wraps a test function with try catch and logs success and failures
    def test_wrapper(self, test_function):
        def wrapper(*args, **kwargs):
            try:
                test_function(*args, **kwargs)
                print('Test passed')
                self.passed_tests += 1
            except Exception as e:
                print('Test failed:', e)
                self.failed_tests += 1

    @test_wrapper
    def test_get_data(self):
        assert self.test_data.get_data() == self.test_data.get_data_as_pandas_df().values.tolist()

    @test_wrapper
    def test_get_total_income(self):
        assert self.test_data.get_total_income() == self.test_data.get_data_as_pandas_df()['income'].sum()

    @test_wrapper
    def test_plot_data(self):
        self.test_data.plot_data()

    @test_wrapper
    def test_add_is_taxable_col_to_df(self):
        assert self.test_data.get_data_as_pandas_df()['is_taxable'].values.tolist()

    @test_wrapper
    def test_add_tax_col_to_df(self):
        assert self.test_data.get_data_as_pandas_df()['tax'].values.tolist()

    @test_wrapper
    def test_add_pre_tax_col_to_df(self):
        assert self.test_data.get_data_as_pandas_df()['pre_tax'].values.tolist()

    @test_wrapper
    def test_pre_tax_tax_and_income_data_adds_up(self):
        assert self.test_data.get_data_as_pandas_df()['pre_tax'].sum() == \
               self.test_data.get_data_as_pandas_df()['income'].sum() - \
               self.test_data.get_data_as_pandas_df()['tax'].sum()

    @test_wrapper
    def test_tax_data_adds_up(self):
        assert self.test_data.get_data_as_pandas_df()['tax'].sum() == \
               self.test_data.get_data_as_pandas_df()['income'].sum() * self.test_data.il_vat_tax

    @test_wrapper
    def test_tax_data_is_not_negative(self):
        assert self.test_data.get_data_as_pandas_df()['tax'].sum() >= 0

    @test_wrapper
    def test_tax_data_is_not_greater_than_income(self):
        assert self.test_data.get_data_as_pandas_df()['tax'].sum() <= self.test_data.get_data_as_pandas_df()[
            'income'].sum()

    @test_wrapper
    def test_split_df_by_month(self):
        assert self.test_data.split_df_by_month() == self.test_data.get_data_as_pandas_df().groupby(
            ['month']).sum().values.tolist()

    @test_wrapper
    def test_get_total_tax_by_month(self):
        assert self.test_data.get_total_tax_by_month() == self.test_data.get_data_as_pandas_df()['tax'].groupby(
            ['month']).sum().values.tolist()

    @test_wrapper
    def test_get_total_income_by_month(self):
        assert self.test_data.get_total_income_by_month() == self.test_data.get_data_as_pandas_df()['income'].groupby(
            ['month']).sum().values.tolist()

    @test_wrapper
    def test_get_pre_tax_by_month(self):
        assert self.test_data.get_total_pre_tax_by_month() == self.test_data.get_data_as_pandas_df()['pre_tax'].groupby(
            ['month']).sum().values.tolist()

    @test_wrapper
    def test_get_total_taxable_income_by_month(self):
        assert self.test_data.get_total_taxable_income_by_month() == self.test_data.get_data_as_pandas_df()[
            'income'].groupby(['month']).sum().values.tolist()

    @test_wrapper
    def test_show_gui_with_input_dialog(self):
        self.test_data.show_gui_with_input_dialog()

    def run_suite(self):
        self.test_get_data()
        self.test_get_total_income()
        self.test_plot_data()
        self.test_add_is_taxable_col_to_df()
        self.test_add_tax_col_to_df()
        self.test_add_pre_tax_col_to_df()
        self.test_pre_tax_tax_and_income_data_adds_up()
        self.test_tax_data_adds_up()
        self.test_tax_data_is_not_negative()
        self.test_tax_data_is_not_greater_than_income()
        self.test_split_df_by_month()
        self.test_get_total_tax_by_month()
        self.test_get_total_income_by_month()
        self.test_get_pre_tax_by_month()
        self.test_get_total_taxable_income_by_month()
        self.test_show_gui_with_input_dialog()

        # visualize results

