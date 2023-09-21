import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Reading a dataset from a CSV file
def read_dataset(input_file_path):
    data_frame = pd.read_csv(input_file_path, skipinitialspace=True)
    data_frame.columns = (
        data_frame.columns.str.strip()
    )  # Remove any leading/trailing white spaces from column names
    return data_frame


# Generate summary statistics
def summary_statistics(input_df):
    # Only select the numeric columns
    numeric_df = input_df.select_dtypes(include=[np.number])

    mean_values = numeric_df.mean()
    median_values = numeric_df.median()
    std_dev_values = numeric_df.std()

    return {"mean": mean_values, "median": median_values, "std_dev": std_dev_values}


# Create a data visualization
def data_visualization(input_df, input_column_name):
    plt.hist(input_df[input_column_name])
    plt.title(f"Histogram of {input_column_name}")
    plt.xlabel(input_column_name)
    plt.ylabel("Frequency")
    plt.savefig(f"{input_column_name}_histogram.png")
    plt.show()


if __name__ == "__main__":
    # Replace this path with the path to your own CSV file
    file_path = "hurricanes.csv"

    df = read_dataset(file_path)

    # Calculate summary statistics for the "Average" column
    stats = summary_statistics(df[["Average"]])
    mean = stats["mean"]
    median = stats["median"]
    std_dev = stats["std_dev"]

    print("Mean:", mean)
    print("Median:", median)
    print("Standard Deviation:", std_dev)

    # Visualize the "Average" column
    data_visualization(df, "Average")

    # Generate summary report
    with open("summary_report.md", "w", encoding="utf-8") as f:
        f.write("# Summary Report\n")
        f.write("## Descriptive Statistics\n")
        f.write(f"### Mean:\n{mean}\n")
        f.write(f"### Median:\n{median}\n")
        f.write(f"### Standard Deviation:\n{std_dev}\n")
