# Program for Demonstrating Converting Dict Data into Json file string format data

d = {'FN': 'ZAID', 'LN': 'SHAIKH', 'mail': 'zaid@gmail.com', 'state': 'MH'}

print(d,type(d))
print("-"*80)
jsondata = str(d)
print(jsondata,type(jsondata))
print("-"*80)
