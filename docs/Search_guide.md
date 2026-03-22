# 🔍 AJ-Bench — Search Domain

---

## 📦 Setup

### 1. Install Dependencies

```bash
pip install -e .
```

### 2. Install Node.js & Playwright

```bash
brew install node

# Verify installation (Our Version)
node -v   # v24.8.0
npm -v    # 11.6.1
npx -v    # 11.6.1

# Install Playwright
npm install -g playwright
npx playwright install
```

> In the Search domain, we use **Playwright 1.55.0** with **Chromium-1187**.

### 3. Configure Environment Variables

Create a `.mcp_env` file in the **root directory** of the project with the following content:

```bash
# 🔑 OpenAI
OPENAI_BASE_URL="YOUR_OPENAI_BASE_URL"
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"

# 🔑 DeepSeek
OPENAI_BASE_URL="YOUR_DEEPSEEK_BASE_URL"
DEEPSEEK_API_KEY="YOUR_DEEPSEEK_API_KEY"

# 🌐 Playwright
PLAYWRIGHT_BROWSER="chromium"
PLAYWRIGHT_HEADLESS="True"
PLAYWRIGHT_EXECUTABLE_PATH="~/Library/Caches/ms-playwright/chromium-1187/chrome-mac/Chromium.app/Contents/MacOS/Chromium"
```

---

## 🚀 Run

### 🤖 Agent-as-a-Judge

```bash
bash agent_judge_search_pipeline.sh
```

### 🧠 LLM-as-a-Judge

#### Deep

```bash
python3 src/llm-judge/Search/deep_llm_judge_pipeline.py
python3 src/llm-judge/Search/deep_llm_judge_verify.py
```

#### Wide

```bash
python3 src/llm-judge/Search/wide_llm_judge_pipeline.py
python3 src/llm-judge/Search/wide_llm_judge_verify.py
```

---

## 📊 Evaluation

#### Deep

```bash
python3 src/eval/Search/deep_eval.py
```

#### Wide

```bash
python3 src/eval/Search/wide_eval.py
```