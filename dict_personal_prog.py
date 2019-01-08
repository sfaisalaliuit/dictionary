dict = {'Name' : 'Jibran', 'Age': 12, 'Class':'Sixth', 'DOB':'16 April 2006'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
print("dict['DOB']: ", dict['DOB'])
print("dict['Class']:", dict['Class'])

dict['Age'] = 12.5
dict['School'] = 'The Seeds School'

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

dict['Friend1'] = 'Adnan'
dict['Friend2'] = 'Akbar'
dict['Friend3'] = 'Jazil'

print("dict['Friend1']" , dict['Friend1'])
print("dict['Friend2']" , dict['Friend2'])
print("dict['Friend3']" , dict['Friend3']) 
    
del dict['Friend1']     

print("dict['Friend2']" , dict['Friend2'])
print("dict['Friend3']" , dict['Friend3'])     

