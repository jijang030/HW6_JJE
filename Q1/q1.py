def main():
    import csv
    import matplotlib.pyplot as plt
    f1=open('seoul.csv','r',encoding='ANSI')
    data=csv.reader(f1,delimiter=',')
    header=next(data)
    X=[]
    seoul=[]
    for row in data:
        #print(row)
        if row[2]!='':
            seoul.append(float(row[2]))
            X.append(row[0])
    f1.close()

    f2=open('all.csv','r',encoding='ANSI')
    data2=csv.reader(f2,delimiter=',')
    header2=next(data2)
    all=[]
    for row2 in data2:
        #print(row2)
        if row2[2]!='':
            all.append(float(row2[2]))
    f2.close()
    
    f3=open('daejeon.csv','r',encoding='ANSI')
    data3=csv.reader(f3,delimiter=',')
    header3=next(data3)
    daejeon=[]
    
    for row3 in data3:
        #print(row3)
        if row3[2]!='':
            daejeon.append(float(row3[2]))
    f3.close()

    f4=open('busan.csv','r',encoding='ANSI')
    data4=csv.reader(f4,delimiter=',')
    header4=next(data4)
    busan=[]
    for row4 in data4:
        #print(row4)
        if row4[2]!='':
            busan.append(float(row4[2]))
    f4.close()

    f5=open('jeju.csv','r',encoding='ANSI')
    data5=csv.reader(f5,delimiter=',')
    header5=next(data5)
    jeju=[]
    for row5 in data5:
        #print(row5)
        if row3[2]!='':
            jeju.append(float(row5[2]))
    f5.close()
    
    plt.title('Monthly Average Temperature In Seoul,Busan,Daejeon,Jeju,Nation in 2022')
    plt.plot(X,seoul,label='seoul',marker='s')
    plt.plot(X,all,label='all',marker='s')
    plt.plot(X,daejeon,label='daejeon',marker='s')
    plt.plot(X,busan,label='busan',marker='s')
    plt.plot(X,jeju,label='jeju',marker='s')
    plt.xlabel('Months in 2022')
    plt.ylabel('Monthly Average Temperature')
    plt.legend()
    plt.show()
                         
if __name__ == '__main__':
    main()
