DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MINTS_PER_HOUR = 60
SECS_PER_MINT = 60

def main():

    # seconds in a year
    seconds_per_year = DAYS_PER_YEAR * HOURS_PER_DAY * MINTS_PER_HOUR * SECS_PER_MINT
    
    print(f'\nThere are {seconds_per_year} seconds in a year!')

if __name__ == '__main__':
    main()
