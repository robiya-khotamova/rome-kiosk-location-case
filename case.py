"""
Market Entry Case: where should a specialty-coffee kiosk open its first site in Rome?
Author: Robiyabonu Khotamova
Structure: market sizing -> district profit model -> ranking -> stress test (-20% footfall) -> recommendation
"""
import pandas as pd

d = pd.read_csv("districts.csv")

# --- Client assumptions ---
CAPTURE = 0.04        # kiosk captures 4% of daily footfall, shared equally with competitors
BASE_TICKET = 3.2     # EUR per customer
STUDENT_PREMIUM = 0.6 # extra EUR where students >= 30% of footfall
DAYS = 30             # days per month
STAFF = 4200          # EUR staff cost per month
COGS = 0.3            # cost of goods sold, share of revenue
CAPEX = 45000         # EUR one-off investment

# --- Step 1: Demand & revenue ---
d["daily_customers"] = (d["daily_footfall"] * CAPTURE) / (d["competitors"] + 1)
d["ticket"] = BASE_TICKET + STUDENT_PREMIUM * (d["students_share"] >= 0.3)
d["revenue_m"] = d["daily_customers"] * d["ticket"] * DAYS

# --- Step 2: Profit ---
d["costs_m"] = d["rent_month"] + STAFF + (d["revenue_m"] * COGS)
d["profit_m"] = d["revenue_m"] - d["costs_m"]

# --- Step 3: Rank ---
ranked = d.sort_values("profit_m", ascending=False)
top3 = ranked["district"].head(3).tolist()

# --- Step 4: Stress test: footfall 20% lower (COGS falls with revenue, rent and staff don't) ---
rev_low = d["revenue_m"] * 0.8
profit_low = rev_low - (d["rent_month"] + STAFF + rev_low * COGS)
robust = d.loc[profit_low > 0, "district"].tolist()

# --- Step 5: Recommend ---
best = top3[0]
p = d.loc[d["district"] == best, "profit_m"].iloc[0]
payback = CAPEX / p
rec = f"Open in {best}: profit {p:,.0f} EUR/month, payback {payback:.1f} months."

if __name__ == "__main__":
    cols = ["district", "daily_customers", "ticket", "revenue_m", "costs_m", "profit_m"]
    print(ranked[cols].round(0).to_string(index=False), "\n")
    print("Top 3:", top3)
    print("Still profitable at -20% footfall:", robust)
    print(rec)
