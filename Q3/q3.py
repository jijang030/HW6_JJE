def main():
    import matplotlib.pyplot as plt
    import csv
    f=open('population.csv','r',encoding='ANSI')
    data=csv.reader(f,delimiter=',')
    header=next(data)
    X=[]
    m=[]
    w=[]
    for row in data:
        if (row[3]!=''and row[4]!=''):
            X.append(row[1])
            m.append(int(row[3]))
            w.append(int(row[4]))
    plt.title('Population of Jeju-do')
    plt.plot(X,m,label='Men',marker='s')
    plt.plot(X,w,label='Women',marker='s')
    plt.ylabel('Population')
    plt.xlabel('Year (2011-2022)')
    plt.legend()
    plt.show()


    
if __name__ == '__main__':
    main()
