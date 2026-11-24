# Market Entry Case: Coffee Kiosk Location in Rome

**Question:** A specialty-coffee kiosk brand is entering Rome. Which of 8 districts should host its first kiosk?
**Answer:** Open in **Pigneto**: about 4,900 EUR profit per month and a 9.2-month payback on 45,000 EUR capex. It stays profitable even if footfall falls 20%.

Structured like a strategy-consulting case: **market sizing → district profit model → ranking → stress test → recommendation**.

## Assumptions (from the client brief)
| Driver | Value |
|---|---|
| Capture rate | 4% of daily footfall, shared equally with competitors (÷ competitors + 1) |
| Average ticket | 3.20 EUR, +0.60 where students ≥ 30% of footfall |
| Month | 30 trading days |
| Costs | rent + 4,200 EUR staff + 30% of revenue (COGS) |
| Capex | 45,000 EUR |

## Results

| District | Revenue / month (EUR) | Profit / month (EUR) | Profit at −20% footfall |
|---|---|---|---|
| **Pigneto** | 16,720 | **4,904** | 2,563 ✅ |
| San Lorenzo | 17,100 | 4,670 | 2,276 ✅ |
| Testaccio | 11,520 | 564 | −1,049 ❌ |
| EUR | 12,288 | 202 | −1,519 ❌ |
| Prati | 13,166 | −584 | −2,427 ❌ |
| Monti | 9,874 | −1,988 | −3,370 ❌ |
| Trastevere | 11,093 | −2,635 | −4,188 ❌ |
| Centro Storico | 10,752 | −6,474 | −7,979 ❌ |

## Insights
- **Footfall is not the answer.** Centro Storico has the most foot traffic (42,000/day) but the worst result: 14 competitors split the demand and rent is 9,800 EUR/month.
- **Students raise the ticket.** Both winners (Pigneto, San Lorenzo) have ≥ 30% students, which adds 0.60 EUR per order.
- **Only 2 districts survive a 20% demand shock.** Testaccio, #3 on base profit, turns loss-making, so it is a risky backup.

**Recommendation:** open in Pigneto; keep San Lorenzo as the second site. Next step: validate the 4% capture rate with a one-week footfall count before signing a lease.

## Run it
```bash
pip install -r requirements.txt
python case.py
```

**Tools:** Python 3, pandas
*District figures are illustrative.*
