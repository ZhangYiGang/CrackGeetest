import matplotlib.pyplot as plt
import numpy as np
filepath=r"C:\Users\zhang\Desktop\\"
def  manage_log(log):
       file = open(filepath+log)
       filewrite = open(r"C:\Users\zhang\Desktop\data.txt", 'w')
       for line in file.readlines():
          string = line.split()
          try:
            num = int(string[0])
            if num !=0:
                data = string[3]
                location = data.split(",")
                filewrite.write(location[0] + " ")
                filewrite.write(location[1] + "\n")
          except  ValueError:
                print("文件输入完成")
          except BaseException as e:
                print(e)

def  load_filename(filename):
     """
         加载文件
       :type list
       :return: x,y数组
     """
     xarr = []#x坐标
     yarr = []
     yarrReviese=[]
     min=0
     max=0
     num=0
     try:
        file=open(filename)
     except FileNotFoundError:
        print("文件未找到")
     else:

         for line in file.readlines():
           if(num==0):
               min = float(line.split()[0])
           linearr = []
           num+=1
           linearr.append(float(num))
           linearr.append(1.0)
           xarr.append(linearr)
           data = float(line.split()[0])
           yarr.append(data)
           if(data<min):
               min=data
           max=data
         rangenum=max-min
         print(rangenum)
         for data in yarr:
             data=(data-min)/rangenum
             yarrReviese.append(data)
     #xarr = range(1,num+1)list(xarr
     return xarr,yarrReviese


def plot_data():
    """
    绘制图像
    :return: 无
    """
    xArr,yArr=load_filename(filepath+"data.txt")
    fig = plt.figure()
    plot = fig.add_subplot(111)  # 添加子图
    plot.scatter(xArr,yArr, s=20, c='blue', alpha=.5)
    plt.title('位移与时间')
    plt.show()
def plotlinear():
    """
    :type:numpy
    :return:y数组
    """
    xArr, yArr = load_filename(filepath + "data.txt")

    xMat = np.mat(xArr) #转矩阵

    yMat = np.mat(yArr).T
    xTx = xMat.T * xMat

    if np.linalg.det(xTx) == 0.0:
        print("矩阵为奇异矩阵,不能求逆")
        return
    ws = xTx.I * (xMat.T * yMat)
    print(ws)
    xCopy = xMat.copy()                                                    #拷贝xMat矩阵
    xCopy.sort(0)                                                        #排序
    yHat = xCopy * ws                                                     #计算对应的y值
    # print(yHat)
    fig = plt.figure()
    ax = fig.add_subplot(111)                                            #添加subplot
    ax.plot(xCopy[:, 0], yHat, c = 'red')                                #绘制回归曲线
    ax.scatter(xMat[:,0].flatten().A[0], yMat.flatten().A[0], s = 20, c = 'blue',alpha = .5)                #绘制样本点
    plt.title('DataSet')
    # plt.show()
    return yHat
def plotlwlrRegression():
    """
    函数说明:绘制多条局部加权回归曲线
    Returns:无
    """
    xArr, yArr = load_filename(filepath+'data.txt')
    yHat_1 = lwlrTest(xArr, xArr, yArr, 1.0)
    yHat_2 = lwlrTest(xArr, xArr, yArr, 0.01)
    yHat_3 = lwlrTest(xArr, xArr, yArr, 0.003)
    xMat = np.mat(xArr)
    yMat = np.mat(yArr)
    # srtInd = xMat[:, 0].argsort(0)                                        #排序
    # xSort = xMat[srtInd]
    # print(xSort)
    fig, axs = plt.subplots(nrows=3, ncols=1,sharex=False, sharey=False, figsize=(10,8))
    axs[0].plot(xMat[:, 0], yHat_1, c = 'red')                        #绘制回归曲线
    axs[1].plot(xMat[:, 0], yHat_2, c = 'red')                        #绘制回归曲线
    axs[2].plot(xMat[:, 0], yHat_3, c = 'red')                        #绘制回归曲线
    axs[0].scatter(xMat[:,0].flatten().A[0], yMat.flatten().A[0], s = 20, c = 'blue', alpha = .5)                #绘制样本点
    axs[1].scatter(xMat[:,0].flatten().A[0], yMat.flatten().A[0], s = 20, c = 'blue', alpha = .5)                #绘制样本点
    axs[2].scatter(xMat[:,0].flatten().A[0], yMat.flatten().A[0], s = 20, c = 'blue', alpha = .5)                #绘制样本点
    #设置标题,x轴label,y轴label
    axs0_title_text = axs[0].set_title(r'局部加权回归曲线,k=1.0')
    axs1_title_text = axs[1].set_title(u'局部加权回归曲线,k=0.01')
    axs2_title_text = axs[2].set_title(u'局部加权回归曲线,k=0.003')
    plt.setp(axs0_title_text, size=8, weight='bold', color='red')
    plt.setp(axs1_title_text, size=8, weight='bold', color='red')
    plt.setp(axs2_title_text, size=8, weight='bold', color='red')
    plt.xlabel('X')
    plt.show()
def lwlr(testPoint, xArr, yArr, k = 1.0):
    """
    函数说明:使用局部加权线性回归计算回归系数w
    Parameters:
        testPoint - 测试样本点
        xArr - x数据集
        yArr - y数据集
        k - 高斯核的k,自定义参数
    Returns:ws - 回归系数
    """
    xMat = np.mat(xArr); yMat = np.mat(yArr).T
    m = np.shape(xMat)[0]
    weights = np.mat(np.eye((m)))                                        #创建权重对角矩阵
    for j in range(m):                                                  #遍历数据集计算每个样本的权重
        diffMat = testPoint - xMat[j, :]
        weights[j, j] = np.exp(diffMat * diffMat.T/(-2.0 * k**2))
    xTx = xMat.T * (weights * xMat)
    if np.linalg.det(xTx) == 0.0:
        print("矩阵为奇异矩阵,不能求逆")
        return
    ws = xTx.I * (xMat.T * (weights * yMat))                            #计算回归系数
    return testPoint * ws
def lwlrTest(testArr, xArr, yArr, k=1.0):
    """
    函数说明:局部加权线性回归测试
    Parameters:
        testArr - 测试数据集
        xArr - x数据集
        yArr - y数据集
        k - 高斯核的k,自定义参数
    Returns:
        ws - 回归系数
    Website:
http://www.cuijiahua.com/
    Modify:
        2017-11-15
    """
    m = np.shape(testArr)[0]                                            #计算测试数据集大小
    yHat = np.zeros(m)
    for i in range(m):                                                    #对每个样本点进行预测
        yHat[i] = lwlr(testArr[i],xArr,yArr,k)
    return yHat

if __name__ == '__main__':
    manage_log("自己.log")
    plotlinear()




