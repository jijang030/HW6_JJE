def main():
    import matplotlib.pyplot as plt
    import csv
    from matplotlib import rc
    
    f=open('subway.csv','r',encoding='ANSI')
    data=csv.reader(f,delimiter=',')
    header=next(data)
    geton79=[]
    getoff79=[]
    getonoff79=[]
    for row in data:
        if (row[8]!=''and row[10]!=''):
            geton79.append([(row[1]+'-\n'+row[2]),(int(row[8])+int(row[10]))])
        if (row[9]!=''and row[11]!=''):
            getoff79.append([(row[1]+'-\n'+row[2]),(int(row[9])+int(row[11]))])
        if (row[8]!=''and row[10]!=''and row[9]!=''and row[11]!=''):
            getonoff79.append([(row[1]+'-\n'+row[2]),(int(row[8])+int(row[10])+int(row[9])+int(row[11]))])
    #내림차순 정렬.
    geton79.sort(key=lambda x:-x[1])
    getoff79.sort(key=lambda x:-x[1])
    getonoff79.sort(key=lambda x:-x[1])

    getonX=[]
    getonY=[]
    getoffX=[]
    getoffY=[]
    getonoffX=[]
    getonoffY=[]
    
    #30개추출.
    for i in range(30):
        getonX.append(geton79[i][0])
        getonY.append(geton79[i][1])
    for i in range(30):
        getoffX.append(getoff79[i][0])
        getoffY.append(getoff79[i][1])
    for i in range(30):
        getonoffX.append(getonoff79[i][0])
        getonoffY.append(getonoff79[i][1])

    plt.rc('font',family='Malgun Gothic')
    #plt.rcParams['axes.unicode_minus']=False
    plt.subplot(3,1,1)
    plt.bar(getonX,getonY,color='r')
    plt.xticks(fontsize=5)
    plt.xlabel('Subway Line Number-Station_GetOn')
    plt.ylabel('Passenger Population')

    plt.subplot(3,1,2)
    plt.bar(getoffX,getoffY,color='b')
    plt.xticks(fontsize=5)
    plt.xlabel('Subway Line Number-Station_GetOff')
    plt.ylabel('Passenger Population')

    plt.subplot(3,1,3)
    plt.bar(getonoffX,getonoffY,color='y')
    plt.xticks(fontsize=5)
    plt.xlabel('Subway Line Number-Station_GetOn-off')
    plt.tight_layout()
    plt.show()
    
    plt.ylabel('Passenger Population')
if __name__ == '__main__':
    main()
