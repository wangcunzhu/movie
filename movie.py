import os, yaml
import moviepy.editor as mp

config_file = "config.yaml"

with open(config_file, 'r', encoding="utf-8") as f:
    config_data = yaml.load(f, Loader=yaml.FullLoader)

def import_file():
    top_file = mp.VideoFileClip(config_data["top_file"])
    end_file = mp.VideoFileClip(config_data["end_file"])
    for root, dirs, files in os.walk(config_data["mid_file"]):
        for file in files:
            mid_file = os.path.join(root, file)
            out_file = os.path.join(config_data["finall_file"], file)
            video = mp.VideoFileClip(mid_file)
            #准备log图片
            logo = (mp.ImageClip(config_data["watermark_file"])
                    .set_duration(video.duration)  # 水印持续时间
                    .resize(height=100)  # 水印的高度，会等比缩放
                    .margin(right=0, top=0, opacity=1)  # 水印边距和透明度
                    .set_pos(("right", "top")))  # 水印的位置
            mid_water_file = mp.CompositeVideoClip([video, logo])
            final_clip = mp.concatenate_videoclips([top_file, mid_water_file, end_file])
            final_clip.write_videofile(out_file, **config_data["write_videofile"])
            final_clip.close()


import_file()
