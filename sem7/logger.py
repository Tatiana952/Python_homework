from datetime import datetime as dt

def log(x, data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a') as l:
        l.write(f'\nAt {time} user entered {x} = {data}')

def log_res(y, data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a') as l:
        l.write(f'\nAt {time} Results of operation {y} {data}')

def log_comm(z):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a') as l:
        l.write(f'\nAt {time} Number {z}')
