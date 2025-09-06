# nutritional_assistant

🍽️ Nutritional Assistant

The Nutritional Assistant is an AI-powered tool that helps users discover recipes tailored to their personal profile, preferences, allergies, and nutritional needs.
It not only suggests recipes but also calculates the calorie contribution and compares it against daily recommended intake based on the user’s age, gender, region, and weight goals.

🚀 Features

✅ Personalized recipe suggestions based on:

Age, gender, height, weight

Allergies and disliked foods

Regional dietary guidelines (e.g., Belgium/Europe calorie intake)

✅ Fetches recipes from the web and extracts details automatically

✅ Provides step-by-step instructions for each recipe

✅ Displays nutritional breakdown per serving

✅ Estimates calorie contribution toward daily intake

✅ Easy execution using uv

📦 Installation

Clone the repository:

git clone https://github.com/your-username/nutritional_assistant.git
cd nutritional_assistant


Set up your environment with uv
:

uv venv
uv add openai-agents==0.2.4
uv add openai==1.99.1
uv add tavily-python

▶️ Usage

Run the assistant using uv:

uv run python main.py


Example execution:

(nutritional_assistant) PS C:\Users\exp260\nutritional_assistant> uv run python .\main.py
[TOOL CALLING ... ] Search Recipe...
[TOOL...] Extracting content from URLs: [...]

🍴 Example Recipe Output
Halal Cart Chicken Salad

A delicious and halal-friendly Halal Cart Chicken Salad tailored for:

Farrukh, 35 years old, male, 178 cm tall, 75 kg

Allergies: nuts, broccoli

Recipe Highlights:

Crisp iceberg lettuce base

Spiced shredded rotisserie chicken

Creamy yogurt dressing

Served with pita chips

Nutritional Value (per serving):

Nutrient	Amount	Recommended (Male, 30–59 yrs, EU)
Calories	550–650 kcal	2400–3000 kcal
Protein	45–55 g	56 g
Fat	35–45 g	70–100 g
Carbohydrates	20–30 g	300–400 g
Fiber	3–5 g	30 g

➡️ This dish provides ~600 kcal, making up a solid portion of daily energy needs, with excellent protein for muscle repair, healthy fats, and moderate carbs for energy.


<img width="1387" height="639" alt="image" src="https://github.com/user-attachments/assets/eea77d59-e001-433d-b922-bc2fb7863df8" />


