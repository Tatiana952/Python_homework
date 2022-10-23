import csv

def export():
    lst = []
    with open('Base.txt', 'r', encoding='utf-8') as b:
        k = b.readlines()
    k = list(map(lambda x: x.replace('\n', ''), k))

    print('\nChoose format for export.\n1. txt   2. html')
    f = int(input('Format: '))

    if f == 1:
        with open('Export.txt', 'w', encoding='utf-8') as file:
            for i in range(len(k)):
                if k[i] == '':
                    file.write('\n')
                else:
                    file.write(k[i] + ', ')
    elif f == 2:
        d = {0: 'Surname: ',
        1: 'Name: ',
        2: 'Telephone num.: ',
        3: 'Description: '}
        style = 'style="font-size:15px;"'
        html = '<html>\n    <head></head>\n       <body>\n'
        for i in range(len(k)):
            html += '           <p {}> {} </p>\n'\
                .format(style,k[i])
            # html += '           <p {}>Wind speed: {} m/s</p>\n'\
            #     .format(style,wind_speed_view(device))
            # html += '           <p {}>Pressure: {} mmHg</p>\n'\
            #     .format(style,pressure_view(device))
        html += '      </body>\n</html>'
        with open('Export.html', 'w') as file:
            file.write(html)
            

