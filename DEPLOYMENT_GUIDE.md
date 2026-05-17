# 塔罗牌系统 - 部署指南

## 📋 架构概述

| 组件 | 技术栈 | 托管方式 |
|------|--------|----------|
| 前端 | HTML + CSS + JavaScript | GitHub Pages |
| 后端 | Coze Bot 工作流 | Coze 平台（无服务器） |
| 抽牌逻辑 | Python 代码节点 | Coze 运行时 |
| 解读逻辑 | 大语言模型 | Coze 模型服务 |

---

## 🚀 前端部署步骤

### 1. 准备代码仓库

```bash
# 进入项目目录
cd tarot-ai

# 初始化 git 仓库（如果还没有）
git init
git add .
git commit -m "Initial commit: Tarot system with Coze backend"
```

### 2. 配置前端参数

编辑 `js/config.js`，填入你的 Coze Bot 配置：

```javascript
const COZE_CONFIG = {
    WEBHOOK_URL: "https://api.coze.cn/v1/workflow/trigger/你的触发器ID",
    BEARER_TOKEN: "你的BearerToken",
    BOT_ID: "你的BotID（可选）",
    PAT_TOKEN: "你的PATToken（可选）"
};
```

⚠️ **重要安全提醒**：
- 不要将包含真实 Token 的 `config.js` 提交到公开仓库
- 建议使用环境变量或构建时注入
- 公开仓库中请保留占位符

### 3. 推送到 GitHub

```bash
# 添加远程仓库
git remote add origin https://github.com/你的用户名/你的仓库名.git

# 推送到主分支
git push -u origin main
```

### 4. 启用 GitHub Pages

1. 进入 GitHub 仓库的 **Settings**
2. 找到 **Pages** 选项（在 Code and automation 分类下）
3. 在 **Build and deployment** 中：
   - Source: **Deploy from a branch**
   - Branch: **main** / **root**
4. 点击 **Save**
5. 等待几分钟，GitHub 会自动部署

### 5. 验证部署

访问：`https://你的用户名.github.io/你的仓库名/`

---

## 🤖 Coze Bot 配置步骤

详细配置请参考 [COZE_BOT_CONFIG.md](./COZE_BOT_CONFIG.md)

### 快速配置清单

- ✅ 创建 Bot：玄数塔罗
- ✅ 配置系统提示词（Persona）
- ✅ 创建工作流
- ✅ 添加代码节点（抽牌逻辑）
- ✅ 添加大模型节点（解读逻辑）
- ✅ 配置 Webhook 触发器
- ✅ 复制 Webhook URL 和 Bearer Token

---

## 🔧 高级配置

### 1. Token 安全方案

#### 方案 A：使用 GitHub Secrets（推荐）

1. 在仓库 Settings → Secrets and variables → Actions
2. 添加 Repository secrets:
   - `COZE_WEBHOOK_URL`
   - `COZE_BEARER_TOKEN`

3. 创建 GitHub Actions 工作流 `.github/workflows/deploy.yml`：

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Inject config
        run: |
          cat > js/config.js << EOF
          const COZE_CONFIG = {
              WEBHOOK_URL: "${{ secrets.COZE_WEBHOOK_URL }}",
              BEARER_TOKEN: "${{ secrets.COZE_BEARER_TOKEN }}"
          };
          EOF
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./
```

#### 方案 B：使用反向代理

如果担心 Token 暴露，可以搭建一个简单的代理服务：

```javascript
// 示例：Node.js 代理
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

app.use('/api/coze', createProxyMiddleware({
    target: 'https://api.coze.cn',
    changeOrigin: true,
    headers: {
        'Authorization': `Bearer ${process.env.COZE_TOKEN}`
    },
    pathRewrite: {
        '^/api/coze': ''
    }
}));

app.listen(3000);
```

### 2. 自定义域名

1. 在仓库根目录创建 `CNAME` 文件：
   ```
   tarot.yourdomain.com
   ```

2. 在域名 DNS 管理中添加 CNAME 记录：
   ```
   主机记录：tarot
   记录类型：CNAME
   记录值：你的用户名.github.io
   ```

3. 在 GitHub Pages 设置中启用自定义域名

---

## 🧪 测试与验证

### 1. 本地测试

```bash
# 使用 Python 启动本地服务器
python3 -m http.server 8080

