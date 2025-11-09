"""
compare_demo.py
----------------
Demonstration of the Neighborhood Intelligence MCP Server using comparative analysis.
It evaluates multiple neighborhoods and then performs an AI-driven comparison.
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
# Input: Two neighborhoods
# -------------------------------------------------------------------
locations = [
    {
        "address": "Downtown Austin, Texas",
        "goals": "Find an ideal area for young professionals with good amenities and nightlife."
    },
    {
        "address": "New Orleans, Louisiana",
        "goals": "Find an affordable, family-friendly neighborhood with schools and lower rent."
    }
]

print("🏙️ Comparative Neighborhood Intelligence Demo")
print("=" * 90)

results = []

for loc in locations:
    print(f"\n🔍 Evaluating: {loc['address']}")
    evaluation = evaluate(loc["address"], loc["goals"])
    results.append({
        "address": loc["address"],
        "goals": loc["goals"],
        "evaluation": evaluation
    })
    print(json.dumps(evaluation, indent=2))
    print("-" * 90)

# -------------------------------------------------------------------
# Comparative Analysis
# -------------------------------------------------------------------
print("\n🤖 Running AI Comparative Analysis via Claude 3.5 Sonnet...")
summary_prompt = f"""
You are an AI urban analyst comparing neighborhoods.
Compare the following two evaluations based on livability, affordability, commute, and amenities.

Neighborhood A:
{results[0]}

Neighborhood B:
{results[1]}

Provide a clear, structured comparative summary:
- Overall score for each
- Which neighborhood suits which user type (e.g., students, families, professionals)
- One-line recommendation for each
- Conclude with: 'Best Overall Choice: ____'
"""

if not OPENROUTER_API_KEY:
    print("\n⚠️ No OPENROUTER_API_KEY found. Skipping AI comparison.")
else:
    comparison = client.chat.completions.create(
        model="anthropic/claude-3.5-sonnet",
        messages=[
            {"role": "system", "content": "You are an expert real estate and urban data analyst."},
            {"role": "user", "content": summary_prompt},
        ],
    )

    print("\n🏁 Comparative AI Summary:\n")
    print(comparison.choices[0].message.content)

print("\nComparative Demo Complete.")
