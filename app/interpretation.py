"""
塔罗牌解读模块 - V4.0 结构化输出
包含完整的解读逻辑和结构化文案生成
"""
import random
from datetime import datetime
from .tarot_cards import ALL_CARDS


def analyze_elements(cards):
    """统计牌组元素比例"""
    elements = {"火": 0, "水": 0, "风": 0, "土": 0}
    major_count = 0
    
    for card in cards:
        card_name = card["name"]
        
        # 小阿卡纳：根据牌名判断元素
        if "权杖" in card_name:
            elements["火"] += 1
        elif "圣杯" in card_name:
            elements["水"] += 1
        elif "宝剑" in card_name:
            elements["风"] += 1
        elif "星币" in card_name:
            elements["土"] += 1
        else:
            # 大阿卡纳
            major_count += 1
            element = card.get("element", "")
            if element == "火":
                elements["火"] += 1
            elif element == "水":
                elements["水"] += 1
            elif element == "风":
                elements["风"] += 1
            elif element == "土":
                elements["土"] += 1
    
    return elements, major_count


def get_dominant_element(elements):
    """获取主导元素"""
    return max(elements, key=elements.get)


def get_vibe_check(elements, major_count, cards):
    """生成能量场检查文案"""
    dominant = get_dominant_element(elements)
    total = len(cards)
    element_percent = {k: round(v/total*100) for k, v in elements.items()}
    
    vibe_descriptions = {
        "火": f"🔥 **火元素主导 ({element_percent['火']}%)** - 能量充沛，行动力强，热情正在燃烧。现在是采取行动的好时机！",
        "水": f"💧 **水元素主导 ({element_percent['水']}%)** - 情感流动，直觉敏锐，心灵正在苏醒。倾听内心的声音。",
        "风": f"💨 **风元素主导 ({element_percent['风']}%)** - 思维清晰，沟通顺畅，心智正在扩展。是学习和交流的好时期。",
        "土": f"🌍 **土元素主导 ({element_percent['土']}%)** - 根基稳固，物质丰盈，现实正在显化。适合落地执行计划。"
    }
    
    major_note = f"\n\n大阿卡纳出现 **{major_count}张** - "
    if major_count >= len(cards) * 0.5:
        major_note += "重大课题正在展开，这是灵魂成长的关键时期！"
    else:
        major_note += "日常能量在运作，细微之处见真谛。"
    
    return vibe_descriptions[dominant] + major_note


def interpret_single_card(card, position):
    """单张牌的解读"""
    meaning = card.get("reversed") if card.get("is_reversed", False) and card.get("reversed") else card.get("meaning", "塔罗牌的神秘寓意")
    status = "逆位" if card.get("is_reversed", False) else "正位"
    
    return f"**「{card['name']}」{status}** - {meaning}"


def get_action_suggestions(cards, dominant_element):
    """生成行动建议"""
    suggestions = [
        "保持正念，每天花10分钟冥想静心，与内在智慧连接",
        "记录梦境和直觉闪现，它们正在传递重要信息",
        "相信宇宙的时机，不要急于求成，让事情自然发展",
        "与信任的朋友分享你的感受，倾诉本身就是治愈"
    ]
    
    # 根据元素添加特定建议
    element_suggestions = {
        "火": [
            "将热情转化为具体行动，从最小的一步开始",
            "进行体育锻炼，释放过剩的能量",
            "开展创意项目，让灵感自由流动"
        ],
        "水": [
            "允许自己感受所有情绪，不要压抑",
            "进行与水相关的活动：洗澡、游泳、听雨",
            "滋养亲密关系，给予和接受爱"
        ],
        "风": [
            "阅读、学习、写作，扩展心智边界",
            "与他人进行深度对话，交换观点",
            "制定计划，理清思路，分步骤执行"
        ],
        "土": [
            "关注财务状况，制定预算和储蓄计划",
            "照顾身体健康，注意饮食和休息",
            "脚踏实地，一步一个脚印地推进目标"
        ]
    }
    
    suggestions = element_suggestions.get(dominant_element, suggestions)
    selected = random.sample(suggestions, min(3, len(suggestions)))
    
    return "\n".join([f"- {s}" for s in selected])


