import pytz
import sys
from datetime import datetime

def process_datetime(dt):
    print(f"✅ Valid datetime received: {dt}")
    utc_dt = datetime.strptime(utc_time_str, "%y-%m-%d %H:%M:%S.%f")
    utc_dt = pytz.utc.localize(utc_dt)
    # Convert to India timezone
    india_tz = pytz.timezone("Asia/Kolkata")
    india_dt = utc_dt.astimezone(india_tz)

    # Output
    print("India Time:", india_dt.strftime("%Y-%m-%d %H:%M:%S.%f"))
    

def main():
    if len(sys.argv) != 2:
        print("❌ Usage: python script.py 'dd-mm-yy HH:MM:SS.mmm'")
        sys.exit(1)

    input_str = sys.argv[1]

    try:
        # Format: '25-04-17 04:16:31.662'
        dt = datetime.strptime(input_str, "%d-%m-%y %H:%M:%S.%f")
        process_datetime(dt)
    except ValueError:
        print("❌ Invalid date-time format. Expected format: dd-mm-yy HH:MM:SS.mmm")

if __name__ == "__main__":
    main()
