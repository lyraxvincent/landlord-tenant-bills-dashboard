# THIS IS THE SCRIPT VERSION OF THE (create files.ipynb) NOTEBOOK
#================================================================

# Necessary imports
import numpy as np
np.random.seed(101)
import pandas as pd

# Generate temporary artificial data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
tenants = ['tenant0', 'tenant1', 'tenant2', 'tenant3', 'tenant4', 'tenant5', 'tenant6', 'tenant7', 'tenant8', 'tenant9']
idx = pd.MultiIndex.from_product([months, tenants], names=['Month', 'Tenant_name'])
records = pd.DataFrame(np.random.randint(100, 10000, size=(120, 9)), index=idx, columns=['House_no','Rent', 'Water_units_used',
                                                                                        'Water_bill', 'Garbage_bill',
                                                                                        'Security_fee', 'Total_amount_payable',
                                                                                        'Total_amount_paid','Total_amount_due'])

# A function to actualize generated data
def actualize_data(df):
    # set seed
    np.random.seed(101)

    # flatten columns
    df = df.reset_index()

    # restructure data
    df['House_no'] = df['Tenant_name'].apply(lambda x: x.partition('tenant')[-1])
    df['Rent'] = 10000
    df['Water_units_used'] = np.random.randint(1, 9, 120)
    df['Water_bill'] = df.Water_units_used * 110  # price per unit
    df['Garbage_bill'] = 150
    df['Security_fee'] = 500
    df['Total_amount_payable'] = df[['Rent', 'Water_bill', 'Garbage_bill',
                                     'Security_fee']].agg(func=sum, axis=1)
    df['Total_amount_paid'] = df.Total_amount_payable - np.round(np.random.randint(500, 3000, size=120), decimals=-2)
    df['Total_amount_due'] = df.Total_amount_payable - df.Total_amount_paid

    df = pd.pivot_table(df, index=['Month', 'Tenant_name'])
    df = df[['Rent', 'Water_units_used', 'Water_bill', 'Garbage_bill', 'Security_fee', 'Total_amount_payable',
             'Total_amount_paid', 'Total_amount_due']]
    df = df.reindex(index=idx)
    return df

# Generate actual data
actual_records = actualize_data(records)

# Save actual records to csv
actual_records.to_csv("records.csv")