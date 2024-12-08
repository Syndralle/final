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
v8s = "exp39/results.csv"
our = "exp32/results.csv"

try:
    data_ciou  = pd.read_csv(dir_path+alpha_ciou)
    data_eiou  = pd.read_csv(dir_path+alpha_eiou)
    data_siou  = pd.read_csv(dir_path+alpha_siou)
    data_wiou  = pd.read_csv(dir_path+alpha_wiou)
    data_v8s  = pd.read_csv(dir_path+v8s)
    data_our  = pd.read_csv(dir_path+our)


    data_ciou.columns = data_ciou.columns.str.strip()
    data_eiou.columns = data_eiou.columns.str.strip()
    data_siou.columns = data_siou.columns.str.strip()
    data_wiou.columns = data_wiou.columns.str.strip()
    data_v8s.columns = data_wiou.columns.str.strip()
    data_our.columns = data_wiou.columns.str.strip()


except FileNotFoundError:
    print(f"文件未找到，请确认路径是否正确。")
    exit()

# iou
datas = [data_ciou, data_eiou, data_siou, data_wiou]
labels = ['ciou', 'eiou', 'siou', 'wiou']

# ablation

def smooth_data(data, column, window_size):
    return data[column].rolling(window=window_size, center=False).mean()

def plot_curve(datas, x_column, y_columns, title, xlabel, ylabel, ranger, loc, save_name, insert = True, winsz=10):
    save_path = './curve/'
    # plt.figure(figsize=(10, 6))
    x1, x2, y1, y2 = ranger
    loc1, loc2 = loc
    fig, ax = plt.subplots(figsize=(10, 6))
    for i, data in enumerate(datas):
        y_column = y_columns[0]
        smooth = smooth_data(data, y_column, window_size=winsz) 
        # smooth = data[y_column]
        ax.plot(data[x_column], smooth, linewidth = 1, label=labels[i])
    ax.set_xlabel(xlabel, fontsize=14, family='serif')
    ax.set_ylabel(ylabel, fontsize=14, family='serif')
    ax.set_title(title, fontsize=18, family='serif')
    ax.legend(loc=loc1)
    if insert:
        axins = inset_axes(ax, width="40%", height="40%", loc=loc2)
        for i, data in enumerate(datas):
            y_column = y_columns[0]
            smooth = smooth_data(data, y_column, window_size=winsz) 
            # smooth = data[y_column]
            axins.plot(data[x_column], smooth, linewidth = 1, label=labels[i])
        axins.set_xlim(x1, x2)
        axins.set_ylim(y1, y2)
        axins.set_xticks([])
        axins.set_yticks([])
        mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")
    
    # plt.tight_layout()
    # plt.show()
    plt.savefig(save_path+save_name, dpi=300, bbox_inches = 'tight')


# iou
plot_curve(datas, 'epoch', ['train/box_loss'], 'train/box loss over epochs', 'epoch', 'loss', [280, 300, 0.75, 0.9], ['lower left', 1], 'v8n_train_box_loss.png')
plot_curve(datas, 'epoch', ['val/box_loss'], 'val/box loss over epochs', 'epoch', 'loss', [280, 300, 0.8, 0.9], ['lower left', 1], 'v8n_val_box_loss.png')
plot_curve(datas, 'epoch', ['metrics/precision(B)'], 'precision over epochs', 'epoch', 'loss', [280, 300, 0.85, 0.95], ['lower right', 'center'], 'v8n_precision.png')
plot_curve(datas, 'epoch', ['metrics/recall(B)'], 'recall over epochs', 'epoch', 'loss', [280, 300, 0.87, 0.95], ['lower right', 'center'], 'v8n_recall.png')
plot_curve(datas, 'epoch', ['metrics/mAP50(B)'], 'mAP@50 over epochs', 'epoch', 'mAP@50', [280, 300, 0.95, 0.985], ['lower right', 'center'], 'v8n_map50.png')
plot_curve(datas, 'epoch', ['metrics/mAP50-95(B)'], 'mAP@50:95 over epochs', 'epoch', 'mAP@50:95', [280, 300, 0.68, 0.74], ['lower right', 'center'], 'v8n_map50_95.png')
#

# datas = [data_v8s, data_our]
# labels = ['yolov8s', 'our model']
#
# plot_curve(datas, 'epoch', ['train/box_loss'], 'train/box loss over epochs', 'epoch', 'loss', [280, 300, 0.75, 0.9], ['upper right', 1], 'ablation_train_box_loss.png', False, 30)
# plot_curve(datas, 'epoch', ['val/box_loss'], 'val/box loss over epochs', 'epoch', 'loss', [280, 300, 0.8, 0.9], ['upper right', 1], 'ablation_val_box_loss.png', False, 30)
# plot_curve(datas, 'epoch', ['metrics/precision(B)'], 'precision over epochs', 'epoch', 'loss', [280, 300, 0.85, 0.95], ['lower right', 'center'], 'ablation_precision.png', False, 3)
# plot_curve(datas, 'epoch', ['metrics/recall(B)'], 'recall over epochs', 'epoch', 'loss', [280, 300, 0.87, 0.95], ['lower right', 'center'], 'ablation_recall.png', False, 5)
# plot_curve(datas, 'epoch', ['metrics/mAP50(B)'], 'mAP@50 over epochs', 'epoch', 'mAP@50', [280, 300, 0.95, 0.985], ['lower right', 'center'], 'ablation_map50.png', False, 50)
# plot_curve(datas, 'epoch', ['metrics/mAP50-95(B)'], 'mAP@50:95 over epochs', 'epoch', 'mAP@50:95', [280, 300, 0.68, 0.74], ['lower right', 'center'], 'ablation_map50_95.png', False, 50)
