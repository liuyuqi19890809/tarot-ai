"""
塔罗牌数据模块
包含78张韦特塔罗牌的完整数据
"""

# 大阿卡纳 22张
MAJOR_ARCANA = [
    {"id": 0, "name": "愚者", "name_en": "The Fool", "element": "风", "meaning": "新的开始、冒险、天真、自由", "reversed": "鲁莽、不负责任、冲动"},
    {"id": 1, "name": "魔术师", "name_en": "The Magician", "element": "风", "meaning": "创造力、技能、意志力、自信", "reversed": "欺骗、操纵、技能不足"},
    {"id": 2, "name": "女祭司", "name_en": "The High Priestess", "element": "水", "meaning": "直觉、神秘、智慧、潜意识", "reversed": "隐藏的真相、忽视直觉"},
    {"id": 3, "name": "女皇", "name_en": "The Empress", "element": "土", "meaning": "丰饶、母性、自然、创造力", "reversed": "依赖、创造力受阻"},
    {"id": 4, "name": "皇帝", "name_en": "The Emperor", "element": "火", "meaning": "权威、结构、控制、父亲形象", "reversed": "独裁、缺乏纪律"},
    {"id": 5, "name": "教皇", "name_en": "The Hierophant", "element": "土", "meaning": "传统、信仰、指导、教育", "reversed": "打破常规、新的信仰"},
    {"id": 6, "name": "恋人", "name_en": "The Lovers", "element": "风", "meaning": "爱情、选择、和谐、关系", "reversed": "不和谐、错误的选择"},
    {"id": 7, "name": "战车", "name_en": "The Chariot", "element": "水", "meaning": "胜利、意志力、决心、控制", "reversed": "失去方向、缺乏控制"},
    {"id": 8, "name": "力量", "name_en": "Strength", "element": "火", "meaning": "勇气、耐心、内在力量、慈悲", "reversed": "软弱、自我怀疑"},
    {"id": 9, "name": "隐士", "name_en": "The Hermit", "element": "土", "meaning": "内省、寻找真理、独处、指导", "reversed": "孤立、逃避现实"},
    {"id": 10, "name": "命运之轮", "name_en": "Wheel of Fortune", "element": "火", "meaning": "变化、周期、运气、转折点", "reversed": "抵抗变化、坏运气"},
    {"id": 11, "name": "正义", "name_en": "Justice", "element": "风", "meaning": "公正、真理、因果、法律", "reversed": "不公正、逃避责任"},
    {"id": 12, "name": "倒吊人", "name_en": "The Hanged Man", "element": "水", "meaning": "牺牲、放手、新视角、等待", "reversed": "无谓的牺牲、抗拒改变"},
    {"id": 13, "name": "死神", "name_en": "Death", "element": "水", "meaning": "结束、转变、新生、释放", "reversed": "抗拒改变、停滞不前"},
    {"id": 14, "name": "节制", "name_en": "Temperance", "element": "火", "meaning": "平衡、耐心、调和、适度", "reversed": "不平衡、过度"},
    {"id": 15, "name": "恶魔", "name_en": "The Devil", "element": "土", "meaning": "束缚、物质主义、欲望、阴暗面", "reversed": "解放、克服诱惑"},
    {"id": 16, "name": "塔", "name_en": "The Tower", "element": "火", "meaning": "突变、混乱、启示、破坏", "reversed": "避免灾难、恐惧改变"},
    {"id": 17, "name": "星星", "name_en": "The Star", "element": "风", "meaning": "希望、灵感、平静、疗愈", "reversed": "失望、缺乏信心"},
    {"id": 18, "name": "月亮", "name_en": "The Moon", "element": "水", "meaning": "幻觉、恐惧、潜意识、直觉", "reversed": "释放恐惧、揭示真相"},
    {"id": 19, "name": "太阳", "name_en": "The Sun", "element": "火", "meaning": "成功、快乐、活力、清晰", "reversed": "暂时的失败、缺乏活力"},
    {"id": 20, "name": "审判", "name_en": "Judgement", "element": "火", "meaning": "觉醒、重生、召唤、救赎", "reversed": "自我怀疑、拒绝改变"},
    {"id": 21, "name": "世界", "name_en": "The World", "element": "土", "meaning": "完成、整合、成就、旅行", "reversed": "未完成、缺乏完整性"},
]

# 宫廷牌映射表：11=侍从, 12=骑士, 13=王后, 14=国王
COURT_CARDS = {
    11: ("侍从", "Page"),
    12: ("骑士", "Knight"),
    13: ("王后", "Queen"),
    14: ("国王", "King")
}


