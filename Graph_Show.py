"""
txt 파일 읽어서 그래프로 보이기
"""
import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('User_Dataset.txt', 'r') as csvfile:
        plots = csv.reader(csvfile,delimiter = ' ')
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))

plt.figure()