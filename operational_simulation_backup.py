# Operational RFID baggage tracking simulation

# Load the library

import pandas as pd


# Connect to the prepared RFID dataset

rfid_file = "06_Prepared_Data/02_Prepared_RFID_Data.csv"

rfid_data = pd.read_csv(rfid_file)

print("RFID data connected.")


# Create a copy of the affected RFID scans

dos_scans = rfid_data[
    rfid_data["disruption_window"] == 1
].copy()


# Convert scan timestamps into dates and times

dos_scans["timestamp"] = pd.to_datetime(
    dos_scans["timestamp"],
    errors="coerce"
)


# Check that all timestamps are valid

missing_times = dos_scans["timestamp"].isna().sum()

print("Invalid scan timestamps:", missing_times)

if missing_times > 0:
    raise ValueError("Some scan timestamps could not be read.")


# Sort the records by disruption and scan time

dos_scans = dos_scans.sort_values(
    ["disruption_id", "timestamp"]
)


# Find the first affected scan in each disruption

dos_scans["first_scan_time"] = dos_scans.groupby(
    "disruption_id"
)["timestamp"].transform("min")


# Calculate each scan's arrival time in minutes
# Minute zero is the first affected scan in its disruption

dos_scans["arrival_minute"] = (
    (
        dos_scans["timestamp"]
        - dos_scans["first_scan_time"]
    ).dt.total_seconds() / 60
).round().astype(int)


# Review the arrival times for each disruption

scan_summary = dos_scans.groupby(
    "disruption_id"
).agg(
    affected_scans=("scan_id", "count"),
    first_arrival=("arrival_minute", "min"),
    last_arrival=("arrival_minute", "max"),
    disruption_minutes=("disruption_minutes", "first")
).reset_index()


# Display the results

print("\nRFID scan arrival summary:")

print(scan_summary.to_string(index=False))

print("\nTotal affected scans:", len(dos_scans))

print("Disruption groups:", dos_scans["disruption_id"].nunique())

print("\nStep 2 complete.")

# Step 3: Prepare the simulation arrival times

# Find the last arrival time in each disruption group

last_scan_minute = dos_scans.groupby(
    "disruption_id"
)["arrival_minute"].transform("max")


# Create a separate simulation time for each scan
# Keep the original timestamps unchanged

dos_scans["scenario_arrival_minute"] = (
    dos_scans["arrival_minute"]
    / last_scan_minute
    * (dos_scans["disruption_minutes"] - 1)
).round().astype(int)


# Review the simulated scan arrival times

scenario_summary = dos_scans.groupby(
    "disruption_id"
).agg(
    affected_scans=("scan_id", "count"),
    first_arrival=("scenario_arrival_minute", "min"),
    last_arrival=("scenario_arrival_minute", "max"),
    disruption_minutes=("disruption_minutes", "first")
).reset_index()


# Check that the simulated arrivals fit each disruption

valid_arrivals = (
    dos_scans["scenario_arrival_minute"]
    < dos_scans["disruption_minutes"]
).all()


# Display the results

print("\nSimulation arrival summary:")

print(scenario_summary.to_string(index=False))

print("\nAffected RFID scans:", len(dos_scans))

print("All arrivals within disruption windows:", valid_arrivals)

print("Original RFID records remain unchanged.")

print("\nStep 3 complete.")

# Step 3: Prepare the simulation arrival times

# Find the last arrival time in each disruption group

last_scan_minute = dos_scans.groupby(
    "disruption_id"
)["arrival_minute"].transform("max")


# Create a separate simulation time for each scan
# Keep the original timestamps unchanged

dos_scans["scenario_arrival_minute"] = (
    dos_scans["arrival_minute"]
    / last_scan_minute
    * (dos_scans["disruption_minutes"] - 1)
).round().astype(int)


# Review the simulated scan arrival times

scenario_summary = dos_scans.groupby(
    "disruption_id"
).agg(
    affected_scans=("scan_id", "count"),
    first_arrival=("scenario_arrival_minute", "min"),
    last_arrival=("scenario_arrival_minute", "max"),
    disruption_minutes=("disruption_minutes", "first")
).reset_index()


# Check that the simulated arrivals fit each disruption

valid_arrivals = (
    dos_scans["scenario_arrival_minute"]
    < dos_scans["disruption_minutes"]
).all()


# Display the results

print("\nSimulation arrival summary:")

print(scenario_summary.to_string(index=False))

print("\nAffected RFID scans:", len(dos_scans))

print("All arrivals within disruption windows:", valid_arrivals)

print("Original RFID records remain unchanged.")

print("\nStep 3 complete.")
