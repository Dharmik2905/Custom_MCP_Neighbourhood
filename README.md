# Custom_MCP_Neighbourhood
A comprehensive Model Context Protocol server that transforms AI assistants into intelligent neighborhood analysts by fetching and aggregating real-world location data from multiple APIs.
# Purpose
The Neighborhood Intelligence MCP Server enables AI models to provide data-driven insights about any location by automatically gathering and synthesizing information from over 10 different data sources. Whether you're relocating, investing in real estate, or simply exploring a new area, this server transforms a simple address query into a comprehensive neighborhood analysis.

## Why Neighborhood Intelligence Matters
The Real Cost of Poor Location Decisions
The Relocation Crisis:
Americans move an average of 11.7 times in their lifetime, yet 44% express regret about their last housing decision within the first year. The primary reason? Inadequate neighborhood research before committing.
### Financial Impact:

The average cost of relocating (including moving, deposits, and transaction fees) ranges from $8,000 to $15,000
Property values can vary by 30-40% within a 2-mile radius in major metropolitan areas
A poor neighborhood choice can cost homeowners $50,000-$150,000 in lost equity over a 5-year period

### Quality of Life Statistics:

- Residents in walkable neighborhoods report 13% higher life satisfaction scores
- Crime rates can vary 10x between adjacent ZIP codes
- Commute times over 45 minutes are associated with 40% higher stress levels and increased divorce rates
- Air quality differences within a single city can reduce life expectancy by 1-3 years

### Key Capabilities
- **Smart Context Assembly** – Automatically determines what data is relevant for each query  
- **Multi-Source Integration** – Aggregates weather, crime, housing, walkability, and more  
- **AI-Powered Evaluation** – Uses *Claude 3.5 Sonnet* to synthesize raw data into actionable insights  
- **Comparative Analysis** – Evaluates and compares multiple neighborhoods side-by-side


---

## 🌐 Data Sources & APIs

| Data Source | Purpose | API Used |
|--------------|----------|-----------|
| **OpenStreetMap (Nominatim)** | Address geocoding & reverse lookup | Free |
| **Open-Meteo** | 3-day weather forecast | Free |
| **OpenAQ** | Air quality metrics | `AIR_QUALITY_API_KEY` |
| **RapidAPI – jgentes Crime Data** | Crime statistics & safety scores | `RAPIDAPI_KEY` |
| **RapidAPI – Zillow** | Housing prices, property info | `RAPIDAPI_KEY` |
| **Google Maps API** | Places, commute, nearby amenities | `GOOGLE_MAPS_API_KEY` |
| **Walk Score API** | Walkability ratings | `WALKSCORE_API_KEY` |
| **OpenRouter (Claude 3.5 Sonnet)** | AI contextual analysis | `OPENROUTER_API_KEY` |

---

##  Quick Start

###  Prerequisites
- Python 3.8+
- `pip` package manager
- Valid API keys (see Configuration)

###  Installation
```bash
#Clone the repository
git clone <your-repo-url>
cd neighborhood-intelligence-mcp

# Install dependencies
pip install mcp requests openai

```
## Configuration


Create a .env file or export environment variables:

### Required for AI evaluation
export OPENROUTER_API_KEY="sk-or-v1-..."

### Required for functionality
export GOOGLE_MAPS_API_KEY="AIza..."
export WALKSCORE_API_KEY="..."
export RAPIDAPI_KEY="..."
export AIR_QUALITY_API_KEY="..."

### Optional fallback key
export ATTOM_API_KEY="..."

# Running Server 
# Standalone mode
python server.py

