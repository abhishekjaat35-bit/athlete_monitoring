import pandas as pd
import matplotlib.pyplot as plt


print("=" * 80)
print("              ATHLETE MONITORING DASHBOARD")
print("=" * 80)


# ------------------------------------------
# Load Data
# ------------------------------------------

data = pd.read_csv(
    "athlete_monitoring_dashboard_data.csv"
)

data["Date"] = pd.to_datetime(
    data["Date"]
)

data = data.sort_values(
    ["Athlete", "Date"]
).reset_index(drop=True)


# ------------------------------------------
# Data Validation
# ------------------------------------------

print("\n" + "=" * 80)
print("DATA VALIDATION")
print("=" * 80)

print(f"Rows           : {len(data)}")
print(f"Columns        : {len(data.columns)}")
print(
    f"Missing values : "
    f"{data.isnull().sum().sum()}"
)

print(
    f"Athletes       : "
    f"{data['Athlete'].nunique()}"
)


# ------------------------------------------
# Rolling Training Load
# ------------------------------------------

data["Load_7_Observation_Average"] = (
    data.groupby("Athlete")["Training_Load"]
    .transform(
        lambda x: x.rolling(
            window=7,
            min_periods=1
        ).mean()
    )
)


# ------------------------------------------
# Rolling Readiness
# ------------------------------------------

data["Readiness_7_Observation_Average"] = (
    data.groupby("Athlete")["Readiness_Score"]
    .transform(
        lambda x: x.rolling(
            window=7,
            min_periods=1
        ).mean()
    )
)


# ------------------------------------------
# Rolling Performance
# ------------------------------------------

data["Performance_7_Observation_Average"] = (
    data.groupby("Athlete")["Performance_Score"]
    .transform(
        lambda x: x.rolling(
            window=7,
            min_periods=1
        ).mean()
    )


# ------------------------------------------
# Training Load Change
# ------------------------------------------

data["Previous_Load"] = (
    data.groupby("Athlete")["Training_Load"]
    .shift(1)
)

data["Load_Change_%"] = (
    (
        data["Training_Load"]
        -
        data["Previous_Load"]
    )
    /
    data["Previous_Load"]
) * 100

data["Load_Change_%"] = (
    data["Load_Change_%"]
    .fillna(0)
)


# ------------------------------------------
# Athlete Status
# ------------------------------------------

def classify_status(row):

    readiness = row["Readiness_Score"]
    wellness = row["Wellness_Score"]
    performance = row["Performance_Score"]

    if (
        readiness >= 85
        and wellness >= 17
        and performance >= 88
    ):
        return "READY"

    elif (
        readiness >= 70
        and wellness >= 13
        and performance >= 80
    ):
        return "CAUTION"

    else:
        return "REVIEW"


data["Athlete_Status"] = data.apply(
    classify_status,
    axis=1
)


# ------------------------------------------
# Display Monitoring Data
# ------------------------------------------

print("\n" + "=" * 80)
print("ATHLETE MONITORING DATA")
print("=" * 80)

display_columns = [
    "Athlete",
    "Date",
    "Training_Load",
    "Readiness_Score",
    "Wellness_Score",
    "Performance_Score",
    "Athlete_Status"
]

print(
    data[display_columns]
    .to_string(index=False)
)


# ------------------------------------------
# Athlete Summary
# ------------------------------------------

summary = (
    data.groupby("Athlete")
    .agg(
        Observations=(
            "Athlete",
            "count"
        ),

        Average_Load=(
            "Training_Load",
            "mean"
        ),

        Maximum_Load=(
            "Training_Load",
            "max"
        ),

        Average_Readiness=(
            "Readiness_Score",
            "mean"
        ),

        Average_Wellness=(
            "Wellness_Score",
            "mean"
        ),

        Average_Performance=(
            "Performance_Score",
            "mean"
        ),

        Minimum_Readiness=(
            "Readiness_Score",
            "min"
        ),

        Maximum_Performance=(
            "Performance_Score",
            "max"
        )
    )
    .reset_index()
)


print("\n" + "=" * 80)
print("ATHLETE SUMMARY")
print("=" * 80)

print(
    summary.to_string(
        index=False,
        formatters={
            "Average_Load":
                "{:.1f}".format,

            "Average_Readiness":
                "{:.1f}".format,

            "Average_Wellness":
                "{:.1f}".format,

            "Average_Performance":
                "{:.1f}".format
        }
    )
)


# ------------------------------------------
# Latest Athlete Status
# ------------------------------------------

latest = (
    data.sort_values("Date")
    .groupby("Athlete")
    .tail(1)
)


print("\n" + "=" * 80)
print("LATEST ATHLETE STATUS")
print("=" * 80)

for _, row in latest.iterrows():

    print(
        f"{row['Athlete']:<12} "
        f"Load: {row['Training_Load']:>4.0f} AU | "
        f"Readiness: {row['Readiness_Score']:>3.0f}% | "
        f"Wellness: {row['Wellness_Score']:>2.0f}/20 | "
        f"Performance: {row['Performance_Score']:>3.0f} | "
        f"Status: {row['Athlete_Status']}"
    )


# ==========================================
# VISUALIZATIONS
# ==========================================


# ------------------------------------------
# Training Load Trend
# ------------------------------------------

plt.figure(figsize=(11, 6))

for athlete in data["Athlete"].unique():

    athlete_data = data[
        data["Athlete"] == athlete
    ]

    plt.plot(
        athlete_data["Date"],
        athlete_data["Training_Load"],
        marker="o",
        label=athlete
    )

plt.title(
    "Training Load Trend"
)

plt.xlabel("Date")
plt.ylabel("Training Load (AU)")

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "training_load_trend.png",
    dpi=300
)

