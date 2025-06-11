path = "s3://de-40-training-raw/input_training_data/amazon_best_sellers/csv_with_header_pipe/"

df3 = (
    spark.read
    .option("delimiter", "|")       
    .csv(path)
)

df3.display()