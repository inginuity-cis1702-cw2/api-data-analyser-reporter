import csv
from datetime import datetime


def save_user_log_csv(user_log: dict, filename="user_log.csv"):
    #Open the CSV file in write mode
    with open(filename, mode="w", newline="", encoding="utf=8") as file:
        writer = csv.writer(file)

        #Write the header row in the CSV file
        writer.writerow([
            "log_index",
            "requested_data",
            "value",
            "timestamp"
        ])

        #Iterate over all of the logged user requests
        for index, results in user_log.items():
            for key, value in results.items():
                writer.writerow([
                    index,
                    key,
                    value,
                    datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
                ])