# Or integrate with Claude Desktop
# Add to your MCP settings configuration
`

---

## Example Prompts

When integrated with Claude Desktop, try these queries:

- "Evaluate the neighborhood around 123 Main Street, Austin, TX for a family with young children"
- "Compare the walkability of Downtown Dallas vs Uptown Dallas"
- "What's the air quality and crime rate near Central Park, New York?"
- "I'm moving to Houston for work at the Texas Medical Center. Find me a safe, affordable neighborhood within 30 minutes."

---

## Available Tools

| Tool | Description | Parameters |
|------|-------------|------------|
| `geocode` | Convert address to coordinates | `address` |
| `weather` | 3-day weather forecast | `lat`, `lon` |
| `air_quality` | AQI metrics | `lat`, `lon` |
| `walkability` | Walk Score & OSM density | `lat`, `lon`, `address` |
| `crime_data` | Safety metrics | `lat`, `lon` |
| `housing` | Market data | `lat`, `lon`, `address` |
| `commute` | Commute analysis | `lat`, `lon`, `destination` |
| `amenities` | Nearby schools, parks, stores | `lat`, `lon`, `type` |
| `demographics` | Income, education, density | `lat`, `lon` |
| `evaluate` | Full AI-powered neighborhood evaluation | `address`, `goals` |

---

## Architecture
┌─────────────────────────────────────────────────────────────────┐
│                         🏗️ ARCHITECTURE                         │
└─────────────────────────────────────────────────────────────────┘

                          👤 User Query
                                │
                                ↓
                      ┌─────────────────────┐
                      │  🏗️ MCP Server       │
                      │    (server.py)       │
                      └─────────────────────┘
                                │
                                ↓
        ┌───────────────────────────────────────────────┐
        │     ⚙️  Context Assembly Engine               │
        │  ┌─────────────────────────────────────────┐  │
        │  │  1. 📍 Geocode Address                  │  │
        │  │  2. 🎯 Determine Needed Data Sources    │  │
        │  │  3. ⚡ Fetch Data in Parallel           │  │
        │  │  4. 🛡️  Handle API Failures Gracefully  │  │
        │  └─────────────────────────────────────────┘  │
        └───────────────────────────────────────────────┘
                                │
                                ↓
        ┌───────────────────────────────────────────────┐
        │          📊 Data Sources (10+ APIs)           │
        ├───────────────────────────────────────────────┤
        │  ☀️  Weather  │  🚨 Crime    │  🏠 Housing    │
        │  🏫 Schools   │  🚇 Transit  │  🍽️  Dining    │
        │  💼 Demographics │ 🏥 Health │  🎭 Culture   │
        │  🌳 Parks     │  📈 Trends   │  ... More     │
        └───────────────────────────────────────────────┘
                                │
                                ↓
        ┌───────────────────────────────────────────────┐
        │         🤖 AI Evaluation Layer                │
        │                                               │
        │    Claude 3.5 Sonnet synthesizes raw data    │
        │         into actionable insights              │
        │                                               │
        │  • Identifies patterns                        │
        │  • Contextualizes statistics                  │
        │  • Generates recommendations                  │
        └───────────────────────────────────────────────┘
                                │
                                ↓
                ┌───────────────────────────┐
                │    ✨ Output              │
                │                           │
                │  📄 Comprehensive         │
                │  Neighborhood Report      │
                └───────────────────────────┘
`

## Unique Features

### Intelligent Fallbacks
- Predictive housing prices if Zillow unavailable
- OSM walkability fallback when WalkScore fails
- Synthetic safety index when no crime data exists

### Multi-Source Walkability
- Combines Google Places, WalkScore, and OpenStreetMap density
- Provides a robust blended metric

### Real Crime Data (2024)
- Powered by `jgentes-crime-data`
- Provides total incidents, trend analysis, and severity scoring

### Comparative Analysis Mode
- `demo.py` evaluates multiple neighborhoods
- Uses Claude 3.5 Sonnet for natural-language comparative reports

---

