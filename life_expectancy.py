# Life Expectancy Data Analysis
# Added a feature that finds overall max/min life expectancy
# Added a feature that analyzes specific years with user input
# Added a feature that guides user if invalid year is entered

with open("life-expectancy.csv") as life_file:
    next(life_file)  # Skip header row
    
    # Initialize variables
    print()
    year_of_interest = int(input("Enter the year of interest: "))
    year_max_life = -1
    year_min_life = float('inf')
    year_max_country = ""
    year_min_country = ""
    year_sum = 0
    year_count = 0
    #guides a user on invalid inputs
    min_year = float('inf')
    max_year = -1

    # Overall analysis variables
    overall_max_life = -1
    overall_min_life = float('inf')
    overall_max_country = ""
    overall_min_country = ""
    overall_max_year = 0
    overall_min_year = 0
    
    for line in life_file:
        parts = line.strip().split(",")
        
        # Skip lines that don't have enough columns
        if len(parts) < 4:
            continue
            
        entity = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_exp = float(parts[3])
        
        # Update min and max years
        if year < min_year:
            min_year = year
        if year > max_year:
            max_year = year
        
        # Check for overall max/min
        if life_exp > overall_max_life:
            overall_max_life = life_exp
            overall_max_country = entity
            overall_max_year = year
            
        if life_exp < overall_min_life:
            overall_min_life = life_exp
            overall_min_country = entity
            overall_min_year = year
        
        # Check if this is the year of interest
        if year == year_of_interest:
            year_count += 1
            year_sum += life_exp
            
            if life_exp > year_max_life:
                year_max_life = life_exp
                year_max_country = entity
                
            if life_exp < year_min_life:
                year_min_life = life_exp
                year_min_country = entity

    # Print overall results
    print(f"\nThe overall max life expectancy is: {overall_max_life:.2f} from {overall_max_country} in {overall_max_year}")
    print(f"The overall min life expectancy is: {overall_min_life:.2f} from {overall_min_country} in {overall_min_year}")
    
    # Print year-specific results if data exists
    if year_count > 0:
        year_avg = year_sum / year_count
        print(f"\nFor the year {year_of_interest}:")
        print(f"The average life expectancy across all countries was {year_avg:.2f}")
        print(f"The max life expectancy was in {year_max_country} with {year_max_life:.2f}")
        print(f"The min life expectancy was in {year_min_country} with {year_min_life:.2f}")
    else:
        print(f"\nNo data found for {year_of_interest}.")
        print(f"Try a year between {min_year} and {max_year}.")
print()