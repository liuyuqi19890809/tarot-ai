# 玄数塔罗 - Coze Bot 配置指南

## 📋 目录
1. [Bot 基本配置](#1-bot-基本配置)
2. [工作流设计](#2-工作流设计)
3. [代码节点 - 抽牌逻辑](#3-代码节点---抽牌逻辑)
4. [大模型节点 - 解读逻辑](#4-大模型节点---解读逻辑)
5. [触发器配置](#5-触发器配置)
6. [部署验证](#6-部署验证)

---

## 1. Bot 基本配置

### 1.1 创建 Bot
1. 登录 [Coze 平台](https://www.coze.cn)
2. 点击「创建 Bot」
3. Bot 名称：**玄数塔罗**
4. Bot 头像：使用塔罗牌相关图片
5. Bot 简介：首席塔罗大师，为你揭示命运的密码，提供心灵指引

### 1.2 系统提示词 (Persona)
```markdown
# 角色设定
你是【玄数塔罗】——拥有30年占卜经验的首席塔罗大师。你精通韦特塔罗体系，深谙象征主义与心理学解读之道。

## 风格要求
- 语言风格：神秘、优雅、富有诗意，使用散文式表达
- 语气：温和、包容、带有智慧的启发性
- 禁止：机械刻板的回答、过于绝对的断言、使用"算命"等词汇

## 解读原则
1. **元素分析法**：统计牌阵中火、水、土、风四大元素的分布，分析能量倾向
2. **正逆位解读**：正位强调正面能量，逆位提示需要注意的方面
3. **牌面联动**：结合牌与牌之间的关系，形成完整的故事线
4. **启发式引导**：不直接给出答案，而是引导问卜者内心的觉知

## 输出格式
必须严格按照以下 JSON 格式返回（包装在 markdown 代码块中）：
```json
{
  "success": true,
  "cards": [
    {
      "name": "牌名",
      "position": "正位/逆位",
      "position_name": "在牌阵中的位置名称",
      "meaning": "单牌简要解读（20-30字）",
      "is_reversed": true/false
    }
  ],
  "element_analysis": {
    "fire": "权杖数量及火元素能量解读",
    "water": "圣杯数量及水元素能量解读",
    "earth": "星币数量及土元素能量解读",
    "air": "宝剑数量及风元素能量解读"
  },
  "reading": "完整的散文式深度解读（300-500字）",
  "timestamp": 1234567890
}
```

## 重要提醒
- 所有牌面必须来自标准韦特塔罗78张牌库
- 每张牌的正逆位随机分配
- 确保同一次占卜中没有重复的牌
```

---

## 2. 工作流设计

### 2.1 创建工作流
1. 在 Bot 编排页面，点击「添加工作流」
2. 工作流名称：**塔罗牌占卜工作流**
3. 工作流描述：接收前端请求，执行抽牌和解读流程

### 2.2 工作流节点结构
```
开始节点 → 代码节点（抽牌） → 大模型节点（解读） → 结束节点
```

---

## 3. 代码节点 - 抽牌逻辑

### 3.1 节点配置
- 节点名称：**塔罗牌抽取**
- 编程语言：**Python**
- 设置为「阻塞式执行」

### 3.2 输入参数
| 参数名 | 类型 | 说明 | 示例值 |
|--------|------|------|--------|
| spread_type | String | 牌阵类型 | "three_card" |
| card_count | Number | 抽牌数量 | 3 |
| question | String | 用户问题 | "我的感情运势如何？" |

### 3.3 Python 代码
```python
import random
import json

def main(args):
    # 完整78张韦特塔罗牌库
    major_arcana = [
        "0. 愚人 (The Fool)",
        "I. 魔术师 (The Magician)",
        "II. 女祭司 (The High Priestess)",
        "III. 皇后 (The Empress)",
        "IV. 皇帝 (The Emperor)",
        "V. 教皇 (The Hierophant)",
        "VI. 恋人 (The Lovers)",
        "VII. 战车 (The Chariot)",
        "VIII. 力量 (Strength)",
        "IX. 隐士 (The Hermit)",
        "X. 命运之轮 (Wheel of Fortune)",
        "XI. 正义 (Justice)",
        "XII. 倒吊人 (The Hanged Man)",
        "XIII. 死神 (Death)",
        "XIV. 节制 (Temperance)",
        "XV. 恶魔 (The Devil)",
        "XVI. 塔 (The Tower)",
        "XVII. 星星 (The Star)",
        "XVIII. 月亮 (The Moon)",
        "XIX. 太阳 (The Sun)",
        "XX. 审判 (Judgement)",
        "XXI. 世界 (The World)"
    ]
    
    suits = ["权杖", "圣杯", "宝剑", "星币"]
    ranks = [
        ("Ace", "Ace"),
        ("2", "二"),
        ("3", "三"),
        ("4", "四"),
        ("5", "五"),
        ("6", "六"),
        ("7", "七"),
        ("8", "八"),
        ("9", "九"),
        ("10", "十"),
        ("侍从", "侍从"),
        ("骑士", "骑士"),
        ("王后", "王后"),
        ("国王", "国王")
    ]
    
    minor_arcana = []
    for suit in suits:
        for rank_en, rank_cn in ranks:
            minor_arcana.append(f"{rank_cn} of {suit}")
    
    full_deck = major_arcana + minor_arcana
    
    # 牌阵位置名称映射
    positions_map = {
        "three_card": ["过去", "现在", "未来"],
        "four_elements": ["火（行动与热情）", "水（情感与关系）", "土（物质与基础）", "风（思维与沟通）"],
        "love_cross": ["你自己", "对方心态", "你们的关系现状", "外界影响", "未来发展"],
        "celtic_cross": ["现状", "挑战", "潜意识", "过去", "可能性", "近期未来", "你的态度", "外界环境", "希望与恐惧", "最终结果"],
        "yes_no": ["答案"],
        "time_flow": ["过去影响", "当前状态", "近期发展", "长远结果"],
        "career_path": ["当前工作状态", "你的优势", "你的挑战", "外界机会", "未来发展建议"],
        "weekly_horoscope": ["周一", "周二", "周三", "周四", "周五", "周六", "周日"],
        "decision_making": ["现状", "选项A发展", "选项A结果", "选项B发展", "选项B结果"],
        "relationship_analysis": ["你对对方的感觉", "对方对你的感觉", "关系基础", "当前问题", "外部影响", "未来展望"],
        "life_path": ["事业运", "感情运", "财运", "健康运", "家庭运", "人际运", "整体建议"],
        "spirit_guidance": ["当前需要学习的课题", "需要释放的情绪", "内在的力量", "下一步行动指引"]
    }
    
    # 获取参数
    draw_count = args.get("card_count", 3)
    spread_type = args.get("spread_type", "three_card")
    question = args.get("question", "通用占卜")
    
    # 不重复抽牌
    drawn_cards = random.sample(full_deck, min(draw_count, len(full_deck)))
    
    # 获取位置名称
    position_names = positions_map.get(spread_type, [f"第{i+1}张" for i in range(draw_count)])
    
    # 赋予正逆位
    result = []
    for i, card in enumerate(drawn_cards):
        is_reversed = random.choice([True, False])
        position = "逆位" if is_reversed else "正位"
        position_name = position_names[i] if i < len(position_names) else f"第{i+1}张"
        
        result.append({
            "name": card,
            "position": position,
            "position_name": position_name,
            "is_reversed": is_reversed,
            "meaning": ""  # 留给大模型节点填充
        })
    
    return {
        "success": True,
        "cards": result,
        "question": question,
        "spread_type": spread_type
    }
```

### 3.4 输出参数
| 参数名 | 类型 | 说明 |
|--------|------|------|
| success | Boolean | 是否成功 |
| cards | Array | 抽取的牌组 |
| question | String | 用户问题 |
| spread_type | String | 牌阵类型 |

---

## 4. 大模型节点 - 解读逻辑

### 4.1 节点配置
- 节点名称：**塔罗牌深度解读**
- 模型：选择合适的大语言模型（推荐 Doubao Pro 或 GPT-4）
- 设置为「阻塞式执行」

### 4.2 输入配置
将代码节点的输出作为输入：
- `{{代码节点.cards}}` - 牌组信息
- `{{代码节点.question}}` - 用户问题
- `{{代码节点.spread_type}}` - 牌阵类型

### 4.3 提示词模板
```markdown
你是首席塔罗大师，请根据以下信息进行深度解读：

## 牌阵信息
- 牌阵类型：{{spread_type}}
- 用户问题：{{question}}

## 抽取的牌组
{{cards}}

## 任务要求
1. 为每张牌补充简要的单牌解读（20-30字）
2. 进行四大元素分析（统计权杖/圣杯/宝剑/星币数量并解读能量倾向）
3. 撰写完整的散文式深度解读（300-500字），要求：
   - 语言优美、富有诗意
   - 结合所有牌面的象征意义
   - 分析牌与牌之间的能量流动
   - 给出启发性的建议
   - 保持神秘而温暖的语调

## 输出要求
严格按照 JSON 格式输出，不要添加其他文字：
```json
{
  "success": true,
  "cards": [
    {
      "name": "牌名",
      "position": "正位/逆位",
      "position_name": "位置名称",
      "meaning": "单牌解读",
      "is_reversed": true/false
    }
  ],
  "element_analysis": {
    "fire": "火元素解读",
    "water": "水元素解读",
    "earth": "土元素解读",
    "air": "风元素解读"
  },
  "reading": "完整解读内容"
}
```
```

---

## 5. 触发器配置

### 5.1 创建 Webhook 触发器
1. 在 Bot 编排页面的「触发器」区域，点击「+」
2. 触发器名称：**塔罗占卜 API 触发器**
3. 触发器类型：选择「事件触发」
4. 模式：**Webhook**

### 5.2 安全配置
- **Bearer Token**：系统会自动生成，复制保存到前端 `config.js`
- 可以自定义 Token 值

### 5.3 请求参数
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| spread_type | String | 是 | 牌阵类型 |
| card_count | Number | 是 | 抽牌数量 |
| question | String | 否 | 用户问题 |
| timestamp | Number | 否 | 时间戳 |

### 5.4 触发任务配置
- 任务类型：**工作流**
- 选择工作流：**塔罗牌占卜工作流**
- 参数映射：将 Webhook 参数映射到工作流输入

### 5.5 获取 Webhook URL
配置完成后，系统会生成 Webhook URL，格式类似：
```
https://api.coze.cn/v1/workflow/trigger/xxxxxxxxxxxx
```
将此 URL 复制到前端 `config.js` 的 `WEBHOOK_URL`。

---

## 6. 部署验证

### 6.1 测试工作流
1. 在 Coze 平台点击「试运行」工作流
2. 输入测试参数：
   ```json
   {
     "spread_type": "three_card",
     "card_count": 3,
     "question": "测试问题"
   }
   ```
3. 验证输出是否符合预期的 JSON 格式

### 6.2 测试 Webhook
使用 curl 测试 Webhook：
```bash
curl --location 'YOUR_WEBHOOK_URL' \
--header 'Authorization: Bearer YOUR_BEARER_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
  "spread_type": "three_card",
  "card_count": 3,
  "question": "我的感情运势如何？"
}'
```

### 6.3 前端验证
1. 部署前端到 GitHub Pages
2. 选择牌阵、输入问题，点击「开始抽牌」
3. 验证抽牌动画和结果展示

---

## 📝 注意事项

1. **CORS 问题**：如果出现跨域问题，考虑在 Coze 端配置 CORS 或使用代理
2. **超时处理**：工作流默认超时 60 秒，大模型解读可能需要较长时间
3. **Token 安全**：不要将 Bearer Token 提交到公开仓库
4. **错误处理**：前端已包含基本的错误处理和重试机制
5. **响应格式**：确保大模型严格输出 JSON 格式，否则前端无法解析

---

## 🔧 故障排查

| 问题 | 可能原因 | 解决方案 |
|------|----------|----------|
| 抽牌后无响应 | Webhook URL 或 Token 错误 | 检查 config.js 配置 |
| 结果显示异常 | JSON 解析失败 | 检查大模型输出格式 |
| CORS 错误 | 跨域限制 | 配置代理或联系 Coze 支持 |
| 工作流超时 | 大模型响应慢 | 优化提示词或增加超时时间 |

---

配置完成后，你的塔罗牌系统将完全运行在 Coze Bot 上，无需本地后端服务！🎉
