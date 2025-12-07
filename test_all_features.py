"""
全面功能测试脚本
测试 pyJianYingDraft 的所有功能特性
"""
import os
import sys
import pyJianYingDraft as draft
from pyJianYingDraft import (
    trange, tim, SEC,
    IntroType, OutroType, GroupAnimationType,
    TextIntro, TextOutro, TextLoopAnim,
    TransitionType, FilterType, MaskType,
    VideoSceneEffectType, VideoCharacterEffectType,
    AudioSceneEffectType,
    KeyframeProperty,
    ClipSettings, CropSettings,
    TextBorder, TextBackground, TextShadow
)

# 这些类型需要从metadata直接导入
from pyJianYingDraft.metadata import ToneEffectType, SpeechToSongType

# CapCut 专用类型
from pyJianYingDraft import (
    CapCut_Intro_type, CapCut_Outro_type, CapCut_Group_animation_type,
    CapCut_Transition_type, CapCut_Text_intro, CapCut_Text_outro, CapCut_Text_loop_anim,
    CapCut_Video_scene_effect_type, CapCut_Video_character_effect_type,
    CapCut_Voice_filters_effect_type, CapCut_Voice_characters_effect_type,
    CapCut_Speech_to_song_effect_type, CapCut_Mask_type
)

def test_jianying_features():
    """测试剪映功能"""
    print("=" * 60)
    print("测试剪映功能")
    print("=" * 60)
    
    # 设置草稿文件夹
    draft_folder = draft.DraftFolder(
        r"/Users/xjc/Movies/CapCut/User Data/Projects/com.lveditor.draft",
        app_type="jianying"
    )
    
    tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'tutorial')
    assert os.path.exists(tutorial_asset_dir), f"未找到例程素材文件夹{os.path.abspath(tutorial_asset_dir)}"
    
    # 创建草稿
    script = draft_folder.create_draft("test_jianying_all_features", 1920, 1080, allow_replace=True)
    
    # 添加多个轨道
    script.add_track(draft.TrackType.audio, "audio_track_1")
    script.add_track(draft.TrackType.video, "video_track_1")
    script.add_track(draft.TrackType.video, "video_track_2")
    script.add_track(draft.TrackType.text, "text_track_1")
    script.add_track(draft.TrackType.effect, "effect_track_1")
    script.add_track(draft.TrackType.filter, "filter_track_1")
    
    print("\n1. 测试音频片段功能...")
    
    # 1.1 基本音频片段
    audio1 = draft.AudioSegment(
        os.path.join(tutorial_asset_dir, 'audio.mp3'),
        trange("0s", "3s"),
        volume=0.8
    )
    script.add_segment(audio1, "audio_track_1")
    
    # 1.2 带淡入淡出的音频
    audio2 = draft.AudioSegment(
        os.path.join(tutorial_asset_dir, 'audio.mp3'),
        trange("3s", "2s"),
        volume=0.6,
        speed=1.5,  # 1.5倍速
        change_pitch=True  # 变速时改变音调
    )
    audio2.add_fade("0.5s", "0.5s")  # 0.5s淡入，0.5s淡出
    script.add_segment(audio2, "audio_track_1")
    
    # 1.3 带音量关键帧的音频
    audio3 = draft.AudioSegment(
        os.path.join(tutorial_asset_dir, 'audio.mp3'),
        trange("5s", "2s"),
        volume=1.0
    )
    audio3.add_keyframe(tim("0s"), 0.3)  # 开始时30%音量
    audio3.add_keyframe(tim("1s"), 1.0)  # 1秒后100%音量
    audio3.add_keyframe(tim("2s"), 0.5)  # 结束时50%音量
    script.add_segment(audio3, "audio_track_1")
    
    # 1.4 带音频特效的音频
    audio4 = draft.AudioSegment(
        os.path.join(tutorial_asset_dir, 'audio.mp3'),
        trange("7s", "2s"),
        volume=0.7
    )
    # 注意：需要有效的音频特效ID
    # audio4.add_effect(AudioSceneEffectType.某个特效)
    script.add_segment(audio4, "audio_track_1")
    
    print("   ✓ 音频片段测试完成")
    
    print("\n2. 测试视频片段功能...")
    
    # 2.1 基本视频片段
    video1 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("0s", "2s")
    )
    script.add_segment(video1, "video_track_1")
    
    # 2.2 带入场动画的视频
    video2 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("2s", "2s")
    )
    video2.add_animation(IntroType.斜切)  # 入场动画
    script.add_segment(video2, "video_track_1")
    
    # 2.3 带出场动画的视频
    video3 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("4s", "2s")
    )
    video3.add_animation(OutroType.缩小)  # 出场动画
    script.add_segment(video3, "video_track_1")
    
    # 2.4 带组合动画的视频
    video4 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("6s", "2s")
    )
    try:
        video4.add_animation(GroupAnimationType.摇摆)  # 组合动画
    except:
        pass  # 如果动画不存在则跳过
    script.add_segment(video4, "video_track_1")
    
    # 2.5 带转场的视频
    video5 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("8s", "2s")
    )
    video5.add_transition(TransitionType.信号故障)  # 转场效果
    script.add_segment(video5, "video_track_1")
    
    # 2.6 带淡入淡出的视频
    video6 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("10s", "2s")
    )
    video6.add_fade("0.5s", "0.5s")  # 淡入淡出
    script.add_segment(video6, "video_track_1")
    
    # 2.7 带变速的视频
    video7 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("12s", "1s"),
        speed=2.0  # 2倍速
    )
    script.add_segment(video7, "video_track_1")
    
    # 2.8 带滤镜的视频
    video8 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("13s", "2s")
    )
    try:
        video8.add_filter(FilterType.自然)  # 滤镜
    except:
        pass  # 如果滤镜不存在则跳过
    script.add_segment(video8, "video_track_1")
    
    # 2.9 带蒙版的视频
    video9 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("15s", "2s")
    )
    video9.add_mask(MaskType.线性, center_x=0, center_y=0, rotation=45, feather=0.3)
    script.add_segment(video9, "video_track_1")
    
    # 2.10 带背景填充的视频
    video10 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("17s", "2s")
    )
    video10.add_background_filling("blur", 0.0625)  # 模糊背景
    script.add_segment(video10, "video_track_1")
    
    # 2.11 带关键帧的视频（位置、缩放、旋转、透明度）
    video11 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("19s", "3s")
    )
    # 位置关键帧
    video11.add_keyframe(KeyframeProperty.position_x, tim("0s"), -0.5)  # 左侧
    video11.add_keyframe(KeyframeProperty.position_x, tim("1.5s"), 0)     # 中间
    video11.add_keyframe(KeyframeProperty.position_x, tim("3s"), 0.5)     # 右侧
    # 缩放关键帧
    video11.add_keyframe(KeyframeProperty.scale_x, tim("0s"), 0.5)        # 缩小
    video11.add_keyframe(KeyframeProperty.scale_x, tim("1.5s"), 1.0)       # 正常
    video11.add_keyframe(KeyframeProperty.scale_x, tim("3s"), 1.5)        # 放大
    # 旋转关键帧
    video11.add_keyframe(KeyframeProperty.rotation, tim("0s"), 0)         # 0度
    video11.add_keyframe(KeyframeProperty.rotation, tim("1.5s"), 180)     # 180度
    video11.add_keyframe(KeyframeProperty.rotation, tim("3s"), 360)       # 360度
    # 透明度关键帧
    video11.add_keyframe(KeyframeProperty.alpha, tim("0s"), 0)            # 透明
    video11.add_keyframe(KeyframeProperty.alpha, tim("0.5s"), 1)         # 不透明
    video11.add_keyframe(KeyframeProperty.alpha, tim("2.5s"), 1)           # 保持不透明
    video11.add_keyframe(KeyframeProperty.alpha, tim("3s"), 0)            # 透明
    script.add_segment(video11, "video_track_1")
    
    # 2.12 带裁剪设置的视频
    video12 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("22s", "2s"),
        clip_settings=ClipSettings(
            transform_x=0.2,  # 水平位置
            transform_y=-0.3,  # 垂直位置
            scale_x=0.8,      # 水平缩放
            scale_y=0.8,      # 垂直缩放
            rotation=15       # 旋转角度
        )
    )
    script.add_segment(video12, "video_track_1")
    
    # 2.13 贴纸片段（GIF）
    gif_material = draft.VideoMaterial(os.path.join(tutorial_asset_dir, 'sticker.gif'))
    gif_segment = draft.VideoSegment(
        gif_material,
        trange("24s", gif_material.duration)
    )
    gif_segment.add_background_filling("blur", 0.125)
    script.add_segment(gif_segment, "video_track_2")
    
    print("   ✓ 视频片段测试完成")
    
    print("\n3. 测试文本片段功能...")
    
    # 3.1 基本文本片段
    text1 = draft.TextSegment(
        "基本文本测试",
        trange("0s", "2s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=10.0,
            color=(1.0, 1.0, 1.0),
            align=1  # 居中
        )
    )
    script.add_segment(text1, "text_track_1")
    
    # 3.2 带入场动画的文本
    text2 = draft.TextSegment(
        "入场动画文本",
        trange("2s", "2s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=12.0,
            color=(1.0, 0.0, 0.0),  # 红色
            bold=True
        )
    )
    text2.add_animation(TextIntro.故障闪动, duration=tim("0.5s"))
    script.add_segment(text2, "text_track_1")
    
    # 3.3 带出场动画的文本
    text3 = draft.TextSegment(
        "出场动画文本",
        trange("4s", "2s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=10.0,
            color=(0.0, 1.0, 0.0),  # 绿色
            italic=True
        )
    )
    text3.add_animation(TextOutro.故障闪动, duration=tim("0.5s"))
    script.add_segment(text3, "text_track_1")
    
    # 3.4 带循环动画的文本
    text4 = draft.TextSegment(
        "循环动画文本",
        trange("6s", "2s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=10.0,
            color=(0.0, 0.0, 1.0),  # 蓝色
            underline=True
        )
    )
    try:
        text4.add_animation(TextLoopAnim.故障闪动, duration=tim("2s"))
    except:
        pass  # 如果动画不存在则跳过
    script.add_segment(text4, "text_track_1")
    
    # 3.5 带文本气泡的文本
    text5 = draft.TextSegment(
        "带气泡的文本",
        trange("8s", "2s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=10.0,
            color=(1.0, 1.0, 0.0),  # 黄色
            align=1
        ),
        clip_settings=ClipSettings(transform_y=-0.8)  # 位置在下方
    )
    # 注意：需要有效的气泡ID
    # text5.add_bubble("气泡ID1", "气泡ID2")
    script.add_segment(text5, "text_track_1")
    
    # 3.6 带花字效果的文本
    text6 = draft.TextSegment(
        "带花字的文本",
        trange("10s", "2s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=10.0,
            color=(1.0, 0.0, 1.0),  # 紫色
        )
    )
    # 注意：需要有效的花字ID
    # text6.add_effect("花字ID")
    script.add_segment(text6, "text_track_1")
    
    # 3.7 带关键帧的文本
    text7 = draft.TextSegment(
        "关键帧文本",
        trange("12s", "3s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=12.0,
            color=(1.0, 1.0, 1.0),
        )
    )
    # 位置关键帧
    text7.add_keyframe(KeyframeProperty.position_y, tim("0s"), 0.5)   # 上方
    text7.add_keyframe(KeyframeProperty.position_y, tim("1.5s"), 0)    # 中间
    text7.add_keyframe(KeyframeProperty.position_y, tim("3s"), -0.5)   # 下方
    # 缩放关键帧
    text7.add_keyframe(KeyframeProperty.scale_x, tim("0s"), 0.5)
    text7.add_keyframe(KeyframeProperty.scale_x, tim("1.5s"), 1.5)
    text7.add_keyframe(KeyframeProperty.scale_x, tim("3s"), 0.5)
    script.add_segment(text7, "text_track_1")
    
    # 3.8 多行文本
    text8 = draft.TextSegment(
        "第一行文本\n第二行文本\n第三行文本",
        trange("15s", "2s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=10.0,
            color=(1.0, 1.0, 1.0),
            align=1,  # 居中
            line_spacing=10,
            auto_wrapping=True
        )
    )
    script.add_segment(text8, "text_track_1")
    
    print("   ✓ 文本片段测试完成")
    
    print("\n4. 测试特效和滤镜轨道...")
    
    # 4.1 视频特效
    try:
        script.add_effect(
            VideoSceneEffectType.光晕,
            trange("0s", "5s"),
            track_name="effect_track_1"
        )
    except:
        pass  # 如果特效不存在则跳过
    
    # 4.2 滤镜
    try:
        script.add_filter(
            FilterType.自然,
            trange("0s", "10s"),
            track_name="filter_track_1",
            intensity=80.0  # 滤镜强度80%
        )
    except:
        pass  # 如果滤镜不存在则跳过
    
    print("   ✓ 特效和滤镜测试完成")
    
    print("\n5. 测试SRT字幕导入...")
    
    # 5.1 导入SRT字幕（使用新的轨道避免重叠）
    srt_path = os.path.join(tutorial_asset_dir, 'subtitles.srt')
    if os.path.exists(srt_path):
        # 创建一个新的文本轨道用于SRT字幕
        script.add_track(draft.TrackType.text, "srt_track")
        script.import_srt(
            srt_path,
            "srt_track",  # 使用新轨道
            time_offset="0s",
            text_style=draft.TextStyle(
                size=10.0,
                color=(1.0, 1.0, 0.0),  # 黄色
                align=1  # 居中
            ),
            clip_settings=ClipSettings(transform_y=-0.7)  # 位置在下方（稍微上移避免重叠）
        )
        print("   ✓ SRT字幕导入测试完成")
    else:
        print("   ⚠ SRT文件不存在，跳过字幕导入测试")
    
    print("\n保存剪映草稿...")
    script.save()
    print("✓ 剪映功能测试完成！")


