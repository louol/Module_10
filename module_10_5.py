import multiprocessing
from datetime import datetime as dt

def read_info(name):
    all_data = []
    with open(name,'r') as file:
        while True:
            line = file.readline().strip()
            all_data.append(line)
            if not line:
                break

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
start1 = dt.now()

for f in files:
    read_info(f)

finish1 = dt.now()

print(f'Время работы линейного вызова: {finish1 - start1}')

if __name__ == '__main__':
    start2 = dt.now()

    with multiprocessing.Pool(processes=4) as pool:
            pool.map(read_info, files)

    finish2 = dt.now()
    print(f'Время работы многопроцессорного вызова: {finish2 - start2}')