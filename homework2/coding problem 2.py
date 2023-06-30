#Alyza Vergel de Dios
#ID 2222332
import datetime

tday = datetime.datetime.today()
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

input_dates = open('inputDates.txt', 'r')
output_dates = open('parsedDates.txt', 'w')
for line in input_dates:
    if line == '-1':
        break
    else:
        for m in months:
            if line.find(m) != -1:
                input_date = datetime.datetime.strptime(line.strip(), '%B %d, %Y')
                if input_date < tday:
                    output_dates.write(input_date.strftime('%#m/%#d/%Y\n'))

output_dates.close()
input_dates.close()
