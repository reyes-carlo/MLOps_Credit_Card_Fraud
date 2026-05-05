# On Application/API Startup
    # Call Load Latest Model Function
    # Store as global variable

# Load Latest Model Function
    # Load most recently validated model
    # Store in model global variable

# Prediction Function
    # Validate input
        # JSON file parameter
    # Run model prediction with input
    # Return results
        # JSON format
        # Contains class prediction
        # Also contains probability/confidence metric
            # Probability or how confident model is that data is fraud

# Validate Input Function
    # Recieves JSON file
    # Defined expected format (feature names and corresponding datatypes)
        # Make sure data fields are in correct order
        # Can cause silent errors

    # Check for all data fields
        # If there are missing data fields, return error message
    # CHeck for data types
        # If there are incorrect data types, return error message

    # Format into model format
        # Array or DataFrame object
    # Assign values to corresponding fields
    # Return input object

# API Layer (FastAPI)

# POST/predict
    # Recieve JSON request
    # Call prediction function
    # Return results in JSON format

# Error handling
    # If model doesn't load -> return error
    # If validation fails -> return error message
    # If prediction fails -> return error message