# 或使用 Node.js
npx serve . -p 8080
```

访问：`http://localhost:8080`

### 2. 功能测试清单

- ✅ 页面加载正常，星空背景显示
- ✅ 牌阵选择网格正确渲染
- ✅ 选择牌阵后按钮可用
- ✅ 输入问题页面正常
- ✅ 抽牌动画正常播放
- ✅ API 请求成功发送
- ✅ 结果页面正确显示牌组
- ✅ 解读文字正常显示
- ✅ 重新占卜功能正常

### 3. 错误场景测试

| 场景 | 预期行为 |
|------|----------|
| 网络断开 | 显示错误提示，允许重试 |
| Token 错误 | 显示错误信息 |
| API 超时 | 显示超时提示 |
| 返回格式错误 | 优雅降级，提示重试 |

---

## 📊 监控与优化

### 1. 性能监控

推荐使用以下工具监控 GitHub Pages：

- **GitHub Insights**：查看访问统计
- **Google Analytics**：添加分析代码到 index.html
- **UptimeRobot**：监控网站可用性

### 2. Coze 使用统计

在 Coze 平台查看：
- API 调用次数
- 工作流执行成功率
- 平均响应时间
- Token 消耗统计

### 3. 性能优化建议

- ✅ 启用 gzip 压缩（GitHub Pages 默认启用）
- ✅ 优化图片大小
- ✅ 减少 CSS/JS 文件大小
- ✅ 考虑使用 CDN 加速静态资源

---

## 🔒 安全最佳实践

### 1. Token 管理
- ❌ 不要在代码中硬编码 Token
- ❌ 不要将包含 Token 的文件提交到公开仓库
- ✅ 使用环境变量或 Secrets
- ✅ 定期轮换 Token
- ✅ 限制 Token 权限（仅授予必要权限）

### 2. 请求安全
- ✅ 使用 HTTPS（GitHub Pages 默认启用）
- ✅ 验证请求来源
- ✅ 添加请求速率限制（在代理层）
- ✅ 记录请求日志（用于排查问题）

### 3. 内容安全
- ✅ 添加 CSP（内容安全策略）
- ✅ 验证用户输入
- ✅ XSS 防护（前端已处理）

---

## 🆘 常见问题

### Q1: 前端显示 CORS 错误？

**原因**：Coze Webhook 可能未配置 CORS 允许

**解决方案**：
1. 检查 Coze 触发器配置是否正确
2. 使用反向代理方案（见上文）
3. 联系 Coze 技术支持

### Q2: 抽牌后一直加载不显示结果？

**原因**：可能是大模型响应超时或返回格式错误

**排查步骤**：
1. 打开浏览器开发者工具 → Console 查看错误
2. 查看 Network 标签，检查 API 响应内容
3. 在 Coze 平台查看工作流执行日志
4. 验证大模型输出是否为有效的 JSON 格式

### Q3: GitHub Pages 部署后 404？

**原因**：部署需要时间，或分支配置错误

**解决方案**：
1. 等待 5-10 分钟
2. 检查 Pages 设置中的分支是否正确
3. 确保仓库是公开的（私有仓库需要 Pro 计划）
4. 清除浏览器缓存

### Q4: 如何更新前端代码？

```bash
# 修改代码后
git add .
git commit -m "Update: xxx"
git push
```

GitHub Pages 会自动重新部署。

### Q5: Coze 工作流执行失败？

1. 查看 Coze 平台的工作流日志
2. 检查代码节点的语法错误
3. 验证大模型提示词是否正确
4. 检查输入参数是否符合预期

---

## 📞 技术支持

如果遇到问题：

1. 先查看本文档的「常见问题」部分
2. 查看 Coze 官方文档：https://www.coze.cn/docs
3. 检查浏览器控制台的错误信息
4. 查看 Coze 平台的工作流执行日志

---

## 🎉 部署完成清单

- [ ] 前端代码推送到 GitHub
- [ ] GitHub Pages 已启用并可访问
- [ ] Coze Bot 已创建并配置完成
- [ ] 工作流测试通过
- [ ] Webhook 触发器配置完成
- [ ] 前端 config.js 填入正确的 URL 和 Token
- [ ] 完整功能测试通过
- [ ] Token 安全措施已实施
- [ ] 自定义域名配置（可选）
- [ ] 监控工具已配置（可选）

**恭喜！你的塔罗牌系统已成功部署！** 🌟
