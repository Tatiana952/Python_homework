from datetime import datetime as dt

def log(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a') as l:
        l.write('{};  ')
