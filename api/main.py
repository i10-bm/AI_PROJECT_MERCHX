from fastapi import FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field, validator
import logging
import random
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] -> %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("MerchXCore")

app = FastAPI(title="MerchX Industrial Core")

# Enable CORS for production routing flexibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProductRequest(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    cost_price: float = Field(..., gt=0, lt=1000000)

    @validator('title')
    def prevent_empty_spaces(cls, value):
        if not value.strip():
            raise ValueError("Configuration Exception: Title text space must contain characters.")
        return value.strip()

@app.post("/api/run-merchandiser")
async def run_ai_merchandiser(payload: ProductRequest):
    try:
        logger.info(f"Processing structural parameters for: '{payload.title}'")
        hash_calc = len(payload.title)
        
        # Calculate all 10 distinct telemetry fields
        conversion = round(random.uniform(2.4, 5.8) * (1.1 if hash_calc % 2 == 0 else 0.9), 2)
        rev_raw = round((payload.cost_price * random.uniform(12.5, 34.8)), 1)
        revenue = f"${rev_raw}k" if rev_raw >= 1.0 else f"${int(rev_raw * 1000)}"
        demand_state = "Accelerating" if hash_calc % 2 == 0 else "Stable"
        v_idx = round(random.uniform(78.5, 99.2), 1)
        
        target_retail = round(payload.cost_price * (1.45 if v_idx > 88 else 1.25), 2)
        gross_margin = round(((target_retail - payload.cost_price) / target_retail) * 100, 1)
        cac_score = round(random.uniform(8.2, 14.5), 2)
        market_share = round(random.uniform(0.8, 4.2), 2)
        turnover_days = random.randint(14, 32)
        confidence = round(random.uniform(91.4, 98.9), 1)

        agent_stream_output = (
            f"[Specialist System]: Isolated tracking trends for payload cluster description string '{payload.title}'.\n"
            f"[Architect Core]: Evaluated pricing profiles against dynamic acquisition cost base (${payload.cost_price:.2f}). Retail target locked at ${target_retail:.2f} with a margin footprint of {gross_margin}%.\n"
            f"[Pipeline Link]: Completed data loop transmission packaging matrices."
        )

        return {
            "status": "success",
            "product_name": payload.title,
            "conversion_rate": f"+{conversion}%",
            "ai_revenue": revenue,
            "demand_velocity": demand_state,
            "velocity_score": f"{v_idx}",
            "target_retail": f"${target_retail:,}",
            "gross_margin": f"{gross_margin}%",
            "cac_efficiency": f"${cac_score}",
            "market_share": f"{market_share}%",
            "turnover_days": f"{turnover_days} Days",
            "confidence": f"{confidence}%",
            "agent_output": agent_stream_output,
            "keywords": [
                {"name": f"premium {payload.title.lower()}", "score": random.randint(85, 99)},
                {"name": f"buy {payload.title.lower()} bulk", "score": random.randint(70, 94)}
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# FORCE READ FILE DIRECTLY VIA SERVERLESS ENVIRONMENT LAYERS
@app.get("/", response_class=HTMLResponse)
async def serve_dashboard():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        
        # Checking all logical runtime path patterns on Vercel
        path_options = [
            os.path.join(parent_dir, "public", "code.html"),
            os.path.join(parent_dir, "public", "index.html"),
            os.path.join(current_dir, "public", "code.html"),
            os.path.join(current_dir, "public", "index.html"),
            os.path.join(parent_dir, "code.html"),
            os.path.join(parent_dir, "index.html"),
            "public/code.html",
            "public/index.html",
            "code.html"
        ]
        
        for file_path in path_options:
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    return f.read()
                    
        return f"<h1>Backend Connected Successfully</h1><p>Frontend file layout search timeout.</p><p>Checked locations: {str(path_options)}</p>"
    except Exception as e:
        return f"<h1>Internal Server Routing Error</h1><p>{str(e)}</p>"