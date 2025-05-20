# Solar Challenge Week 1 - Streamlit Dashboard (Bonus)

This is the interactive dashboard for comparing solar metrics (GHI, DNI, DHI) across Benin, Sierra Leone, and Togo, built with Streamlit.

## Structure

```

app/
├─ main.py         # Streamlit app
├─ utils.py        # Helper functions
dashboard\_screenshots/  # Screenshots for submission
data/                  # Cleaned CSVs (gitignored)
requirements.txt       # Dependencies

```

## Features

- Select countries to compare
- Boxplots for GHI, DNI, DHI
- Summary table (mean, median, std)
- Top regions table
- Clean, interactive UI

## Run Locally

1. Clone repo and create venv  
2. Install requirements: `pip install -r requirements.txt`  
3. Add cleaned CSVs to `data/` folder  
4. Run: `streamlit run app/main.py`

## Notes

- Data files excluded from repo (in `.gitignore`)  
- Developed on `dashboard-dev` branch  
- Screenshots in `dashboard_screenshots/`

---

For questions, open an issue or contact me.

```

