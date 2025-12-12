import csv
import random
import datetime

def analyze_samples():
    # Simulate sample analysis
    samples = []
    for i in range(1, 11):
        sample_id = f"SAMP-{i:03d}"
        value = random.uniform(0.0, 100.0)
        status = "PASS" if value > 50 else "FAIL"
        samples.append([sample_id, datetime.datetime.now().isoformat(), value, status])

    # Write to CSV
    output_file = "analysis_results.csv"
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Sample ID", "Timestamp", "Value", "Status"])
        writer.writerows(samples)
    
    print(f"Analysis complete. Results saved to {output_file}")

if __name__ == "__main__":
    analyze_samples()
