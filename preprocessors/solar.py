import pandas as pd
import os


# Directories
INPUT_FILE = 'data/solar-energy/solar_AL.txt'
OUTPUT_FILE = 'data/solar-energy/Alabama_137_Plants_2006.csv'

# Solar details
START_DATE = '2006-01-01 00:00:00'
FREQ = '10min'
EXPECTED_ROWS = 52560  # Total 10min intervals


def main():
    print(f"Reading raw data from: {INPUT_FILE}...")

    if not os.path.exists(INPUT_FILE):
        print(f"ERROR: File not found at {INPUT_FILE}")
        return

    # Read the raw text file
    try:
        df = pd.read_csv(INPUT_FILE, header=None)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    print(f"  -> Initial Shape: {df.shape}")

    # Auto-Transpose Logic
    if df.shape[0] != EXPECTED_ROWS and df.shape[1] == EXPECTED_ROWS:
        print("  -> Detected [Plants x Time] format. Transposing to [Time x Plants]...")
        df = df.T

    # Verify final shape
    if df.shape[0] != EXPECTED_ROWS:
        print(f"  WARNING: Expected {EXPECTED_ROWS} rows (time steps), but got {df.shape[0]}.")
        print("           Check if your input file is complete or if the frequency is correct.")

    # Rename columns to simple indices
    df.columns = [str(i) for i in range(df.shape[1])]

    # Generate and Insert Time Column
    print(f"  -> Generating timestamps for {START_DATE} ({FREQ})...")
    date_range = pd.date_range(start=START_DATE, periods=len(df), freq=FREQ)
    df.insert(0, 'date', date_range)

    # Save
    print(f"Saving to {OUTPUT_FILE}...")
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    df.to_csv(OUTPUT_FILE, index=False)
    print("Done! Here are the first 5 rows:")
    print(df.head())


if __name__ == "__main__":
    main()