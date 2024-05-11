# PostgreSQL Analysis: Tobacco Disparities Dashboard

## Summary Statistics Analysis

### Explanation
This analysis provides summary statistics for the tobacco disparities dataset, including the number of rows and average values for certain columns.

### SQL Queries

```sql
-- Summary Statistics
SELECT
    COUNT(*) AS num_rows,
    AVG("Cigarette Use Prevalence % (Focus group)") AS avg_cigarette_use_focus,
    AVG("Cigarette Use Prevalence % (Reference group)") AS avg_cigarette_use_reference,
    AVG("Disparity Value") AS avg_disparity_value
FROM
    tobacco_disparities;
```

### Results
- Number of rows: 38110
- Average cigarette use prevalence % (focus group): 19.79%
- Average cigarette use prevalence % (reference group): 19.79%
- Average disparity value: 1.30

### Interpretation
The average cigarette use prevalence among both the focus and reference groups is quite similar, indicating that there is not a significant difference in smoking prevalence between these groups on average.
The average disparity value of approximately 1.30 suggests that, on average, adults in the focus group (e.g., based on demographic characteristics) smoke cigarettes at a 30% higher rate compared to the reference group. This indicates potential disparities in cigarette smoking prevalence among different demographic groups.

## Data Distribution Analysis

### Explanation
This analysis examines the distribution of cigarette use prevalence among different demographic groups.

### SQL Queries

```sql
-- Data Distribution
SELECT
    "Cigarette Use Prevalence % (Focus group)",
    COUNT(*) AS frequency
FROM
    tobacco_disparities
GROUP BY
    "Cigarette Use Prevalence % (Focus group)";
```

### Results
Full table in Data Distribution Analysis.csv

| Cigarette Use Prevalence % (Focus group) | Frequency |
|------------------------------------------|-----------|
| 16.2                                     | 212       |
| 3                                        | 9         |
| 14                                       | 129       |
| 39.4                                     | 24        |
| 27.5                                     | 65        |
| ...                                      | ...       |

Analysis
1. **Range**: The prevalence of cigarette use among the focus group ranges from 2.1% to 61.5%.

2. **Distribution**: Most values are clustered around 10% to 20%, with some outliers at higher percentages. (reference distribution.ipynb for visualization)

3. **Common Levels**: Prevalence levels around 10% to 20% are more frequent.

4. **Variation**: There's significant variation in prevalence, suggesting disparities in smoking behavior among demographic groups.


## Correlation Analysis

### Explanation
This analysis explores correlations between different variables in the dataset.

### SQL Queries
```sql
-- Correlation Analysis
SELECT
    CORR("Cigarette Use Prevalence % (Focus group)", "Cigarette Use Prevalence % (Reference group)") AS correlation
FROM
    tobacco_disparities;
```

### Results
The correlation coefficient provided (-0.00017531446171648832) indicates a very weak correlation between the variables being analyzed. I.e there is little to no linear relationship between the variables.


## Time Series Analysis

### Explanation
Offer valuable insights into how certain variables, such as cigarette use prevalence percentages, evolve over time

### SQL Queries
```sql
-- Time Series Analysis
-- Trends over the years
SELECT
    Year,
    AVG("Cigarette Use Prevalence % (Focus group)") AS avg_cigarette_use_focus,
    AVG("Cigarette Use Prevalence % (Reference group)") AS avg_cigarette_use_reference
FROM
    tobacco_disparities
GROUP BY
    Year
ORDER BY
    Year;
```

### Results
Reference time series analysis.csv for full table

## Time Series Analysis

The following table shows the trends in cigarette use prevalence over the years for both the focus group and the reference group:

| Year | Average Cigarette Use Prevalence % (Focus Group) | Average Cigarette Use Prevalence % (Reference Group) |
|------|--------------------------------------------------|------------------------------------------------------|
| 2011 | 22.93                                            | 22.93                                                |
| 2012 | 22.37                                            | 22.37                                                |
| 2013 | 22.10                                            | 22.10                                                |
| 2014 | 21.24                                            | 21.24                                                |
| 2015 | 20.54                                            | 20.54                                                |
| 2016 | 20.17                                            | 20.17                                                |
| 2017 | 19.94                                            | 19.94                                                |
| 2018 | 19.26                                            | 19.26                                                |
| 2019 | 18.86                                            | 18.86                                                |
| 2020 | 17.80                                            | 17.80                                                |
| 2021 | 16.57                                            | 16.57                                                |
| 2022 | 15.92                                            | 15.92                                                |

These values represent the average cigarette use prevalence % for each year, calculated separately for the focus group and the reference group.

The data shows a steady decrease in cigarette use prevalence over time, with minor fluctuations, highlighting the importance of continued efforts to combat smoking.
