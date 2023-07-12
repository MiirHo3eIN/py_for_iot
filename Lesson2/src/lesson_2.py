import pandas as pd 
import matplotlib.pyplot as plt

"""
    This script contains the solutions for the exercise of the second lesson of the course "Python for IoT data analysis"

"""



def main():
    
    path = "../data/bejing_air_quality.csv"
    df_ = pd.read_csv(path, sep=",")
    

    # 1. Load the dataset into a Pandas DataFrame. Create a DateTimeIndex by properly merging the columns “year”, “month”, “day”, “hour”
    df_.index = pd.to_datetime(df_[["year", "month", "day", "hour"]])
    print(df_.head())
    # 2. Filter the samples from Jan 2014 to Jan 2017.
    time_mask = (df_.index > pd.to_datetime("2014-01-01")) & (df_.index < pd.to_datetime("2017-01-01"))
    df_ = df_[time_mask] 
    print(df_.head()) 
    print(df_.tail())
    # 3. By applying the undersampling technique, compute the weekly average of the "PM2.5" sensor.
    df_weekly = df_["PM2.5"].resample("W").mean()
    # 3-B. Plot the result.
    #df_weekly.plot(label = "Weekly average", legend=True)
    # 4. By applying the undersampling technique, compute the monthly average of the "PM2.5" sensor.
    df_monthly = df_["PM2.5"].resample("M").mean()
    # 4-B. Plot the result.
    #df_monthly.plot(label = "Monthly average", legend=True)
    # 5. By applying the moving average technique, compute the average of the "PM2.5" sensor, with a window size equal to 30 days. 
    df_moving_avg = df_["PM2.5"].rolling("30D").mean()
    # 5-B. Plot the result.
    #df_moving_avg.plot(label = "Moving average", legend=True)
    # 6. Compute on a monthly base the number of environmental alerts. An alert is triggered when the value of the "PM2.5" sensor is higher than a threshold (set to 50 µg/mc). 
    env_alert_mask = df_["PM2.5"] > 50
    df_alerts = df_[env_alert_mask]["PM2.5"].resample("M").count()
    # 6-B. Plot the result.
    #df_alerts.plot(label = "# of Events", legend=True)
    # 7. Shift the Time series of "PM2.5" sensor of 2000 samples forward in 5me. 
    df_shifted = df_["PM2.5"].shift(2000)
    # 7-B.Plot the original and the shiWed 5me series. 
    df_["PM2.5"].plot(label = "Original", legend=True)
    df_shifted.plot(label = "Shifted", legend=True)
    
    plt.show()


if __name__ == "__main__":
    main()