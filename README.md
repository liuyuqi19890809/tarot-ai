# 🎴 玄数塔罗 - 在线占卜系统

基于 Coze Bot 的无服务器塔罗牌占卜系统，前端托管在 GitHub Pages，后端完全由 Coze 工作流驱动。

## ✨ 特性

- 🎭 **首席塔罗大师人设** - 专业的塔罗解读提示词
- 🎴 **完整78张韦特塔罗牌库** - 大阿卡纳 + 小阿卡纳
- 🔮 **13种专业牌阵** - 圣三角、四元素、爱情十字、凯尔特十字等
- ✨ **神秘视觉效果** - 星空背景、粒子特效、抽牌动画
- 🧠 **AI 深度解读** - 元素分析 + 散文式解读
- 🚀 **无服务器架构** - 无需后端服务器，完全基于 Coze 平台

## 🏗️ 架构

```
┌─────────────────────────────────────────────────────┐
│                   前端 (GitHub Pages)                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │   HTML   │  │   CSS    │  │    JS    │      │
│  └──────────┘  └──────────┘  └──────────┘      │
│                    │                            │
└────────────────────┼────────────────────────────┘
                     │ HTTP POST
                     ▼
┌─────────────────────────────────────────────────────┐
│              Coze Bot 平台                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │ Webhook  │→│ 代码节点  │→│ 大模型节点 │      │
│  │ 触发器   │  │ (抽牌)    │  │ (解读)   │      │
│  └──────────┘  └──────────┘  └──────────┘      │
└─────────────────────────────────────────────────────┘
```

## 📦 项目结构

```
tarot-ai/
├── index.html              # 主页面
├── css/
│   └── style.css          # 样式文件
├── js/
│   ├── config.js          # Coze 配置（需自行填写）
│   └── app.js             # 前端逻辑
├── COZE_BOT_CONFIG.md     # Coze Bot 详细配置指南
├── DEPLOYMENT_GUIDE.md  # 部署指南
└── README.md              # 本文件
```

## 🚀 快速开始

### 1. 配置 Coze Bot

详细步骤请参考 [COZE_BOT_CONFIG.md](./COZE_BOT_CONFIG.md)

**概览：**
1. 在 Coze 平台创建 Bot
2. 配置系统提示词
3. 创建工作流，添加代码节点和大模型节点
4. 配置 Webhook 触发器
5. 获取 Webhook URL 和 Bearer Token

### 2. 配置前端

编辑 `js/config.js`：

```javascript
const COZE_CONFIG = {
    WEBHOOK_URL: "你的 Coze Webhook URL",
    BEARER_TOKEN: "你的 Bearer Token"
};
```

### 3. 本地测试

```bash
# 启动本地服务器
python3 -m http.server 8080

# 访问 http://localhost:8080
```

### 4. 部署到 GitHub Pages

详细步骤请参考 [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)

## 🎴 支持的牌阵

| 牌阵名称 | 牌数 | 适用场景 |
|---------|------|---------|
| 圣三角 | 3张 | 通用问题，过去现在未来 |
| 四元素 | 4张 | 全面现状分析 |
| 爱情十字 | 5张 | 感情问题 |
| 凯尔特十字 | 10张 | 复杂问题深度分析 |
| 是/否单张 | 1张 | 快速回答 |
| 时间流 | 4张 | 发展趋势分析 |
| 事业发展 | 5张 | 职业问题 |
| 每周运势 | 7张 | 周运预测 |
| 二选一决策 | 5张 | 两难选择 |
| 关系深度分析 | 6张 | 人际关系 |
| 人生发展 | 7张 | 各领域运势 |
| 心灵指引 | 4张 | 内心探索 |

## 🔧 技术栈

**前端：**
- 原生 JavaScript (ES6+)
- CSS3 动画
- 响应式设计

**后端：**
- Coze Bot 平台
- Python 代码节点
- 大语言模型（LLM）

**部署：**
- GitHub Pages
- 无服务器架构

## 📝 配置文件说明

### js/config.js - Coze 配置

```javascript
const COZE_CONFIG = {
    // 必填：从 Coze 触发器配置中获取
    WEBHOOK_URL: "YOUR_COZE_WEBHOOK_URL_HERE",
    BEARER_TOKEN: "YOUR_BEARER_TOKEN_HERE",
    
    // 可选：用于 API 直连方式
    BOT_ID: "YOUR_BOT_ID_HERE",
    PAT_TOKEN: "YOUR_PAT_TOKEN_HERE"
};
```

⚠️ **安全提醒**：不要将包含真实 Token 的文件提交到公开仓库！

## 🎯 API 请求/响应格式

### 请求格式 (前端 → Coze Webhook)

```json
{
  "spread_type": "three_card",
  "card_count": 3,
  "question": "我的感情运势如何？",
  "timestamp": 1742820175000
}
```

### 响应格式 (Coze → 前端)

```json
{
  "success": true,
  "cards": [
    {
      "name": "I. 魔术师 (The Magician)",
      "position": "正位",
      "position_name": "过去",
      "meaning": "象征创造力与潜能的觉醒，新的开始...",
      "is_reversed": false
    }
  ],
  "element_analysis": {
    "fire": "权杖2张，行动热情充沛",
    "water": "圣杯1张，情感能量流动",
    "earth": "星币0张，物质基础待加强",
    "air": "宝剑0张，思维活跃度一般"
  },
  "reading": "完整的散文式深度解读...",
  "timestamp": 1742820175000
}
```

## 🔒 安全最佳实践

1. **Token 管理**
   - 不要硬编码 Token
   - 使用 GitHub Secrets 注入配置
   - 定期轮换 Token

2. **请求安全**
   - 始终使用 HTTPS
   - 验证请求来源
   - 添加速率限制

3. **内容安全**
   - 启用 CSP
   - 验证用户输入
   - XSS 防护

## 🐛 故障排查

### 问题：抽牌后无响应
- 检查网络连接
- 验证 Webhook URL 和 Token 是否正确
- 查看浏览器控制台错误
- 检查 Coze 工作流执行日志

### 问题：结果显示异常
- 验证大模型输出是否为有效 JSON
- 检查前端 JSON 解析逻辑
- 确认响应格式是否符合预期

### 问题：CORS 跨域错误
- 使用反向代理方案
- 检查 Coze 触发器配置

## 📄 相关文档

- [COZE_BOT_CONFIG.md](./COZE_BOT_CONFIG.md) - Coze Bot 详细配置指南
- [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) - 完整部署指南

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📜 许可证

MIT License

## ⚠️ 免责声明

本系统仅供娱乐和参考，不构成任何决策建议。
命运掌握在自己手中，请相信自己的判断和选择。

---

**✨ 愿塔罗之光指引你的道路 ✨
