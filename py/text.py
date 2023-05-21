from os import system
import requests
# message="下载视频 BV1LX4y1m7Xe"
# # system('rm /root/NewBing/bbdown/video.mp4')
# bv = message.replace("下载视频", "").strip()
# bv = bv[bv.find("BV"):bv.find("/?")]
# print(len(bv))
# system('/root/NewBing/bbdown/BBDown ' + bv + ' --dfn-priority "8K 超高清, 1080P 高码率, HDR 真彩, 杜比视界" --work-dir "/root/NewBing/bbdown" -F "video.mp4"')
# print("开始BBDown下载")
# video_url = "/root/NewBing/bbdown/video.mp4"
# print("下载完成")
# message = "[CQ:video,file=file:///root/NewBing/bbdown/video.mp4]"
# while 1:
res = requests.post(url='http://localhost:8600' + "/send_group_msg",
                            params={'group_id': int(698405409), 'message': "[CQ:image,file=https://mmbiz.qpic.cn/mmbiz_jpg/y1WjHtHDNP7URC1OkcZBYDcGt8TBlXIg02RHqWl5CIzC1ia2g42hFpUicbzStgsTm7dHOtyyRQ1wGm1LH9tpVm8w/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1]"}).json()