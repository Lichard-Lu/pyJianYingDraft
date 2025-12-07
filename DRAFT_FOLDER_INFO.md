# 剪映草稿文件夹设置指南

## 🎯 你的草稿文件夹应该填什么

根据系统扫描，你的剪映草稿文件夹路径是：

```
/Users/xjc/Movies/JianyingPro/User Data/Projects/com.lveditor.draft
```

## 📝 在 demo.py 中的修改

将 demo.py 第 7 行：

```python
draft_folder = draft.DraftFolder(r"<你的草稿文件夹>")
```

修改为：

```python
draft_folder = draft.DraftFolder(r"/Users/xjc/Movies/JianyingPro/User Data/Projects/com.lveditor.draft")
```

## 🚀 快速测试

我已经为你创建了两个测试文件：

### 1. `demo_configured.py`
- 使用自动检测到的路径
- 创建一个简单的文本草稿（不需要额外素材）
- 可以直接运行测试

### 2. `find_draft_folder.py`
- 草稿文件夹查找工具
- 如果路径有问题可以重新运行

## 🏃‍♂️ 运行测试

```bash
# 激活虚拟环境
source venv/bin/activate

# 运行配置好的测试
python demo_configured.py

# 或者重新查找草稿文件夹
python find_draft_folder.py
```

## 🔧 其他可能的路径

如果上述路径不工作，可能的原因：

1. **剪映版本不同**：不同版本的剪映可能使用不同的文件夹结构
2. **自定义设置**：你可能设置了自定义的草稿位置
3. **系统差异**：macOS 不同版本可能路径有差异

### 检查剪映设置

1. 打开剪映
2. 进入「全局设置」
3. 查看「草稿位置」设置
4. 使用显示的路径

### 常见路径模式

- `~/Movies/JianyingPro/User Data/Projects/com.lveditor.draft`
- `~/Documents/JianyingPro Drafts`
- `~/Desktop/JianyingPro Drafts`

## 💡 使用技巧

- 使用原始字符串（r"..."）避免路径转义问题
- 确保路径存在且可访问
- 运行前先在剪映中创建一个测试草稿确认路径正确

## 🆘 如果还有问题

1. 在剪映中创建一个新的测试草稿
2. 记下草稿保存的位置
3. 或者联系项目维护者获取帮助