import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def plot_data(df, ax, title):
    # Plot the data
    ax.plot(df.index, df['Gold_close'], label='Gold', color='gold')
    ax.plot(df.index, df['Silver_close'], label='Silver', color='silver')
    ax.plot(df.index, df['Nasdaq_close'], label='NASDAQ', color='blue')
    ax.plot(df.index, df['Spx_close'], label='S&P500', color='green')

    # Set plot properties
    ax.set_title(title)
    ax.set_ylabel('Close Price')
    ax.legend()
    ax.grid(True)

def add_annotations(df, ax):
    # Add labels at the end of each line
    labels = {'Gold_close': 'Gold', 'Silver_close': 'Silver', 'Nasdaq_close': 'NASDAQ', 'Spx_close': 'S&P500'}
    colors = {'Gold_close': 'gold', 'Silver_close': 'silver', 'Nasdaq_close': 'blue', 'Spx_close': 'green'}

    for col, label in labels.items():
        ax.annotate(
            label,
            xy=(df.index[-1], df[col].iloc[-1]),  # Position (end of the line)
            xytext=(10, 0),  # Offset for the text
            textcoords='offset points',
            fontsize=9,
            color='black'  # Color of the annotation text
        )

# Load the merged datasets
merged_df = pd.read_csv("merged_close_df.csv", parse_dates=["Date"], index_col="Date")
interpolated_df = pd.read_csv("merged_close_interpolated_df.csv", parse_dates=["Date"], index_col="Date")

# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Plot and annotate original merged dataset
plot_data(merged_df, axs[0], 'Original Merged Dataset')
add_annotations(merged_df, axs[0])

# Plot and annotate interpolated dataset
plot_data(interpolated_df, axs[1], 'Interpolated Dataset')
add_annotations(interpolated_df, axs[1])
axs[1].set_xlabel('Date')

# Format the x-axis to show only years and mark every 4 years
for ax in axs:
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  # Format dates to show only the year
    ax.xaxis.set_major_locator(mdates.YearLocator(4))  # Place tick marks every 4 years
    plt.setp(ax.get_xticklabels(), rotation=45, ha='right')  # Rotate labels for better readability

# Show plots
plt.tight_layout()
plt.show()

