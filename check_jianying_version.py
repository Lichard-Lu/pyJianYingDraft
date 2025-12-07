#!/usr/bin/env python3
"""
检查剪映版本和兼容性
"""

import os
import json
import subprocess
from pathlib import Path

def get_jianying_version():
    """尝试获取剪映版本信息"""

    # 检查剪映应用
    possible_paths = [
        "/Applications/JianyingPro.app",
        "/Applications/CapCut.app",
        "~/Applications/JianyingPro.app",
        "~/Applications/CapCut.app",
    ]

    jianying_paths = []
    for path in possible_paths:
        expanded_path = os.path.expanduser(path)
        if os.path.exists(expanded_path):
            jianying_paths.append(expanded_path)

    print("🔍 检查剪映安装情况...")
    if jianying_paths:
        print(f"✅ 找到剪映应用: {len(jianying_paths)} 个")
        for i, path in enumerate(jianying_paths, 1):
            print(f"  {i}. {path}")

            # 尝试获取版本信息
            try:
                result = subprocess.run([
                    "mdls", "-name", "kMDItemVersion", path
                ], capture_output=True, text=True)

                if result.returncode == 0 and result.stdout.strip():
                    version = result.stdout.split("=")[1].strip()
                    print(f"     版本: {version}")
                else:
                    print("     版本: 未知")
            except Exception as e:
                print(f"     无法获取版本信息: {e}")
    else:
        print("❌ 未找到剪映应用")

    return jianying_paths

def check_existing_drafts():
    """检查现有草稿的版本信息"""

    print("\n🔍 检查现有草稿...")

    draft_base = os.path.expanduser("~/Movies/JianyingPro/User Data/Projects/com.lveditor.draft")
    if not os.path.exists(draft_base):
        print("❌ 草稿文件夹不存在")
        return

    # 获取所有草稿文件夹
    draft_folders = []
    for item in os.listdir(draft_base):
        item_path = os.path.join(draft_base, item)
        if os.path.isdir(item_path) and not item.startswith('.'):
            draft_folders.append(item_path)

    if not draft_folders:
        print("❌ 未找到草稿文件夹")
        return

    print(f"✅ 找到草稿文件夹: {len(draft_folders)} 个")

    # 检查最新的几个草稿
    draft_folders.sort(key=lambda x: os.path.getmtime(x), reverse=True)

    for i, folder in enumerate(draft_folders[:3], 1):
        print(f"\n📁 草稿 {i}: {os.path.basename(folder)}")

        # 检查关键文件
        files_to_check = ["draft_info.json", "draft_content.json"]

        for filename in files_to_check:
            file_path = os.path.join(folder, filename)
            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                print(f"  ✅ {filename}: {file_size} bytes")

                # 尝试读取前几个字节检查是否加密
                try:
                    with open(file_path, 'rb') as f:
                        first_bytes = f.read(100)

                    # 检查是否是 JSON 格式
                    try:
                        decoded = first_bytes.decode('utf-8')
                        if decoded.strip().startswith('{'):
                            print(f"     格式: JSON (可能未加密)")
                        else:
                            print(f"     格式: 二进制或加密数据")
                    except UnicodeDecodeError:
                        print(f"     格式: 二进制数据 (已加密)")

                except Exception as e:
                    print(f"     无法读取文件: {e}")
            else:
                print(f"  ❌ {filename}: 不存在")

def check_pyjianyingdraft_compatibility():
    """检查 pyJianYingDraft 兼容性"""

    print("\n🔍 pyJianYingDraft 兼容性分析...")

    # 检查项目文档中的兼容性说明
    readme_path = "README.md"
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 查找版本相关信息
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if '剪映6+版本' in line or '5.9' in line:
                print(f"📖 兼容性说明 (第{i+1}行):")
                print(f"   {line.strip()}")
                if i+1 < len(lines):
                    print(f"   {lines[i+1].strip()}")

def main():
    print("=" * 60)
    print("🎬 剪映版本与 pyJianYingDraft 兼容性检查")
    print("=" * 60)

    # 检查剪映版本
    jianying_paths = get_jianying_version()

    # 检查现有草稿
    check_existing_drafts()

    # 检查兼容性说明
    check_pyjianyingdraft_compatibility()

    print("\n" + "=" * 60)
    print("📋 总结:")
    print("=" * 60)

    if not jianying_paths:
        print("❌ 未安装剪映，请先安装剪映")
    else:
        print("✅ 已安装剪映")
        print("⚠️  注意：如果剪映版本 >= 6.0，草稿文件会被加密")
        print("   pyJianYingDraft 目前仅支持剪映 5.9 及以下版本")

    print("\n💡 解决方案:")
    print("1. 检查剪映版本，如果是 6.0+ 需要降级到 5.9")
    print("2. 或者等待项目更新支持 6.0+ 版本的解密")
    print("3. 也可以尝试在虚拟机中安装剪映 5.9 版本")

    print("\n🔧 测试建议:")
    print("1. 先运行 demo_configured.py 创建简单草稿测试")
    print("2. 如果剪映无法打开，说明版本不兼容")
    print("3. 可以尝试手动创建新草稿，查看文件是否被加密")

if __name__ == "__main__":
    main()