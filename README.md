# Custom_MCP_Neighbourhood
A comprehensive Model Context Protocol server that transforms AI assistants into intelligent neighborhood analysts by fetching and aggregating real-world location data from multiple APIs.
# Purpose
The Neighborhood Intelligence MCP Server enables AI models to provide data-driven insights about any location by automatically gathering and synthesizing information from over 10 different data sources. Whether you're relocating, investing in real estate, or simply exploring a new area, this server transforms a simple address query into a comprehensive neighborhood analysis.
Key Capabilities:

Smart Context Assembly: Automatically determines what data is relevant for location analysis
Multi-Source Integration: Aggregates weather, crime statistics, housing prices, walkability scores, air quality, and more
AI-Powered Evaluation: Uses Claude 3.5 Sonnet to synthesize raw data into actionable insights
Comparative Analysis: Can evaluate and compare multiple neighborhoods side-by-side

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
# Configuration


Create a .env file or export environment variables:

# Required for AI evaluation
export OPENROUTER_API_KEY="sk-or-v1-..."

# Required for functionality
export GOOGLE_MAPS_API_KEY="AIza..."
export WALKSCORE_API_KEY="..."
export RAPIDAPI_KEY="..."
export AIR_QUALITY_API_KEY="..."

# Optional fallback key
export ATTOM_API_KEY="..."

