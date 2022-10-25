
def export():
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
        style = 'style="font-size:15px;"'
        html = '<html>\n    <head></head>\n       <body>\n'
        for i in range(len(k)):
            if k[i] == '':
                html += '           <p {}>~~~~~~~~~{} </p>\n'\
                    .format(style,k[i])
            else:
                html += '           <p {}> {} </p>\n'\
                    .format(style,k[i])
        html += '      </body>\n</html>'
        with open('Export.html', 'w', encoding = 'utf-8') as file:
            file.write(html)
