# CapCut 专用 demo
# 使用 CapCut 专用的元数据（动画、转场、特效等）
import os
import pyJianYingDraft as draft
from pyJianYingDraft import trange, tim

# 设置 CapCut 草稿文件夹
# 注意：使用 CapCut 时需要指定 app_type="capcut"
draft_folder = draft.DraftFolder(r"/Users/xjc/Movies/CapCut/User Data/Projects/com.lveditor.draft", app_type="capcut")

tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'tutorial')
assert os.path.exists(tutorial_asset_dir), f"未找到例程素材文件夹{os.path.abspath(tutorial_asset_dir)}"

# 创建 CapCut 草稿
script = draft_folder.create_draft("demo_capcut", 1920, 1080, allow_replace=True)  # 1920x1080分辨率

# 添加音频、视频和文本轨道
script.add_track(draft.TrackType.audio).add_track(draft.TrackType.video).add_track(draft.TrackType.text)

# 创建音频片段
audio_segment = draft.AudioSegment(os.path.join(tutorial_asset_dir, 'audio.mp3'),
                                   trange("0s", "5s"),
                                   volume=0.6)
audio_segment.add_fade("1s", "0s")

# 创建视频片段 - 使用 CapCut 的入场动画
video_segment = draft.VideoSegment(os.path.join(tutorial_asset_dir, 'video.mp4'),
                                   trange("0s", "4.2s"))
# 使用 CapCut 专用动画：Zoom_In（放大）
video_segment.add_animation(draft.CapCut_Intro_type.Zoom_In)

# 创建贴纸片段
gif_material = draft.VideoMaterial(os.path.join(tutorial_asset_dir, 'sticker.gif'))
gif_segment = draft.VideoSegment(gif_material,
                                 trange(video_segment.end, gif_material.duration))
gif_segment.add_background_filling("blur", 0.0625)

# 使用 CapCut 专用转场：Dissolve（溶解）
video_segment.add_transition(draft.CapCut_Transition_type.Dissolve)

# 将片段添加到轨道中
script.add_segment(audio_segment).add_segment(video_segment).add_segment(gif_segment)

# 创建文本片段 - 使用 CapCut 的文本动画
text_segment = draft.TextSegment(
    "pyJianYingDraft\n现在支持CapCut!", video_segment.target_timerange,
    font=draft.FontType.文轩体,
    style=draft.TextStyle(color=(1.0, 1.0, 0.0)),
    clip_settings=draft.ClipSettings(transform_y=-0.8)
)
# 使用 CapCut 专用文本出场动画
text_segment.add_animation(draft.CapCut_Text_outro.Fade_Out, duration=tim("1s"))
script.add_segment(text_segment)

# 保存草稿
script.save()
print("CapCut 草稿已保存到 demo_capcut 文件夹")

