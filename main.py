import functions
import numpy as np
import ocr_imgs
import img_to_plot

# 用户告知！/ Users informed!
print("Welcome to use wyb_project!")
print("Please place the video under the video folder")

# 逻辑判断 / logical judgment
video_path_lj = int(input("Whether to set the video_path( default video_path = ./video/wybdata.mp4)(1/0): "))
interval_lj = int(input("Whether to set the interval( default screenshot / fps = 30)(1/0): "))

video_path = "./video/wybdata.mp4"
output_folder = "./img"
# 输入 video name / Enter your video name
if video_path_lj:
    vi_name = input("Enter a video name(mind add suffix)： ")
    video_path = "./video/" + vi_name

# screenshot/fps
interval = 30  # 默认每隔30帧截取一张图片
if interval_lj:
    interval = int(input("screenshot / fps: "))

# screenshot
extract_frames = functions.extract_frames
extract_frames(video_path, output_folder, interval)

# 计数文件夹里的文件个数
directory = output_folder
count_files_in_directory = functions.count_files_in_directory
file_count = count_files_in_directory(directory) - 1

# 定义要遍历的文件夹路径
folder_path = output_folder
# 每帧计数
frame_count = 0
# 数据数组
data_str = []
# 丢失数组
data_lost = []

# ocr imgs
ocr_imgs = ocr_imgs.ocr_imgs(file_count, folder_path, interval, data_str, data_lost)

data_float = [float(x) for x in data_str]

# 绘图
# 定义万用表绘制的数据列表
Real_time_value = []
Maximum = []
Average = []
Minimum = []

for i in range(len(data_float)):
    if i % 4 == 0:
        Real_time_value.append(data_float[i])
        Maximum.append(data_float[i + 1])
        Average.append(data_float[i + 2])
        Minimum.append(data_float[i + 3])

fps = interval  # 30
Real_time_value = np.array(Real_time_value)
Maximum = np.array(Maximum)
Average = np.array(Average)
Minimum = np.array(Minimum)

x_y_lj = int(input("Whether to set x and y axis scale( default x_scale=2, y_scale=0.500)(1/0): "))
if x_y_lj:
    x_scale = float(input("input x axis scale: "))
    y_scale = float(input("input y axis scale: "))

title_lj = int(input("Whether to set the title of plot ( default \"wyb_plot\")(1/0): "))
if title_lj:
    title = input("enter a title for plot: ")

title = "wyb_plot"
wyb_plot = img_to_plot.wyb_plot(Real_time_value, Maximum, Average, Minimum, fps, title, x_scale=2, y_scale=0.500)

img_del_lj = int(input("Whether to delete imgs of imgs folder( default delete)(1/0): "))
if img_del_lj:
    folder_path = output_folder
    del_imgs  = functions.del_imgs(folder_path)
