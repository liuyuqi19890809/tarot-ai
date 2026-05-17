// 塔罗牌图片映射 - 包含完整的78张牌
// 使用SVG占位符生成牌面图片，后续可替换为真实图片

const cardImages = {
    // 大阿卡纳 - 22张
    '愚者': '00_fool',
    '魔术师': '01_magician',
    '女祭司': '02_high_priestess',
    '女皇': '03_empress',
    '皇帝': '04_emperor',
    '教皇': '05_hierophant',
    '恋人': '06_lovers',
    '战车': '07_chariot',
    '力量': '08_strength',
    '隐士': '09_hermit',
    '命运之轮': '10_wheel_of_fortune',
    '正义': '11_justice',
    '倒吊人': '12_hanged_man',
    '死神': '13_death',
    '节制': '14_temperance',
    '恶魔': '15_devil',
    '塔': '16_tower',
    '星星': '17_star',
    '月亮': '18_moon',
    '太阳': '19_sun',
    '审判': '20_judgement',
    '世界': '21_world',
    
    // 权杖 - 14张
    '权杖Ace': 'wands_ace',
    '权杖2': 'wands_02',
    '权杖3': 'wands_03',
    '权杖4': 'wands_04',
    '权杖5': 'wands_05',
    '权杖6': 'wands_06',
    '权杖7': 'wands_07',
    '权杖8': 'wands_08',
    '权杖9': 'wands_09',
    '权杖10': 'wands_10',
    '权杖侍从': 'wands_page',
    '权杖骑士': 'wands_knight',
    '权杖王后': 'wands_queen',
    '权杖国王': 'wands_king',
    
    // 圣杯 - 14张
    '圣杯Ace': 'cups_ace',
    '圣杯2': 'cups_02',
    '圣杯3': 'cups_03',
    '圣杯4': 'cups_04',
    '圣杯5': 'cups_05',
    '圣杯6': 'cups_06',
    '圣杯7': 'cups_07',
    '圣杯8': 'cups_08',
    '圣杯9': 'cups_09',
    '圣杯10': 'cups_10',
    '圣杯侍从': 'cups_page',
    '圣杯骑士': 'cups_knight',
    '圣杯王后': 'cups_queen',
    '圣杯国王': 'cups_king',
    
    // 宝剑 - 14张
    '宝剑Ace': 'swords_ace',
    '宝剑2': 'swords_02',
    '宝剑3': 'swords_03',
    '宝剑4': 'swords_04',
    '宝剑5': 'swords_05',
    '宝剑6': 'swords_06',
    '宝剑7': 'swords_07',
    '宝剑8': 'swords_08',
    '宝剑9': 'swords_09',
    '宝剑10': 'swords_10',
    '宝剑侍从': 'swords_page',
    '宝剑骑士': 'swords_knight',
    '宝剑王后': 'swords_queen',
    '宝剑国王': 'swords_king',
    
    // 星币 - 14张
    '星币Ace': 'pentacles_ace',
    '星币2': 'pentacles_02',
    '星币3': 'pentacles_03',
    '星币4': 'pentacles_04',
    '星币5': 'pentacles_05',
    '星币6': 'pentacles_06',
    '星币7': 'pentacles_07',
    '星币8': 'pentacles_08',
    '星币9': 'pentacles_09',
    '星币10': 'pentacles_10',
    '星币侍从': 'pentacles_page',
    '星币骑士': 'pentacles_knight',
    '星币王后': 'pentacles_queen',
    '星币国王': 'pentacles_king'
};

