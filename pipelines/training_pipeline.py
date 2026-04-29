# Imports
    # Import load_processed_data from src/data
    # Import split_data from src/data
    # Import train_model from src/models
    # Import evaluate_model from src/evaluation
    # Import experiment tracking utilities (MLflow)
    # Import baseline metrics for validation

# CLI Entrypoint
    # Parse arguments function    
        # Define arguments
            # data_path
            # model_type
            # test_size
            # random_seed
        # return config object

# Training Pipeline Function
    # Start experiment run
    # Log parameters from config

    # Load processed data
        # Use config object data_path
    # Split data using config object test_size and random_seed
        # Return X_train, X_val, y_train, y_val
    # Train model
        # Return trained model
    # Evaluate model
        # Return metrics (precision, recall, F1, etc.)

    # Send metrics to validation function
        # Function returns validation_status (1 or 0), and reason

        # If validation fails:
            # Exit pipeline early
            # Log validation status (0) and reason for failure
            # Log metrics
                # DON'T log model artifact

    # If validation succeeds:
        # Log metrics
        # Log trained model artifact
        # Log validations status (1)

    # End experiment run

    # Return metrics

# Validation Function
    # Parameters are the model metrics after evaluation
    # Rules and thresholds need to be set and defined
        # Min_Recall, Min_Precision, etc.

    # Compare recall to Min_Recall
        # If less than threshold, return fail
            # Reason is "Doesn't meet recall threshold"
    # Compare precision to Min_Precision
        # If less than threshold, return fail
            # Reason is "Doesn't meet precision threshold"
    # Compare precision to baseline model
        # If worse than baseline metrics, return fail
            # Reason is "Performed worse than baseline"

    # Return validation_status and reason


# Main Execution
    # Create config object using parse_args() function
    # Call training_pipeline with config object as parameter