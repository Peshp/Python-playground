path = "s3://de-40-training-raw/input_training_data/amazon_best_sellers/csv_with_header_pipe/"

df = spark.read.csv(path)
df.show()