## Sample Output
`
Running AI Comparative Analysis via Claude 3.5 Sonnet...

Comparative AI Summary:

Here's a structured comparison of Downtown Austin and North Dallas:

OVERALL SCORES:
Downtown Austin: 8.2/10
North Dallas: 7.0/10

BEST SUITED FOR:
Downtown Austin:
- Young professionals (25-35)
- Tech workers
- Singles/couples without children
- Nightlife enthusiasts
- Urban lifestyle seekers
- Higher income individuals

North Dallas:
- Young families
- Education-focused households
- Mid-career professionals
- Suburban-minded urbanites
- School-age children
- Those seeking balance of urban/suburban

CORE METRICS COMPARISON:
Housing Costs:
- Downtown Austin: Higher ($1,850 rent, $550k median home)
- North Dallas: Moderate ($1,600 rent, $375k median home)

Amenities:
- Downtown Austin: Strong entertainment, dining, cultural venues
- North Dallas: Strong educational facilities, family-oriented services

Safety:
- Both areas rate 7/10 for safety (based on available data)

ONE-LINE RECOMMENDATIONS:
Downtown Austin: "Ideal for young professionals seeking vibrant urban 
lifestyle with strong career opportunities, despite higher living costs."

North Dallas: "Solid choice for families prioritizing education and 
suburban qualities while maintaining urban conveniences."

Best Overall Choice: Downtown Austin
(Due to higher overall score, stronger amenities, and better alignment 
with current urban development trends.)


### Searching for best neighbourhood mode 

#### Input: check the college_station_test.py. Demonstration of the Neighborhood Intelligence MCP Server focused on College Station, TX.
Evaluates multiple neighborhoods and provides individual and comparative AI analysis.
#### Output:
Comparative AI Summary:

Here's your structured comparison of College Station neighborhoods:

1. NEIGHBORHOOD OVERVIEWS
- Southwood Valley: Established family-friendly area with strong educational infrastructure and moderate housing costs, though car-dependent
- Wolf Pen Creek District: [Limited data available]
- Pebble Creek: Upscale suburban development farther from town center, offering quiet living and good schools but requiring longer commutes

2. COMPARATIVE INSIGHTS
Southwood Valley:
- Best for: Young families, university staff
- Strengths: School proximity, 10-min campus commute
- Weaknesses: Poor walkability

Pebble Creek:
- Best for: Mid-career professionals, established families
- Strengths: Quieter environment, safety
- Weaknesses: 16-min commute, very car-dependent

Wolf Pen Creek:
- [Insufficient data for comparison]

3. RANKED BY OVERALL LIVABILITY
1️⃣ Southwood Valley (7.2/10)
- Better location
- Shorter commute
- More amenities nearby
- Same safety score as Pebble Creek

2️⃣ Pebble Creek (7.2/10)
- More suburban feel
- Longer commute
- Fewer nearby amenities
- Equal safety rating

3️⃣ Wolf Pen Creek District
- Unable to rank due to insufficient data

Key Differentiators:
- Location: Southwood Valley is more centrally located
- Commute: Southwood Valley (10 mins) vs Pebble Creek (16 mins)
- Amenities: Southwood Valley has better access to services
- Schools: Both areas have excellent schools
- Safety: Both rate 7/10
- Housing Costs: Similar in both areas ($285,000 median)

Best Overall Neighborhood: Southwood Valley
Reasoning: While both rated neighborhoods score 7.2/10, Southwood Valley edges out Pebble Creek due to its more convenient location, shorter commute times, and better access to amenities while maintaining the same safety rating and housing costs. It offers the best balance of family-friendly features and practical convenience for College Station residents.

College Station Comparative Demo Complete.

# Contributing
This project was developed for the Build-Your-Own-MCP Challenge @ TAMUDATATHON 2025.
We welcome contributions! Please submit pull requests or open issues for:

New data source integrations
Enhanced evaluation algorithms
Performance optimizations
Documentation improvements



# License
MIT License – Free to use, fork, and modify.

# Acknowledgments

Anthropic for MCP and Claude AI
OpenStreetMap for geospatial data
RapidAPI for housing and crime APIs
Google Maps and WalkScore for local metrics
OpenRouter for model orchestration


# Support
For issues, questions, or feature requests:

Open an issue on GitHub
Contact the development team
Check the documentation wiki