# ============================================
# 权杖牌组完整含义（火元素 - 创造力、行动、热情）
# ============================================
WANDS_MEANINGS = {
    1: {"meaning": "新的开始、创造力迸发、灵感闪现、行动的契机", "reversed": "缺乏方向、创造力受阻、错过机会"},
    2: {"meaning": "规划未来、做决定、发现新机会、准备行动", "reversed": "拖延、恐惧变化、计划受阻"},
    3: {"meaning": "初步成功、扩展、远见、贸易合作", "reversed": "延迟、缺乏进展、合作失败"},
    4: {"meaning": "庆祝、和谐、家庭团聚、稳定基础", "reversed": "不和谐、缺乏支持、根基不稳"},
    5: {"meaning": "竞争、冲突、张力、立场斗争", "reversed": "和解、结束冲突、避免斗争"},
    6: {"meaning": "胜利、成功、公众认可、骄傲", "reversed": "虚假的成功、骄傲自满、得意忘形"},
    7: {"meaning": "挑战、防御、坚持立场、勇气", "reversed": "感到不知所措、放弃、防御过度"},
    8: {"meaning": "快速行动、进展、改变、旅程", "reversed": "延迟、阻碍、缺乏方向"},
    9: {"meaning": "坚韧、毅力、最后的冲刺、勇气", "reversed": "精疲力竭、缺乏坚持、恐惧挑战"},
    10: {"meaning": "负担、责任过重、压力、完成", "reversed": "释放负担、 delegation、无法完成"},
    11: {"meaning": "探索、热情的开始、信息、新的冒险", "reversed": "坏消息、缺乏方向、不切实际"},
    12: {"meaning": "行动、冒险、能量、冲动", "reversed": "鲁莽、无方向、混乱、冲动行事"},
    13: {"meaning": "自信、独立、温暖、领导力", "reversed": "自私、嫉妒、冷漠、缺乏安全感"},
    14: {"meaning": "远见、领导力、创造力、创业精神", "reversed": "专横、冲动、缺乏远见"}
}


# ============================================
# 圣杯牌组完整含义（水元素 - 情感、爱、关系）
# ============================================
CUPS_MEANINGS = {
    1: {"meaning": "新的感情、直觉、心灵开启、爱的开始", "reversed": "情感封闭、缺乏直觉、错过爱的机会"},
    2: {"meaning": "合一、伙伴关系、真爱、连接", "reversed": "不和谐、不平衡、沟通不良"},
    3: {"meaning": "庆祝、友谊、创造力、社交活动", "reversed": "过度放纵、缺乏社交、友谊破裂"},
    4: {"meaning": "冥想、冷漠、重新评估、新的机会", "reversed": "觉醒、走出冷漠、抓住机会"},
    5: {"meaning": "失落、悲伤、遗憾、失望", "reversed": "接受、放下过去、向前看"},
    6: {"meaning": "怀旧、童年、纯真、给予和接受", "reversed": "活在过去、不成熟、需要成长"},
    7: {"meaning": "幻想、选择、想象力、白日梦", "reversed": "迷茫、缺乏方向、幻想破灭"},
    8: {"meaning": "离开、放弃、寻找更深的意义、前进", "reversed": "害怕离开、停滞、逃避问题"},
    9: {"meaning": "满足、愿望实现、感恩、享乐", "reversed": "贪得无厌、缺乏满足、物质主义"},
    10: {"meaning": "和谐、家庭幸福、情感满足、伙伴关系", "reversed": "家庭冲突、不和谐、破碎的梦想"},
    11: {"meaning": "创意灵感、情感的消息、新的开始、直觉", "reversed": "情感的坏消息、缺乏创意、不切实际"},
    12: {"meaning": "浪漫、魅力、理想主义、追求", "reversed": "情绪化、喜怒无常、不切实际的理想"},
    13: {"meaning": "同理心、无条件的爱、直觉、治愈", "reversed": "情感不稳定、缺乏同理心、压抑情绪"},
    14: {"meaning": "情感成熟、控制情绪、同情心、智慧", "reversed": "情感冷漠、操纵、情绪爆发"}
}


