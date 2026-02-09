# Imports

# Load processed data
    # Locate processed data in data/processed
    # CSV has already been checked so convert into dataframe object

# Split data
    # Check number of examples per class
        # Use sklearn compute_class_weight() to determine class weights
    # Split into train/validation/test set
        # 75/15/10

# Train simple baseline model
    # Logisitic regression
        # Simple binary classifier that would make sense with the csv data types
    # Configure model to account for class imbalance using class weights

# Evaluate with appropriate metrics
    # Possibility of class imbalance
    # Accuracy, Precision, Recall, and F1-Score
        # Accuracy may be misleading, especially if class imbalance is present
    # Record metrics as a baseline comparison point