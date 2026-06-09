# Production Setup Blueprint: AI-Driven E-commerce Merchandising Suite

Welcome to the definitive engineering guide for building, scaling, and deploying the **AI-Driven E-commerce Merchandising Suite**. This file acts as your master reference manual for development inside VS Code, code configuration, database initialization, and cloud execution.

---

## 1. Complete Architecture Overview
This application utilizes a decoupled architecture split into three core layers:
1. **Frontend Layer (React + Vite + Tailwind CSS):** A responsive, single-page application dashboard providing observability into multi-agent operations, historical logs, store metrics, and inventory control.
2. **Backend Engine Layer (FastAPI + CrewAI + GPT-4o):** An asynchronous REST API acting as the orchestrator for stateful, long-running agent execution pipelines.
3. **Storage & Feedback Layer (PostgreSQL):** A relational data store recording telemetry from external APIs (Shopify, SEMrush, Google Trends), historical agent decisions, and live storefront performance metrics.

---

## 2. Directory Architecture
Create this exact structural setup inside your VS Code workspace:

```text
ai-merchandising-suite/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── agents/
│   │   │   ├── __init__.py
│   │   │   ├── crew_manager.py
│   │   │   ├── trend_agent.py
│   │   │   ├── pricing_agent.py
│   │   │   ├── copy_agent.py
│   │   │   ├── seo_agent.py
│   │   │   └── analytics_agent.py
│   │   └── tools/
│   │       ├── shopify_tool.py
│   │       ├── semrush_tool.py
│   │       └── trends_tool.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── context/
│   │   ├── hooks/
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Inventory.jsx
│   │   │   └── AgentLogs.jsx
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   ├── tailwind.config.js
│   └── vite.config.js
└── .gitignore
```

---

## 3. Global `.gitignore` Configuration
Place a `.gitignore` file at the root level of your directory to protect sensitive access tokens and localized caches from being committed to GitHub:

```text
# Node dependencies
node_modules/
dist/
dist-ssr
*.local

# Python environment modules
venv/
ENV/
env.bak/
venv.bak/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python

# Sensitive environments
.env
.env.production
.env.development
.env.local

# IDE Specific metadata
.vscode/
.idea/
*.suo
*.ntvs*
*.njsproj
*.sln
*.swp
```

---

## 4. Database Initialization Script (PostgreSQL)
Run the following relational layout inside your PostgreSQL instance to create the necessary table structures and track your agents' autonomous routines:

```sql
-- Operational Enumerations
CREATE TYPE agent_status AS ENUM ('idle', 'running', 'completed', 'failed');
CREATE TYPE execution_trigger AS ENUM ('manual', 'cron', 'analytics_feedback');

-- Core Products Master Inventory Table
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    shopify_product_id VARCHAR(255) UNIQUE,
    title VARCHAR(255) NOT NULL,
    sku VARCHAR(100) UNIQUE,
    cost_price NUMERIC(10, 2) NOT NULL,
    current_retail_price NUMERIC(10, 2) NOT NULL,
    compare_at_price NUMERIC(10, 2),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Orchestration Execution Cycles Logger
CREATE TABLE agent_runs (
    id SERIAL PRIMARY KEY,
    run_trigger execution_trigger DEFAULT 'manual',
    status agent_status DEFAULT 'idle',
    started_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP WITH TIME ZONE,
    error_log TEXT
);

-- AI Content Generation & Search Telemetry Meta Table
CREATE TABLE product_merchandising_data (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id) ON DELETE CASCADE,
    agent_run_id INT REFERENCES agent_runs(id) ON DELETE SET NULL,
    target_keywords JSONB, 
    generated_title VARCHAR(255),
    generated_description TEXT,
    meta_title VARCHAR(150),
    meta_description TEXT,
    seo_tags VARCHAR(255)[],
    is_pushed_to_shopify BOOLEAN DEFAULT FALSE,
    evaluated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Storefront Analytics Matrix Tracking Table
CREATE TABLE storefront_metrics (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id) ON DELETE CASCADE,
    captured_date DATE NOT NULL,
    page_views INT DEFAULT 0,
    add_to_carts INT DEFAULT 0,
    purchases INT DEFAULT 0,
    conversion_rate NUMERIC(5, 2) GENERATED ALWAYS AS (
        CASE WHEN page_views > 0 THEN (purchases::NUMERIC / page_views::NUMERIC) * 100 
        ELSE 0 
        END
    ) STORED,
    revenue_generated NUMERIC(12, 2) DEFAULT 0.00,
    UNIQUE(product_id, captured_date)
);
```

