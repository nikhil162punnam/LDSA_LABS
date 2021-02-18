
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession
from operator import add


# In[4]:


spark_session = SparkSession        .builder        .master("spark://192.168.1.153:7077")         .appName("project_team25_example")        .config("spark.dynamicAllocation.enabled", True)        .config("spark.shuffle.service.enabled", True)        .config("spark.dynamicAllocation.executorIdleTimeout","30s")        .config("spark.executor.cores",8)        .getOrCreate()

# Old API (RDD)
spark_context = spark_session.sparkContext


# In[5]:


# Load the csv from HDFS
data_frame = spark_session.read    .option("header", "true")    .csv('hdfs://192.168.1.153:9000/team25/libraryDataset/Integrated_Library_System__ILS__Data_Dictionary.csv')    .cache()


# In[6]:


data_frame.head()


# In[3]:


spark_context.stop()

