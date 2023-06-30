import datetime

tday = datetime.datetime.today()
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

with open('inputDates.txt', 'r') as input_dates:
    for line in input_dates:
        if line == '-1':
            break
        else:
            for m in months:
                if line.find(m) != -1:
                    input_date = datetime.datetime.strptime(line.strip(), '%B %d, %Y')
                    if input_date < tday:
                        print(input_date.strftime('%#m/%#d/%Y'))

