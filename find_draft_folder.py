#!/usr/bin/env python3
"""
剪映草稿文件夹查找工具
帮助确定 pyJianYingDraft 中需要设置的草稿文件夹路径
"""

import os
import json
from pathlib import Path

def find_jianying_folders():
    """查找剪映相关的文件夹"""
    possible_paths = [
        "~/Movies/JianyingPro",
        "~/Documents/JianyingPro",
        "~/Desktop/JianyingPro",
        os.path.expanduser("~/Movies/JianyingPro"),
        os.path.expanduser("~/Documents/JianyingPro"),
        os.path.expanduser("~/Desktop/JianyingPro"),
    ]

    found_paths = []
    for path in possible_paths:
        expanded_path = os.path.expanduser(path)
        if os.path.exists(expanded_path):
            found_paths.append(expanded_path)

    return found_paths

def find_draft_content_folders(base_path):
    """在给定路径中查找包含 draft_content.json 的文件夹"""
    draft_folders = []

    # 查找可能的草稿文件夹结构
    patterns = [
        "User Data/Projects/com.lveditor.draft",
        "User Data/Draft",
        "Draft",
    ]

    for pattern in patterns:
        search_path = os.path.join(base_path, pattern)
        if os.path.exists(search_path):
            draft_folders.append(search_path)

            # 检查子文件夹中是否有 JianyingPro Drafts
            for item in os.listdir(search_path):
                item_path = os.path.join(search_path, item)
                if os.path.isdir(item_path):
                    jianying_drafts = os.path.join(item_path, "JianyingPro Drafts")
                    if os.path.exists(jianying_drafts):
                        draft_folders.append(jianying_drafts)

    return draft_folders

def main():
    print("🔍 正在查找剪映草稿文件夹...")
    print("=" * 50)

    # 查找剪映根目录
    jianying_paths = find_jianying_folders()

    if not jianying_paths:
        print("❌ 未找到剪映文件夹")
        print("\n💡 建议:")
        print("1. 确认剪映已安装")
        print("2. 打开剪映软件，在全局设置中查看草稿位置")
        print("3. 或手动指定路径")
        return

    print(f"✅ 找到剪映文件夹: {len(jianying_paths)} 个")
    for i, path in enumerate(jianying_paths, 1):
        print(f"  {i}. {path}")

    print("\n🔍 正在查找草稿文件夹...")

    all_draft_folders = []
    for jianying_path in jianying_paths:
        draft_folders = find_draft_content_folders(jianying_path)
        all_draft_folders.extend(draft_folders)

    if all_draft_folders:
        print(f"✅ 找到可能的草稿文件夹: {len(all_draft_folders)} 个")
        print("\n📁 推荐的草稿文件夹路径（用于 demo.py）:")

        for i, folder in enumerate(all_draft_folders, 1):
            print(f"\n选项 {i}:")
            print(f"  路径: {folder}")

            # 检查是否为空
            try:
                items = os.listdir(folder)
                if items:
                    print(f"  内容: {len(items)} 个文件/文件夹")
                    # 查找 draft_content.json
                    draft_files = [f for f in items if f == "draft_content.json"]
                    if draft_files:
                        print("  ✅ 包含 draft_content.json")
                    else:
                        print("  ⚠️  不包含 draft_content.json（可能是空的草稿文件夹）")
                else:
                    print("  内容: 空文件夹")
            except PermissionError:
                print("  ⚠️  无法访问（权限问题）")

        # 推荐最可能正确的路径
        if all_draft_folders:
            print(f"\n💡 推荐使用:")
            print(f"   draft_folder = draft.DraftFolder(r\"{all_draft_folders[0]}\")")
            print("\n或使用绝对路径:")
            print(f"   draft_folder = draft.DraftFolder(r\"{os.path.abspath(all_draft_folders[0])}\")")
    else:
        print("❌ 未找到具体的草稿文件夹")
        print("\n💡 可能的原因:")
        print("1. 剪映版本不同，文件夹结构有差异")
        print("2. 还没有创建任何草稿")
        print("3. 草稿保存在其他位置")

    print("\n🔧 使用说明:")
    print("1. 将上述推荐路径复制到 demo.py 的第7行")
    print("2. 替换 '<你的草稿文件夹>' 为找到的实际路径")
    print("3. 运行 demo.py 测试")

if __name__ == "__main__":
    main()