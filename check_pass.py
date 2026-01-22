print('Enter your password')
passwordinput = input()
if passwordinput == 'admin123':
    print('Access Granted')
elif passwordinput == 'Admin123':
    print('Hint: the password is in lower case')
elif passwordinput == '123':
    print('Hint: the password also contains string')
else:
    print('Access Denied')
print('Done')