// 获取牌面元素符号
function getCardElement(cardName) {
    if (cardName.includes('权杖')) return { symbol: '🔥', color: '#e74c3c', name: '火' };
    if (cardName.includes('圣杯')) return { symbol: '💧', color: '#3498db', name: '水' };
    if (cardName.includes('宝剑')) return { symbol: '💨', color: '#f39c12', name: '风' };
    if (cardName.includes('星币')) return { symbol: '🌍', color: '#27ae60', name: '土' };
    
    // 大阿卡纳元素映射
    const majorElements = {
        '愚者': { symbol: '✨', color: '#9b59b6', name: '风' },
        '魔术师': { symbol: '✨', color: '#f39c12', name: '风' },
        '女祭司': { symbol: '🌙', color: '#3498db', name: '水' },
        '女皇': { symbol: '🌍', color: '#27ae60', name: '土' },
        '皇帝': { symbol: '🔥', color: '#e74c3c', name: '火' },
        '教皇': { symbol: '🌍', color: '#27ae60', name: '土' },
        '恋人': { symbol: '💧', color: '#3498db', name: '水' },
        '战车': { symbol: '💨', color: '#f39c12', name: '风' },
        '力量': { symbol: '🔥', color: '#e74c3c', name: '火' },
        '隐士': { symbol: '🌍', color: '#27ae60', name: '土' },
        '命运之轮': { symbol: '✨', color: '#9b59b6', name: '综合' },
        '正义': { symbol: '💨', color: '#f39c12', name: '风' },
        '倒吊人': { symbol: '💧', color: '#3498db', name: '水' },
        '死神': { symbol: '💧', color: '#3498db', name: '水' },
        '节制': { symbol: '🔥', color: '#e74c3c', name: '火' },
        '恶魔': { symbol: '🌍', color: '#27ae60', name: '土' },
        '塔': { symbol: '🔥', color: '#e74c3c', name: '火' },
        '星星': { symbol: '💧', color: '#3498db', name: '水' },
        '月亮': { symbol: '💧', color: '#3498db', name: '水' },
        '太阳': { symbol: '🔥', color: '#e74c3c', name: '火' },
        '审判': { symbol: '🔥', color: '#e74c3c', name: '火' },
        '世界': { symbol: '✨', color: '#9b59b6', name: '综合' }
    };
    
    return majorElements[cardName] || { symbol: '✧', color: '#d4af37', name: '未知' };
}

// 生成SVG牌面（当图片不存在时使用）
function generateCardSVG(cardName) {
    const element = getCardElement(cardName);
    const isMajor = !cardName.includes('权杖') && !cardName.includes('圣杯') && 
                    !cardName.includes('宝剑') && !cardName.includes('星币');
    
    const svgContent = `
    <svg viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <linearGradient id="cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#1a1a2e;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#16213e;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="borderGold" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#d4af37" />
                <stop offset="50%" style="stop-color:#f4e4bc" />
                <stop offset="100%" style="stop-color:#d4af37" />
            </linearGradient>
        </defs>
        
        <!-- 背景 -->
        <rect width="200" height="320" rx="12" fill="url(#cardBg)"/>
        
        <!-- 边框 -->
        <rect x="3" y="3" width="194" height="314" rx="10" fill="none" 
              stroke="url(#borderGold)" stroke-width="3"/>
        <rect x="8" y="8" width="184" height="304" rx="8" fill="none" 
              stroke="${element.color}" stroke-width="1" opacity="0.5"/>
        
        <!-- 装饰角落 -->
        <text x="15" y="30" font-size="20" fill="#d4af37" opacity="0.8">✧</text>
        <text x="170" y="30" font-size="20" fill="#d4af37" opacity="0.8">✧</text>
        <text x="15" y="310" font-size="20" fill="#d4af37" opacity="0.8">✧</text>
        <text x="170" y="310" font-size="20" fill="#d4af37" opacity="0.8">✧</text>
        
        <!-- 中心大符号 -->
        <text x="100" y="180" font-size="80" text-anchor="middle" 
              fill="${element.color}" opacity="0.9">${element.symbol}</text>
        
        <!-- 牌名 -->
        <text x="100" y="260" font-size="16" font-weight="bold" text-anchor="middle" 
              fill="#fff" font-family="serif">${cardName}</text>
        
        <!-- 元素标签 -->
        <text x="100" y="290" font-size="12" text-anchor="middle" 
              fill="${element.color}" opacity="0.8">${isMajor ? '大阿卡纳' : element.name + '元素'}</text>
    </svg>
    `;
    
    return 'data:image/svg+xml;base64,' + btoa(unescape(encodeURIComponent(svgContent)));
}
