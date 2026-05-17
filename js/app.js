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
                <span>📍 ${spread.positions}个位置</span>
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

// 生成粒子特效
function createParticles() {
    const container = document.getElementById('particlesContainer');
    for (let i = 0; i < 30; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        particle.style.animationDelay = Math.random() * 3 + 's';
        particle.style.animationDuration = (2 + Math.random() * 2) + 's';
        container.appendChild(particle);
    }
    
    // 添加星光
    for (let i = 0; i < 10; i++) {
        const star = document.createElement('div');
        star.className = 'star-sparkle';
        star.textContent = '✧';
        star.style.left = (10 + Math.random() * 80) + '%';
        star.style.top = (10 + Math.random() * 80) + '%';
        star.style.animationDelay = Math.random() * 2 + 's';
        container.appendChild(star);
    }
}

// 抽牌飞行动画
function createFlyingCard() {
    const container = document.getElementById('drawingContainer');
    const card = document.createElement('div');
    card.className = 'flying-card tarot-card-back';
    container.appendChild(card);
    
    setTimeout(() => {
        card.remove();
    }, 1500);
}

// 闪光特效
function createFlash(element) {
    const flash = document.createElement('div');
    flash.className = 'card-flash';
    element.appendChild(flash);
    setTimeout(() => flash.remove(), 800);
}

// 解析 Coze 流式响应
function parseCozeStreamResponse(text) {
    const lines = text.split('\n');
    let fullContent = '';
    let isReadingMode = false;
    
    for (const line of lines) {
        if (line.startsWith('data:')) {
            try {
                const data = JSON.parse(line.slice(5));
                if (data.content) {
                    fullContent += data.content;
                }
            } catch (e) {
                // 忽略解析错误
            }
        }
    }
    
    return fullContent;
}

// 从 Coze 响应中提取 JSON
function extractJsonFromResponse(text) {
    // 尝试提取 Markdown 代码块中的 JSON
    const jsonMatch = text.match(/```(?:json)?\s*([\s\S]*?)\s*```/);
    if (jsonMatch) {
        try {
            return JSON.parse(jsonMatch[1]);
        } catch (e) {
            console.error('JSON parse error from code block:', e);
        }
    }
    
    // 尝试直接解析整个响应为 JSON
    try {
        return JSON.parse(text);
    } catch (e) {
        console.error('Direct JSON parse error:', e);
    }
    
    // 尝试提取文本中的 JSON 对象
    const bracketMatch = text.match(/\{[\s\S]*\}/);
    if (bracketMatch) {
        try {
            return JSON.parse(bracketMatch[0]);
        } catch (e) {
            console.error('Bracket JSON parse error:', e);
        }
    }
    
    return null;
}

// 开始抽牌 - 调用 Coze Bot API
document.getElementById('startDrawing').onclick = async () => {
    const question = document.getElementById('questionInput').value;
    const spreadConfig = spreads[selectedSpread];
    
    document.getElementById('questionSection').style.display = 'none';
    document.getElementById('drawingSection').style.display = 'block';
    document.getElementById('step2').classList.remove('active');
    document.getElementById('step3').classList.add('active');

    // 创建粒子特效
    createParticles();
    
    // 开始洗牌动画
    const drawingSection = document.getElementById('drawingSection');
    drawingSection.classList.add('shuffling');
    
    // 动态更新提示文字
    const drawingText = document.getElementById('drawingText');
    const messages = [
        '正在连接宇宙能量，请静心等待...',
        '✨ 洗牌中...',
        '🔮 感知你的能量...',
        '🌟 抽取命运之牌...',
        '✧ 解读中...'
    ];
    
    let messageIndex = 0;
    const messageInterval = setInterval(() => {
        messageIndex++;
        if (messageIndex < messages.length) {
            drawingText.textContent = messages[messageIndex];
        }
    }, 800);
    
    // 每隔一段时间执行抽牌飞行动画
    const flyInterval = setInterval(createFlyingCard, 600);

    try {
        // 调用 Coze Bot Webhook API
        const response = await fetch(COZE_CONFIG.WEBHOOK_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${COZE_CONFIG.BEARER_TOKEN}`
            },
            body: JSON.stringify({
                spread_type: selectedSpread,
                card_count: spreadConfig.cards,
                question: question || "通用占卜",
                timestamp: Date.now()
            })
        });

        if (!response.ok) {
            throw new Error(`API request failed: ${response.status}`);
        }

        const responseText = await response.text();
        const result = extractJsonFromResponse(responseText);

        clearInterval(messageInterval);
        clearInterval(flyInterval);
        drawingSection.classList.remove('shuffling');
        
        if (result && result.success) {
            setTimeout(() => showResult(result, question), 500);
        } else {
            throw new Error(result?.error || '抽牌结果解析失败');
        }
    } catch (err) {
        console.error('抽牌错误:', err);
        clearInterval(messageInterval);
        clearInterval(flyInterval);
        drawingSection.classList.remove('shuffling');
        alert(`抽牌失败: ${err.message || '请重试'}`);
        location.reload();
    }
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
        cardEl.style.animationDelay = (index * 0.3) + 's';
        
        const elementSymbol = getElementSymbol(card.name);
        const isReversed = card.position === '逆位' || card.is_reversed;
        const statusText = isReversed ? '↻ 逆位' : '✧ 正位';
        
        cardEl.innerHTML = `
            <div class="card-corner top-left">${elementSymbol}</div>
            <div class="card-corner top-right">${elementSymbol}</div>
            <div class="card-position">${card.position_name || card.position || '未知位置'}</div>
            <div class="card-divider"></div>
            <div class="card-name">${card.name}</div>
            <div class="card-status">${statusText}</div>
            <div class="card-divider"></div>
            <div class="card-meaning">${card.meaning || '塔罗牌的神秘寓意'}</div>
            <div class="card-corner bottom-left">${elementSymbol}</div>
            <div class="card-corner bottom-right">${elementSymbol}</div>
        `;
        
        cardsDisplay.appendChild(cardEl);
        
        // 为每张牌添加翻开时的闪光特效
        setTimeout(() => {
            createFlash(cardEl);
        }, 800 + index * 300);
    });

    // 解读文字延迟显示 - 使用 marked 解析 Markdown
    setTimeout(() => {
        document.getElementById('reading').innerHTML = marked.parse(data.reading);
    }, data.cards.length * 300 + 500);
}
