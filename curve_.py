import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

dir_path = "/home/syndra/DL/yolov8/ultralytics/run/train/"
alpha_ciou = "exp39/results.csv"
alpha_eiou = "exp40/results.csv"
alpha_siou = "exp41/results.csv"
alpha_wiou = "exp42/results.csv"

try:
    data_ciou  = pd.read_csv(dir_path+alpha_ciou)
    data_eiou  = pd.read_csv(dir_path+alpha_eiou)
    data_siou  = pd.read_csv(dir_path+alpha_siou)
    data_wiou  = pd.read_csv(dir_path+alpha_wiou)
    data_ciou.columns = data_ciou.columns.str.strip()
    data_eiou.columns = data_eiou.columns.str.strip()
    data_siou.columns = data_siou.columns.str.strip()
    data_wiou.columns = data_wiou.columns.str.strip()

except FileNotFoundError:
    print(f"文件未找到，请确认路径是否正确。")
    exit()

datas = [data_ciou, data_eiou, data_siou, data_wiou]
labels = ['ciou', 'eiou', 'siou', 'wiou']

def smooth_data(data, column, window_size):
    return data[column].rolling(window=window_size, center=False).mean()

def plot_curve(datas, x_column, y_columns, title, xlabel, ylabel, ranger, loc):
    # plt.figure(figsize=(10, 6))
    x1, x2, y1, y2 = ranger
    loc1, loc2 = loc
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, data in enumerate(datas):
        y_column = y_columns[0]
        smooth = smooth_data(data, y_column, window_size=10) 
        # smooth = data[y_column]
        ax.plot(data[x_column], smooth, linewidth = 1, label=labels[i])
    ax.set_xlabel(xlabel, fontsize=14, family='serif')
    ax.set_ylabel(ylabel, fontsize=14, family='serif')
    ax.set_title(title, fontsize=18, family='serif')
    ax.legend(loc=loc1)
    axins = inset_axes(ax, width="40%", height="40%", loc=loc2)
    for i, data in enumerate(datas):
        y_column = y_columns[0]
        smooth = smooth_data(data, y_column, window_size=10) 
        # smooth = data[y_column]
        axins.plot(data[x_column], smooth, linewidth = 1, label=labels[i])
    axins.set_xlim(x1, x2)
    axins.set_ylim(y1, y2)
    axins.set_xticks([])
    axins.set_yticks([])
    mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")
    
    # plt.tight_layout()
    plt.show()

# plot_curve(datas, 'epoch', ['train/box_loss'], 'Box Loss', 'Epoch', 'Loss', [280, 300, 0.75, 0.9], ['lower left', 1])
# plot_curve(datas, 'epoch', ['val/box_loss'], 'Box Loss', 'Epoch', 'Loss', [280, 300, 0.75, 0.9], ['lower left', 1])
# plot_curve(datas, 'epoch', ['metrics/precision(B)'], 'Precision', 'Epoch', 'Loss', [280, 300, 0.8, 0.98], ['lower right', 'center'])
# plot_curve(datas, 'epoch', ['metrics/recall(B)'], 'Box Loss', 'Epoch', 'Loss', [280, 300, 0.8, 0.98], ['lower right', 'center'])
# plot_curve(datas, 'epoch', ['metrics/precision(B)'], 'Precision', 'Epoch', 'Value')
# plot_curve(datas, 'epoch', ['metrics/recall(B)'], 'Precision', 'Epoch', 'Value')
# plot_curve(datas, 'epoch', ['metrics/mAP50(B)'], 'mAP@50', 'Epoch', 'Value', [280, 300, 0.95, 0.985], ['lower right', 'center'])
plot_curve(datas, 'epoch', ['metrics/mAP50-95(B)'], 'Precision', 'Epoch', 'Value', [280, 300, 0.68, 0.74], ['lower right', 'center'])
