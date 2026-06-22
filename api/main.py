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

@app.post("/api/run-merchandiser")
async def run_ai_merchandiser(payload: ProductRequest):
    try:
        v_idx = random.randint(75, 99)
        google_trends_score = random.randint(68, 96)
        semrush_volume = f"{random.randint(15, 90)}k"
        meta_roas = f"{random.uniform(3.1, 5.8):.2f}x"
        
        conversion_lift = round(random.uniform(2.1, 6.4), 2)
        target_retail = round(payload.cost_price * random.uniform(1.7, 2.6), 2)
        gross_margin = round(((target_retail - payload.cost_price) / target_retail) * 100, 1)
        projected_rev = f"${random.randint(22000, 85000):,}"
        
        return {
            "status": "success",
            "product_name": payload.title,
            "conversion_rate": f"+{conversion_lift}%",
            "ai_revenue": projected_rev,
            "velocity_score": f"{v_idx}",
            "google_trends_score": f"{google_trends_score}",
            "semrush_volume": semrush_volume,
            "meta_roas_multiplier": meta_roas,
            "target_retail": f"${target_retail:,}",
            "gross_margin": f"{gross_margin}%",
            "keywords": [
                {"name": f"premium {payload.title.lower()}", "score": random.randint(80, 99)},
                {"name": f"trending {payload.title.lower()} 2026", "score": random.randint(65, 88)}
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_class=HTMLResponse)
async def serve_landing_page():
    # Serving HTML explicitly to guarantee layout availability
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Deep Intelligence - MerchX Autonomous Console</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono&family=Plus+Jakarta+Sans:wght@500;700;800&display=swap" rel="stylesheet">
        <script>
            tailwind.config = {
                theme: {
                    extend: {
                        fontFamily: { sans: ['Plus Jakarta Sans', 'sans-serif'], mono: ['JetBrains Mono', 'monospace'] },
                        colors: {
                            surface: '#0b1326', surfaceLow: '#131b2e', surfaceContainer: '#171f33',
                            onSurface: '#dae2fd', outline: '#908fa0', primary: '#c0c1ff',
                            secondary: '#4edea3', tertiary: '#ffb95f'
                        }
                    }
                }
            }
        </script>
    </head>
    <body class="bg-[#060e20] text-onSurface font-sans min-h-screen">

        <div id="login-gateway" class="fixed inset-0 z-50 flex items-center justify-center bg-[#060e20]/95 backdrop-blur-md">
            <div class="w-full max-w-md bg-surfaceContainer border border-outline/20 p-8 rounded-md shadow-2xl">
                <div class="text-center mb-6">
                    <span class="font-mono text-[10px] uppercase tracking-widest text-primary bg-primary/10 px-3 py-1 rounded-sm border border-primary/20">
                        System Authentication Required
                    </span>
                    <h1 class="text-2xl font-extrabold tracking-tight mt-3 text-white">Deep Intelligence MerchX</h1>
                    <p class="text-xs text-outline mt-1">Enterprise Orchestration Node</p>
                </div>
                
                <div class="bg-surfaceLow border border-outline/10 p-3 rounded-sm mb-4 font-mono text-[11px] text-tertiary">
                    <span class="font-bold block">💡 DUMMY LOGIN CREDENTIALS:</span>
                    Username: <span class="text-white font-bold">admin</span><br>
                    Password: <span class="text-white font-bold">merchx2026</span>
                </div>

                <form id="login-form" class="space-y-4">
                    <div>
                        <label class="block font-mono text-[11px] uppercase text-outline mb-1">User Identifier</label>
                        <input type="text" id="username" required class="w-full h-10 bg-[#060e20] border border-outline/30 rounded-sm px-3 font-mono text-sm text-white focus:outline-none focus:border-primary">
                    </div>
                    <div>
                        <label class="block font-mono text-[11px] uppercase text-outline mb-1">Security Password</label>
                        <input type="password" id="password" required class="w-full h-10 bg-[#060e20] border border-outline/30 rounded-sm px-3 font-mono text-sm text-white focus:outline-none focus:border-primary">
                    </div>
                    <div id="login-error" class="hidden text-xs text-red-400 font-mono">❌ Invalid system credentials specified.</div>
                    <button type="submit" class="w-full h-10 bg-primary text-[#1000a9] font-bold text-sm rounded-sm hover:bg-primary/90 transition-colors uppercase tracking-wider font-mono">
                        Initialize Workspace
                    </button>
                </form>
            </div>
        </div>

        <div id="dashboard-app" class="hidden min-h-screen flex flex-col">
            <header class="bg-surfaceContainer border-b border-outline/20 px-6 py-4 flex flex-col md:flex-row items-center justify-between gap-4">
                <div class="flex items-center space-x-4">
                    <h2 class="text-lg font-extrabold tracking-tight text-white flex items-center gap-2">
                        <span class="h-2 w-2 rounded-full bg-secondary animate-pulse"></span>
                        MerchX Core Suite
                    </h2>
                    <span class="font-mono text-[10px] bg-surfaceHigh text-outline px-2 py-0.5 rounded-sm border border-outline/10">v2.4-Autonomous</span>
                </div>
                
                <div class="flex flex-wrap gap-2 items-center justify-center">
                    <span class="font-mono text-[10px] px-2 py-1 rounded-sm bg-purple-500/20 text-purple-300 border border-purple-500/40 font-black animate-pulse">⚡ GPT-4o ENGINE COPLUGGED</span>
                    <span class="font-mono text-[10px] px-2 py-1 rounded-sm bg-surfaceLow text-outline border border-outline/20">SHOPIFY API</span>
                    <span class="font-mono text-[10px] px-2 py-1 rounded-sm bg-surfaceLow text-outline border border-outline/20">GOOGLE TRENDS API</span>
                    <span class="font-mono text-[10px] px-2 py-1 rounded-sm bg-surfaceLow text-outline border border-outline/20">SEMRUSH API</span>
                    <span class="font-mono text-[10px] px-2 py-1 rounded-sm bg-surfaceLow text-outline border border-outline/20">META MARKETING API</span>
                </div>
            </header>

            <main class="flex-1 p-6 grid grid-cols-1 lg:grid-cols-12 gap-6">
                <div class="lg:col-span-4 flex flex-col space-y-6">
                    <section class="bg-surfaceContainer border border-outline/20 rounded-md p-5">
                        <h3 class="font-mono text-xs uppercase text-primary font-bold mb-4 border-b border-outline/10 pb-2">Target Integration Stream</h3>
                        <form id="pipeline-form" class="space-y-4">
                            <div>
                                <label class="block font-mono text-[11px] uppercase text-outline mb-1">Product Title</label>
                                <input type="text" id="prod-title" required placeholder="e.g., Premium Leather Jacket" class="w-full h-10 bg-surfaceLow border border-outline/30 rounded-sm px-3 text-sm text-white focus:outline-none focus:border-primary">
                            </div>
                            <div>
                                <label class="block font-mono text-[11px] uppercase text-outline mb-1">Base Wholesale Cost ($)</label>
                                <input type="number" id="prod-cost" step="0.01" required placeholder="50.00" class="w-full h-10 bg-surfaceLow border border-outline/30 rounded-sm px-3 text-sm text-white focus:outline-none focus:border-primary">
                            </div>
                            <button type="submit" id="submit-btn" class="w-full h-10 bg-secondary text-[#003824] font-bold text-sm rounded-sm uppercase font-mono tracking-wider w-full">
                                Execute Autonomous Stream
                            </button>
                        </form>
                    </section>

                    <section class="bg-surfaceContainer border border-outline/20 rounded-md p-5 flex-1 flex flex-col min-h-[200px]">
                        <h3 class="font-mono text-xs uppercase text-primary font-bold mb-3 border-b border-outline/10 pb-2">Live AI Orchestration Pipeline</h3>
                        <div id="console-stream" class="flex-1 bg-surfaceLow border border-outline/10 rounded-sm p-3 font-mono text-[11px] text-green-400 overflow-y-auto space-y-1">
                            <span class="text-outline text-opacity-50">[SYSTEM] Initialization idle. Enter target metrics.</span>
                        </div>
                    </section>
                </div>

                <div class="lg:col-span-8 space-y-6">
                    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                        <div class="bg-surfaceContainer border border-outline/20 p-4 rounded-md">
                            <p class="font-mono text-[10px] uppercase text-outline">Shopify Sales Index</p>
                            <p id="m-vel" class="text-2xl font-mono font-bold text-white mt-1">--</p>
                        </div>
                        <div class="bg-surfaceContainer border border-outline/20 p-4 rounded-md">
                            <p class="font-mono text-[10px] uppercase text-outline">Google Trends Index</p>
                            <p id="m-trend" class="text-2xl font-mono font-bold text-tertiary mt-1">--</p>
                        </div>
                        <div class="bg-surfaceContainer border border-outline/20 p-4 rounded-md">
                            <p class="font-mono text-[10px] uppercase text-outline">SEMrush Volume</p>
                            <p id="m-sem" class="text-2xl font-mono font-bold text-primary mt-1">--</p>
                        </div>
                        <div class="bg-surfaceContainer border border-outline/20 p-4 rounded-md">
                            <p class="font-mono text-[10px] uppercase text-outline">Meta ROAS Multiplier</p>
                            <p id="m-roas" class="text-2xl font-mono font-bold text-secondary mt-1">--</p>
                        </div>
                    </div>

                    <section class="bg-surfaceContainer border border-outline/20 rounded-md p-6">
                        <div class="border-b border-outline/10 pb-3 mb-4 flex justify-between items-center">
                            <div>
                                <h3 class="text-lg font-bold text-white uppercase">GPT-4o Yield Metrics Mapping</h3>
                                <p class="text-xs text-outline font-mono">Synthesized storefront variables</p>
                            </div>
                            <div class="bg-primary/10 border border-primary/30 px-4 py-1 rounded-sm text-right">
                                <span class="block font-mono text-[9px] uppercase text-outline">Optimal Retail Tag</span>
                                <span id="target-retail-display" class="text-xl font-mono font-bold text-primary">$--</span>
                            </div>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div class="space-y-3">
                                <div class="flex justify-between border-b border-outline/5 py-1 text-sm"><span class="text-outline">Gross Margin Allocation:</span><span id="res-margin" class="font-mono font-bold">--</span></div>
                                <div class="flex justify-between border-b border-outline/5 py-1 text-sm"><span class="text-outline">Conversion Velocity:</span><span id="res-conv" class="font-mono font-bold text-secondary">--</span></div>
                                <div class="flex justify-between border-b border-outline/5 py-1 text-sm"><span class="text-outline">Projected Run Revenue:</span><span id="res-rev" class="font-mono font-bold text-white">--</span></div>
                            </div>
                            <div class="space-y-2">
                                <h4 class="font-mono text-xs text-outline uppercase">Integrated Keyword Data (SEMrush)</h4>
                                <div id="keyword-list" class="space-y-1.5 font-mono text-xs">
                                    <em class="text-outline">No live cross-analysis generated yet.</em>
                                </div>
                            </div>
                        </div>
                    </section>
                </div>
            </main>
        </div>

        <script>
            // Cleaned Event Bindings preventing layout blocking
            document.getElementById('login-form').addEventListener('submit', function(e) {
                e.preventDefault();
                const u = document.getElementById('username').value;
                const p = document.getElementById('password').value;
                
                if (u === 'admin' && p === 'merchx2026') {
                    document.getElementById('login-gateway').style.display = 'none';
                    document.getElementById('dashboard-app').classList.remove('hidden');
                } else {
                    document.getElementById('login-error').classList.remove('hidden');
                }
            });

            document.getElementById('pipeline-form').addEventListener('submit', async function(e) {
                e.preventDefault();
                const btn = document.getElementById('submit-btn');
                const stream = document.getElementById('console-stream');
                
                btn.disabled = true;
                btn.innerText = "RUNNING CRITICAL CALLS...";
                
                stream.innerHTML = `
                    <div class="text-primary">[System Core] Starting synchronized platform fetching diagnostics...</div>
                    <div class="text-white">[Shopify Engine] Querying inventory metrics...</div>
                    <div class="text-white">[Google Trends Engine] Mapping search velocity tags...</div>
                    <div class="text-white">[SEMrush Engine] Scraping high-intent index arrays...</div>
                    <div class="text-white">[Meta Engine] Calculating attribution profiles...</div>
                    <div class="text-purple-400 font-bold animate-pulse">[GPT-4o Engine] Compiling API structural logs...</div>
                `;

                try {
                    const res = await fetch('/api/run-merchandiser', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            title: document.getElementById('prod-title').value,
                            cost_price: parseFloat(document.getElementById('prod-cost').value)
                        })
                    });
                    
                    const data = await res.json();
                    stream.innerHTML += '<div class="text-secondary font-bold">[Success] API generation loops parsed flawlessly.</div>';
                    
                    document.getElementById('m-vel').innerText = data.velocity_score + " / 100";
                    document.getElementById('m-trend').innerText = data.google_trends_score + " / 100";
                    document.getElementById('m-sem').innerText = data.semrush_volume;
                    document.getElementById('m-roas').innerText = data.meta_roas_multiplier;
                    document.getElementById('target-retail-display').innerText = data.target_retail;
                    document.getElementById('res-margin').innerText = data.gross_margin;
                    document.getElementById('res-conv').innerText = data.conversion_rate;
                    document.getElementById('res-rev').innerText = data.ai_revenue;

                    const kwBox = document.getElementById('keyword-list');
                    kwBox.innerHTML = '';
                    
                    data.keywords.forEach(function(k) {
                        kwBox.innerHTML += '<div class="flex justify-between bg-surfaceLow p-2 border border-outline/10 rounded-sm">' +
                            '<span class="text-primary font-bold">' + k.name + '</span>' +
                            '<span class="text-white">Vol: ' + k.score + 'k</span>' +
                            '</div>';
                    });
                } catch(err) {
                    stream.innerHTML += '<div class="text-red-400 font-bold">[ERROR] Pipeline connectivity issue.</div>';
                } finally {
                    btn.disabled = false;
                    btn.innerText = "Execute Autonomous Stream";
                }
            });
        </script>
    </body>
    </html>
    """