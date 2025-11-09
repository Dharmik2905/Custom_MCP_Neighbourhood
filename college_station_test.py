"""
college_station_demo.py
-----------------------
Demonstration of the Neighborhood Intelligence MCP Server focused on College Station, TX.
Evaluates multiple neighborhoods and provides individual and comparative AI analysis.
"""

import json
from server import evaluate
from openai import OpenAI
import os

# -------------------------------------------------------------------
# Setup
# -------------------------------------------------------------------
OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

# -------------------------------------------------------------------
# Input: 3 Neighborhoods within College Station
# -------------------------------------------------------------------
locations = [
    {
        "address": "Southwood Valley, College Station, Texas",
        "goals": "Evaluate for young families seeking good schools, safety, and affordability."
    },
    {
        "address": "Wolf Pen Creek District, College Station, Texas",
        "goals": "Assess suitability for students and young professionals wanting nightlife and walkability."
    },
    {
        "address": "Pebble Creek, College Station, Texas",
        "goals": "Evaluate for mid-career professionals seeking suburban living with access to parks and amenities."
    },
]

print("🏙️ College Station Neighborhood Intelligence Demo")
print("=" * 95)

results = []

for loc in locations:
    print(f"\n🔍 Evaluating: {loc['address']}")
    try:
        evaluation = evaluate(loc["address"], loc["goals"])
        results.append({
            "address": loc["address"],
            "goals": loc["goals"],
            "evaluation": evaluation
        })
        print(json.dumps(evaluation, indent=2))
    except Exception as e:
        print(f"⚠️ Error evaluating {loc['address']}: {e}")
    print("-" * 95)

# -------------------------------------------------------------------
# Comparative AI Summary
# -------------------------------------------------------------------
print("\n🤖 Running Multi-Neighborhood Comparative Analysis via Claude 3.5 Sonnet...")
summary_prompt = f"""
You are an expert urban analyst comparing neighborhoods within College Station, TX.
You have evaluation data for three neighborhoods:

1️⃣ Southwood Valley
{results[0]}

2️⃣ Wolf Pen Creek District
{results[1]}

3️⃣ Pebble Creek
{results[2]}

Compare them on:
- Livability & quality of life
- Affordability & housing
- Access to schools, parks, and amenities
- Commute convenience
- Ideal resident profile

Provide a structured report:
1. Overview of each neighborhood (1–2 lines each)
2. Comparative insights (who each area suits best)
3. A ranked list (1st, 2nd, 3rd) based on overall livability
4. End with “🏆 Best Overall Neighborhood: ____”
"""

if not OPENROUTER_API_KEY:
    print("\n⚠️ No OPENROUTER_API_KEY found. Skipping AI comparison.")
else:
    comparison = client.chat.completions.create(
        model="anthropic/claude-3.5-sonnet",
        messages=[
            {"role": "system", "content": "You are an expert urban planning and livability analyst."},
            {"role": "user", "content": summary_prompt},
        ],
    )

    print("\n🏁 Comparative AI Summary:\n")
    print(comparison.choices[0].message.content)

print("\n✅ College Station Comparative Demo Complete.")
