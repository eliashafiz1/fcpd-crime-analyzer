#author elias hafiz
#FCPD Crime Records Analyzer
#purpose - to go through a police report database, and being able to use methods to filter records in various ways

class FCPDCrime(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def load(self, filename = 'CrimeReports.csv'):
        f = open(filename, 'r')
        lines = f.readlines()
        self.clear()

        for line in lines:
            if len(line) > 3:
                splitline = line.split(',')
                for n in range(len(splitline)):
                    splitline[n] = splitline[n].strip()

                row = splitline[:9]
                self.append(row)

        f.close()

        if len(self) > 0:
            self.startDate = self[0][3]
            self.endDate = self[-1][3]

        return len(self)

    def printCrimes(self, searchKey='all', zip='all', locale='all'):
        print(self.name)
        print("Crime calls for week", self.startDate, "through", self.endDate)

        count = 0

        if searchKey == 'all' and zip == 'all' and locale == 'all':
            for r in self:
                print(r)
                count += 1

        else:
            for r in self:
                desc = r[2]
                zipcode = r[8]
                city = r[6]

                if searchKey != 'all':
                    if searchKey.upper() not in desc.upper():
                        continue

                if zip != 'all':
                    if zipcode != zip:
                        continue

                if locale != 'all':
                    if locale.upper() not in city.upper():
                        continue

                print(r)
                count += 1

        print(count, "calls recorded for the timeframe\n")


    def countByCrime(self, select='all'):
        crimes = {}
        total = 0

        for r in self:
            zipcode = r[8]
            if select != 'all' and zipcode != select:
                continue

            crimeCode = r[1]
            desc = r[2]
            key = (crimeCode, desc)

            if key not in crimes:
                crimes[key] = 0
            crimes[key] += 1
            total += 1

        if select == 'all':
            print('List of crimes by code, sorted by frequency, for all zip codes')
        else:
            print(f"List of crimes by code, sorted by frequency, for zip code: {select}")
        print(f'\nFCPD Police Crime Statistics for the week {self.startDate} through {self.endDate}\n')

        crime_list = []
        for key in crimes:
            crimeCode = key[0]
            desc = key[1]
            count = crimes[key]
            crime_list.append([crimeCode, desc, count])

        for i in range(len(crime_list)):
            highest = i
            for x in range(i+1, len(crime_list)):
                if crime_list[x][2] > crime_list[highest][2]:
                    highest = x
            crime_list[i], crime_list[highest] = crime_list[highest], crime_list[i]

        for crimeCode, desc, count in crime_list:
            if total > 0:
                percent = count / total * 100
            else:
                percent = 0.0
            percent_format = f"{percent:.2f}%"
            print(crimeCode, count, percent_format, desc)



    def zipCodeList(self, zip):
        result = []

        for r in self:
            zipcode = r[8]
            if zipcode == zip:
                result.append(r)
        return result

    def countByZip(self):
        zips = {}
        total = 0
        for r in self:
            zipcode = r[8]
            if zipcode == '':
                continue
            if zipcode not in zips:
                zips[zipcode] = 0
            zips[zipcode] += 1
            total += 1
        print("Count of number of reports by Zip Code, sorted by frequency\n")
        print(f'FCPD Police Crime Statistics for the week {self.startDate} through {self.endDate}\n')

        zip_list = []
        for zipcode in zips:
            count = zips[zipcode]
            zip_list.append([zipcode, count])

        for i in range(len(zip_list)):
            highest = i
            for x in range(i+1, len(zip_list)):
                if zip_list[x][1] > zip_list[highest][1]:
                    highest = x
            zip_list[i], zip_list[highest] = zip_list[highest], zip_list[i]
        for zipcode, count in zip_list:
            if total > 0:
                percent = count / total * 100
            else:
                percent = 0.0
            percent_format = f"{percent:.2f}%"
            print(zipcode, count, percent_format)


def display_menu():
    print("\n========== FCPD Crime Records Analyzer ==========")
    print("1. Display all records")
    print("2. Search by offense type")
    print("3. Search by zip code")
    print("4. Search by offense + zip code")
    print("5. Search by locale")
    print("6. Count crimes by zip code")
    print("7. Count crimes by type (all zips)")
    print("8. Count crimes by type (specific zip)")
    print("9. List records for a zip code")
    print("0. Exit")
    print("=================================================")


if __name__ == '__main__':
    FC = FCPDCrime("Fairfax Police Calls")
    count = FC.load('CrimeReports.csv')
    print(f"Loaded {count} records successfully.\n")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            FC.printCrimes()

        elif choice == '2':
            offense = input("Enter offense to search for (e.g. assault, larceny, bite): ").strip()
            FC.printCrimes(searchKey=offense)

        elif choice == '3':
            zip_code = input("Enter 5-digit zip code (e.g. 22030): ").strip()
            FC.printCrimes(zip=zip_code)

        elif choice == '4':
            offense = input("Enter offense to search for: ").strip()
            zip_code = input("Enter 5-digit zip code: ").strip()
            FC.printCrimes(searchKey=offense, zip=zip_code)

        elif choice == '5':
            locale = input("Enter locale (e.g. Fairfax, Annandale, Mclean): ").strip()
            FC.printCrimes(locale=locale)

        elif choice == '6':
            FC.countByZip()

        elif choice == '7':
            FC.countByCrime('all')

        elif choice == '8':
            zip_code = input("Enter 5-digit zip code: ").strip()
            FC.countByCrime(zip_code)

        elif choice == '9':
            zip_code = input("Enter 5-digit zip code: ").strip()
            ZL = FC.zipCodeList(zip=zip_code)
            if len(ZL) == 0:
                print("No records found for that zip code.")
            else:
                for c in ZL:
                    print(c)
                print(f"{len(ZL)} records found.")

        elif choice == '0':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")