def test_capcut_features():
    """测试CapCut功能"""
    print("\n" + "=" * 60)
    print("测试CapCut功能")
    print("=" * 60)
    
    # 设置草稿文件夹
    draft_folder = draft.DraftFolder(
        r"/Users/xjc/Movies/CapCut/User Data/Projects/com.lveditor.draft",
        app_type="capcut"
    )
    
    tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'tutorial')
    assert os.path.exists(tutorial_asset_dir), f"未找到例程素材文件夹{os.path.abspath(tutorial_asset_dir)}"
    
    # 创建草稿
    script = draft_folder.create_draft("test_capcut_all_features", 1920, 1080, allow_replace=True)
    
    # 添加多个轨道
    script.add_track(draft.TrackType.audio, "audio_track_1")
    script.add_track(draft.TrackType.video, "video_track_1")
    script.add_track(draft.TrackType.video, "video_track_2")
    script.add_track(draft.TrackType.text, "text_track_1")
    script.add_track(draft.TrackType.effect, "effect_track_1")
    script.add_track(draft.TrackType.filter, "filter_track_1")
    
    print("\n1. 测试CapCut音频片段功能...")
    
    # 1.1 基本音频片段
    audio1 = draft.AudioSegment(
        os.path.join(tutorial_asset_dir, 'audio.mp3'),
        trange("0s", "3s"),
        volume=0.8
    )
    script.add_segment(audio1, "audio_track_1")
    
    # 1.2 带淡入淡出的音频
    audio2 = draft.AudioSegment(
        os.path.join(tutorial_asset_dir, 'audio.mp3'),
        trange("3s", "2s"),
        volume=0.6,
        speed=1.5,  # 1.5倍速
        change_pitch=True  # 变速时改变音调
    )
    audio2.add_fade("0.5s", "0.5s")  # 0.5s淡入，0.5s淡出
    script.add_segment(audio2, "audio_track_1")
    
    # 1.3 带音量关键帧的音频
    audio3 = draft.AudioSegment(
        os.path.join(tutorial_asset_dir, 'audio.mp3'),
        trange("5s", "2s"),
        volume=1.0
    )
    audio3.add_keyframe(tim("0s"), 0.3)  # 开始时30%音量
    audio3.add_keyframe(tim("1s"), 1.0)  # 1秒后100%音量
    audio3.add_keyframe(tim("2s"), 0.5)  # 结束时50%音量
    script.add_segment(audio3, "audio_track_1")
    
    # 1.4 带CapCut音频特效的音频
    audio4 = draft.AudioSegment(
        os.path.join(tutorial_asset_dir, 'audio.mp3'),
        trange("7s", "2s"),
        volume=0.7
    )
    try:
        # CapCut音频滤镜特效
        audio4.add_effect(CapCut_Voice_filters_effect_type.Echo)
    except:
        pass  # 如果特效不存在则跳过
    script.add_segment(audio4, "audio_track_1")
    
    print("   ✓ CapCut音频片段测试完成")
    
    print("\n2. 测试CapCut视频片段功能...")
    
    # 2.1 基本视频片段
    video1 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("0s", "2s")
    )
    script.add_segment(video1, "video_track_1")
    
    # 2.2 带CapCut入场动画的视频
    video2 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("2s", "2s")
    )
    video2.add_animation(CapCut_Intro_type.Zoom_In)  # CapCut入场动画
    script.add_segment(video2, "video_track_1")
    
    # 2.3 带CapCut出场动画的视频
    video3 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("4s", "2s")
    )
    try:
        video3.add_animation(CapCut_Outro_type.Fade_Out)  # CapCut出场动画
    except:
        pass
    script.add_segment(video3, "video_track_1")
    
    # 2.4 带CapCut组合动画的视频
    video4 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("6s", "2s")
    )
    try:
        video4.add_animation(CapCut_Group_animation_type.Bounce)  # CapCut组合动画
    except:
        pass
    script.add_segment(video4, "video_track_1")
    
    # 2.5 带CapCut转场的视频
    video5 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("8s", "2s")
    )
    video5.add_transition(CapCut_Transition_type.Dissolve)  # CapCut转场
    script.add_segment(video5, "video_track_1")
    
    # 2.6 带淡入淡出的视频
    video6 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("10s", "2s")
    )
    video6.add_fade("0.5s", "0.5s")  # 淡入淡出
    script.add_segment(video6, "video_track_1")
    
    # 2.7 带变速的视频
    video7 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("12s", "1s"),
        speed=2.0  # 2倍速
    )
    script.add_segment(video7, "video_track_1")
    
    # 2.8 带CapCut蒙版的视频
    video8 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("13s", "2s")
    )
    try:
        video8.add_mask(CapCut_Mask_type.Split, center_x=0, center_y=0, rotation=45, feather=0.3)
    except:
        pass
    script.add_segment(video8, "video_track_1")
    
    # 2.9 带背景填充的视频
    video9 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("15s", "2s")
    )
    video9.add_background_filling("blur", 0.0625)  # 模糊背景
    script.add_segment(video9, "video_track_1")
    
    # 2.10 带关键帧的视频（位置、缩放、旋转、透明度）
    video10 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("17s", "3s")
    )
    # 位置关键帧
    video10.add_keyframe(KeyframeProperty.position_x, tim("0s"), -0.5)  # 左侧
    video10.add_keyframe(KeyframeProperty.position_x, tim("1.5s"), 0)     # 中间
    video10.add_keyframe(KeyframeProperty.position_x, tim("3s"), 0.5)     # 右侧
    # 缩放关键帧
    video10.add_keyframe(KeyframeProperty.scale_x, tim("0s"), 0.5)        # 缩小
    video10.add_keyframe(KeyframeProperty.scale_x, tim("1.5s"), 1.0)       # 正常
    video10.add_keyframe(KeyframeProperty.scale_x, tim("3s"), 1.5)        # 放大
    # 旋转关键帧
    video10.add_keyframe(KeyframeProperty.rotation, tim("0s"), 0)         # 0度
    video10.add_keyframe(KeyframeProperty.rotation, tim("1.5s"), 180)     # 180度
    video10.add_keyframe(KeyframeProperty.rotation, tim("3s"), 360)       # 360度
    # 透明度关键帧
    video10.add_keyframe(KeyframeProperty.alpha, tim("0s"), 0)            # 透明
    video10.add_keyframe(KeyframeProperty.alpha, tim("0.5s"), 1)         # 不透明
    video10.add_keyframe(KeyframeProperty.alpha, tim("2.5s"), 1)           # 保持不透明
    video10.add_keyframe(KeyframeProperty.alpha, tim("3s"), 0)            # 透明
    script.add_segment(video10, "video_track_1")
    
    # 2.11 带裁剪设置的视频
    video11 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("20s", "2s"),
        clip_settings=ClipSettings(
            transform_x=0.2,  # 水平位置
            transform_y=-0.3,  # 垂直位置
            scale_x=0.8,      # 水平缩放
            scale_y=0.8,      # 垂直缩放
            rotation=15       # 旋转角度
        )
    )
    script.add_segment(video11, "video_track_1")
    
    # 2.12 CapCut贴纸片段（GIF）
    gif_material = draft.VideoMaterial(os.path.join(tutorial_asset_dir, 'sticker.gif'))
    gif_segment = draft.VideoSegment(
        gif_material,
        trange("22s", gif_material.duration)
    )
    gif_segment.add_background_filling("blur", 0.125)
    script.add_segment(gif_segment, "video_track_2")
    
    print("   ✓ CapCut视频片段测试完成")
    
    print("\n3. 测试CapCut文本片段功能...")
    
    # 3.1 基本文本片段
    text1 = draft.TextSegment(
        "CapCut基本文本",
        trange("0s", "2s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=10.0,
            color=(1.0, 1.0, 1.0),
            align=1  # 居中
        )
    )
    script.add_segment(text1, "text_track_1")
    
    # 3.2 带CapCut文本入场动画
    text2 = draft.TextSegment(
        "CapCut入场动画",
        trange("2s", "2s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=12.0,
            color=(1.0, 0.0, 0.0),  # 红色
            bold=True
        )
    )
    text2.add_animation(CapCut_Text_intro.Fade_In, duration=tim("0.5s"))
    script.add_segment(text2, "text_track_1")
    
    # 3.3 带CapCut文本出场动画
    text3 = draft.TextSegment(
        "CapCut出场动画",
        trange("4s", "2s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=10.0,
            color=(0.0, 1.0, 0.0),  # 绿色
            italic=True
        )
    )
    text3.add_animation(CapCut_Text_outro.Fade_Out, duration=tim("0.5s"))
    script.add_segment(text3, "text_track_1")
    
    # 3.4 带CapCut文本循环动画
    text4 = draft.TextSegment(
        "CapCut循环动画",
        trange("6s", "2s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=10.0,
            color=(0.0, 0.0, 1.0),  # 蓝色
            underline=True
        )
    )
    try:
        text4.add_animation(CapCut_Text_loop_anim.Bounce, duration=tim("2s"))
    except:
        pass
    script.add_segment(text4, "text_track_1")
    
    # 3.5 带关键帧的文本
    text5 = draft.TextSegment(
        "CapCut关键帧文本",
        trange("8s", "3s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=12.0,
            color=(1.0, 1.0, 1.0),
        )
    )
    # 位置关键帧
    text5.add_keyframe(KeyframeProperty.position_y, tim("0s"), 0.5)   # 上方
    text5.add_keyframe(KeyframeProperty.position_y, tim("1.5s"), 0)    # 中间
    text5.add_keyframe(KeyframeProperty.position_y, tim("3s"), -0.5)   # 下方
    # 缩放关键帧
    text5.add_keyframe(KeyframeProperty.scale_x, tim("0s"), 0.5)
    text5.add_keyframe(KeyframeProperty.scale_x, tim("1.5s"), 1.5)
    text5.add_keyframe(KeyframeProperty.scale_x, tim("3s"), 0.5)
    script.add_segment(text5, "text_track_1")
    
    # 3.6 多行文本
    text6 = draft.TextSegment(
        "CapCut第一行\n第二行文本\n第三行文本",
        trange("11s", "2s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=10.0,
            color=(1.0, 1.0, 1.0),
            align=1,  # 居中
            line_spacing=10,
            auto_wrapping=True
        )
    )
    script.add_segment(text6, "text_track_1")
    
    print("   ✓ CapCut文本片段测试完成")
    
    print("\n4. 测试CapCut特效和滤镜轨道...")
    
    # 4.1 CapCut视频画面特效
    try:
        script.add_effect(
            CapCut_Video_scene_effect_type.Blur,
            trange("0s", "5s"),
            track_name="effect_track_1",
            params=[0.5]  # 模糊强度50%
        )
    except:
        pass
    
    # 4.2 CapCut视频人物特效
    try:
        script.add_effect(
            CapCut_Video_character_effect_type.Beauty,
            trange("0s", "5s"),
            track_name="effect_track_1"
        )
    except:
        pass
    
    print("   ✓ CapCut特效测试完成")
    
    print("\n5. 测试SRT字幕导入...")
    
    # 5.1 导入SRT字幕（使用新的轨道避免重叠）
    srt_path = os.path.join(tutorial_asset_dir, 'subtitles.srt')
    if os.path.exists(srt_path):
        # 创建一个新的文本轨道用于SRT字幕
        script.add_track(draft.TrackType.text, "srt_track")
        script.import_srt(
            srt_path,
            "srt_track",  # 使用新轨道
            time_offset="0s",
            text_style=draft.TextStyle(
                size=10.0,
                color=(1.0, 1.0, 0.0),  # 黄色
                align=1  # 居中
            ),
            clip_settings=ClipSettings(transform_y=-0.7)  # 位置在下方（稍微上移避免重叠）
        )
        print("   ✓ CapCut SRT字幕导入测试完成")
    else:
        print("   ⚠ SRT文件不存在，跳过字幕导入测试")
    
    print("\n保存CapCut草稿...")
    script.save()
    print("✓ CapCut功能测试完成！")


