#!/bin/bash
# 🎴 塔罗牌占卜系统启动脚本

echo "🎴 塔罗牌占卜系统启动中..."
echo ""

# 检查Python环境
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误：未找到 Python3，请先安装 Python"
    exit 1
fi

# 安装依赖（如果需要）
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv venv
fi

echo "🔧 激活虚拟环境并安装依赖..."
source venv/bin/activate
pip install -q -r requirements.txt

echo ""
echo "🚀 启动服务..."
echo "📱 访问地址：http://localhost:9999"
echo "="*60
echo ""

python -m app.main
