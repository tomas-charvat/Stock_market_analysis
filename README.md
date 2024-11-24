# Stock Market Analysis and Visualizations

This project involves creating datasets and visualizations to analyze trends and relationships between various financial assets. The visualizations were made using Python for preprocessing and Tableau Public for the presentation.

---

## Line Chart Visualization

1. Downloaded daily data from [stooq.com](https://stooq.com) for gold, silver, Nasdaq, and S&P500.
2. Processed the data (`data_processing.ipynb`), checked for null values, and merged all files into one dataframe called `merged_close_df`.
3. Now that we have a dataset with only close prices, I used the `interpolate` function with the `linear` method to connect the prices on days where the assets were not traded to create a continuous line.
4. Created a quick line chart in `Line_chart.py` just to check for obvious mistakes.
5. Lastly, plotted the dataset in Tableau Public.
6. The goal was to show the overall trend and visually compare the returns of the four assets.

**[Link to visualization](https://public.tableau.com/app/profile/tom.charv.t/viz/Stockmarketanalysis_17324617995550/Dashboard1)**

---

## Gold and Silver Correlation

1. Used the gold and silver data from above.
2. Created a dataset with gold and silver prices.
3. Used `datetime` and `timedelta` to filter data for the past year.
4. Then used the `corr()` function to calculate the correlation with a 30-day rolling window between the two assets (2023-10-20 to 2024-09-10).
5. The final dataset is `final_corr_df.csv`.
6. The goal was to show the correlation for the past year and decide if u can make trading decisions based on the movement of 1 asset.

**[Link to visualization](https://public.tableau.com/app/profile/tom.charv.t/viz/Stockmarketanalysis_17324617995550/Dashboard1)**

---

## Metals vs Inflation

1. Downloaded data from [stooq.com](https://stooq.com) for metals and [FRED](https://fred.stlouisfed.org) for inflation data (yearly close prices).
2. Timeframe: 1990-2023.
3. Asked Claude.ai to adjust my inflation data because it was in a different date format than my metals data, as you can see in `inflation.csv` compared to `xauusd_y.csv`.
4. Processed the data to get one dataset with close prices and inflation (`inflation_vs_metals.csv`).
5. Goal was to visually compare the price progress of metals to inflation and see if there is any correlation.

**[Link to visualization](https://public.tableau.com/app/profile/tom.charv.t/viz/Stockmarketanalysis_17324617995550/Dashboard1)**

---

## Real Dollar Index vs Metals

1. Downloaded data from [stooq.com](https://stooq.com) for metals and [FRED](https://fred.stlouisfed.org) for real dollar index data (monthly close prices).
2. Timeframe: 2006-2023.
3. Processed the data in `data.ipynb` and got the final dataframe: `final_dollar_vs_metals.csv`.
4. Goal was to visually compare the relationship between metals and the real dollar index since they correlate with each other negatively.
5. Also, the goal was to show that you can make trading decisions (metals) based on what’s happening to the dollar strength index.

**[Link to visualization](https://public.tableau.com/app/profile/tom.charv.t/viz/Stockmarketanalysis_17324617995550/Dashboard1)**

---

## Heatmap Visualization

1. Created a dataset with:
   - Gold, silver, platinum, Crude Oil WTI - NYMEX (CL.F), S&P500, Nasdaq, copper (High Grade Copper - COMEX (HG.F)), iShares USD Treasury Bond 1-3yr UCITS ETF (IBTA.UK).
   - Time period: 2018-01-01 to 2023-01-01.
   - Source: [stooq.com](https://stooq.com), [investing.com](https://investing.com).
   - Using daily closes.
2. Processed the data in `heatmap.ipynb` and got the final correlation matrix using the `corr()` function.
3. Created heatmaps using the **Seaborn** library: `heatmap2.png`, `correlation_heatmap.png`.
4. Played with AI tools and heatmap settings to create a visualization I liked.
5. Goal was to show the correlation between various assets for trading purposes.

**[Link to visualization](https://public.tableau.com/app/profile/tom.charv.t/viz/Stockmarketanalysis_17324617995550/Dashboard1)**

