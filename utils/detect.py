import cv2
from utils.yolo_segment import YOLOSegmentationSupport
from utils.helperFunc import imageLoader, frame_hyt, frame_wid


def find_width(points):
     print(points)

def find_width(coords):
    """
    Calculates the difference between the minimum and maximum x positions
    of a list of x coordinates.
    """
    x_coords = coords[:,0]
    min_x = min(x_coords)
    max_x = max(x_coords)
    diff = max_x - min_x
    print(f'Width = {diff}')
    print(f'Width = {coords[0]}')
    return diff

def detectCracks(image_path_list, image_name_list):
    for img_path, image_name in zip(image_path_list, image_name_list):
        img = cv2.imread(img_path)
        
        # Segmentation detector
        ys = YOLOSegmentationSupport("..\model\crackDetect50epoch.pt")

        bboxes, classes, segmentations, scores = ys.detect(img)
        for bbox, class_id, seg, score in zip(bboxes, classes, segmentations, scores):
            # print("bbox:", bbox, "class id:", class_id, "seg:", seg, "score:", score)
            # print("class id:", class_id)
            (x, y, x2, y2) = bbox
            if class_id == 0:
                find_width(seg)
                cv2.polylines(img, [seg], True, (0, 0, 255), 4)
                # cv2.rectangle(img, (x, y), (x2, y2), (255, 0, 0), 2)
                # cv2.putText(img, str(class_id), (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

        img = cv2.resize(img, (frame_wid, frame_hyt))
        cv2.imshow(image_name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()