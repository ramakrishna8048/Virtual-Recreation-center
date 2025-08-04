import mlflow

def log_run():
    with mlflow.start_run():
        mlflow.log_param("algorithm", "spaCy")
        mlflow.log_metric("intent_accuracy", 0.91)

if __name__ == "__main__":
    log_run()
