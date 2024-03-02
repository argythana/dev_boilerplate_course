from dashboard_functions import plot_daily_dashboard, activities_datafile, plot_daily_averages

if __name__ == "__main__":
    # datafile = "./data/run4moreProd.activities.csv"
    plot_daily_dashboard(activities_datafile)
    plot_daily_averages(activities_datafile)
