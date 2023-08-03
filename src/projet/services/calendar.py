import holidays
import datetime

class WorkingDaysService:
    def get_public_holidays(self, year):
        fr_holidays = holidays.France(years=year)
        return fr_holidays


    def get_working_days(self, year):
        # Get public holidays
        public_holidays = self.get_public_holidays(year)

        working_days = []
        start_date = datetime.date(year, 1, 1)
        end_date = datetime.date(year, 12, 31)

        # Loop through the days of the year
        current_date = start_date
        while current_date <= end_date:
            # Check if the date is a working day (e.g., Monday to Friday)
            if current_date.weekday() < 5 and current_date not in public_holidays:
                working_days.append(current_date)
            current_date += datetime.timedelta(days=1)

        return working_days
