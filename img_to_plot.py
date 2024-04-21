import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


def wyb_plot(Real_time_value, Maximum, Average, Minimum, fps, title, x_scale=2, y_scale=0.500):
    x = [i for i in range(len(Real_time_value))]
    plt.figure(dpi=200)

    x_major_locator = MultipleLocator(x_scale)
    # 把x轴的刻度间隔设置为2，并存在变量里
    y_major_locator = MultipleLocator(y_scale)
    # 把y轴的刻度间隔设置为0.0500，并存在变量里
    ax = plt.gca()
    # ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    # 把x轴的主刻度设置为1的倍数
    ax.yaxis.set_major_locator(y_major_locator)
    # 把y轴的主刻度设置为10的倍数

    # # 绘制柱状图
    # y = Real_time_value
    # plt.bar(x, y)

    # 绘制曲线图
    plt.plot(x, Real_time_value, label='Real_time_value')
    plt.plot(x, Maximum, label='Maximum')
    plt.plot(x, Average, label='Average')
    plt.plot(x, Minimum, label='Minimum')

    # 绘制曲线图，并标出最大值和最小值
    max_y = np.max(Real_time_value)
    min_y = np.min(Real_time_value)
    max_index = np.argmax(Real_time_value)
    min_index = np.argmin(Real_time_value)
    plt.annotate("(%s,%s)" % (x[max_index], max_y), xy=(x[max_index], max_y), xytext=(x[max_index], max_y + 0.5),
                 textcoords='offset points',
                 color='red')
    plt.savefig('wyb_plot.png')
    plt.annotate("(%s,%s)" % (x[min_index], min_y), xy=(x[min_index], min_y), xytext=(x[min_index], min_y - 0.5),
                 textcoords='offset points',
                 color='green')

    max_y = np.max(Maximum)
    min_y = np.min(Maximum)
    max_index = np.argmax(Maximum)
    min_index = np.argmin(Maximum)
    plt.annotate("(%s,%s)" % (x[max_index], max_y), xy=(x[max_index], max_y), xytext=(x[max_index], max_y + 0.5),
                 textcoords='offset points',
                 color='red')
    plt.savefig('wyb_plot.png')
    plt.annotate("(%s,%s)" % (x[min_index], min_y), xy=(x[min_index], min_y), xytext=(x[min_index], min_y - 0.5),
                 textcoords='offset points',
                 color='green')

    max_y = np.max(Average)
    min_y = np.min(Average)
    max_index = np.argmax(Average)
    min_index = np.argmin(Average)
    plt.annotate("(%s,%s)" % (x[max_index], max_y), xy=(x[max_index], max_y), xytext=(x[max_index], max_y + 0.5),
                 textcoords='offset points',
                 color='red')
    plt.savefig('wyb_plot.png')
    plt.annotate("(%s,%s)" % (x[min_index], min_y), xy=(x[min_index], min_y), xytext=(x[min_index], min_y - 0.5),
                 textcoords='offset points',
                 color='green')

    max_y = np.max(Minimum)
    min_y = np.min(Minimum)
    max_index = np.argmax(Average)
    min_index = np.argmin(Average)
    plt.annotate("(%s,%s)" % (x[max_index], max_y), xy=(x[max_index], max_y), xytext=(x[max_index], max_y + 0.5),
                 textcoords='offset points',
                 color='red')
    plt.savefig('wyb_plot.png')
    plt.annotate("(%s,%s)" % (x[min_index], min_y), xy=(x[min_index], min_y), xytext=(x[min_index], min_y - 0.5),
                 textcoords='offset points',
                 color='green')

    plt.xlabel('x/'+str(fps)+"fps")
    plt.ylabel('y/A')
    plt.title(title)
    plt.legend()
    plt.savefig('wyb_plot.png')
    # plt.show()
