# U.S. Unemployment Data Trends

An analytical overview of how unemployment rates in the U.S. have evolved across decades, with emphasis on major disruptions like the 2008 global financial crisis and the COVID-19 pandemic.

## Description

This project explores monthly U.S. unemployment data sourced from the Federal Reserve Economic Data (FRED). Using Python and pandas, the analysis uncovers economic patterns, evaluates employment stability by decade, and highlights the labor market response during notable downturns. The work emphasizes statistical rigor and clean, reproducible code, offering a useful foundation for data-driven economic insight.

## Getting Started

### Dependencies

- Python 3.10+
- pandas
- Jupyter Notebook (recommended for interactive use)
- Platform: Windows, macOS, or Linux

### Installing

Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/us-unemployment-trends
cd us-unemployment-trends
```

(Optional) Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate
```

Install required packages:
```bash
pip install -r requirements.txt
```

### Executing Program

To run the script:
```bash
python analyze_unemployment.py
```

Or launch the notebook:
```bash
jupyter notebook unemployment_analysis.ipynb
```

## Results

The analysis generated the following key insights:

### General Statistics

- **Overall Mean Unemployment Rate**: 5.68%
- **Historical Minimum**: 2.5% (May–June 1953)
- **Historical Maximum**: 14.8% (April 2020)

### 2008 Financial Crisis (GFC)

- **Time Period Analyzed**: July 2007 – June 2010
- **Peak Unemployment Rate**: 10.0% (October 2009)
- **Average Rate During GFC**: ~7.44%

### COVID-19 Pandemic

- **Time Period Analyzed**: February 2020 – April 2023 
- **Peak Unemployment**: 14.8% (April 2020)
- **Average Rate During Pandemic Period**: ~5.53%

### Most Stable Decade

- The **1990s** had the lowest standard deviation in unemployment (1.05), indicating relative labor market stability.

### Long-Term Observations

- U.S. unemployment rates follow a recurring cyclical pattern.
- Crisis periods (like 2008 and 2020) create rapid surges, followed by gradual declines.
- Long-term stability has improved in recent decades despite short-term shocks.

Visualizations were created to support these findings and are included in the project repository.

---

## Help

If the script fails to run, confirm your environment is active and dependencies are properly installed:
```
pip list
```

## Author

Lama A.  
[@Lama-github](https://github.com/Englama1)

## Version History

* 0.2  
  - Refined visualizations and updated summary metrics  
  - See [commit history](https://github.com/your-username/us-unemployment-trends/commits)

* 0.1  
  - Initial dataset exploration and structure setup


## Resources

Useful guides and resources that helped shape this project:
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [dbader](https://github.com/dbader/readme-template)


## GenAI Usage Acknowledgment

ChatGPT was used during the development of this project to support the following tasks:

- Improving sentence clarity and grammar in documentation files (`README.md`, `results.txt`)
- Formatting and organizing section headings and code blocks in a clean, readable style
- Suggesting titles and labels for plots, such as highlighting peaks in unemployment trends
- Summarizing and rewriting background context on the COVID-19 pandemic and the 2008 financial crisis to enhance analytical explanations

All code and final outputs were reviewed and executed independently to ensure accuracy.