import pandas as pd


INPUT_FILE = 'mpi_roof_2024.csv'
OUTPUT_FILE = 'weather_2024.csv'


def preprocess():
    print(f"Reading raw file: {INPUT_FILE}")

    # Use latin1 encoding to handle symbols
    try:
        df = pd.read_csv(INPUT_FILE, encoding='latin1')
    except FileNotFoundError:
        print(f"Error: Could not find {INPUT_FILE}. Please check the path.")
        return

    # Change 'Date Time' to 'date'
    if 'Date Time' in df.columns:
        print("Renaming 'Date Time' column to 'date'...")
        df.rename(columns={'Date Time': 'date'}, inplace=True)

    # Convert "DD.MM.YYYY" to standard ISO format
    print("Standardizing date format (this may take a moment)...")
    try:
        # Explicitly tell pandas the format is Day.Month.Year
        df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y %H:%M:%S')
    except ValueError:
        print("   (Standard parse failed, attempting flexible day-first parsing)")
        df['date'] = pd.to_datetime(df['date'], dayfirst=True)

    # Save as standard UTF-8 CSV
    print(f"Saving cleaned data to {OUTPUT_FILE}...")
    df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')

    print("\n[SUCCESS] Preprocessing complete!")
    print(f"New file created: {OUTPUT_FILE}")
    print(f"Rows: {len(df)}, Columns: {len(df.columns)}")


if __name__ == "__main__":
    preprocess()