# Imports
    # Import MLFlow for model logging and tracking
        # import mlflow
        # import mlflow.sklearn

# Start an experiment run
    # mlflow.set_experiment()
        # Organizing runs
            # Organize by dataset used
    # mlflow.start_run()
        # Name based on what dataset they're using as well as number of run appended

# Log important values
    # mlflow.log_param() to log parameters and metadata
        # Model params
        # Class weighting strategy
        # Dataset metadata

# Train model
    # model.fit()

# Logging results
    # mlflow.log_metric()
        # Evaluation metrics
    # mlflow.sklearn.log_model()
        # Trained model artifact