# ============================================
# 宝剑牌组完整含义（风元素 - 思维、沟通、冲突）
# ============================================
SWORDS_MEANINGS = {
    1: {"meaning": "新的想法、突破、清晰的思维、真理", "reversed": "思维混乱、缺乏灵感、决策困难"},
    2: {"meaning": "僵局、盲目、选择困难、平衡", "reversed": "看清真相、做出决定、摆脱困境"},
    3: {"meaning": "心碎、痛苦、伤心、背叛", "reversed": "治愈、放下、重新开始"},
    4: {"meaning": "休息、恢复、冥想、暂时的撤退", "reversed": "觉醒、回归现实、走出孤独"},
    5: {"meaning": "冲突、竞争、失败、损失", "reversed": "和解、放下争执、走出泥潭"},
    6: {"meaning": "远行、搬家、离开、平静的过渡", "reversed": "拖延、不愿离开、犹豫不决"},
    7: {"meaning": "欺骗、谋略、隐藏意图、不诚实", "reversed": "谎言被揭穿、良心发现、坦白"},
    8: {"meaning": "束缚、困境、受害者心态、限制", "reversed": "解放、重获自由、找回力量"},
    9: {"meaning": "焦虑、担忧、失眠、噩梦", "reversed": "绝望、偏执、情况好转"},
    10: {"meaning": "毁灭、痛苦、终结、背叛", "reversed": "复苏、新的开始、从废墟中重生"},
    11: {"meaning": "新的计划、好奇心、消息、学习", "reversed": "拖延、欺骗、八卦、坏消息"},
    12: {"meaning": "行动、野心、速度、冲动", "reversed": "鲁莽、无方向、混乱、言行不一"},
    13: {"meaning": "独立、清晰、边界、客观", "reversed": "刻薄、孤独、冷漠、心胸狭隘"},
    14: {"meaning": "权威、逻辑、控制、智力", "reversed": "暴君、操纵、无情、滥用权力"}
}


# ============================================
# 星币牌组完整含义（土元素 - 物质、财富、稳定）
# ============================================
PENTACLES_MEANINGS = {
    1: {"meaning": "新的机会、财富、繁荣、物质收获", "reversed": "错失机会、财务损失、缺乏规划"},
    2: {"meaning": "平衡、灵活性、时间管理、适应", "reversed": "失去平衡、 overwhelmed、财务不稳定"},
    3: {"meaning": "团队合作、技能发展、工作、成就", "reversed": "缺乏合作、平庸、技能不足"},
    4: {"meaning": "占有欲、控制、保守、财务稳定", "reversed": "财务损失、放手、慷慨"},
    5: {"meaning": "财务困难、贫困、缺乏支持、艰难时期", "reversed": "恢复、改善、慈善、接受帮助"},
    6: {"meaning": "慷慨、给予和接受、慈善、分享", "reversed": "负债、自私、不平等的交换"},
    7: {"meaning": "耐心、投资、长期视角、收获", "reversed": "缺乏耐心、糟糕的投资、急于求成"},
    8: {"meaning": "学徒、技能发展、勤奋、质量", "reversed": "缺乏技能、懒惰、工作不认真"},
    9: {"meaning": "奢侈、自给自足、独立、成就", "reversed": "过度工作、贪婪、缺乏安全感"},
    10: {"meaning": "财富、家庭、传承、成功", "reversed": "家庭冲突、财务失败、遗产问题"},
    11: {"meaning": "新的工作、学习、实用的技能、消息", "reversed": "缺乏方向、懒惰、坏消息"},
    12: {"meaning": "努力工作、责任、可靠、效率", "reversed": "懒惰、不负责任、无聊"},
    13: {"meaning": "实际、养育、资源丰富、稳定", "reversed": "财务不安全、嫉妒、缺乏家庭支持"},
    14: {"meaning": "繁荣、安全、领导力、商业头脑", "reversed": "财务失败、贪婪、缺乏安全感"}
}


def generate_minor_arcana(suit_name_cn, suit_name_en, element, base_id, meanings_dict):
    """生成小阿卡纳牌组 - 使用每一张牌的独立含义"""
    cards = []
    for i in range(14):
        num = i + 1
        if num == 1:
            # Ace
            card_name_cn = f"{suit_name_cn}首牌"
            card_name_full = f"{suit_name_cn} ({suit_name_en}) Ace"
            card_name_en = f"Ace of {suit_name_en}"
        elif num <= 10:
            # 数字牌 2-10
            card_name_cn = f"{suit_name_cn}{num}"
            card_name_full = f"{suit_name_cn} ({suit_name_en}) {num}"
            card_name_en = f"{num} of {suit_name_en}"
        else:
            # 宫廷牌 11-14 → 侍从、骑士、王后、国王
            court_cn, court_en = COURT_CARDS[num]
            card_name_cn = f"{suit_name_cn}{court_cn}"
            card_name_full = f"{suit_name_cn} ({suit_name_en}) {court_en}"
            card_name_en = f"{court_en} of {suit_name_en}"
        
        # 获取该牌的独立含义
        card_meanings = meanings_dict[num]
        
        cards.append({
            "id": base_id + i,
            "name": card_name_cn,
            "name_full": card_name_full,
            "name_en": card_name_en,
            "suit": suit_name_en.lower(),
            "element": element,
            "meaning": card_meanings["meaning"],
            "reversed": card_meanings["reversed"]
        })
    return cards


