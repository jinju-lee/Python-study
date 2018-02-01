list_ex1=['risk','issue','test','maintenance','maturity']
list_ex2=['security','plan','design','systematic','safety']
list_ex3=['maintenance','verification','validation']

if ('maintenance' in list_ex1) and (len(list_ex1)>=5):
    print('list_ex1 will be tested')
elif ('maintenance' in list_ex2) and (len(list_ex2)>=5):
    print('list_ex2 will be tested')
elif ('maintenance' in list_ex3) and (len(list_ex3)>=5):
    print('list_ex3 will be tested')
else:
    print('There is no available test list')
