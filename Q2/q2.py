def main():
    import random
    import matplotlib.pyplot as plt
    r1=[]
    r2=[]
    r3=[]
    r4=[]
    for i in range (100):
        r=random.randint(1,6)
        r1.append(r)
    for i in range (1000):
        r=random.randint(1,6)
        r2.append(r)
    for i in range (10000):
        r=random.randint(1,6)
        r3.append(r)
    for i in range (100000):
        r=random.randint(1,6)
        r4.append(r)

    r1_n=[]
    r2_n=[]
    r3_n=[]
    r4_n=[]
    for i in range(6):
        r1_n.append(r1.count(i+1))
    for i in range(6):
        r2_n.append(r2.count(i+1))
    for i in range(6):
        r3_n.append(r3.count(i+1))
    for i in range(6):
        r4_n.append(r4.count(i+1))

    f=open('q2.csv','w',encoding='ANSI')
    f.write("시행횟수, 숫자1, 숫자2, 숫자3, 숫자4,숫자5,숫자6\n")
    f.write("{},{},{},{},{},{},{}\n".format("100번",r1_n[0],r1_n[1],r1_n[2],r1_n[3],r1_n[4],r1_n[5]))
    f.write("{},{},{},{},{},{},{}\n".format("1000번",r2_n[0],r2_n[1],r2_n[2],r2_n[3],r2_n[4],r2_n[5]))
    f.write("{},{},{},{},{},{},{}\n".format("10000번",r3_n[0],r3_n[1],r3_n[2],r3_n[3],r3_n[4],r3_n[5]))
    f.write("{},{},{},{},{},{},{}\n".format("100000번",r4_n[0],r4_n[1],r4_n[2],r4_n[3],r4_n[4],r4_n[5]))
    f.close()
            
    k=6
    X=[1,2,3,4,5,6]
    plt.subplot(2,2,1)
    plt.hist(r1,bins=range(1,k+2),color='r',rwidth=0.8, align='left')
    plt.xticks(X)
    plt.xlabel('Dice Number')
    plt.ylabel('Appearance Number of Each Dice Number')
    plt.title('Implement 100 times')

    plt.subplot(2,2,2)
    plt.hist(r2,bins=range(1,k+2),color='b',rwidth=0.8, align='left')
    plt.xticks(X)
    plt.xlabel('Dice Number')
    plt.ylabel('Appearance Number of Each Dice Number')
    plt.title('Implement 1000 times')

    plt.subplot(2,2,3)
    plt.hist(r3,bins=range(1,k+2),color='g',rwidth=0.8, align='left')
    plt.xticks(X)
    plt.xlabel('Dice Number')
    plt.ylabel('Appearance Number of Each Dice Number')
    plt.title('Implement 10000 times')

    plt.subplot(2,2,4)
    plt.hist(r4,bins=range(1,k+2),color='y',rwidth=0.8, align='left')
    plt.xticks(X)
    plt.xlabel('Dice Number')
    plt.ylabel('Appearance Number of Each Dice Number')
    plt.title('Implement 10000 times')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
