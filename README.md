# Automated Analytics Dashboard
gk-mokaya |kevinmokaya001@gmail.com |+254 797 252 133

## Description
This project is an Automated Analytics Dashboard built with Streamlit. It provides a user-friendly interface for data-driven decision making through descriptive and predictive analytics, along with an AI-powered chatbot for interactive data queries. The app includes user authentication powered by Supabase.

## Features
- User authentication (Sign up, Login, Logout) using Supabase
- Descriptive Analytics dashboard with interactive visualizations
- Predictive Analytics dashboard for forecasting and insights
- AI-powered chatbot for asking questions about the data
- Multiple visualization libraries used: Plotly, Seaborn, Altair, Matplotlib

## Technologies Used
- Python
- Streamlit
- Supabase (for authentication)
- Pandas, NumPy
- Plotly, Seaborn, Altair, Matplotlib
- Scikit-learn
- Other supporting libraries as listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd kskanalytics/Analytics-Dashboard
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the App

Run the Streamlit app using the following command:
```
streamlit run 1_👨‍💻Main.py
```

This will launch the app in your default web browser.

## Project Structure

```
Analytics-Dashboard/
├── 1_👨‍💻Main.py               # Main Streamlit app with authentication
├── pages/
│   ├── 2_📊Descriptive_Analytics.py  # Descriptive analytics page
│   ├── 3_📈Predictive_Analytics.py    # Predictive analytics page
│   ├── 4_®️Ask_KSK_Chatbot.py         # Chatbot page
│   └── add_data.p                     # Additional data file
├── static/
│   └── logod.png                     # Logo image
├── dataksk.csv                      # Dataset file
├── dataksk1.csv                     # Dataset file
├── requirements.txt                 # Python dependencies
├── Pipfile                         # Pipenv dependencies
└── .gitignore                      # Git ignore file
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
