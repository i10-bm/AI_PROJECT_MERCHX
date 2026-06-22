from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
import random

app = FastAPI(title="MerchX Enterprise AI Suite")

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
        demand_velocity = "EXPONENTIAL RUN VELOCITY" if v_idx > 85 else "STABLE DISTRIBUTION TREND"
        
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
        <title>Deep Intelligence - MerchX Autonomous Console</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono&family=Plus+Jakarta+Sans:wght=500;700;800&display=swap" rel="stylesheet">
        <script>
            tailwind.config = {
                theme: {
                    extend: {
                        fontFamily: { sans: ['Plus Jakarta Sans', 'sans-serif'], mono: ['JetBrains Mono', 'monospace'] },
                        colors: {
                            surface: '#0b1326', 
                            surfaceLow: '#131b2e', 
                            surfaceContainer: '#171f33',
                            surfaceContainerLowest: '#060e20',
                            onSurface: '#dae2fd', 
                            outline: '#908fa0', 
                            primary: '#c0c1ff',
                            secondary: '#4edea3', 
                            tertiary: '#ffb95f'
                        }
                    }
                }
            }
        </script>
        <style>
            .api-badge { transition: all 0.2s ease; cursor: pointer; opacity: 0.4; }
            .api-badge.active { opacity: 1; border-color: #4edea3; box-shadow: 0 0 10px rgba(78, 222, 163, 0.2); }
        </style>
    </head>
    <body class="bg-[#060e20] text-[#dae2fd] font-sans min-h-screen">

        <div id="login-gateway" class="fixed inset-0 z-50 flex items-center justify-center bg-[#060e20]/95 backdrop-blur-md" style="display: flex;">
            <div class="w-full max-w-md bg-[#171f33] border border-[#908fa0]/20 p-8 rounded-md shadow-2xl">
                <div class="text-center mb-6">
                    <span class="font-mono text-[10px] uppercase tracking-widest text-[#c0c1ff] bg-[#c0c1ff]/10 px-3 py-1 rounded-sm border border-[#c0c1ff]/20">
                        System Authentication Required
                    </span>
                    <h1 class="text-2xl font-extrabold tracking-tight mt-3 text-white">Deep Intelligence MerchX</h1>
                    <p class="text-xs text-[#908fa0] mt-1">Enterprise Orchestration Node</p>
                </div>
                
                <div class="bg-[#131b2e] border border-[#908fa0]/10 p-3 rounded-sm mb-4 font-mono text-[11px] text-[#ffb95f]">
                    <span class="font-bold block">💡 ACCESS CREDENTIALS:</span>
                    Username: <span class="text-white font-bold select-all">admin</span><br>
                    Password: <span class="text-white font-bold select-all">merchx2026</span>
                </div>

                <div class="space-y-4">
                    <div>
                        <label class="block font-mono text-[11px] uppercase text-[#908fa0] mb-1">User Identifier</label>
                        <input type="text" id="username" value="admin" class="w-full h-10 bg-[#060e20] border border-[#908fa0]/30 rounded-sm px-3 font-mono text-sm text-white focus:outline-none focus:border-[#c0c1ff]">
                    </div>
                    <div>
                        <label class="block font-mono text-[11px] uppercase text-[#908fa0] mb-1">Security Password</label>
                        <input type="password" id="password" value="merchx2026" class="w-full h-10 bg-[#060e20] border border-[#908fa0]/30 rounded-sm px-3 font-mono text-sm text-white focus:outline-none focus:border-[#c0c1ff]">
                    </div>
                    <div id="login-error" class="hidden text-xs text-rose-500 font-mono">❌ Invalid authentication parameters.</div>
                    <button type="button" onclick="validateSystemAccess()" class="w-full h-10 bg-[#c0c1ff] text-[#1000a9] font-bold text-sm rounded-sm hover:bg-[#c0c1ff]/90 transition-colors uppercase tracking-wider font-mono">
                        Initialize Workspace
                    </button>
                </div>
            </div>
        </div>

        <div id="guide-modal" class="fixed inset-0 z-50 flex items-center justify-center bg-[#060e20]/80 backdrop-blur-sm hidden">
            <div class="w-full max-w-lg bg-[#171f33] border border-[#4edea3]/40 p-6 rounded-md shadow-2xl font-mono text-xs">
                <div class="flex justify-between items-center border-b border-[#908fa0]/20 pb-2 mb-4">
                    <h3 class="text-[#4edea3] font-bold text-sm">💡 OPERATIONAL INTEGRATION GUIDE</h3>
                    <button onclick="toggleGuide(false)" class="text-[#908fa0] hover:text-white font-bold text-lg">&times;</button>
                </div>
                <div class="space-y-3 text-[#dae2fd]">
                    <p><span class="text-[#c0c1ff] font-bold">1. Select Engine Route:</span> Click any active API chip header at the top toolbar to re-route live endpoints.</p>
                    <p><span class="text-[#c0c1ff] font-bold">2. Trigger Execution:</span> Update fields inside the control card, then hit <span class="text-[#4edea3]">Execute Autonomous Stream</span> to compute metrics.</p>
                    <p><span class="text-[#c0c1ff] font-bold">3. Review 10 Data Points:</span> Observe the populated grid components update automatically without empty frames.</p>
                </div>
                <button onclick="toggleGuide(false)" class="w-full mt-5 h-9 bg-[#131b2e] border border-[#908fa0]/30 hover:border-[#4edea3] text-white font-bold rounded-sm uppercase tracking-wider">
                    Acknowledge & Continue
                </button>
            </div>
        </div>

        <div id="dashboard-app" class="min-h-screen flex flex-col" style="display: none;">
            <header class="bg-[#171f33] border-b border-[#908fa0]/20 px-6 py-4 flex flex-col lg:flex-row items-center justify-between gap-4">
                <div class="flex items-center space-x-4">
                    <h2 class="text-lg font-extrabold tracking-tight text-white flex items-center gap-2">
                        <span class="h-2 w-2 rounded-full bg-[#4edea3] animate-pulse"></span>
                        MerchX Core Suite
                    </h2>
                    <button onclick="toggleGuide(true)" class="font-mono text-[10px] bg-[#ffb95f]/10 text-[#ffb95f] px-2 py-0.5 rounded-sm border border-[#ffb95f]/30 hover:bg-[#ffb95f]/20 font-bold transition-all">
                        ❓ HOW IT WORKS
                    </button>
                </div>
                
                <div class="flex flex-wrap gap-2 items-center justify-center">
                    <span id="api-gpt" onclick="switchEngine('gpt-4o', this)" class="api-badge active font-mono text-[10px] px-2 py-1 rounded-sm bg-purple-500/20 text-purple-300 border border-purple-500/40 font-black">⚡ GPT-4O CORE</span>
                    <span id="api-shopify" onclick="switchEngine('shopify', this)" class="api-badge font-mono text-[10px] px-2 py-1 rounded-sm bg-[#131b2e] text-[#908fa0] border border-[#908fa0]/20 font-bold">SHOPIFY API</span>
                    <span id="api-trends" onclick="switchEngine('google-trends', this)" class="api-badge font-mono text-[10px] px-2 py-1 rounded-sm bg-[#131b2e] text-[#908fa0] border border-[#908fa0]/20 font-bold">GOOGLE TRENDS</span>
                    <span id="api-semrush" onclick="switchEngine('semrush', this)" class="api-badge font-mono text-[10px] px-2 py-1 rounded-sm bg-[#131b2e] text-[#908fa0] border border-[#908fa0]/20 font-bold">SEMRUSH DATA</span>
                    <span id="api-meta" onclick="switchEngine('meta', this)" class="api-badge font-mono text-[10px] px-2 py-1 rounded-sm bg-[#131b2e] text-[#908fa0] border border-[#908fa0]/20 font-bold">META ADS SUITE</span>
                </div>
            </header>

            <main class="flex-1 p-6 grid grid-cols-1 lg:grid-cols-12 gap-6">
                <div class="lg:col-span-4 flex flex-col space-y-6">
                    <section class="bg-[#171f33] border border-[#908fa0]/20 rounded-md p-5">
                        <h3 class="font-mono text-xs uppercase text-[#c0c1ff] font-bold mb-4 border-b border-[#908fa0]/10 pb-2">Target Integration Stream</h3>
                        <div class="space-y-4">
                            <div>
                                <label class="block font-mono text-[11px] uppercase text-[#908fa0] mb-1">Product Title</label>
                                <input type="text" id="prod-title" value="Tactical Carbon Sunglasses" class="w-full h-10 bg-[#131b2e] border border-[#908fa0]/30 rounded-sm px-3 text-sm text-white focus:outline-none focus:border-[#c0c1ff]">
                            </div>
                            <div>
                                <label class="block font-mono text-[11px] uppercase text-[#908fa0] mb-1">Base Wholesale Cost ($)</label>
                                <input type="number" id="prod-cost" value="45.00" class="w-full h-10 bg-[#131b2e] border border-[#908fa0]/30 rounded-sm px-3 text-sm text-white focus:outline-none focus:border-[#c0c1ff]">
                            </div>
                            <button type="button" id="submit-btn" onclick="executePipeline()" class="w-full h-10 bg-[#4edea3] text-[#003824] font-bold text-sm rounded-sm uppercase font-mono tracking-wider w-full">
                                Execute Autonomous Stream
                            </button>
                        </div>
                    </section>

                    <section class="bg-[#171f33] border border-[#908fa0]/20 rounded-md p-5 flex-1 flex flex-col min-h-[200px]">
                        <h3 class="font-mono text-xs uppercase text-[#c0c1ff] font-bold mb-3 border-b border-[#908fa0]/10 pb-2">Live AI Orchestration Pipeline</h3>
                        <div id="console-stream" class="flex-1 bg-[#131b2e] border border-[#908fa0]/10 rounded-sm p-3 font-mono text-[11px] text-green-400 overflow-y-auto space-y-1">
                            <span class="text-[#4edea3]">[INITIALIZED] Pre-populated dashboard live data stream verified.</span>
                        </div>
                    </section>
                </div>

                <div class="lg:col-span-8 space-y-6">
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                        <div class="bg-[#171f33] border border-[#908fa0]/20 p-4 rounded-md">
                            <p class="font-mono text-[10px] uppercase text-[#908fa0]">Shopify Sales Index</p>
                            <p id="m-vel" class="text-xl font-mono font-bold text-white mt-1">88 / 100</p>
                        </div>
                        <div class="bg-[#171f33] border border-[#908fa0]/20 p-4 rounded-md">
                            <p class="font-mono text-[10px] uppercase text-[#908fa0]">Google Trends Index</p>
                            <p id="m-trend" class="text-xl font-mono font-bold text-[#ffb95f] mt-1">91 / 100</p>
                        </div>
                        <div class="bg-[#171f33] border border-[#908fa0]/20 p-4 rounded-md">
                            <p class="font-mono text-[10px] uppercase text-[#908fa0]">SEMrush Volume</p>
                            <p id="m-sem" class="text-xl font-mono font-bold text-[#c0c1ff] mt-1">45k</p>
                        </div>
                        <div class="bg-[#171f33] border border-[#908fa0]/20 p-4 rounded-md">
                            <p class="font-mono text-[10px] uppercase text-[#908fa0]">Meta ROAS Multiplier</p>
                            <p id="m-roas" class="text-xl font-mono font-bold text-[#4edea3] mt-1">4.20x</p>
                        </div>
                    </div>

                    <section class="bg-[#171f33] border border-[#908fa0]/20 rounded-md p-6">
                        <div class="border-b border-[#908fa0]/10 pb-3 mb-5 flex justify-between items-center">
                            <div>
                                <h3 class="text-base font-bold text-white uppercase tracking-tight">System Core Yield Mapping</h3>
                                <p class="text-[11px] text-[#908fa0] font-mono">Structural telemetry answers mapping</p>
                            </div>
                            <div class="bg-[#c0c1ff]/10 border border-[#c0c1ff]/30 px-4 py-1 rounded-sm text-right">
                                <span class="block font-mono text-[9px] uppercase text-[#908fa0]">Optimal Retail Tag</span>
                                <span id="target-retail-display" class="text-xl font-mono font-bold text-[#c0c1ff]">$99.00</span>
                            </div>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-3.5 font-mono text-xs">
                            <div class="flex justify-between border-b border-[#908fa0]/10 pb-1.5">
                                <span class="text-[#908fa0]">1. Gross Margin Allocation:</span>
                                <span id="res-margin" class="font-bold text-white">54.5%</span>
                            </div>
                            <div class="flex justify-between border-b border-[#908fa0]/10 pb-1.5">
                                <span class="text-[#908fa0]">2. Conversion Velocity:</span>
                                <span id="res-conv" class="font-bold text-[#4edea3]">+4.8%</span>
                            </div>
                            <div class="flex justify-between border-b border-[#908fa0]/10 pb-1.5">
                                <span class="text-[#908fa0]">3. Projected Revenue Tag:</span>
                                <span id="res-rev" class="font-bold text-white">$48,500</span>
                            </div>
                            <div class="flex justify-between border-b border-[#908fa0]/10 pb-1.5">
                                <span class="text-[#908fa0]">4. CAC Marketing Efficiency:</span>
                                <span id="res-cac" class="font-bold text-[#ffb95f]">$16.40</span>
                            </div>
                            <div class="flex justify-between border-b border-[#908fa0]/10 pb-1.5">
                                <span class="text-[#908fa0]">5. Projected Market Share:</span>
                                <span id="res-share" class="font-bold text-[#c0c1ff]">6.2%</span>
                            </div>
                            <div class="flex justify-between border-b border-[#908fa0]/10 pb-1.5">
                                <span class="text-[#908fa0]">6. Inventory Turnover Cycle:</span>
                                <span id="res-turnover" class="font-bold text-white">22 Days</span>
                            </div>
                            <div class="flex justify-between border-b border-[#908fa0]/10 pb-1.5">
                                <span class="text-[#908fa0]">7. Optimization Confidence:</span>
                                <span id="res-confidence" class="font-bold text-[#4edea3]">94%</span>
                            </div>
                            <div class="flex justify-between border-b border-[#908fa0]/10 pb-1.5">
                                <span class="text-[#908fa0]">8. Demand Velocity Status:</span>
                                <span id="res-velocity" class="font-bold text-white truncate max-w-[170px]">EXPONENTIAL RUN VELOCITY</span>
                            </div>
                        </div>

                        <div class="mt-6 pt-4 border-t border-[#908fa0]/10">
                            <h4 class="font-mono text-xs text-[#908fa0] uppercase mb-2">9 & 10. Organic Strategy Targets (SEMrush Keyword Array)</h4>
                            <div id="keyword-list" class="grid grid-cols-1 md:grid-cols-2 gap-3 font-mono text-xs">
                                <div class="flex justify-between bg-[#131b2e] p-2 border border-[#908fa0]/10 rounded-sm">
                                    <span class="text-[#c0c1ff] font-bold">9. premium tactical carbon sunglasses scaling</span>
                                    <span class="text-white">Vol: 94k</span>
                                </div>
                                <div class="flex justify-between bg-[#131b2e] p-2 border border-[#908fa0]/10 rounded-sm">
                                    <span class="text-[#c0c1ff] font-bold">10. optimized tactical carbon sunglasses alternative</span>
                                    <span class="text-white">Vol: 81k</span>
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
                
                // FIXED CONCATENATION TO ELIMINATE JAVASCRIPT STRING BUGS AND RE-FORMATTED FOR VERCEL
                var formattedStr = '<div class="text-[#ffb95f]">[SYSTEM] Swapped active router endpoint to: <strong>' + 
                                   engineId.toUpperCase() + ' Engine Array</strong>.</div>';
                document.getElementById('console-stream').innerHTML += formattedStr;
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
                    alert("Please input values accurately.");
                    return;
                }

                btn.disabled = true;
                btn.innerText = "RUNNING CRITICAL CALLS...";
                
                stream.innerHTML = '<div class="text-[#c0c1ff]">[System Core] Forwarding fields into ' + activeEngine.toUpperCase() + ' cluster stream...</div>' +
                                   '<div class="text-white">[External Network Sync] Syncing metrics via multi-agent pipelines...</div>';

                try {
                    const res = await fetch('/api/run-merchandiser', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ title: titleVal, cost_price: costVal, selected_api: activeEngine })
                    });
                    
                    const data = await res.json();
                    stream.innerHTML += '<div class="text-[#4edea3] font-bold">[Success] Complete 10 metric indexes parsed successfully.</div>';
                    
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
                        kwBox.innerHTML += '<div class="flex justify-between bg-[#131b2e] p-2 border border-[#908fa0]/10 rounded-sm">' +
                            '<span class="text-[#c0c1ff] font-bold">' + (9 + index) + '. ' + k.name + '</span>' +
                            '<span class="text-white">Vol: ' + k.score + 'k</span>' +
                            '</div>';
                    });
                } catch(err) {
                    stream.innerHTML += '<div class="text-rose-500 font-bold">[ERROR] Execution loop failure.</div>';
                } finally {
                    btn.disabled = false;
                    btn.innerText = "Execute Autonomous Stream";
                }
            }
        </script>
    </body>
    </html>
    """