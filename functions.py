import cv2
import os
import glob

# video to img
def extract_frames(video_path, output_folder, interval):
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % interval == 0:
            output_path = f"{output_folder}/frame_{interval}_{frame_count // interval}.jpg"
            cv2.imwrite(output_path, frame)
        frame_count += 1
    cap.release()


# 计数文件夹里的文件个数
def count_files_in_directory(directory):
    return len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])


# 删除文件夹下的图片
def del_imgs(folder_path):
    # 定义要删除的图片文件夹路径
    # 获取文件夹中所有图片文件的路径
    image_files = glob.glob(os.path.join(folder_path, '*.jpg')) + glob.glob(os.path.join(folder_path, '*.png'))

    # 遍历所有图片文件并删除
    for image_file in image_files:
        os.remove(image_file)
