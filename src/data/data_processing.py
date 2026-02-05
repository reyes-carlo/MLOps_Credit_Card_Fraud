# Imports

# Load data function
    # Locate zip folder
    # Unzip data
    # Check dataset columns
        # Verify column names
        # Check column counts
    # Once both are verified, log datashape and column names
        # Observe class balance

# Validate schema function
    # Check the data type of all columns
        # Check if categories should contain boolean, numeric, or categorical data
        # Raise error if data type doesn't match

# Saving processed data function
    # Save .csv file into /data/processed
        # Overwrite processed data if it currently exists
        # Name as processed_data.csv
    # No modification of data yet