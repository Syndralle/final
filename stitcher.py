from PIL import Image, ImageDraw, ImageFont
import os

class ImageStitcher:
    def __init__(self):
        self.grid_height = 1  # 默认网格高度
        self.grid_width = 1   # 默认网格宽度
        self.horizontal_spacing = 10  # 默认水平间距
        self.vertical_spacing = 10    # 默认垂直间距
        self.text_list = []           # 默认文本为空列表

    def set(self, h, w, horizontal_spacing=10, vertical_spacing=10):
        """
        设置网格布局和间距。
        Args:
            h (int): 网格高度（行数）。
            w (int): 网格宽度（列数）。
            horizontal_spacing (int): 图片之间的水平间距。
            vertical_spacing (int): 图片之间的垂直间距。
        """
        self.grid_height = h
        self.grid_width = w
        self.horizontal_spacing = horizontal_spacing
        self.vertical_spacing = vertical_spacing

    def func(self, *image_paths, text_list=None, output_path="output_stitched_image.png"):
        """
        拼接图片，支持手动网格设置。
        
        Args:
            image_paths (tuple): 图片路径列表。
            text_list (list): 每列底部显示的文本列表（可选）。
            output_path (str): 输出拼接图片的保存路径。
        """
        # 加载图片
        images = [Image.open(path) for path in image_paths]
        img_width, img_height = images[0].size  # 假设所有图片尺寸相同
        
        # 计算总网格大小
        total_width = self.grid_width * img_width + (self.grid_width - 1) * self.horizontal_spacing
        total_height = self.grid_height * img_height + (self.grid_height - 1) * self.vertical_spacing + 40  # 留出40像素给文本

        # 创建画布
        stitched_image = Image.new("RGB", (total_width, total_height), (255, 255, 255))
        draw = ImageDraw.Draw(stitched_image)

        # 设置字体
        try:
            font = ImageFont.truetype("/home/syndra/.local/share/fonts/NerdFonts/FiraCodeNerdFont-Bold.ttf", 25)
        except IOError:
            font = ImageFont.load_default()

        # 填充图片到网格
        for idx, img in enumerate(images):
            if idx >= self.grid_height * self.grid_width:
                print("警告: 图片数量超过网格容量，多余图片将被忽略")
                break

            row = idx // self.grid_width
            col = idx % self.grid_width
            x_offset = col * (img_width + self.horizontal_spacing)
            y_offset = row * (img_height + self.vertical_spacing)

            # 粘贴图片
            stitched_image.paste(img, (x_offset, y_offset))

            # 添加文本（如果提供了文本列表）
            # print(text_list)
            # print(idx)
            # print(row)
            # print(len(text_list))
            if row == self.grid_height - 1 and text_list:
                # print("yes")
                # print(idx)
                text = text_list[idx % 7]
                # print(text)
                text_bbox = font.getbbox(text)  # 获取文本边界框
                text_width = text_bbox[2] - text_bbox[0]
                text_height = text_bbox[3] - text_bbox[1]
                text_x = x_offset + (img_width - text_width) // 2
                text_y = y_offset + img_height + 10  # 文本位置略向下偏移
                draw.text((text_x, text_y), text, fill="black", font=font)
        # 保存结果
        stitched_image.save(output_path)
        print(f"拼接完成，保存到: {output_path}")


# 使用示例
if __name__ == "__main__":
    stitcher = ImageStitcher()
    
    # 设置网格布局（5 行 3 列），并设置间距
    stitcher.set(h=5, w=7, horizontal_spacing=10, vertical_spacing=10)

    # 指定图片路径
    # image_folder = "."  # 替换为你的图片文件夹路径
    # image_files = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith((".png", ".jpg"))]
    image_files = ["./origin/001250.png", "./mask/001250.png", "./faster/001250.png", "./ssd/001250.png", "./v5/001250.png", "./v8/001250.png", "./v8-improve/001250.png",
                   "./origin/000623.png", "./mask/000623.png", "./faster/000623.png", "./ssd/000623.png", "./v5/000623.png", "./v8/000623.png", "./v8-improve/000623.png",
                   "./origin/000672.png", "./mask/000672.png", "./faster/000672.png", "./ssd/000672.png", "./v5/000672.png", "./v8/000672.png", "./v8-improve/000672.png",
                   "./origin/000600.png", "./mask/000600.png", "./faster/000600.png", "./ssd/000600.png", "./v5/000600.png", "./v8/000600.png", "./v8-improve/000600.png",
                   "./origin/000527.png", "./mask/000527.png", "./faster/000527.png", "./ssd/000527.png", "./v5/000527.png", "./v8/000527.png", "./v8-improve/000527.png",
                  ]

    # mask_dir_path = "/home/syndra/dataset/NUDT-SIRST/masks/"
    # origin_dir_path = "/home/syndra/dataset/NUDT-SIRST/dataset/test/images/"
    # result_path = "./box_result/"
    # image_files = [
    #     origin_dir_path + "000613.png", mask_dir_path + "000613.png", result_path + "faster000613.png", result_path + "ssd000613.png", result_path + "v5000613.png", result_path + "v8000613.png", result_path + "our000613.png",
    #     origin_dir_path + "001298.png", mask_dir_path + "001298.png", result_path + "faster001298.png", result_path + "ssd001298.png", result_path + "v5001298.png", result_path + "v8001298.png", result_path + "our001298.png",
    #     origin_dir_path + "001292.png", mask_dir_path + "001292.png", result_path + "faster001292.png", result_path + "ssd001292.png", result_path + "v5001292.png", result_path + "v8001292.png", result_path + "our001292.png",
    #     origin_dir_path + "001280.png", mask_dir_path + "001280.png", result_path + "faster001280.png", result_path + "ssd001280.png", result_path + "v5001280.png", result_path + "v8001280.png", result_path + "our001280.png",
    #     origin_dir_path + "001250.png", mask_dir_path + "001250.png", result_path + "faster001250.png", result_path + "ssd001250.png", result_path + "v5001250.png", result_path + "v8001250.png", result_path + "our001250.png",
    #     origin_dir_path + "000489.png", mask_dir_path + "000489.png", result_path + "faster000489.png", result_path + "ssd000489.png", result_path + "v5000489.png", result_path + "v8000489.png", result_path + "our000489.png",
    # ]
    # # 添加文本
    # text_labels = ["Baseline", "Ground Truth", "Faster-Rcnn", "SSD", "Yolov5s", "Yolov8s", "Our Method"]
    text_labels = ["Baseline", "Ground Truth", "Faster-RCNN", "SSD", "Yolov5s", "Yolov8s", "Our Method"]

    # 调用拼接函数
    stitcher.func(*image_files, text_list=text_labels, output_path="output_grid_image.png")
