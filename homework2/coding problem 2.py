import datetime

tday = datetime.datetime.today()
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
while True:
    user_input = input()
    if user_input == '-1':
        break
    else:
        for m in months:
            if user_input.find(m) != -1:
                input_date = datetime.datetime.strptime(user_input, '%B %d, %Y')
                if input_date < tday:
                    print(input_date.strftime('%#m/%#d/%Y'))
