from cnocr import CnOcr
import re


def ocr_imgs(file_count, folder_path, interval, data_str, data_lost):
    # 遍历文件夹文件(图片)，进行文字识别
    for frame_count in range(file_count):
        img_fp = f"{folder_path}/frame_{interval}_{frame_count}.jpg"
        ocr = CnOcr()  # 所有参数都使用默认值
        out_list = ocr.ocr(img_fp)
        data_list = []
        for dict in out_list:
            text = dict.get('text')
            match = re.search(r'[0-9Oo][.,][0-9Oo][0-9Oo][0-9Oo][0-9Oo]|[Q][0-9Oo][0-9Oo][0-9Oo][0-9Oo]', text)  # 正则化匹配
            if match:
                result = match.group()
                # print(result)
                # with open('output.txt', 'a') as f:
                #     print(result, file=f)
                result = result.replace('O', '0').replace('o', '0').replace(',', '.')  # 修正数据
                data_list.append(result)
                # with open('output.txt', 'a') as f:
                #     print(result, file=f)
        if len(data_list) % 4 == 0:
            data_str += data_list
        else:
            print("数据丢失," + "frame_" + str(interval) + "_" + str(frame_count) + ".jpg" + "未采集")
            data_lost.append(frame_count)

    # 手动采集图片数据 / manual capture
    man_cap = int(input("Whether manual collection(1/0): "))
    if man_cap:
        for frame in data_lost:
            data_ins = 0
            for i in range(4):
                if i == 0:
                    data_ins = (input("rea: "))
                if i == 1:
                    data_ins = (input("max: "))
                if i == 2:
                    data_ins = (input("ave: "))
                if i == 3:
                    data_ins = (input("min: "))
                data_str.insert((file_count - len(data_list) + 1) * 4 + i, data_ins)
