from datetime import datetime, timedelta, timezone
import pytz

Curren_date = datetime.now()

print(f"Current date and time is : {Curren_date}")

Yeserday = datetime.now() - timedelta(days=1)                         
print(f"Yesterdays date and time is : {Yeserday}")


d_m_y = Curren_date.strftime("%d-%m-%Y")                             #fromat date 
print(f"Date Month Year: {d_m_y} ")



#timezones = pytz.all_timezones
#print(timezones)

UTC = datetime.now(timezone.utc)

timezone = pytz.timezone('Asia/Kolkata')
print(f"Indian Time: {datetime.now(timezone)}")

timezone = pytz.timezone('Europe/Berlin')
print(f"German Time: {datetime.now(timezone)}")     




# Get Current Time in different Timezone using Python