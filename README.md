# Athlete Monitoring Dashboard

A Python-based sports performance monitoring dashboard that visualizes training load, readiness, wellness and performance trends across multiple athletes.

## Objective

The purpose of this project is to transform longitudinal athlete monitoring data into a visual analytics workflow that helps identify trends and changes in athlete state.

## Data Flow

```text
Athlete Monitoring Data
          ↓
Data Validation
          ↓
Feature Engineering
          ↓
Rolling Metrics
          ↓
Trend Analysis
          ↓
Visualization
          ↓
Athlete Comparison
          ↓
Monitoring Decision
```

## Dataset

The sample dataset contains longitudinal observations from multiple athletes.

Variables include:

- Athlete
- Date
- Training load
- Sleep quality
- Wellness
- Readiness
- Performance

## Key Features

### Training Load Monitoring

The system visualizes training-load changes over time for each athlete.

### Readiness Monitoring

Readiness trends are plotted to identify changes in athlete preparedness.

### Wellness Monitoring

Wellness scores are tracked across observations.

### Performance Monitoring

Performance trends are visualized alongside athlete monitoring data.

### Rolling Averages

The system calculates rolling averages for:

- Training load
- Readiness
- Performance

These help reduce the influence of individual observations and highlight broader trends.

## Athlete Status

The system provides a basic monitoring classification.

```text
READY
CAUTION
REVIEW
```

The classification uses:

- Readiness
- Wellness
- Performance

It is intended for educational demonstration rather than validated athlete-risk assessment.

## Visualizations

The program generates:

```text
training_load_trend.png
readiness_trend.png
wellness_trend.png
performance_trend.png
athlete_comparison.png
```

## Output

The program generates:

```text
athlete_monitoring_summary.csv
```

The summary contains athlete-level:

- Average training load
- Maximum training load
- Average readiness
- Average wellness
- Average performance
- Minimum readiness
- Maximum performance

## Technologies

- Python
- Pandas
- Matplotlib
- CSV
- Time-series analysis
- Rolling averages
- Data visualization

## Installation

```bash
pip install pandas matplotlib
```

## Running the Project

Place the Python script and CSV dataset in the same directory.

Run:

```bash
python athlete_monitoring_dashboard.py
```

## Sports Science Applications

The workflow can support:

- Strength and conditioning
- Athlete monitoring
- Training-load monitoring
- Recovery monitoring
- Performance analysis
- Coaching support
- Sports analytics

## Important Limitation

The dataset is synthetic and the monitoring rules are simplified for educational purposes.

The dashboard should not be used as a standalone system for medical, injury or training-prescription decisions.

Real athlete monitoring should consider:

- Individual baselines
- Measurement reliability
- Training phase
- Competition schedule
- Athlete history
- Injury status
- Recovery
- Contextual factors
- Coach and sport-science expertise

## Future Development

Potential extensions include:

- GPS data
- Heart-rate data
- Force-plate data
- Jump testing
- Velocity-based training
- Acute and chronic load metrics
- Individual baselines
- Statistical process control
- Machine-learning predictions
- Interactive dashboards
- Streamlit
- Power BI
- Automated alerts
- AI decision support

## Skills Demonstrated

```text
Python
   ↓
Pandas
   ↓
Time-Series Data
   ↓
Rolling Averages
   ↓
Data Aggregation
   ↓
Visualization
   ↓
Athlete Monitoring
   ↓
Sports Performance Analytics
```

## Author

**Abhishek Tomar**

Strength & Conditioning | Sports Performance | Sports Analytics | Python

## License

MIT License