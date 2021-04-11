# Necessary imports
import pandas as pd # data I/O
pd.set_option('display.max_rows', None)
from IPython.display import display

# Read in the data
records = pd.read_csv("records.csv", index_col=['Month', 'Tenant_name'])
tenant_passwords = {'tenant0': 'pass0', 'tenant1': 'pass1', 'tenant2': 'pass2', 'tenant3': 'pass3',
                    'tenant4': 'pass4', 'tenant5': 'pass5', 'tenant6': 'pass6', 'tenant7': 'pass7',
                    'tenant8': 'pass8', 'tenant9': 'pass9'}
passwords = tenant_passwords.values()

# User prompt
user = int(input("Landlord(1) or Tenant(2)? : "))

###################################################################################################################
# USER LANDLORD
###################################################################################################################
if user == 1:
    pswd = input("Enter landlord password: ")

    if pswd == 'land01': # passwords will be set

        # Monthly total amounts statistics
        print("\n=============================\nMonthly total amounts")
        print("===================================================================================================="
              "=================")
        display(pd.DataFrame(records.reset_index().groupby('Month')[['Total_amount_payable', 'Total_amount_paid',
                                                                'Total_amount_due']].sum()).T)

        # End year statistics
        print("\n=============================\nEnd Year Totals")
        print("===================================================================================================="
              "=================")
        display(pd.DataFrame(records.reset_index().groupby('Month')[['Total_amount_payable', 'Total_amount_paid',
                                                                'Total_amount_due']].sum()).T.agg(sum, axis=1))

        # All records
        print("\n======================\nAll records...")
        print("====================================================================================================="
              "=========================================")
        display(records)
        print("====================================================================================================="
              "=========================================")

        # pull data for a specific tenant
        choice = input("\nGet data for a specific tenant?(Y/n): ").upper()

        if choice == 'Y':
            tnant = input("Enter house number(tenant name/number): ")
            if tnant in tenant_passwords.keys():
                print(f"\n===================\nRecords for {tnant}")
                print(
                    "=============================================================================================="
                    "====================================")
                display(records.reset_index()[records.reset_index().Tenant_name == tnant])
                print(
                    "=============================================================================================="
                    "====================================")
        else:
            pass



    else:
        print("Wrong password. Please use the tenant option if you're a tenant.")


###################################################################################################################
# USER TENANT
###################################################################################################################
elif user == 2:
    pswd = input("Enter tenant password: ")

    if pswd in passwords:
        tname = dict(map(reversed, tenant_passwords.items()))[pswd]
        print(f"\n==============================\nShowing records for {tname}")
        print("====================================================================================================="
              "=============================")
        display(records.reset_index()[records.reset_index().Tenant_name == tname].pivot_table(index='Month').reindex(
            ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']))
        print("====================================================================================================="
              "=============================")
    else:
        print("Wrong password.")

else:
    print("Wrong input.")