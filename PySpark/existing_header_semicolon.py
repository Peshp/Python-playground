path = "s3://de-40-training-raw/input_training_data/amazon_best_sellers/csv_with_header_semicolon/"

df4 = (
    spark.read
    .option("delimiter", "|")
    .option("header", False)
    .csv(path)
)

df4.show()