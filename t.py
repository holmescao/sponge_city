import datetime

time_step = 1/60
start_dt = datetime.datetime.strptime("2021-05-25 00:01","%Y-%m-%d %H:%M")
end_dt = datetime.datetime.strptime("2021-06-29 00:00","%Y-%m-%d %H:%M")
time_delta = end_dt - start_dt
total_min = time_delta.days *24 *60 + time_delta.seconds // 60 + 1
step_per_min = 1/time_step/60
time_num = total_min *step_per_min
print(total_min)

import pandas as pd

dates = pd.date_range(start=start_dt,end=end_dt,freq='min')
indice_num = len(dates)//4
show_dates = dates[::indice_num]
show_dates = [str(show_dates[i])[:-3] for i in range(4)]
print(show_dates)