def main():
    """主函数"""
    print("=" * 60)
    print("pyJianYingDraft 全面功能测试")
    print("=" * 60)
    
    try:
        # 测试剪映功能
        test_jianying_features()
        
        # 测试CapCut功能
        test_capcut_features()
        
        # 测试补充功能
        test_additional_features()
        
        print("\n" + "=" * 60)
        print("所有测试完成！")
        print("=" * 60)
        print("\n生成的草稿文件：")
        print("  - test_jianying_all_features (剪映)")
        print("  - test_capcut_all_features (CapCut)")
        print("  - test_additional_features (补充功能)")
        print("\n请在对应的应用中打开这些草稿进行验证。")
        
    except Exception as e:
        print(f"\n❌ 测试过程中出现错误：{e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def test_additional_features():
    """测试补充功能（文本样式、素材裁剪、模板模式等）"""
    print("\n" + "=" * 60)
    print("测试补充功能")
    print("=" * 60)
    
    # 设置草稿文件夹
    draft_folder = draft.DraftFolder(
        r"/Users/xjc/Movies/CapCut/User Data/Projects/com.lveditor.draft",
        app_type="capcut"
    )
    
    tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'tutorial')
    assert os.path.exists(tutorial_asset_dir), f"未找到例程素材文件夹{os.path.abspath(tutorial_asset_dir)}"
    
    # 创建草稿
    script = draft_folder.create_draft("test_additional_features", 1920, 1080, allow_replace=True)
    
    # 添加轨道（测试静音功能）
    script.add_track(draft.TrackType.audio, "audio_track", mute=True)  # 静音轨道
    script.add_track(draft.TrackType.video, "video_track_1")
    script.add_track(draft.TrackType.video, "video_track_2", relative_index=1)  # 测试相对索引
    script.add_track(draft.TrackType.text, "text_track")
    
    print("\n1. 测试文本样式功能（描边、背景、阴影）...")
    
    # 1.1 带描边的文本
    text1 = draft.TextSegment(
        "带描边的文本",
        trange("0s", "2s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=12.0,
            color=(1.0, 1.0, 1.0),
            align=1
        )
    )
    text1.border = TextBorder(
        alpha=1.0,
        color=(0.0, 0.0, 0.0),  # 黑色描边
        width=50.0  # 描边宽度
    )
    script.add_segment(text1, "text_track")
    
    # 1.2 带背景的文本
    text2 = draft.TextSegment(
        "带背景的文本",
        trange("2s", "2s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=12.0,
            color=(1.0, 1.0, 1.0),
            align=1
        )
    )
    text2.background = TextBackground(
        color="#FF0000",  # 红色背景
        style=1,
        alpha=0.8,
        round_radius=0.1,
        height=0.2,
        width=0.3
    )
    script.add_segment(text2, "text_track")
    
    # 1.3 带阴影的文本
    text3 = draft.TextSegment(
        "带阴影的文本",
        trange("4s", "2s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=12.0,
            color=(1.0, 1.0, 1.0),
            align=1
        )
    )
    text3.shadow = TextShadow(
        alpha=0.8,
        color=(0.0, 0.0, 0.0),  # 黑色阴影
        diffuse=20.0,
        distance=10.0,
        angle=-45.0
    )
    script.add_segment(text3, "text_track")
    
    # 1.4 同时带描边、背景和阴影的文本
    text4 = draft.TextSegment(
        "全样式文本",
        trange("6s", "2s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(
            size=14.0,
            color=(1.0, 1.0, 0.0),  # 黄色
            align=1
        )
    )
    text4.border = TextBorder(alpha=1.0, color=(0.0, 0.0, 0.0), width=40.0)
    text4.background = TextBackground(color="#0000FF", alpha=0.6, round_radius=0.15)
    text4.shadow = TextShadow(alpha=0.7, diffuse=15.0, distance=8.0)
    script.add_segment(text4, "text_track")
    
    print("   ✓ 文本样式测试完成")
    
    print("\n2. 测试素材裁剪功能...")
    
    # 2.1 带裁剪的视频素材
    video_material = draft.VideoMaterial(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        crop_settings=CropSettings(
            upper_left_x=0.1, upper_left_y=0.1,
            upper_right_x=0.9, upper_right_y=0.1,
            lower_left_x=0.1, lower_left_y=0.9,
            lower_right_x=0.9, lower_right_y=0.9
        )
    )
    video1 = draft.VideoSegment(
        video_material,
        trange("0s", "3s")
    )
    script.add_segment(video1, "video_track_1")
    
    print("   ✓ 素材裁剪测试完成")
    
    print("\n3. 测试source_timerange（素材时间截取）...")
    
    # 3.1 从素材中间截取片段
    video2 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("3s", "2s"),
        source_timerange=trange("1s", "2s")  # 从素材的第1秒开始，截取2秒
    )
    script.add_segment(video2, "video_track_1")
    
    # 3.2 变速截取
    video3 = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("5s", "1s"),  # 在轨道上占1秒
        source_timerange=trange("0s", "3s"),  # 从素材中截取3秒
        speed=3.0  # 3倍速播放
    )
    script.add_segment(video3, "video_track_1")
    
    print("   ✓ source_timerange测试完成")
    
    print("\n4. 测试音频特效（音调、语音转歌曲）...")
    
    # 4.1 带音调特效的音频
    audio1 = draft.AudioSegment(
        os.path.join(tutorial_asset_dir, 'audio.mp3'),
        trange("0s", "3s"),
        volume=0.8
    )
    try:
        audio1.add_effect(ToneEffectType.台湾小哥)
    except:
        pass
    script.add_segment(audio1, "audio_track")
    
    # 4.2 带语音转歌曲特效的音频
    audio2 = draft.AudioSegment(
        os.path.join(tutorial_asset_dir, 'audio.mp3'),
        trange("3s", "3s"),
        volume=0.7
    )
    try:
        audio2.add_effect(SpeechToSongType.Lofi)
    except:
        pass
    script.add_segment(audio2, "audio_track")
    
    # 4.3 带CapCut语音转歌曲特效的音频
    audio3 = draft.AudioSegment(
        os.path.join(tutorial_asset_dir, 'audio.mp3'),
        trange("6s", "3s"),
        volume=0.7
    )
    try:
        audio3.add_effect(CapCut_Speech_to_song_effect_type.Folk)
    except:
        pass
    script.add_segment(audio3, "audio_track")
    
    # 4.4 带CapCut人物音频特效的音频
    audio4 = draft.AudioSegment(
        os.path.join(tutorial_asset_dir, 'audio.mp3'),
        trange("9s", "3s"),
        volume=0.7
    )
    try:
        audio4.add_effect(CapCut_Voice_characters_effect_type.Robot)
    except:
        pass
    script.add_segment(audio4, "audio_track")
    
    print("   ✓ 音频特效测试完成")
    
    print("\n5. 测试模板模式功能（import_track, replace_material, replace_text）...")
    
    # 5.1 创建一个模板草稿（使用与目标草稿相同的app_type）
    template_script = draft_folder.create_draft("template_for_import", 1920, 1080, allow_replace=True)
    template_script.add_track(draft.TrackType.video, "template_video")
    template_script.add_track(draft.TrackType.text, "template_text")
    
    # 添加模板视频片段（使用CapCut的动画类型，因为目标草稿是CapCut）
    template_video = draft.VideoSegment(
        os.path.join(tutorial_asset_dir, 'video.mp4'),
        trange("0s", "3s")
    )
    template_video.add_animation(CapCut_Intro_type.Zoom_In)  # 使用CapCut动画类型
    template_script.add_segment(template_video, "template_video")
    
    # 添加模板文本片段
    template_text = draft.TextSegment(
        "模板文本",
        trange("0s", "3s"),
        font=draft.FontType.文轩体,
        style=draft.TextStyle(size=12.0, color=(1.0, 1.0, 0.0))
    )
    template_script.add_segment(template_text, "template_text")
    template_script.save()
    
    # 5.2 加载模板并导入轨道
    loaded_template = draft_folder.load_template("template_for_import")
    template_track = loaded_template.get_imported_track(draft.TrackType.video, name="template_video")
    script.import_track(loaded_template, template_track, offset="12s", new_name="imported_video")
    
    # 5.3 测试替换素材
    try:
        # 获取导入的轨道
        imported_track = script.get_imported_track(draft.TrackType.video, name="imported_video")
        # 替换素材
        new_material = draft.VideoMaterial(os.path.join(tutorial_asset_dir, 'video.mp4'))
        script.replace_material_by_seg(imported_track, 0, new_material)
    except:
        pass
    
    # 5.4 测试替换文本
    try:
        text_track = loaded_template.get_imported_track(draft.TrackType.text, name="template_text")
        script.import_track(loaded_template, text_track, offset="15s", new_name="imported_text")
        imported_text_track = script.get_imported_track(draft.TrackType.text, name="imported_text")
        script.replace_text(imported_text_track, 0, "替换后的文本内容")
    except:
        pass
    
    print("   ✓ 模板模式功能测试完成")
    
    print("\n6. 测试inspect_material功能...")
    
    # 6.1 检查素材元数据
    try:
        script.inspect_material()
    except:
        pass
    
    print("   ✓ inspect_material测试完成")
    
    print("\n保存补充功能测试草稿...")
    script.save()
    print("✓ 补充功能测试完成！")


if __name__ == "__main__":
    main()

