import json


def wealth_check(Digi_Asset_string):
    Transaction_string = Digi_Asset_string
    # Do all the aggregation/processing here
    agg = {}
    agg_credit = {}
    agg_debit = {}
    user_id = int(input("Enter your User_id\n"))
    CASA_list = Transaction_string['CASA']
    for trans in CASA_list:
        if trans['User_id'] == user_id:
            agg = trans.copy()
            del agg['id']
            del agg["User_id"]
    #        print(agg)
    Transaction_list = Transaction_string["Transaction"]
    for trans1 in Transaction_list:
        if (trans1['User_id'] == user_id) and 'credit' in trans1.values():
            agg_credit = trans1.copy()
        else:
            agg_debit = trans1.copy()
    # print(agg_credit)
    # print(agg_debit)
    if 'credit' in agg_credit.values():
        agg['current_bal'] = agg['current_bal'] + agg_credit['Trnx_amt']
        del agg_credit['id']
        del agg_credit['User_id']
        print("Current Balance after credit : \n" + str(agg) + ' , ' + str(agg_credit))
    if 'debit' in agg_debit.values():
        agg['current_bal'] = agg['current_bal'] - agg_debit['Trnx_amt']
        del agg_debit['id']
        del agg_debit['User_id']
        print("Current Balance after debit : \n" + str(agg) + ' , ' + str(agg_debit))


Digi_Asset_string = {
    "CASA": [
        {
            "id": 72,
            "User_id": 77,
            "bank_name": "universal bank",
            "Branch_Name": "Guindy",
            "IFSC Code": "AKUI0001124",
            "Account_type": "deposit",
            "opening_date": "2004-08-06",
            "status": "ACTIVE",
            "Currency": "INR",
            "current_bal": 100000
        },
        {
            "id": 73,
            "User_id": 79,
            "bank_name": "universal bank",
            "Branch_Name": "Guindy",
            "IFSC Code": "AKUI0001124",
            "Account_type": "deposit",
            "opening_date": "2004-08-16",
            "status": "ACTIVE",
            "Currency": "INR",
            "current_bal": 200000
        },
        {
            "id": 75,
            "User_id": 83,
            "bank_name": "HDFC bank",
            "Branch_Name": "Guindy",
            "IFSC Code": "HDFC0001124",
            "Account_type": "savings",
            "opening_date": "2004-08-06",
            "status": "ACTIVE",
            "Currency": "INR",
            "current_bal": 200000
        },
        {
            "id": 75,
            "User_id": 83,
            "bank_name": "HDFC bank",
            "Branch_Name": "Guindy",
            "IFSC Code": "HDFC0001124",
            "Account_type": "savings",
            "opening_date": "2004-08-06",
            "status": "ACTIVE",
            "Currency": "INR",
            "current_bal": 200000
        }
    ],
    "Transaction": [
        {
            "id": 75,
            "User_id": 83,
            "Trxn_type": "credit",
            "Trxn_Date": "12/02/2022",
            "Trnx_amt": 36000
        },
        {
            "id": 74,
            "User_id": 81,
            "Trxn_type": "credit",
            "Trxn_Date": "04/03/2022",
            "Trnx_amt": 41000
        },
        {
            "id": 75,
            "User_id": 83,
            "Trxn_type": "debit",
            "Trxn_Date": "12/02/2022",
            "Trnx_amt": 36000
        },
        {
            "id": 72,
            "User_id": 77,
            "Trxn_type": "debit",
            "Trxn_Date": "04/03/2022",
            "Trnx_amt": 41000
        }
    ]
}
result = wealth_check(Digi_Asset_string)
