# 主要是需要moviepy这个库
# from moviepy.editor import VideoFileClip, concatenate_videoclips
import os, xlrd, yaml
import moviepy.editor as mp

def mkdir(path):
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False


# filename = "config_clip.xlsx"

# def read_xlsx(filename):
#     if not os.path.exists(filename):
#         print(f"当前目录下文件{filename}不存在！！！！！！！！！")
#         return
#     data1 = xlrd.open_workbook(filename)
#     return data1

# def all_file(data1):
#     all_table = data1.sheet_by_name("合并")
#     if not all_table:
#         print("没有合并页签")
#         return
#     n_rows = all_table.nrows

#     for v in range(1,n_rows):
#         data_list = all_table.row_values(v)
#         for index in  data_list[1::]:
#             if not os.path.exists(index):
#                 print(f"路径{index}配置错误")
#                 return 

#     for v in range(1,n_rows):
#         data_list = all_table.row_values(v)
#         L = []
#         for index in data_list[1::]:
#             video = VideoFileClip(index)
#             L.append(video)
#         final_clip = concatenate_videoclips(L)
#         new_path = os.path.split(data_list[0])[0]
#         mkdir(new_path)
#         final_clip.write_videofile(data_list[0],write_logfile=True)
#         final_clip.close()

# def shuiyin_file(data1):
#     all_table = data1.sheet_by_name("水印")
#     if not all_table:
#         print("没有水印页签")
#         return
#     n_rows = all_table.nrows

#     for v in range(1,n_rows):
#         data_list = all_table.row_values(v)
#         if not os.path.exists(data_list[1]):
#             print(f"路径{data_list[1]}配置错误")
#             return

#         if not os.path.exists(data_list[2]):
#             print(f"路径{data_list[2]}配置错误")
#             return

#     for v in range(1,n_rows):
#         data_list = all_table.row_values(v)
#         video = mp.VideoFileClip(data_list[1])
#         #准备log图片
#         logo = (mp.ImageClip(data_list[2])
#                 .set_duration(video.duration) # 水印持续时间
#                 .resize(height=100) # 水印的高度，会等比缩放
#                 .margin(right=0, top=0, opacity=1) # 水印边距和透明度
#                 .set_pos(("right","top"))) # 水印的位置

#         final_clip = mp.CompositeVideoClip([video, logo])

#         new_path = os.path.split(data_list[0])[0]
#         mkdir(new_path)
#         final_clip.write_videofile(data_list[0],write_logfile=True)
#         final_clip.close()

# data1 = read_xlsx(filename)
# if data1:
#     shuiyin_file(data1)
#     all_file(data1)

config_file = "config.yaml"

with open(config_file, 'r', encoding="utf-8") as yamlfile:
    config_data = yaml.load(yamlfile)

def import_file():
    top_file = mp.VideoFileClip(config_data["top_file"])
    end_file = mp.VideoFileClip(config_data["end_file"])
    for root, dirs, files in os.walk(config_data["mid_file"]):
        for file in files:
            mid_file = os.path.join(root,file)
            out_file = os.path.join(config_data["finall_file"],file)
            video = mp.VideoFileClip(mid_file)
            #准备log图片
            logo = (mp.ImageClip(config_data["watermark_file"])
                    .set_duration(video.duration) # 水印持续时间
                    .resize(height=100) # 水印的高度，会等比缩放
                    .margin(right=0, top=0, opacity=1) # 水印边距和透明度
                    .set_pos(("right","top"))) # 水印的位置
            mid_water_file = mp.CompositeVideoClip([video, logo])
            final_clip = mp.concatenate_videoclips([top_file, mid_water_file, end_file])
            final_clip.write_videofile(out_file, **config_data["write_videofile"])
            final_clip.close()

import_file()