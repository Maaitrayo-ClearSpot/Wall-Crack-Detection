import sys
from utils.detect import detectCracks
from utils.helperFunc import imageLoader


if __name__ == '__main__':
        path_arg = sys.argv[1:]

        try:       
            image_path_list, image_name_list = imageLoader(path_arg)
            detectCracks(image_path_list=image_path_list, image_name_list = image_name_list)
        except Exception as Err:
             print(Err)
