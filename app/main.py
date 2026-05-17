"""
塔罗牌占卜系统 - FastAPI主入口
"""
import random
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from .tarot_cards import ALL_CARDS, SPREADS
from .interpretation import generate_reading

app = FastAPI(title="塔罗牌占卜系统", description="78张韦特塔罗 + 12种牌阵 + 深度解读")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/api/health")
async def health():
    """健康检查"""
    return {"status": "ok", "message": "🎴 塔罗牌占卜系统运行正常"}


@app.get("/api/spreads")
async def get_spreads():
    """获取所有可用牌阵"""
    return {"success": True, "data": SPREADS}


@app.get("/api/cards")
async def get_cards():
    """获取所有塔罗牌"""
    return {"success": True, "total": len(ALL_CARDS), "data": ALL_CARDS}


@app.post("/api/draw")
async def draw_cards(request: Request):
    """
    抽牌接口
    请求参数：spread_type, question
    """
    try:
        data = await request.json()
        spread_type = data.get("spread_type", "three_card")
        question = data.get("question", "")

        if spread_type not in SPREADS:
            return {"success": False, "error": "未知牌阵类型"}

        spread = SPREADS[spread_type]
        card_count = spread["cards"]
        positions = spread["positions"]

        # 随机抽牌
        selected_indices = random.sample(range(len(ALL_CARDS)), card_count)
        drawn_cards = []

        for i, idx in enumerate(selected_indices):
            card = ALL_CARDS[idx].copy()
            # 50%概率逆位（仅文字标注，卡片不翻转）
            is_reversed = random.random() < 0.5
            card["is_reversed"] = is_reversed
            card["position"] = positions[i]
            card["position_index"] = i
            drawn_cards.append(card)

        # 生成深度解读
        interpretation = generate_reading(drawn_cards, spread["name"], question)

        return {
            "success": True,
            "spread_name": spread["name"],
            "spread_description": spread["description"],
            "question": question,
            "cards": drawn_cards,
            "reading": interpretation,
            "draw_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    except Exception as e:
        return {"success": False, "error": str(e)}


@app.get("/", response_class=HTMLResponse)
async def index():
    """主页"""
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()


from datetime import datetime

if __name__ == "__main__":
    print("🎴 塔罗牌占卜系统启动中...")
    print("📱 访问地址：http://localhost:9999")
    print("="*60)
    uvicorn.run(app, host="0.0.0.0", port=9999)
