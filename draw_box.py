import cv2
import argparse

def draw_yolo_box(image, bbox, class_name, 
                  box_color=(0, 255, 0), box_thickness=2, 
                  font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=0.5, 
                  font_color=(255, 255, 255), font_thickness=1):
    """
    Draws a bounding box and label on an image.

    Parameters:
        image (numpy.ndarray): The image on which to draw.
        bbox (tuple): YOLO format bounding box (class_id, x_center, y_center, width, height).
        class_name (str): The name of the class.
        box_color (tuple): Color of the bounding box in BGR.
        box_thickness (int): Thickness of the bounding box.
        font (int): Font type for the label.
        font_scale (float): Scale of the font for the label.
        font_color (tuple): Color of the font in BGR.
        font_thickness (int): Thickness of the font.
    """
    img_h, img_w = image.shape[:2]
    x_center, y_center, width, height = bbox

    # Convert YOLO format to pixel values
    x_center *= img_w
    y_center *= img_h
    width *= img_w
    height *= img_h

    # Calculate the top-left and bottom-right corners of the bounding box
    x1 = int(x_center - width / 2)
    y1 = int(y_center - height / 2)
    x2 = int(x_center + width / 2)
    y2 = int(y_center + height / 2)

    # Draw the bounding box
    cv2.rectangle(image, (x1, y1), (x2, y2), color=box_color, thickness=box_thickness)

    # Draw the label above the bounding box
    label_size, _ = cv2.getTextSize(class_name, font, font_scale, font_thickness)
    label_x = x1
    label_y = y1 - 10 if y1 - 10 > 10 else y1 + 10 + label_size[1]

    # Draw a filled rectangle behind the label for readability
    cv2.rectangle(image, (label_x, label_y - label_size[1] - 5), 
                         (label_x + label_size[0], label_y + 5), 
                         box_color, cv2.FILLED)
    
    # Put the class name text
    cv2.putText(image, class_name, (label_x, label_y), font, font_scale, 
                font_color, thickness=font_thickness)

def draw_yolo_box2(image, bbox, class_name, 
                  box_color=(0, 255, 0), box_thickness=2, 
                  font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=0.5, 
                  font_color=(255, 255, 255), font_thickness=1):
    """
    Draws a bounding box and label on an image.

    Parameters:
        image (numpy.ndarray): The image on which to draw.
        bbox (tuple): Bounding box in the format (x1, y1, x2, y2).
        class_name (str): The name of the class.
        box_color (tuple): Color of the bounding box in BGR.
        box_thickness (int): Thickness of the bounding box.
        font (int): Font type for the label.
        font_scale (float): Scale of the font for the label.
        font_color (tuple): Color of the font in BGR.
        font_thickness (int): Thickness of the font.
    """
    x1, y1, x2, y2 = bbox

    # Draw the bounding box
    cv2.rectangle(image, (x1, y1), (x2, y2), color=box_color, thickness=box_thickness)

    # Draw the label above the bounding box
    label_size, _ = cv2.getTextSize(class_name, font, font_scale, font_thickness)
    label_x = x1
    label_y = y1 - 10 if y1 - 10 > 10 else y1 + 10 + label_size[1]

    # Draw a filled rectangle behind the label for readability
    cv2.rectangle(image, (label_x, label_y - label_size[1] - 5), 
                         (label_x + label_size[0], label_y + 5), 
                         box_color, cv2.FILLED)
    
    # Put the class name text
    cv2.putText(image, class_name, (label_x, label_y), font, font_scale, 
                font_color, thickness=font_thickness)



if __name__ == "__main__":
    result_path = "./v5/"
    parser = argparse.ArgumentParser(); 
    parser.add_argument("image", type=str)
    parser.add_argument("bbox", type=str)
    args = parser.parse_args()

    bbox =  list(map(int, args.bbox.split(',')))
    class_name = "target"

    img = cv2.imread(args.image)

    draw_yolo_box2(img, bbox, class_name, 
                  box_color=(255, 0, 0), box_thickness=1, 
                  font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=0.6, 
                  font_color=(255, 255, 255), font_thickness=1)

    # Display the result
    cv2.imshow("Image with Bounding Box", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imwrite(result_path + args.image, img)
