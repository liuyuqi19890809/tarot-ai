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
    {"id": 8, "name": "力量", "name_en": "Strength", "element": "火", "meaning": "勇气、耐心、内在力量、 compassion", "reversed": "软弱、自我怀疑"},
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


def generate_minor_arcana(suit_name_cn, suit_name_en, element, base_id, meanings):
    """生成小阿卡纳牌组"""
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
        
        cards.append({
            "id": base_id + i,
            "name": card_name_cn,
            "name_full": card_name_full,
            "name_en": card_name_en,
            "suit": suit_name_en.lower(),
            "element": element,
            "meaning": meanings["meaning"],
            "reversed": meanings["reversed"]
        })
    return cards


# 小阿卡纳 56张
WANDS = generate_minor_arcana("权杖", "Wands", "火", 22, {
    "meaning": "创造力、行动、热情、事业发展",
    "reversed": "阻碍、延迟、缺乏动力"
})

CUPS = generate_minor_arcana("圣杯", "Cups", "水", 36, {
    "meaning": "情感、爱、关系、直觉",
    "reversed": "情感疏远、失望、压抑情绪"
})

SWORDS = generate_minor_arcana("宝剑", "Swords", "风", 50, {
    "meaning": "思维、沟通、冲突、真理",
    "reversed": "混乱、欺骗、内心挣扎"
})

PENTACLES = generate_minor_arcana("星币", "Pentacles", "土", 64, {
    "meaning": "物质、财富、工作、稳定",
    "reversed": "财务困难、不稳定、失去基础"
})

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
        "best_for": ["每周运势", "日程规划"]
    },
    "decision_making": {
        "name": "二选一决策牌阵",
        "description": "帮助在两个选项中做选择",
        "cards": 5,
        "positions": ["现状", "选项A发展", "选项A结果", "选项B发展", "选项B结果"],
        "best_for": ["二选一决策", "两难选择"]
    },
    "relationship_analysis": {
        "name": "关系深度分析",
        "description": "深度分析两人关系的各个层面",
        "cards": 6,
        "positions": ["你对对方的感觉", "对方对你的感觉", "关系基础", "当前问题", "外部影响", "未来展望"],
        "best_for": ["感情关系", "人际关系分析"]
    },
    "life_path": {
        "name": "人生发展牌阵",
        "description": "分析人生各领域的发展方向",
        "cards": 7,
        "positions": ["事业运", "感情运", "财运", "健康运", "家庭运", "人际运", "整体建议"],
        "best_for": ["人生规划", "全面运势"]
    },
    "spirit_guidance": {
        "name": "心灵指引牌阵",
        "description": "获取内心智慧和高我指引",
        "cards": 4,
        "positions": ["当前需要学习的课题", "需要释放的情绪", "内在的力量", "下一步行动指引"],
        "best_for": ["心灵成长", "自我探索", "疗愈"]
    }
}
