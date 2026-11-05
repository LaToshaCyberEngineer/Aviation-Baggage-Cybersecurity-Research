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

# Step 4: Simulate the network processing queue

# Set the simulated network conditions

buffer_capacity = 6
delivery_capacity = 2

# Create a list to save the processing results

queue_results = []

# Process each DoS disruption separately

for disruption_id, group in dos_scans.groupby("disruption_id"):

    # Identify the disruption duration

    outage_minutes = int(group["disruption_minutes"].iloc[0])

    # Create an empty queue for waiting scans

    waiting_scans = []

    # Process the network one minute at a time

    for minute in range(outage_minutes + 10):

        # Identify scans arriving during this minute

        new_scans = group[
            group["scenario_arrival_minute"] == minute
        ]

        # Place arriving scans into the buffer

        for _, scan in new_scans.iterrows():

            if len(waiting_scans) < buffer_capacity:

                waiting_scans.append((
                    scan["scan_id"],
                    scan["bag_id"],
                    minute
                ))

            else:

                # Record scans lost when the buffer is full

                queue_results.append({
                    "disruption_id": disruption_id,
                    "scan_id": scan["scan_id"],
                    "bag_id": scan["bag_id"],
                    "status": "Lost",
                    "delay_minutes": None
                })

        # Communication is unavailable during the outage

        if minute < outage_minutes:
            available_capacity = 0

        else:
            available_capacity = delivery_capacity

        # Deliver waiting scans when capacity is available

        for _ in range(min(available_capacity, len(waiting_scans))):

            scan_id, bag_id, arrival_minute = waiting_scans.pop(0)

            delay = minute - arrival_minute

            queue_results.append({
                "disruption_id": disruption_id,
                "scan_id": scan_id,
                "bag_id": bag_id,
                "status": "Delivered",
                "delay_minutes": delay
            })


# Create the simulation results table

queue_data = pd.DataFrame(queue_results)


# Review the operational results

print("\nOperational queue results:")

print(queue_data["status"].value_counts())

print("\nTotal processed scans:", len(queue_data))

print(
    "Unique scans:",
    queue_data["scan_id"].nunique()
)

# Calculate the average delay for delivered scans

average_delay = queue_data.loc[
    queue_data["status"] == "Delivered",
    "delay_minutes"
].mean()

print(
    "Average delivery delay:",
    round(average_delay, 2),
    "minutes"
)

# Confirm every affected scan has an outcome

print(
    "All affected scans accounted for:",
    len(queue_data) == 75
    and queue_data["scan_id"].nunique() == 75
)

print("\nStep 4 complete.")


# Step 5: Connect cybersecurity detection results

# Load the existing DoS detection decisions

alerts_file = "09_H3_Results/h3_adaptive_detection_decisions.csv"

alerts = pd.read_csv(alerts_file)

# Confirm each disruption has one detection record

if alerts["disruption_id"].duplicated().any():
    raise ValueError("Duplicate disruption IDs found.")

# Connect the detection decisions to RFID scans

connected_scans = dos_scans.merge(
    alerts,
    on="disruption_id",
    how="left",
    validate="many_to_one"
)

# Check for missing detection decisions

if connected_scans[["rule_alert", "ml_alert"]].isna().any().any():
    raise ValueError("Some disruptions have no detection result.")

# Display the results

print("\nCybersecurity detection summary:")

print(alerts.to_string(index=False))

print("\nTraditional rule alerts:", alerts["rule_alert"].sum())

print("Machine learning alerts:", alerts["ml_alert"].sum())

print("RFID scans connected:", len(connected_scans))

print("\nStep 5 complete.")
