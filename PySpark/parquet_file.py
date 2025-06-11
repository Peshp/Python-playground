path = "s3://de-40-training-raw/input_training_data/amazon_best_sellers/parquet_format"
df6 = spark.read.parquet(path)

df6.limit(5).toPandas()