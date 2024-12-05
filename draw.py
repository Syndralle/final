from ultralytics import YOLO
import numpy as np
import cv2
from ultralytics.utils.plotting import Annotator
from pathlib import Path

def yolo_to_abs_corner(label, image_width, image_height):
    x_center, y_center, width, height = label
    
    # 转换到绝对像素坐标
    x_center_abs = x_center * image_width
    y_center_abs = y_center * image_height
    width_abs = width * image_width
    height_abs = height * image_height
    
    x_min = x_center_abs - width_abs / 2
    y_min = y_center_abs - height_abs / 2
    x_max = x_center_abs + width_abs / 2
    y_max = y_center_abs + height_abs / 2
    print(x_min, y_min, x_max, y_max) 
    return [x_min, y_min, x_max, y_max]

if __name__=="__main__":
    # 加载图像
    dir_path = "/home/syndra/dataset/NUDT-SIRST/dataset/test/images/"
    result_path = Path('./box_result/')
    result_path.mkdir(parents = True, exist_ok=True)
    filename = "000489.png"
    # img_path = "000527.png"
    image = cv2.imread(dir_path + filename)
    h, w = image.shape[:2]

    # 000613
    # label_fast = [[130.61017, 130.42162, 140.11275, 134.08096]]
    # label_ssd = [[130.34772, 130.64674, 140.67593, 134.31941]]
    # label_v5 = [[0.53125,0.515625,0.0390625,0.015625]]
    # label_v5 = [yolo_to_abs_corner(label, w, h) for label in label_v5] 
    # label_v8 = [[0.52961,0.515874,0.0400087,0.0128153]]
    # label_v8 = [yolo_to_abs_corner(label, w, h) for label in label_v8] 
    # label_our = [[0.529374, 0.515787, 0.038038, 0.0141975]]
    # label_our = [yolo_to_abs_corner(label, w, h) for label in label_our] 

    # 001298
    # label_fast = [[93.99909, 205.1092, 101.46007, 211.26918 ], [134.0211, 158.30006, 146.36322, 168.4314]]
    # label_ssd = []
    # label_v5 = [[0.382812, 0.8125, 0.03125, 0.0234375]]
    # label_v5 = [yolo_to_abs_corner(label, w, h) for label in label_v5] 
    # label_v8 = [[0.383227, 0.813157, 0.0277526, 0.0240112]]  
    # label_v8 = [yolo_to_abs_corner(label, w, h) for label in label_v8] 
    # label_our = [[0.383103, 0.813503, 0.0270129, 0.0250805]]
    # label_our = [yolo_to_abs_corner(label, w, h) for label in label_our] 

    # 001292
    # label_fast = [[47.76933, 207.55952, 63.749348, 213.63043],
    #             [85.31143, 16.242117, 91.53997, 18.72726],
    #             [1.7834557, 32.110626, 23.179853, 41.94258],
    #             [18.587584, 75.86402, 27.873085, 78.54434],]
    #
    # label_ssd = []
    # label_v5 = [[0.345703, 0.0683594, 0.0273438, 0.0117188]]
    # label_v8 = [[0.346034, 0.0681593, 0.0270306, 0.00964238]]
    # label_our = [[0.346497, 0.0682517, 0.0258991, 0.00996265]]
    # label_v5 = [yolo_to_abs_corner(label, w, h) for label in label_v5] 
    # label_v8 = [yolo_to_abs_corner(label, w, h) for label in label_v8] 
    # label_our = [yolo_to_abs_corner(label, w, h) for label in label_our] 

    # 001280
    # label_fast = [[177.42847, 88.11353, 189.1566, 93.07168],
    #              [16.132524, 150.1967, 19.584246, 152.79279]]
    # label_ssd = [[176.99213, 87.79378, 189.06763, 92.97829]]
    # label_v5 = [[0.0683594, 0.589844, 0.0117188, 0.0078125],
    #             [0.712891, 0.353516, 0.0429688, 0.0195312]
    #             ]
    # label_v8 = [[0.714723, 0.354362, 0.0424465, 0.019552]]
    # label_our = [[0.715312, 0.353847, 0.0434522, 0.0192886]]
    # label_v5 = [yolo_to_abs_corner(label, w, h) for label in label_v5] 
    # label_v8 = [yolo_to_abs_corner(label, w, h) for label in label_v8] 
    # label_our = [yolo_to_abs_corner(label, w, h) for label in label_our] 

    # 001250
    # label_fast = [[125.397964, 125.31384, 141.02556, 137.55247],
    #              [56.200584, 242.83003, 59.217743, 250.01578 ]]
    # label_ssd = [[125.692085, 125.18349, 140.61963, 137.81194]]
    # label_v5 = [[0.519531, 0.513672, 0.0625, 0.0507812]]
    # label_v8 = [[0.519727, 0.513528, 0.0624174, 0.0504332]]
    # label_our = [[0.519761, 0.513865, 0.0625423, 0.0507019]]
    #
    # label_v5 = [yolo_to_abs_corner(label, w, h) for label in label_v5] 
    # label_v8 = [yolo_to_abs_corner(label, w, h) for label in label_v8] 
    # label_our = [yolo_to_abs_corner(label, w, h) for label in label_our] 

    # 000489
    label_fast = [[57.5485, 48.12487, 71.59709, 56.162674],
                 [183.74646, 218.2591, 198.00352, 224.48035],
                 [189.09102, 91.96685, 192.7668, 96.807556],
                 [3.7086835, 233.48732, 14.195627, 237.7097],
                 [15.9418745, 97.665085, 20.217356, 102.84661]]
    label_ssd = [[183.2667, 218.15388, 198.2591, 224.63301],
                 [59.085037, 47.67995, 72.00343, 55.714092]]
    label_v5 = [[0.744141, 0.865234, 0.0585938, 0.0273438],
                [0.253906, 0.203125, 0.0546875, 0.03125]
                ]
    label_v8 = [[0.253185, 0.202833, 0.0551331, 0.0318597],
                [0.744279, 0.864941, 0.0572076, 0.0272434],
                [0.745996, 0.369144, 0.0180925, 0.0194983],
                ]
    label_our = [[0.253617, 0.20295, 0.0551091, 0.0316331],
                 [0.744739, 0.865173, 0.0581381, 0.0266682]
                ]
    label_v5 = [yolo_to_abs_corner(label, w, h) for label in label_v5] 
    label_v8 = [yolo_to_abs_corner(label, w, h) for label in label_v8] 
    label_our = [yolo_to_abs_corner(label, w, h) for label in label_our] 
    all_label = [label_fast, label_ssd, label_v5, label_v8, label_our]
    result_name = ['faster', 'ssd', 'v5', 'v8', 'our']

    # label_ini = [[0.416016, 0.587891, 0.0195312, 0.0195312], [0.445312, 0.367188, 0.015625, 0.0234375]]
    # label_ini = [[0.931641, 0.462891, 0.0195312, 0.0195312]]
    # all_lable = [[236, 115, 242, 122],
    #              [65, 176, 71, 183],
    #              [66, 216, 73, 221],
    #              [120, 195, 126, 198],
    #              [240, 219, 248, 224],
    #              [168, 216, 186, 224],
    #              [11, 152, 28, 158]
    #             ]
    # h, w = image.shape[:2]
    # print(w)
    # print(h)
    # label_convert = [yolo_to_abs_corner(label, w, h) for label in label_ini]

    # print(label_convert) 
    # 定义多个 bounding boxes 和类信息
    # bboxes = label_convert  # 例如，多个框
    # bboxes = [all_lable[6]]
    # class_names = ["class1", "class2", "class3"]

    # 将图像转换为 YOLOv8 的 Annotator 对象

    for i, bboxes in enumerate(all_label):
        print(bboxes)

        img = cv2.imread(dir_path + filename)
        annotator = Annotator(img, line_width=1, font="Arial.ttf")
        class_names = ["target" for j in bboxes]
        confidences = [0.97 for j in bboxes]  # 每个框的置信度（可选）
        for (x1, y1, x2, y2), class_name, confidence in zip(bboxes, class_names, confidences):
            # label = f"{class_name}{confidence}"
            label = f"{class_name}"
            # annotator.box_label((x1, y1, x2, y2), label, color=(0, 255, 0))
            print(x1, y1, x2, y2)
            annotator.box_label(
                (x1, y1, x2, y2),
                label,
                color=(255, 0, 0),
                txt_color=(255, 255, 255),
                rotated=False,
            )
        # 获取带注释的图像
        annotated_image = annotator.result()
        # cv2.imshow("Annotated Image", annotated_image)

        cv2.imwrite(str(result_path / f"{result_name[i]}{filename}"), annotated_image)