plt.show()


# ------------------------------------------
# Readiness Trend
# ------------------------------------------

plt.figure(figsize=(11, 6))

for athlete in data["Athlete"].unique():

    athlete_data = data[
        data["Athlete"] == athlete
    ]

    plt.plot(
        athlete_data["Date"],
        athlete_data["Readiness_Score"],
        marker="o",
        label=athlete
    )

plt.title(
    "Athlete Readiness Trend"
)

plt.xlabel("Date")
plt.ylabel("Readiness Score (%)")

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "readiness_trend.png",
    dpi=300
)

plt.show()


# ------------------------------------------
# Wellness Trend
# ------------------------------------------

plt.figure(figsize=(11, 6))

for athlete in data["Athlete"].unique():

    athlete_data = data[
        data["Athlete"] == athlete
    ]

    plt.plot(
        athlete_data["Date"],
        athlete_data["Wellness_Score"],
        marker="o",
        label=athlete
    )

plt.title(
    "Athlete Wellness Trend"
)

plt.xlabel("Date")
plt.ylabel("Wellness Score")

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "wellness_trend.png",
    dpi=300
)

plt.show()


# ------------------------------------------
# Performance Trend
# ------------------------------------------

plt.figure(figsize=(11, 6))

for athlete in data["Athlete"].unique():

    athlete_data = data[
        data["Athlete"] == athlete
    ]

    plt.plot(
        athlete_data["Date"],
        athlete_data["Performance_Score"],
        marker="o",
        label=athlete
    )

plt.title(
    "Athlete Performance Trend"
)

plt.xlabel("Date")
plt.ylabel("Performance Score")

plt.legend()

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "performance_trend.png",
    dpi=300
)

plt.show()


# ------------------------------------------
# Athlete Comparison
# ------------------------------------------

comparison = summary.set_index(
    "Athlete"
)[
    [
        "Average_Load",
        "Average_Readiness",
        "Average_Wellness",
        "Average_Performance"
    ]
]


comparison.plot(
    kind="bar",
    figsize=(11, 6)
)

plt.title(
    "Athlete Monitoring Comparison"
)

plt.xlabel("Athlete")

plt.ylabel("Average Value")

plt.xticks(rotation=0)

plt.legend(
    [
        "Training Load",
        "Readiness",
        "Wellness",
        "Performance"
    ]
)

plt.tight_layout()

plt.savefig(
    "athlete_comparison.png",
    dpi=300
)

plt.show()


# ------------------------------------------
# Export Summary
# ------------------------------------------

summary.to_csv(
    "athlete_monitoring_summary.csv",
    index=False
)


# ------------------------------------------
# Final Output
# ------------------------------------------

print("\n" + "=" * 80)
print("DASHBOARD ANALYSIS COMPLETE")
print("=" * 80)

print("Generated files:")

print("1. athlete_monitoring_summary.csv")
print("2. training_load_trend.png")
print("3. readiness_trend.png")
print("4. wellness_trend.png")
print("5. performance_trend.png")
print("6. athlete_comparison.png")

print("\n" + "=" * 80)
print("MONITOR • VISUALIZE • INTERPRET • DECIDE")
print("=" * 80)