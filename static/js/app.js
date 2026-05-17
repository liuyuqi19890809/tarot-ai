// 生成星空背景
function generateStars() {
    const starsContainer = document.getElementById('stars');
    for (let i = 0; i < 100; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.left = Math.random() * 100 + '%';
        star.style.top = Math.random() * 100 + '%';
        star.style.animationDelay = Math.random() * 3 + 's';
        star.style.width = Math.random() * 2 + 1 + 'px';
        star.style.height = star.style.width;
        starsContainer.appendChild(star);
    }
}
generateStars();

// 全局状态
let selectedSpread = null;

// 牌阵数据
const spreads = {
    "three_card": { name: "圣三角", description: "最经典的三张牌阵，适用于所有问题", cards: 3, positions: ["过去", "现在", "未来"] },
    "four_elements": { name: "四元素", description: "火水土风四元素分析，全面了解现状", cards: 4, positions: ["火（行动与热情）", "水（情感与关系）", "土（物质与基础）", "风（思维与沟通）"] },
    "love_cross": { name: "爱情十字", description: "专为感情问题设计的五张牌阵", cards: 5, positions: ["你自己", "对方心态", "你们的关系现状", "外界影响", "未来发展"] },
    "celtic_cross": { name: "凯尔特十字", description: "最全面的十张牌阵，深度分析复杂问题", cards: 10, positions: ["现状", "挑战", "潜意识", "过去", "可能性", "近期未来", "你的态度", "外界环境", "希望与恐惧", "最终结果"] },
    "yes_no": { name: "是/否 单张牌", description: "快速回答简单问题", cards: 1, positions: ["答案"] },
    "time_flow": { name: "时间流", description: "分析时间线上的发展趋势", cards: 4, positions: ["过去影响", "当前状态", "近期发展", "长远结果"] },
    "career_path": { name: "事业发展牌阵", description: "专为事业问题设计", cards: 5, positions: ["当前工作状态", "你的优势", "你的挑战", "外界机会", "未来发展建议"] },
    "weekly_horoscope": { name: "每周运势", description: "预测未来一周的整体运势", cards: 7, positions: ["周一", "周二", "周三", "周四", "周五", "周六", "周日"] },
    "decision_making": { name: "二选一决策牌阵", description: "帮助在两个选项中做选择", cards: 5, positions: ["现状", "选项A发展", "选项A结果", "选项B发展", "选项B结果"] },
    "relationship_analysis": { name: "关系深度分析", description: "深度分析两人关系的各个层面", cards: 6, positions: ["你对对方的感觉", "对方对你的感觉", "关系基础", "当前问题", "外部影响", "未来展望"] },
    "life_path": { name: "人生发展牌阵", description: "分析人生各领域的发展方向", cards: 7, positions: ["事业运", "感情运", "财运", "健康运", "家庭运", "人际运", "整体建议"] },
    "spirit_guidance": { name: "心灵指引牌阵", description: "获取内心智慧和高我指引", cards: 4, positions: ["当前需要学习的课题", "需要释放的情绪", "内在的力量", "下一步行动指引"] }
};

// 渲染牌阵选择
function renderSpreads() {
    const grid = document.getElementById('spreadGrid');
    Object.entries(spreads).forEach(([key, spread]) => {
        const card = document.createElement('div');
        card.className = 'spread-card';
        card.dataset.spread = key;
        card.innerHTML = `
            <div class="spread-name">${spread.name}</div>
            <div class="spread-desc">${spread.description}</div>
            <div class="spread-meta">
                <span>🎴 ${spread.cards}张牌</span>
                <span>📍 ${spread.positions.length}个位置</span>
            </div>
        `;
        card.onclick = () => selectSpread(key, card);
        grid.appendChild(card);
    });
}
renderSpreads();

// 选择牌阵
function selectSpread(key, element) {
    selectedSpread = key;
    document.querySelectorAll('.spread-card').forEach(c => c.classList.remove('selected'));
    element.classList.add('selected');
    document.getElementById('nextToQuestion').disabled = false;
}

// 下一步到问题输入
document.getElementById('nextToQuestion').onclick = () => {
    document.getElementById('spreadSection').style.display = 'none';
    document.getElementById('questionSection').style.display = 'block';
    document.getElementById('step1').classList.remove('active');
    document.getElementById('step2').classList.add('active');
};

// 返回牌阵选择
document.getElementById('backToSpread').onclick = () => {
    document.getElementById('questionSection').style.display = 'none';
    document.getElementById('spreadSection').style.display = 'block';
    document.getElementById('step2').classList.remove('active');
    document.getElementById('step1').classList.add('active');
};

// 开始抽牌
document.getElementById('startDrawing').onclick = () => {
    const question = document.getElementById('questionInput').value;

    document.getElementById('questionSection').style.display = 'none';
    document.getElementById('drawingSection').style.display = 'block';
    document.getElementById('step2').classList.remove('active');
    document.getElementById('step3').classList.add('active');

    // 调用抽牌API
    fetch('/api/draw', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ spread_type: selectedSpread, question: question })
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            setTimeout(() => showResult(data, question), 2000);
        } else {
            alert('抽牌失败，请重试');
            location.reload();
        }
    })
    .catch(err => {
        console.error(err);
        alert('抽牌失败，请重试');
        location.reload();
    });
};

// 显示结果
function showResult(data, question) {
    document.getElementById('drawingSection').style.display = 'none';
    document.getElementById('resultSection').style.display = 'block';
    document.getElementById('step3').classList.remove('active');
    document.getElementById('step4').classList.add('active');

    document.getElementById('resultQuestion').textContent = question || "通用占卜 - 未指定问题";

    const cardsDisplay = document.getElementById('cardsDisplay');
    cardsDisplay.innerHTML = '';

    // 塔罗元素符号映射
    const getElementSymbol = (cardName) => {
        if (cardName.includes('权杖')) return '▴';
        if (cardName.includes('圣杯')) return '▾';
        if (cardName.includes('宝剑')) return '▸';
        if (cardName.includes('星币')) return '◊';
        return '✧';
    };

    data.cards.forEach((card, index) => {
        const cardEl = document.createElement('div');
        cardEl.className = 'tarot-card';
        const elementSymbol = getElementSymbol(card.name);
        const statusText = card.is_reversed ? '↻ 逆位' : '✧ 正位';
        
        cardEl.innerHTML = `
            <div class="card-corner top-left">${elementSymbol}</div>
            <div class="card-corner top-right">${elementSymbol}</div>
            <div class="card-position">${card.position}</div>
            <div class="card-divider"></div>
            <div class="card-name">${card.name}</div>
            <div class="card-status">${statusText}</div>
            <div class="card-divider"></div>
            <div class="card-meaning">${card.is_reversed ? card.reversed || card.meaning : card.meaning}</div>
            <div class="card-corner bottom-left">${elementSymbol}</div>
            <div class="card-corner bottom-right">${elementSymbol}</div>
        `;
        cardsDisplay.appendChild(cardEl);
    });

    document.getElementById('reading').textContent = data.reading;
}
