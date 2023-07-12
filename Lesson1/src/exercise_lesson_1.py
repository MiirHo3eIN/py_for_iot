import pandas as pd 


"""

    This script contains the solutions for the exercise of the first lesson of the course "Python for IoT data analysis"

"""


def main(): 
    # Path: ~/projects/phd_courses/Lesson1/data/bejing_air_quality.csv
    path = "../data/bejing_air_quality.csv"
    df_ = pd.read_csv(path, sep=",")

    # 1. Print the number of rows and columns of the dataset 
    print(f"Number of rows: {len(df_)} \t Number of columns: {len(df_.columns)}")
    # 2. Print the ﬁrst 24 rows of the dataset (and only columns: hour, PM2.5, PM10)
    print(f"Head of dataset is \n {df_[['hour', 'PM2.5', 'PM10']].head(24)}")
    # 3. Print the rainy samples (Rain value > 0).
    print(df_[df_["RAIN"] > 0])
    # 4. Print a tuple containing the max and min value of the PM2.5 column.
    print((df_["PM2.5"].max(), df_["PM2.5"].min()))
    # 5. Print the correlation between the PM2.5 and PM10 column.
    print(df_[["PM2.5", "PM10"]].corr())
    # 6. Add a new column Ftled “AQI” (Air Quality Index). For each row, the value of AQI must be set to “Good” if the value of PM2.5 is lower than 300; it must set to “Bad” otherwise.
    df_["AQI"] = df_["PM2.5"].apply(lambda x: "Good" if x < 300 else "Bad")
    # 7. Transform the column “hour”, from 24 to 12(am/pm) hour clock.
    df_["hour"] = df_["hour"].apply(lambda x: x-12 if x > 12 else x)
    # 8. Drop rows with missing values (NA).
    df_.dropna(inplace=True)
    # 9. Compute the average of the TEMP column, for each distinct value of the wind direction (column wd).
    print(df_.groupby("wd")["TEMP"].mean())


if __name__ == "__main__":
    main()  

