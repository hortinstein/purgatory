import time
from datetime import datetime, timedelta
from tqdm import tqdm

# Start and end dates
start_date = datetime(2009, 5, 8)
end_date = start_date + timedelta(days=20*365)  # 20 years later

# Current date
current_date = datetime.now()

# Total number of seconds in the period
total_seconds = int((end_date - start_date).total_seconds())

# Number of seconds elapsed until now
elapsed_seconds = int((current_date - start_date).total_seconds())

# Function to get days and months left
def get_time_left(seconds_left):
    days_left = seconds_left // 86400
    months_left = days_left // 30
    return days_left, months_left

# Main function to show the progress bar
def main():
    with tqdm(total=total_seconds, initial=elapsed_seconds, desc="Progress", unit="s", dynamic_ncols=True) as pbar:
        for elapsed in range(elapsed_seconds, total_seconds + 1):
            days_left, months_left = get_time_left(total_seconds - elapsed)
            pbar.set_description(f'Days left: {days_left} | Months left: {months_left} | Progress')
            pbar.update(1)
            time.sleep(1)

if __name__ == "__main__":
    main()
