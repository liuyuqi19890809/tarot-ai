"""
塔罗牌解读模块
包含完整的解读逻辑和文案生成
"""
import random
from datetime import datetime
from .tarot_cards import ALL_CARDS


def analyze_elements(cards):
    """统计牌组元素比例"""
    elements = {"火": 0, "水": 0, "风": 0, "土": 0}
    major_count = 0
    
    for card in cards:
        element = card.get("element", "")
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
            # 大阿卡纳：使用预定义的元素属性
            major_count += 1
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
        "火": f"🔥 火元素主导 ({element_percent['火']}%) - 能量充沛，行动力强，热情正在燃烧",
        "水": f"💧 水元素主导 ({element_percent['水']}%) - 情感流动，直觉敏锐，心灵正在苏醒",
        "风": f"💨 风元素主导 ({element_percent['风']}%) - 思维清晰，沟通顺畅，心智正在扩展",
        "土": f"🌍 土元素主导 ({element_percent['土']}%) - 根基稳固，物质丰盈，现实正在显化"
    }
    
    major_vibe = f"\n\n✧ 大阿卡纳出现 {major_count} 张 - "
    if major_count >= len(cards) * 0.5:
        major_vibe += "重大课题正在展开，这是灵魂成长的关键时期"
    else:
        major_vibe += "日常能量在运作，细微之处见真谛"
    
    return vibe_descriptions[dominant] + major_vibe


def interpret_single_card(card, position):
    """单张牌的散文式解读"""
    meaning = card["reversed"] if card.get("is_reversed", False) and card.get("reversed") else card["meaning"]
    status = "逆位" if card.get("is_reversed", False) else "正位"
    
    templates = [
        f"在「{position}」的位置上，「{card['name']}」以{status}的姿态呈现。{meaning}。这股能量正在你的生命中编织着某种方式运作。",
        f"「{card['name']}」出现在「{position}」——{status}能量的智慧正在向你低语。{meaning}。",
        f"「{position}」的能量中心是「{card['name']}」，{status}状态下的启示：{meaning}。"
    ]
    
    return random.choice(templates)


def generate_reading(cards, spread_name, question=""):
    """生成完整的深度解读"""
    elements, major_count = analyze_elements(cards)
    
    reading = f"""
> ✧ 首席塔罗解读 ✧
> **牌阵：{spread_name}**
> **时间：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}**

---

## ✧ 灵性共振 ✧

{get_vibe_check(elements, major_count, cards)}

---

## ✧ 牌面星图 ✧

"""
    
    # 优雅展示所有牌
    for card in cards:
        reading += f"\n{interpret_single_card(card, card['position'])}\n\n"
    
    reading += """---

## ✧ 灵魂指引 ✧

"""
    
    # 根据牌阵类型生成解读
    dominant = get_dominant_element(elements)
    
    if len(cards) == 3:  # 圣三角
        past_card = cards[0]
        present_card = cards[1]
        future_card = cards[2]
        
        reading += f"""
### **时光之流**

从 **{past_card['name']}** 带来的课题，走到当下 **{present_card['name']}** 的状态——你已经走了很长的路。过去的经历如同刻在灵魂上的印记，塑造了今天看世界的眼睛。

而前方，**{future_card['name']}** 的能量正在等待着你。这不是一个终点，而是灵魂邀请你进入下一个阶段的邀请函。

---

### **大师箴言**

1. **接纳当下的状态** —— 无论现在看起来是好是坏，这都是你旅途中必经的风景。每一张牌都有它出现的意义。
2. **与过去和解** —— 那些你以为放不下的人和事，其实早已准备好离你而去，只等你轻轻挥手。
3. **勇敢向前迈步** —— 未来的牌已经准备好了，你只需要伸出手，接住宇宙为你准备的礼物。

"""
    elif len(cards) >= 5:  # 复杂牌阵
        reading += f"""
### **核心羁绊**

**{cards[0]['name']}** 与 **{cards[1]['name']}** 的能量正在你的生命中上演一场深刻的对话。

这不是简单的因果关系，而是更深层次的灵魂课题——你内心的某个部分，正在通过这两张牌的碰撞，让你看到自己未曾觉察的真相。当下以{dominant}元素为主导的能量场，为这个课题提供了独特的解决视角。

---

### **大师箴言**

1. **暂停，而非停止** —— 有些时候，"不动"比"动"需要更大的勇气。允许自己停在原地，直到你听见内心真正的声音。
2. **倾听身体的智慧** —— 你的感受永远比你的头脑更接近真相。紧绷、放松、喜悦、悲伤——身体从不说谎。
3. **相信宇宙的时机** —— 该发生的，不会早一秒，也不会晚一秒。所有的等待，都有它神圣的理由。

"""
    else:  # 单张牌
        reading += f"""
### **当下的启示**

**{cards[0]['name']}** 的出现绝非偶然。这张牌带着宇宙的讯息来到你面前，不是为了告诉你一个标准答案，而是为了唤醒你内在深处早已知道的那个部分。

{dominant}元素的能量正在支持你，邀请你以全新的视角看待当下的处境。

---

### **大师箴言**

1. **向内看，答案就在那里** —— 所有你需要的智慧，从来都不在外面，而在你之内。
2. **信任第一念** —— 你看到牌的那一瞬间，脑海中浮现的第一个想法，往往就是最准确的答案。
3. **保持开放** —— 宇宙比你想象的更爱你，它为你准备的，往往超出你所能想象。

"""
    
    reading += """
---

> ✧ 愿星光照亮你的道路，愿智慧指引你的心灵 ✧
> *塔罗展示的是当下的能量轨迹，你永远是自己命运的书写者*
"""
    
    return reading