---

## 5. Backend Code Samples & Implementation

### A. Python Dependencies (`backend/requirements.txt`)
```text
fastapi==0.110.0
uvicorn==0.28.0
crewai==0.28.8
langchain-openai==0.1.1
sqlalchemy==2.0.28
psycopg2-binary==2.9.9
pydantic==2.6.4
pydantic-settings==2.2.1
requests==2.31.0
```

### B. Dynamic Environment Gateway Settings (`backend/app/config.py`)
```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    DATABASE_URL: str
    SHOPIFY_API_ACCESS_TOKEN: str
    SHOPIFY_STORE_URL: str
    SEMRUSH_API_KEY: str
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()
```

### C. Multi-Agent Engine Core (`backend/app/agents/crew_manager.py`)
```python
from crewai import Agent, Crew, Process, Task
from langchain_openai import ChatOpenAI
from app.config import settings

class EcomMerchandisingOrchestrator:
    def __init__(self, product_context: dict):
        self.product_context = product_context
        self.llm = ChatOpenAI(model="gpt-4o", api_key=settings.OPENAI_API_KEY)

    def assemble_crew(self) -> Crew:
        # 1. Trend Agent Configuration
        trend_agent = Agent(
            role='Market Intelligence Specialist',
            goal='Scrape market trends and competitive keyword metrics.',
            backstory='An analytical data gatherer reading consumer velocity signatures and external signals.',
            llm=self.llm,
            verbose=True
        )

        # 2. Pricing Agent Configuration
        pricing_agent = Agent(
            role='Dynamic Yield & Margin Architect',
            goal='Optimize margins while balancing market competitive ceilings.',
            backstory='A financial algorithms master calculating elasticity profiles based on retail tracking data.',
            llm=self.llm,
            verbose=True
        )

        # 3. Copywriting Agent Configuration
        copy_agent = Agent(
            role='Conversion Rate Optimization Copywriter',
            goal='Draft stellar product descriptions using modern conversion frameworks.',
            backstory='A sensory-driven copy writer obsessed with emotional hooks, structured benefits, and customer action.',
            llm=self.llm,
            verbose=True
        )

        # Tasks Execution Assignment Flow
        task_trend = Task(
            description=f"Analyze demand velocity blueprints for incoming query profile: {self.product_context['title']}",
            expected_output="JSON list containing core high-intent keywords, average competitor prices, and demand score multipliers.",
            agent=trend_agent
        )

        task_pricing = Task(
            description=f"Calculate the optimal retail price mapping for item with cost base: {self.product_context['cost_price']}. Use the previous trend analysis metadata.",
            expected_output="Detailed price recommendation schema featuring targeted base prices, comparison metrics, and justification logs.",
            agent=pricing_agent
        )

        task_copy = Task(
            description="Generate fully structural commercial copywriting ready for a storefront layout. Seamlessly blend strategic keywords.",
            expected_output="High-converting structural markdown output layout containing standard e-commerce elements.",
            agent=copy_agent
        )

        return Crew(
            agents=[trend_agent, pricing_agent, copy_agent],
            tasks=[task_trend, task_pricing, task_copy],
            process=Process.sequential
        )

    def execute_workflow(self) -> str:
        crew = self.assemble_crew()
        return crew.kickoff()
```

