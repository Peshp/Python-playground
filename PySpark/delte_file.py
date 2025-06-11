path = "s3://de-40-training-raw/input_training_data/amazon_best_sellers/delta_format"
df7 = spark.read.format("delta").load(path)

display(df7)