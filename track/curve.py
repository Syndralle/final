import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

# 读取YOLOv8生成的result.csv文件
dir_path = "/home/syndra/DL/yolov8/ultralytics/run/train/"
# alpha_ciou = "exp39/results.csv"
# alpha_eiou = "exp40/results.csv"
# alpha_siou = "exp41/results.csv"
alpha_wiou = "exp51/results.csv"


try:
    # data_ciou  = pd.read_csv(dir_path+alpha_ciou)
    # data_eiou  = pd.read_csv(dir_path+alpha_eiou)
    # data_siou  = pd.read_csv(dir_path+alpha_siou)
    data_wiou  = pd.read_csv(dir_path+alpha_wiou)
    # data_ciou.columns = data_ciou.columns.str.strip()
    # data_eiou.columns = data_eiou.columns.str.strip()
    # data_siou.columns = data_siou.columns.str.strip()
    data_wiou.columns = data_wiou.columns.str.strip()
# try:
#     data = pd.read_csv(file_path)
#     data.columns = data.columns.str.strip()
except FileNotFoundError:
    print(f"文件未找到，请确认路径是否正确。")
    exit()

# 检查文件内容
# print("文件头部信息:")
# print(data.head())

# 平滑函数 - 滑动平均
def smooth_data(data, column, window_size):
    return data[column].rolling(window=window_size, center=False).mean()

# 绘制曲线
def plot_curve(datas, x_column, y_columns, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    # print(data.columns)
    for i, data in enumerate(datas):
        for y_column in y_columns:
            if y_column in data.columns:
                # smooth = smooth_data(data, y_column, window_size=15) 
                # plt.plot(data[x_column], smooth, linewidth = 1, label=labels[i])
                # print(smooth)
                # smooth = gaussian_filter1d(data[y_column], sigma=1)
                # smooth = data[y_column]

                # coefficients = np.polyfit(data[x_column], data[y_column], 5)
                # polynomial = np.poly1d(coefficients)
                # x_smooth = np.linspace(0, 300, 300) 
                # y_smooth = polynomial(x_smooth)
                # plt.plot(x_smooth, y_smooth, label=y_column+str(i))

                plt.plot(data[x_column], data[y_column], label=y_column+str(i))
            else:
                print(f"列 {y_column} 不在文件中，跳过绘制。")
    plt.title(title, fontsize=18, fontweight='normal', family='serif')
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.legend(prop={"family":"serif", "weight": 'normal', "size": 14})
    # plt.grid()
    plt.tick_params(axis='both', labelsize=14)


    plt.show()

# 可视化不同指标
# datas = [data_ciou, data_eiou, data_siou, data_wiou]
# labels = ['ciou', 'eiou', 'siou', 'wiou']
datas = [data_wiou]
labels = ['loss']

plot_curve(datas, 'epoch', ['train/box_loss'], 'Box Loss', 'Epoch', 'Loss')
# plot_curve(datas, 'epoch', ['val/box_loss'], 'Box Loss', 'Epoch', 'Loss')
# plot_curve(datas, 'epoch', ['metrics/precision(B)'], 'Precision', 'Epoch', 'Value')
# plot_curve(datas, 'epoch', ['metrics/recall(B)'], 'Precision', 'Epoch', 'Value')
# plot_curve(datas, 'epoch', ['metrics/mAP50(B)'], 'Precision', 'Epoch', 'Value')
# plot_curve(datas, 'epoch', ['metrics/mwqAP50-95(B)'], 'Precision', 'Epoch', 'Value')