# 小阿卡纳 56张 - 使用独立含义字典
WANDS = generate_minor_arcana("权杖", "Wands", "火", 22, WANDS_MEANINGS)
CUPS = generate_minor_arcana("圣杯", "Cups", "水", 36, CUPS_MEANINGS)
SWORDS = generate_minor_arcana("宝剑", "Swords", "风", 50, SWORDS_MEANINGS)
PENTACLES = generate_minor_arcana("星币", "Pentacles", "土", 64, PENTACLES_MEANINGS)

# 全部78张牌
ALL_CARDS = MAJOR_ARCANA + WANDS + CUPS + SWORDS + PENTACLES

# 牌阵定义
SPREADS = {
    "three_card": {
        "name": "圣三角",
        "description": "最经典的三张牌阵，适用于所有问题",
        "cards": 3,
        "positions": ["过去", "现在", "未来"],
        "best_for": ["感情", "事业", "学业", "通用"]
    },
    "four_elements": {
        "name": "四元素",
        "description": "火水土风四元素分析，全面了解现状",
        "cards": 4,
        "positions": ["火（行动与热情）", "水（情感与关系）", "土（物质与基础）", "风（思维与沟通）"],
        "best_for": ["自我认知", "全面分析"]
    },
    "love_cross": {
        "name": "爱情十字",
        "description": "专为感情问题设计的五张牌阵",
        "cards": 5,
        "positions": ["你自己", "对方心态", "你们的关系现状", "外界影响", "未来发展"],
        "best_for": ["感情问题", "恋爱关系", "婚姻"]
    },
    "celtic_cross": {
        "name": "凯尔特十字",
        "description": "最全面的十张牌阵，深度分析复杂问题",
        "cards": 10,
        "positions": ["现状", "挑战", "潜意识", "过去", "可能性", "近期未来", "你的态度", "外界环境", "希望与恐惧", "最终结果"],
        "best_for": ["复杂问题", "重要决策", "深度分析"]
    },
    "yes_no": {
        "name": "是/否 单张牌",
        "description": "快速回答简单问题",
        "cards": 1,
        "positions": ["答案"],
        "best_for": ["快速决策", "简单问题"]
    },
    "time_flow": {
        "name": "时间流",
        "description": "分析时间线上的发展趋势",
        "cards": 4,
        "positions": ["过去影响", "当前状态", "近期发展", "长远结果"],
        "best_for": ["趋势分析", "发展预测"]
    },
    "career_path": {
        "name": "事业发展牌阵",
        "description": "专为事业问题设计",
        "cards": 5,
        "positions": ["当前工作状态", "你的优势", "你的挑战", "外界机会", "未来发展建议"],
        "best_for": ["事业发展", "工作决策", "职业规划"]
    },
    "weekly_horoscope": {
        "name": "每周运势",
        "description": "预测未来一周的整体运势",
        "cards": 7,
        "positions": ["周一", "周二", "周三", "周四", "周五", "周六", "周日"],
        "best_for": ["周运", "日常指导"]
    },
    "decision_making": {
        "name": "二选一决策牌阵",
        "description": "帮助在两个选项中做选择",
        "cards": 5,
        "positions": ["现状", "选项A发展", "选项A结果", "选项B发展", "选项B结果"],
        "best_for": ["决策问题", "两难选择"]
    },
    "relationship_analysis": {
        "name": "关系深度分析",
        "description": "深度分析两人关系的各个层面",
        "cards": 6,
        "positions": ["你对对方的感觉", "对方对你的感觉", "关系基础", "当前问题", "外部影响", "未来展望"],
        "best_for": ["关系分析", "感情问题"]
    },
    "life_path": {
        "name": "人生发展牌阵",
        "description": "分析人生各领域的发展方向",
        "cards": 7,
        "positions": ["事业运", "感情运", "财运", "健康运", "家庭运", "人际运", "整体建议"],
        "best_for": ["人生规划", "综合分析"]
    },
    "spirit_guidance": {
        "name": "心灵指引牌阵",
        "description": "获取内心智慧和高我指引",
        "cards": 4,
        "positions": ["当前需要学习的课题", "需要释放的情绪", "内在的力量", "下一步行动指引"],
        "best_for": ["心灵成长", "自我探索"]
    }
}
