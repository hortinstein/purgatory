import time
import os
from datetime import datetime, timedelta

# Start and end dates
start_date = datetime(2009, 5, 8)
end_date = start_date + timedelta(days=20*365)  # 20 years later

# Function to format time breakdown
def get_time_breakdown(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    years = days // 365
    remaining_days = days % 365
    months = remaining_days // 30
    remaining_days = remaining_days % 30

    return years, months, remaining_days, hours, minutes, secs

# Function to create compact progress bar
def create_progress_bar(percentage, width=20):
    filled = int(width * percentage / 100)
    bar = '█' * filled + '░' * (width - filled)
    return bar

# Main function
def main():
    # Clear screen initially
    os.system('clear' if os.name != 'nt' else 'cls')

    total_seconds = int((end_date - start_date).total_seconds())

    while True:
        current_date = datetime.now()
        elapsed_seconds = int((current_date - start_date).total_seconds())

        # Check if we've reached the end
        if elapsed_seconds >= total_seconds:
            print("\n🎉 TIME'S UP! 🎉\n")
            break

        remaining_seconds = total_seconds - elapsed_seconds

        # Calculate breakdown
        years_left, months_left, days_left, hours_left, mins_left, secs_left = get_time_breakdown(remaining_seconds)
        years_elapsed, months_elapsed, days_elapsed, hours_elapsed, mins_elapsed, secs_elapsed = get_time_breakdown(elapsed_seconds)

        # Calculate percentage
        percentage = (elapsed_seconds / total_seconds) * 100

        # Progress bar
        bar = create_progress_bar(percentage, 25)

        # Clear screen and display
        os.system('clear' if os.name != 'nt' else 'cls')

        print("╔═══════════════════════════╗")
        print("║    PURGATORY TIMER        ║")
        print("╚═══════════════════════════╝")
        print(f"\n📅 Start: {start_date.strftime('%b %d, %Y')}")
        print(f"🏁 End:   {end_date.strftime('%b %d, %Y')}")
        print(f"⏰ Now:   {current_date.strftime('%b %d, %Y %H:%M:%S')}")

        print(f"\n[{bar}]")
        print(f"{percentage:.6f}% Complete")

        print("\n" + "─" * 30)
        print("⏳ TIME REMAINING:")
        print(f"  {years_left}y {months_left}m {days_left}d")
        print(f"  {hours_left}h {mins_left}m {secs_left}s")

        print("\n✓ TIME ELAPSED:")
        print(f"  {years_elapsed}y {months_elapsed}m {days_elapsed}d")
        print(f"  {hours_elapsed}h {mins_elapsed}m {secs_elapsed}s")

        print("\n" + "─" * 30)
        print("📊 STATS:")
        total_days = total_seconds // 86400
        elapsed_days = elapsed_seconds // 86400
        remaining_days = remaining_seconds // 86400

        print(f"  Days: {elapsed_days}/{total_days}")
        print(f"  Remaining: {remaining_days:,} days")
        print(f"  Per day: {86400:,} seconds")

        # Milestones
        if percentage >= 50 and percentage < 50.01:
            print("\n🎯 MILESTONE: Halfway there!")
        elif percentage >= 75 and percentage < 75.01:
            print("\n🎯 MILESTONE: 75% complete!")
        elif percentage >= 90 and percentage < 90.01:
            print("\n🎯 MILESTONE: 90% complete!")

        print("\n" + "─" * 30)

        time.sleep(1)

if __name__ == "__main__":
    main()