### D. Primary Asynchronous Web Application Layer (`backend/app/main.py`)
```python
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import ProductRunRequest
from app.agents.crew_manager import EcomMerchandisingOrchestrator

app = FastAPI(title="AI-Driven E-commerce Merchandising API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For production, narrow down to exact frontend URL domain maps
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/run-merchandiser")
async def run_merchandising_suite(payload: ProductRunRequest):
    try:
        orchestrator = EcomMerchandisingOrchestrator(product_context=payload.model_dump())
        result = orchestrator.execute_workflow()
        return {"status": "success", "agent_output": str(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/health")
def health_check():
    return {"status": "healthy"}
```

---

## 6. Frontend Configuration (React + Tailwind CSS)

### A. Tailored Config Matrix (`frontend/tailwind.config.js`)
```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          dark: '#0f172a',
          primary: '#4f46e5',
          accent: '#10b981'
        }
      }
    },
  },
  plugins: [],
}
```

### B. Telemetry Control Dashboard Layout View (`frontend/src/pages/Dashboard.jsx`)
```jsx
import React, { useState, useEffect } from 'react';

export default function Dashboard() {
  const [metrics, setMetrics] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch telemetry from local backend engine / deployed service
    fetch(`${import.meta.env.VITE_API_BASE_URL}/api/health`)
      .then(res => res.json())
      .then(() => {
        setMetrics([
          { label: "Overall Store Conversion Rate", value: "3.24%" },
          { label: "Active Monitored Products", value: "142 Items" },
          { label: "AI Optimization Cycles (24h)", value: "38 Runs" }
        ]);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  return (
    <div className="p-8 min-h-screen bg-slate-900 text-white">
      <header className="mb-8">
        <h1 className="text-3xl font-extrabold tracking-tight">AI Merchandising Command Hub</h1>
        <p className="text-slate-400 mt-2">Observability control node running autonomous orchestration loops.</p>
      </header>

      {loading ? (
        <div className="animate-pulse text-indigo-400">Loading Telemetry Feeds...</div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {metrics.map((item, idx) => (
            <div key={idx} className="p-6 bg-slate-800 border border-slate-700 rounded-xl shadow-lg">
              <div className="text-sm font-semibold text-slate-400 uppercase tracking-wider">{item.label}</div>
              <div className="text-4xl font-black text-indigo-400 mt-3">{item.value}</div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
```

---

## 7. Version Control & Automated Deployment Blueprint

### Step 1: Localizing to Git
Execute the initial registration inside your VS Code terminal panel:
```bash
git init
git add .
git commit -m "Initialize structural framework for AI Merchandising Stack"
git branch -M main
```

### Step 2: Mapping Repository to Upstream GitHub Target
Create an empty repository on GitHub web portal and push your codebase:
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
git push -u origin main
```

### Step 3: Deployment Pipeline Division Configuration

#### Client App Hosting on Vercel
1. Access the **Vercel Web Management Console**. Select **Add New Project**.
2. Connect your GitHub workspace target registry and highlight the repository directory.
3. Apply explicit overrides inside the configuration wizard:
   * **Framework Preset:** `Vite`
   * **Root Directory:** `frontend`
   * **Build Command:** `npm run build`
   * **Output Directory:** `dist`
4. Declare your Runtime Environment Values (e.g., `VITE_API_BASE_URL=https://your-backend-render-url.onrender.com`).
5. Complete setup by triggering **Deploy**.

#### Persistent Execution Agent Backend Hosting on Render / Railway
Because Python agent loops running inside CrewAI frequently iterate through external endpoints and recursively call Large Language Model structures, execution loops can exceed Vercel's standard serverless timeout windows (10–60s). Deploy the backend onto long-running instance blocks like Render:
1. Initialize a new **Web Service** on **Render.com**. Connect the core repository.
2. Configure the system build runtime options:
   * **Runtime environment:** `Python 3`
   * **Root Directory:** `backend`
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
3. Map environment variable credentials (`OPENAI_API_KEY`, `DATABASE_URL`, `SHOPIFY_STORE_URL`, etc.).
4. Select **Deploy Web Service**. Use the generated production URL domain as the target for your frontend's environment configuration.
