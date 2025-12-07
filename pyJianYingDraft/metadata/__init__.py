"""记录各种特效/音效/滤镜等的元数据

音频相关元数据更新时间：2024
其余元数据更新时间：2025-08
CapCut 元数据来源：CapCutAPI-main 项目
"""

from .effect_meta import EffectMeta, EffectParamInstance
from .effect_meta import AnimationMeta

# 视频特效（剪映）
from .video_scene_effect import VideoSceneEffectType
from .video_character_effect import VideoCharacterEffectType

# 视频动画（剪映）
from .video_intro import IntroType
from .video_outro import OutroType
from .video_group_animation import GroupAnimationType

# 音频特效（剪映）
from .audio_scene_effect import AudioSceneEffectType
from .tone_effect import ToneEffectType
from .speech_to_song import SpeechToSongType

# 文本动画（剪映）
from .text_intro import TextIntro
from .text_outro import TextOutro
from .text_loop import TextLoopAnim

# 其它（剪映）
from .font_meta import FontType
from .mask_meta import MaskType, MaskMeta
from .filter_meta import FilterType
from .transition_meta import TransitionType

# CapCut 专用元数据
from .capcut_animation_meta import CapCut_Intro_type, CapCut_Outro_type, CapCut_Group_animation_type
from .capcut_transition_meta import CapCut_Transition_type
from .capcut_effect_meta import CapCut_Video_scene_effect_type, CapCut_Video_character_effect_type
from .capcut_text_animation_meta import CapCut_Text_intro, CapCut_Text_outro, CapCut_Text_loop_anim
from .capcut_mask_meta import CapCut_Mask_type
from .capcut_audio_effect_meta import CapCut_Voice_filters_effect_type, CapCut_Voice_characters_effect_type, CapCut_Speech_to_song_effect_type

__all__ = [
    # 基础类
    "AnimationMeta",
    "EffectMeta",
    "EffectParamInstance",
    
    # 剪映元数据
    "MaskType",
    "MaskMeta",
    "FilterType",
    "FontType",
    "TransitionType",
    "IntroType",
    "OutroType",
    "GroupAnimationType",
    "TextIntro",
    "TextOutro",
    "TextLoopAnim",
    "AudioSceneEffectType",
    "ToneEffectType",
    "SpeechToSongType",
    "VideoSceneEffectType",
    "VideoCharacterEffectType",
    
    # CapCut 专用元数据
    "CapCut_Intro_type",
    "CapCut_Outro_type",
    "CapCut_Group_animation_type",
    "CapCut_Transition_type",
    "CapCut_Video_scene_effect_type",
    "CapCut_Video_character_effect_type",
    "CapCut_Text_intro",
    "CapCut_Text_outro",
    "CapCut_Text_loop_anim",
    "CapCut_Mask_type",
    "CapCut_Voice_filters_effect_type",
    "CapCut_Voice_characters_effect_type",
    "CapCut_Speech_to_song_effect_type",
]
