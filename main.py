import csv
import os

try:
    csvfile = open("ExportsGDP2019.csv", "r")
    reader = csv.DictReader(csvfile, delimiter=",")
    print("Country Name: 2019 [YR2019]")
    for row in reader:
        print(row['Country Name'], ': ', row["2019 [YR2019]"])

    csvfile.close

except:
    print("Файл ExportsGDP2019.csv не знайдено!")

try:
    with open("ExportsGDP2019.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        values = []
        countries = []

        for row in reader:
            country = row["Country Name"]
            value = float(row["2019 [YR2019]"])
            values.append(value)
            countries.append(country)

        min_index = values.index(min(values))
        max_index = values.index(max(values))

        min_country = countries[min_index]
        max_country = countries[max_index]

        with open("new_lab11.csv", "w", newline='') as csvfile2:
            writer = csv.writer(csvfile2, delimiter=",")
            writer.writerow(['Country', 'Min Value/Max Value'])
            writer.writerow([min_country, min(values)])
            writer.writerow([max_country, max(values)])

except:
    print("Файл ExportsGDP2019.csv не знайдено!")

print("Результати пошуку(найменше та найбільше значення) збережено у файлі new_lab11.csv")