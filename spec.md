# Data Analyzer Agent

## Project Summary
A coding agent that generates synthetic datasets, performs statistical analysis, and creates visualizations.

## Use Case
Data scientists and analysts who need quick exploratory analysis on synthetic data for prototyping and testing

## Use Case
Data scientists and analysts who need quick exploratory analysis on synthetic data for prototyping and testing.

## Runtime Inputs
- `dataset_type`: Type of data to generate ("sales", "weather", "users")
- `num_records`: Number of records to generate
- `analysis_type`: Type of analysis ("summary", "trends", "correlations")

## Agent Capabilities
- Generate synthetic datasets matching specified schema
- Perform statistical calculations (mean, median, std dev)
- Create visualizations (bar charts, line plots, scatter plots)
- Save results to files (CSV data, PNG charts, TXT reports)

## Tools
- **execute_code**: Run Python code for data generation and analysis
- **write_file**: Save datasets and reports
- **read_file**: Load previously generated data (optional)

## Expected Outputs
- `data.csv`: Synthetic dataset
- `analysis.txt`: Statistical summary report
- `chart.png`: Visualization (if plotting library available)
  
- ## Example Scenario
User requests: "Generate 100 sales records and analyze monthly trends"
1. Agent generates synthetic sales data (product, quantity, price, date)
2. Agent calculates monthly revenue totals
3. Agent creates trend visualization
4. Agent saves data.csv, analysis.txt, and chart.png