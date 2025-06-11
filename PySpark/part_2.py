import pyspark.sql
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# 1. Define the schema according to your CSV columns and datatypes
schema = StructType([
    StructField("product_name", StringType(), True),
    StructField("category", StringType(), True),
    StructField("rank", IntegerType(), True),
    StructField("price", DoubleType(), True),
    StructField("rating", DoubleType(), True),
    # Add other columns as needed, matching your CSV structure
])

# 2. Path to your data
path = "s3://de-40-training-raw/input_training_data/amazon_best_sellers/csv_with_header_pipe/"

# 3. Read the CSV with the enforced schema
df = (
    spark.read
    .option("header", True)         # Use first row as header
    .schema(schema)                 # Enforce your schema
    .csv(path)
)

df.createOrReplaceTempView("anton_task_1_vw")

result = spark.sql("SELECT * FROM anton_task_1_vw")
result.show()

# Filter rows with a WHERE clause
result2 = spark.sql("SELECT * FROM anton_task_1_vw WHERE price > 50")
result2.show()

# Group by and aggregate
result = spark.sql("""
    SELECT category, AVG(price) as avg_price
    FROM anton_task_1_vw
    GROUP BY category
""")

result2.show()