def get_potential_obstacles(cards):
    """识别潜在阻碍"""
    obstacles = [
        "自我怀疑和限制性信念可能阻碍前进",
        "过度思虑导致行动迟缓",
        "害怕改变而停留在舒适区",
        "外部环境的干扰分散注意力"
    ]
    
    # 检查是否有逆位牌
    reversed_count = sum(1 for card in cards if card.get("is_reversed", False))
    if reversed_count >= len(cards) * 0.5:
        obstacles.insert(0, "较多逆位牌显示当前能量有阻滞，需要更多耐心和内省")
    
    selected = random.sample(obstacles, min(2, len(obstacles)))
    
    return "\n".join([f"- {o}" for o in selected])


def get_timing_guidance(cards):
    """时机与运势提示"""
    now = datetime.now()
    lunar_phase = "🌙" if now.day < 15 else "🌕"
    
    guidances = [
        f"当前宇宙能量正在支持你的成长。{lunar_phase} 月亮周期提醒我们：万物都有其自然节奏。",
        "接下来的两周是关键时期，保持开放和觉知，机会可能在意想不到的时候出现。",
        "相信你已经准备好了，宇宙正在为你安排最好的一切。耐心等待，答案自会显现。",
        "现在是播种的好时机，你所付出的努力将在未来结出丰硕的果实。"
    ]
    
    return random.choice(guidances)


def get_core_insight(cards, spread_name):
    """核心启示"""
    if len(cards) == 1:
        card = cards[0]
        meaning = card.get("meaning", "塔罗牌的神秘寓意")
        return f"**「{card['name']}」**的出现绝非偶然。{meaning} 这是宇宙传递给你的特别讯息，倾听内在的声音，相信直觉的指引。"
    
    first_card = cards[0]
    last_card = cards[-1]
    
    insights = [
        f"从**「{first_card['name']}」**带来的课题，走向**「{last_card['name']}」**的启示——你正在经历一场深刻的内在旅程。",
        f"牌阵核心揭示：**{spread_name}**的能量正在为你揭示深层的真相，邀请你以全新的视角看待当下的处境。",
        f"每张牌都是灵魂的一面镜子。现在是整合这些能量，发现内在智慧的关键时刻。"
    ]
    
    return random.choice(insights)


def generate_reading(cards, spread_name, question=""):
    """生成完整的结构化深度解读 - V4.0"""
    elements, major_count = analyze_elements(cards)
    dominant = get_dominant_element(elements)
    
    reading = f"""---

## ✧ 牌阵整体能量解读 ✧

{get_vibe_check(elements, major_count, cards)}

---

## ✧ 核心启示 ✧

{get_core_insight(cards, spread_name)}

---

## ✧ 各位置牌面解读 ✧

"""
    
    # 优雅展示所有牌
    for card in cards:
        position_name = card.get("position_name", card.get("position", "未知位置"))
        reading += f"\n**📍 {position_name}**\n"
        reading += f"{interpret_single_card(card, position_name)}\n\n"
    
    reading += f"""---

## ✧ 行动建议 ✧

{get_action_suggestions(cards, dominant)}

---

## ✧ 潜在阻碍 ✧

{get_potential_obstacles(cards)}

---

## ✧ 时机与运势 ✧

{get_timing_guidance(cards)}

---

> ✧ **愿星光照亮你的道路，愿智慧指引你的心灵** ✧
> *塔罗展示的是当下的能量轨迹，你永远是自己命运的书写者*

---

⚠️ **仅供娱乐参考，请理性对待**
"""
    
    return reading
