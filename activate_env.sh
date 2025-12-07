#!/bin/bash
# pyJianYingDraft 虚拟环境激活脚本

echo "正在激活 pyJianYingDraft 虚拟环境..."
source venv/bin/activate

echo "✅ 虚拟环境已激活"
echo "📌 Python 版本: $(python --version)"
echo "📌 pyJianYingDraft 已安装并可导入"
echo ""
echo "💡 使用说明："
echo "   - 运行 'python demo.py' 来测试示例代码"
echo "   - 运行 'deactivate' 退出虚拟环境"
echo ""