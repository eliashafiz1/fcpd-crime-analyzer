class FCPDCrime(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def load(self, filename = 'CrimeReports.csv'):
        f = open(filename, 'r')
        lines = f.readlines()
        self.clear()

        for line in lines:
            if len(line) > 3:                          # same pattern as the demo
                splitline = line.split(',')            # split
                for n in range(len(splitline)):        # strip each field
                    splitline[n] = splitline[n].strip()

                row = splitline[:9]                    # only first 9 columns
                self.append(row)

        f.close()

        # start/end date (from field [3])
        if len(self) > 0:
            self.startDate = self[0][3]
            self.endDate = self[-1][3]

        return len(self)

    def printCrimes(self, searchKey='all', zip='all', locale='all'):
        print(self.name)
        print("Crime calls for week", self.startDate, "through", self.endDate)

        count = 0

        # if all filters = 'all'
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
                    if searchKey not in desc:
                        continue

                if zip != 'all':
                    if zipcode != zip:
                        continue

                if locale != 'all':
                    if locale not in city:
                        continue

                print(r)
                count += 1

        print(count, "calls recorded for the timeframe\n")

if __name__ == '__main__':
    FC = FCPDCrime("Fairfax Police Calls")
    FC.load('CrimeReports.csv')  # or full path if not in the working dir
    FC.printCrimes()  # all records
