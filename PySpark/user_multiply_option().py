path = "s3://de-40-training-raw/input_training_data/amazon_best_sellers/csv_with_header_pipe/"

df4 = (
    spark.read
    .options(delimiter=";", header=True)
    .csv(path)
)

df4.show()