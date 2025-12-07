# 导入模块
import os
import pyJianYingDraft as draft
from pyJianYingDraft import IntroType, TransitionType, trange, tim

# 设置草稿文件夹 - 使用自动找到的路径
DRAFT_FOLDER_PATH = r"/Users/xjc/Movies/JianyingPro/User Data/Projects/com.lveditor.draft"
draft_folder = draft.DraftFolder(DRAFT_FOLDER_PATH)

print(f"✅ 草稿文件夹路径: {DRAFT_FOLDER_PATH}")

# 检查素材文件夹是否存在
tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'tutorial')
if not os.path.exists(tutorial_asset_dir):
    print(f"⚠️  未找到例程素材文件夹: {tutorial_asset_dir}")
    print("💡 这是正常的，demo.py 需要额外的素材文件才能完整运行")
    print("📁 你可以从项目仓库下载完整的 readme_assets 文件夹")
else:
    print(f"✅ 找到素材文件夹: {tutorial_asset_dir}")

# 创建剪映草稿
script = draft_folder.create_draft("demo_test", 1920, 1080, allow_replace=True)  # 1920x1080分辨率
print("✅ 成功创建草稿: demo_test")

# 添加音频、视频和文本轨道
script.add_track(draft.TrackType.audio).add_track(draft.TrackType.video).add_track(draft.TrackType.text)
print("✅ 成功添加轨道: 音频、视频、文本")

# 创建一个简单的文本片段作为测试（不需要素材文件）
text_segment = draft.TextSegment(
    "pyJianYingDraft 测试成功！",
    trange("0s", "5s"),  # 5秒时长
    style=draft.TextStyle(size=8.0, color=(1.0, 1.0, 1.0))  # 白色文字
)
script.add_segment(text_segment)
print("✅ 成功添加文本片段")

# 保存草稿
script.save()
print("✅ 草稿已保存！")

print(f"\n🎉 测试完成！")
print(f"📂 请在剪映中查找名为 'demo_test' 的草稿")
print(f"📍 草稿位置: {DRAFT_FOLDER_PATH}")
print(f"\n💡 如果看不到新草稿，请:")
print(f"   1. 在剪映中刷新草稿列表")
print(f"   2. 或重启剪映软件")