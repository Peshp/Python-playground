

path = "s3://de-40-training-raw/input_training_data/amazon_best_sellers/json_format"
df5 = spark.read.json(path)

df5.printSchema()