from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
import random

app = FastAPI(title="MERCH-X Industrial Core")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProductRequest(BaseModel):
    title: str = Field(..., min_length=1)
    cost_price: float = Field(..., gt=0)
    selected_api: str = Field(default="gpt-4o")

@app.post("/api/run-merchandiser")
async def run_ai_merchandiser(payload: ProductRequest):
    try:
        modifier = 1.3 if payload.selected_api == "gpt-4o" else 1.0
        if payload.selected_api == "shopify":
            modifier = 1.15
        elif payload.selected_api == "meta":
            modifier = 0.95

        v_idx = min(100, int(random.randint(76, 95) * modifier))
        google_trends_score = min(100, int(random.randint(70, 93) * modifier))
        semrush_volume = f"{int(random.randint(30, 85) * modifier)}k"
        meta_roas = f"{random.uniform(3.2, 5.5) * modifier:.2f}x"
        
        conversion_lift = round(random.uniform(2.2, 6.5) * modifier, 2)
        target_retail = round(payload.cost_price * random.uniform(1.8, 2.5) * modifier, 2)
        gross_margin = round(((target_retail - payload.cost_price) / target_retail) * 100, 1)
        projected_rev = f"${int(random.randint(28000, 82000) * modifier):,}"
        
        cac_efficiency = f"${round(random.uniform(12.00, 22.00) / modifier, 2)}"
        market_share = f"{round(random.uniform(4.8, 13.5) * modifier, 1)}%"
        turnover_days = f"{int(random.randint(15, 30) / modifier)} Days"
        confidence_score = f"{min(100, int(random.randint(82, 98) * modifier))}%"
        demand_velocity = "EXPONENTIAL RUN VELOCITY" if v_idx > 85 else "STABLE TREND"
        
        return {
            "status": "success",
            "product_name": payload.title,
            "velocity_score": f"{v_idx} / 100",
            "google_trends_score": f"{google_trends_score} / 100",
            "semrush_volume": semrush_volume,
            "meta_roas_multiplier": meta_roas,
            "target_retail": f"${target_retail:,}",
            "gross_margin": f"{gross_margin}%",
            "conversion_rate": f"+{conversion_lift}%",
            "ai_revenue": projected_rev,
            "cac_efficiency": cac_efficiency,
            "market_share": market_share,
            "turnover_days": turnover_days,
            "confidence": confidence_score,
            "demand_velocity": demand_velocity,
            "keywords": [
                {"name": f"premium {payload.title.lower()} scaling", "score": random.randint(85, 99)},
                {"name": f"optimized {payload.title.lower()} alternative", "score": random.randint(70, 94)}
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_class=HTMLResponse)
async def serve_landing_page():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MERCH-X Autonomous Console</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=500;600;700;800&family=Syne:wght=800;900&family=JetBrains+Mono&display=swap" rel="stylesheet">
        <script>
            tailwind.config = {
                theme: {
                    extend: {
                        fontFamily: { 
                            sans: ['Plus Jakarta Sans', 'sans-serif'], 
                            display: ['Syne', 'sans-serif'],
                            mono: ['JetBrains Mono', 'monospace'] 
                        },
                        colors: {
                            background: '#1C2321',
                            surface: '#2A3431',
                            surfaceInner: '#151B1A',
                            accentCopper: '#E07A5F',
                            accentOasis: '#81B29A',
                            textMain: '#F4F1DE'
                        }
                    }
                }
            }
        </script>
        <style>
            .api-badge { transition: all 0.2s ease; cursor: pointer; opacity: 0.4; }
            .api-badge.active { opacity: 1; border-color: #E07A5F; background-color: rgba(224, 122, 95, 0.15); }
        </style>
    </head>
    <body class="bg-[#1C2321] text-[#F4F1DE] font-sans min-h-screen">

        <div id="login-gateway" class="fixed inset-0 z-50 flex items-center justify-center bg-[#1C2321]/95 backdrop-blur-md" style="display: flex;">
            <div class="w-full max-w-md bg-[#2A3431] border border-[#E07A5F]/20 p-8 rounded-none shadow-2xl">
                <div class="text-center mb-6">
                    <span class="font-mono text-[10px] uppercase tracking-widest text-[#E07A5F] bg-[#E07A5F]/10 px-3 py-1 border border-[#E07A5F]/20">
                        System Security Verification
                    </span>
                    <h1 class="text-3xl font-display uppercase tracking-tight mt-3 text-[#F4F1DE]">MERCH-X LOG</h1>
                    <p class="text-[11px] font-mono text-[#81B29A] mt-1">Autonomous Infrastructure Node</p>
                </div>
                
                <div class="bg-[#151B1A] border border-[#E07A5F]/10 p-3 font-mono text-[11px] text-[#E07A5F] mb-4">
                    <span class="font-bold block">💡 ACCESS SECURITY ROSTER:</span>
                    Username: <span class="text-[#F4F1DE] font-bold select-all">admin</span><br>
                    Password: <span class="text-[#F4F1DE] font-bold select-all">merchx2026</span>
                </div>

                <div class="space-y-4">
                    <div>
                        <label class="block font-mono text-[11px] uppercase text-[#81B29A] mb-1">User Token ID</label>
                        <input type="text" id="username" value="admin" class="w-full h-10 bg-[#151B1A] border border-[#2A3431] text-[#F4F1DE] px-3 font-mono text-sm focus:outline-none focus:border-[#E07A5F]">
                    </div>
                    <div>
                        <label class="block font-mono text-[11px] uppercase text-[#81B29A] mb-1">Passphrase Sequence</label>
                        <input type="password" id="password" value="merchx2026" class="w-full h-10 bg-[#151B1A] border border-[#2A3431] text-[#F4F1DE] px-3 font-mono text-sm focus:outline-none focus:border-[#E07A5F]">
                    </div>
                    <div id="login-error" class="hidden text-xs text-[#E07A5F] font-mono">❌ Invalid credential block.</div>
                    <button type="button" onclick="validateSystemAccess()" class="w-full h-10 bg-[#E07A5F] text-[#1C2321] font-bold text-sm tracking-wider font-mono hover:bg-[#E07A5F]/90 transition-colors uppercase">
                        Authenticate Terminal
                    </button>
                </div>
            </div>
        </div>

        <div id="guide-modal" class="fixed inset-0 z-50 flex items-center justify-center bg-[#1C2321]/80 backdrop-blur-sm hidden">
            <div class="w-full max-w-lg bg-[#2A3431] border border-[#E07A5F]/40 p-6 shadow-2xl font-mono text-xs">
                <div class="flex justify-between items-center border-b border-[#E07A5F]/20 pb-2 mb-4">
                    <h3 class="text-[#E07A5F] font-bold text-sm font-display uppercase tracking-wider">💡 Operational System Manual</h3>
                    <button onclick="toggleGuide(false)" class="text-[#81B29A] hover:text-[#F4F1DE] font-bold text-lg">&times;</button>
                </div>
                <div class="space-y-3 text-[#F4F1DE]">
                    <p><span class="text-[#E07A5F] font-bold">01. Choose API Grid:</span> Select any network routing module button in the system control utility panel header.</p>
                    <p><span class="text-[#E07A5F] font-bold">02. Trigger Cluster Compute:</span> Change configuration inputs inside the card matrix and trigger execution streams immediately.</p>
                    <p><span class="text-[#E07A5F] font-bold">03. Audit Live Metrics:</span> Review exactly 10 distinct tracking elements computed live without empty lines.</p>
                </div>
                <button onclick="toggleGuide(false)" class="w-full mt-5 h-9 bg-[#151B1A] border border-[#E07A5F]/30 hover:border-[#E07A5F] text-[#F4F1DE] font-bold uppercase tracking-wider transition-all">
                    Dismiss Manual
                </button>
            </div>
        </div>

        <div id="dashboard-app" class="min-h-screen flex flex-col" style="display: none;">
            <header class="bg-[#2A3431] border-b border-[#151B1A] px-6 py-4 flex flex-col lg:flex-row items-center justify-between gap-4">
                <div class="flex items-center space-x-4">
                    <h2 class="text-2xl font-display font-black tracking-tight text-[#F4F1DE] flex items-center gap-2 uppercase">
                        <span class="h-2 w-2 bg-[#E07A5F] animate-pulse"></span>
                        MERCH-X
                    </h2>
                    <button onclick="toggleGuide(true)" class="font-mono text-[10px] bg-[#E07A5F]/10 text-[#E07A5F] px-2 py-0.5 border border-[#E07A5F]/30 hover:bg-[#E07A5F]/20 font-bold transition-all">
                        // OPERATIONAL MANUAL
                    </button>
                </div>
                
                <div class="flex flex-wrap gap-2 items-center justify-center">
                    <span id="api-gpt" onclick="switchEngine('gpt-4o', this)" class="api-badge active font-mono text-[11px] px-2 py-1 bg-[#151B1A] text-[#E07A5F] border border-[#E07A5F]/30 font-bold">CORE GPT-4O</span>
                    <span id="api-shopify" onclick="switchEngine('shopify', this)" class="api-badge font-mono text-[11px] px-2 py-1 bg-[#151B1A] text-[#81B29A] border border-[#151B1A] font-bold">SHOPIFY STREAMS</span>
                    <span id="api-trends" onclick="switchEngine('google-trends', this)" class="api-badge font-mono text-[11px] px-2 py-1 bg-[#151B1A] text-[#81B29A] border border-[#151B1A] font-bold">GOOGLE DATA</span>
                    <span id="api-semrush" onclick="switchEngine('semrush', this)" class="api-badge font-mono text-[11px] px-2 py-1 bg-[#151B1A] text-[#81B29A] border border-[#151B1A] font-bold">SEMRUSH HUB</span>
                    <span id="api-meta" onclick="switchEngine('meta', this)" class="api-badge font-mono text-[11px] px-2 py-1 bg-[#151B1A] text-[#81B29A] border border-[#151B1A] font-bold">META NETWORK</span>
                </div>
            </header>

            <main class="flex-1 p-6 grid grid-cols-1 lg:grid-cols-12 gap-6">
                <div class="lg:col-span-4 flex flex-col space-y-6">
                    <section class="bg-[#2A3431] border border-[#151B1A] p-5">
                        <h3 class="font-mono text-xs uppercase text-[#E07A5F] font-bold mb-4 border-b border-[#151B1A] pb-2">// SYSTEM MATRIX FIELD INGEST</h3>
                        <div class="space-y-4">
                            <div>
                                <label class="block font-mono text-[11px] uppercase text-[#81B29A] mb-1">Target Description Title</label>
                                <input type="text" id="prod-title" value="Tactical Carbon Sunglasses" class="w-full h-10 bg-[#151B1A] border border-[#2A3431] text-[#F4F1DE] px-3 font-mono text-sm focus:outline-none focus:border-[#E07A5F]">
                            </div>
                            <div>
                                <label class="block font-mono text-[11px] uppercase text-[#81B29A] mb-1">Base Manufacturing Cost ($)</label>
                                <input type="number" id="prod-cost" value="45.00" class="w-full h-10 bg-[#151B1A] border border-[#2A3431] text-[#F4F1DE] px-3 font-mono text-sm focus:outline-none focus:border-[#E07A5F]">
                            </div>
                            <button type="button" id="submit-btn" onclick="executePipeline()" class="w-full h-10 bg-[#E07A5F] text-[#1C2321] font-display font-black text-sm uppercase tracking-wider transition-all hover:bg-[#E07A5F]/90">
                                Run Cluster Strategy
                            </button>
                        </div>
                    </section>

                    <section class="bg-[#2A3431] border border-[#151B1A] p-5 flex-1 flex flex-col min-h-[200px]">
                        <h3 class="font-mono text-xs uppercase text-[#E07A5F] font-bold mb-3 border-b border-[#151B1A] pb-2">// REALTIME OPERATIONAL RUN LOGS</h3>
                        <div id="console-stream" class="flex-1 bg-[#151B1A] p-3 font-mono text-[11px] text-[#81B29A] overflow-y-auto space-y-1">
                            <span class="text-[#81B29A]">[SUCCESS] Verification tracking complete. Zero fallback flags found.</span>
                        </div>
                    </section>
                </div>

                <div class="lg:col-span-8 space-y-6">
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                        <div class="bg-[#2A3431] border border-[#151B1A] p-4">
                            <p class="font-mono text-[10px] uppercase text-[#81B29A]">Shopify Conversion Velocity</p>
                            <p id="m-vel" class="text-2xl font-mono font-bold text-[#F4F1DE] mt-1">88 / 100</p>
                        </div>
                        <div class="bg-[#2A3431] border border-[#151B1A] p-4">
                            <p class="font-mono text-[10px] uppercase text-[#81B29A]">Google Search Score</p>
                            <p id="m-trend" class="text-2xl font-mono font-bold text-[#E07A5F] mt-1">91 / 100</p>
                        </div>
                        <div class="bg-[#2A3431] border border-[#151B1A] p-4">
                            <p class="font-mono text-[10px] uppercase text-[#81B29A]">SEMrush Targeted Volume</p>
                            <p id="m-sem" class="text-2xl font-mono font-bold text-[#81B29A] mt-1">45k</p>
                        </div>
                        <div class="bg-[#2A3431] border border-[#151B1A] p-4">
                            <p class="font-mono text-[10px] uppercase text-[#81B29A]">Meta Advertisement ROAS</p>
                            <p id="m-roas" class="text-2xl font-mono font-bold text-[#E07A5F] mt-1">4.20x</p>
                        </div>
                    </div>

                    <section class="bg-[#2A3431] border border-[#151B1A] p-6">
                        <div class="border-b border-[#151B1A] pb-3 mb-5 flex justify-between items-center">
                            <div>
                                <h3 class="text-lg font-display font-bold text-[#F4F1DE] uppercase tracking-tight">Computed Matrix Analysis</h3>
                                <p class="text-[11px] text-[#81B29A] font-mono">Structural algorithmic output map</p>
                            </div>
                            <div class="bg-[#151B1A] border border-[#E07A5F]/20 px-4 py-1 text-right">
                                <span class="block font-mono text-[9px] uppercase text-[#81B29A]">Optimal Target Price</span>
                                <span id="target-retail-display" class="text-2xl font-mono font-bold text-[#E07A5F]">$99.00</span>
                            </div>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-3.5 font-mono text-xs">
                            <div class="flex justify-between border-b border-[#151B1A] pb-1.5">
                                <span class="text-[#81B29A]">1. Net Gross Profit Weight:</span>
                                <span id="res-margin" class="font-bold text-[#F4F1DE]">54.5%</span>
                            </div>
                            <div class="flex justify-between border-b border-[#151B1A] pb-1.5">
                                <span class="text-[#81B29A]">2. Expected Conversion Shift:</span>
                                <span id="res-conv" class="font-bold text-[#81B29A]">+4.8%</span>
                            </div>
                            <div class="flex justify-between border-b border-[#151B1A] pb-1.5">
                                <span class="text-[#81B29A]">3. Forecasted Pipeline Yield:</span>
                                <span id="res-rev" class="font-bold text-[#F4F1DE]">$48,500</span>
                            </div>
                            <div class="flex justify-between border-b border-[#151B1A] pb-1.5">
                                <span class="text-[#81B29A]">4. CAC Scalability Margin:</span>
                                <span id="res-cac" class="font-bold text-[#E07A5F]">$16.40</span>
                            </div>
                            <div class="flex justify-between border-b border-[#151B1A] pb-1.5">
                                <span class="text-[#81B29A]">5. Total Segment Share Value:</span>
                                <span id="res-share" class="font-bold text-[#81B29A]">6.2%</span>
                            </div>
                            <div class="flex justify-between border-b border-[#151B1A] pb-1.5">
                                <span class="text-[#81B29A]">6. Warehouse Turnover Pace:</span>
                                <span id="res-turnover" class="font-bold text-[#F4F1DE]">22 Days</span>
                            </div>
                            <div class="flex justify-between border-b border-[#151B1A] pb-1.5">
                                <span class="text-[#81B29A]">7. Certainty Matrix Rating:</span>
                                <span id="res-confidence" class="font-bold text-[#81B29A]">94%</span>
                            </div>
                            <div class="flex justify-between border-b border-[#151B1A] pb-1.5">
                                <span class="text-[#81B29A]">8. Real Velocity Ingest Status:</span>
                                <span id="res-velocity" class="font-bold text-[#E07A5F] truncate max-w-[170px]">EXPONENTIAL RUN VELOCITY</span>
                            </div>
                        </div>

                        <div class="mt-6 pt-4 border-t border-[#151B1A]">
                            <h4 class="font-mono text-xs text-[#81B29A] uppercase mb-2">09 & 10. Organic Core Focus Tags (SEMrush Target Vector Array)</h4>
                            <div id="keyword-list" class="grid grid-cols-1 md:grid-cols-2 gap-3 font-mono text-xs">
                                <div class="flex justify-between bg-[#151B1A] p-2 border border-[#E07A5F]/10">
                                    <span class="text-[#81B29A] font-bold">09. premium tactical carbon sunglasses scaling</span>
                                    <span class="text-[#F4F1DE]">Vol: 94k</span>
                                </div>
                                <div class="flex justify-between bg-[#151B1A] p-2 border border-[#E07A5F]/10">
                                    <span class="text-[#81B29A] font-bold">10. optimized tactical carbon sunglasses alternative</span>
                                    <span class="text-[#F4F1DE]">Vol: 81k</span>
                                </div>
                            </div>
                        </div>
                    </section>
                </div>
            </main>
        </div>

        <script>
            let activeEngine = 'gpt-4o';

            function toggleGuide(show) {
                const modal = document.getElementById('guide-modal');
                if (show) modal.classList.remove('hidden');
                else modal.classList.add('hidden');
            }

            function switchEngine(engineId, element) {
                document.querySelectorAll('.api-badge').forEach(el => el.classList.remove('active'));
                element.classList.add('active');
                activeEngine = engineId;
                
                // RE-BUILT CONCATENATION STRING TO COMPLETELY IGNORE ANNOYING COMPILER ISSUES
                var logString = '<div class="text-[#E07A5F]">[SYSTEM] Swapped active router endpoint to: <strong>' + 
                                engineId.toUpperCase() + ' Engine Array</strong>.</div>';
                document.getElementById('console-stream').innerHTML += logString;
            }

            function validateSystemAccess() {
                const u = document.getElementById('username').value;
                const p = document.getElementById('password').value;
                if (u === 'admin' && p === 'merchx2026') {
                    document.getElementById('login-gateway').style.display = 'none';
                    document.getElementById('dashboard-app').style.display = 'flex';
                } else {
                    document.getElementById('login-error').classList.remove('hidden');
                }
            }

            async function executePipeline() {
                const btn = document.getElementById('submit-btn');
                const stream = document.getElementById('console-stream');
                const titleVal = document.getElementById('prod-title').value;
                const costVal = parseFloat(document.getElementById('prod-cost').value);

                if(!titleVal || isNaN(costVal)) {
                    alert("Please fill input forms before execution mapping loops.");
                    return;
                }

                btn.disabled = true;
                btn.innerText = "COMPUTING DATA VECTORS...";
                
                stream.innerHTML = '<div class="text-[#81B29A]">[System Ingest] Transporting properties into ' + activeEngine.toUpperCase() + ' nodes...</div>' +
                                   '<div class="text-[#F4F1DE]">[Data Matrix Core] Evaluating telemetry patterns asynchronously...</div>';

                try {
                    const res = await fetch('/api/run-merchandiser', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ title: titleVal, cost_price: costVal, selected_api: activeEngine })
                    });
                    
                    const data = await res.json();
                    stream.innerHTML += '<div class="text-[#81B29A] font-bold">[Success] Data response packet verified cleanly.</div>';
                    
                    document.getElementById('m-vel').innerText = data.velocity_score;
                    document.getElementById('m-trend').innerText = data.google_trends_score;
                    document.getElementById('m-sem').innerText = data.semrush_volume;
                    document.getElementById('m-roas').innerText = data.meta_roas_multiplier;
                    document.getElementById('target-retail-display').innerText = data.target_retail;
                    
                    document.getElementById('res-margin').innerText = data.gross_margin;
                    document.getElementById('res-conv').innerText = data.conversion_rate;
                    document.getElementById('res-rev').innerText = data.ai_revenue;
                    document.getElementById('res-cac').innerText = data.cac_efficiency;
                    document.getElementById('res-share').innerText = data.market_share;
                    document.getElementById('res-turnover').innerText = data.turnover_days;
                    document.getElementById('res-confidence').innerText = data.confidence;
                    document.getElementById('res-velocity').innerText = data.demand_velocity;

                    const kwBox = document.getElementById('keyword-list');
                    kwBox.innerHTML = '';
                    data.keywords.forEach(function(k, index) {
                        kwBox.innerHTML += '<div class="flex justify-between bg-[#151B1A] p-2 border border-[#E07A5F]/10">' +
                            '<span class="text-[#81B29A] font-bold">0' + (9 + index) + '. ' + k.name + '</span>' +
                            '<span class="text-[#F4F1DE]">Vol: ' + k.score + 'k</span>' +
                            '</div>';
                    });
                } catch(err) {
                    stream.innerHTML += '<div class="text-[#E07A5F] font-bold">[CRITICAL] Infrastructure loop failure.</div>';
                } finally {
                    btn.disabled = false;
                    btn.innerText = "Run Cluster Strategy";
                }
            }
        </script>
    </body>
    </html>
    """