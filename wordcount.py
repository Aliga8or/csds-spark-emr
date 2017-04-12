import sys
from operator import add
from pyspark import SparkConf, SparkContext

#for SparkConf() check out http://spark.apache.org/docs/latest/configuration.html
conf = (SparkConf()
         .setMaster("local")
         .setAppName("WordCounter")
         .set("spark.executor.memory", "1g"))
sc = SparkContext(conf = conf)

print("Launch App..")
if __name__ == "__main__":
	print("Initiating main..")
	
	inputFile = "s3://csds1129/spark-emr/input.txt"
	print("Counting words in ", inputFile)
	lines = sc.textFile(inputFile)
	
	#for lambdas check out https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
	lines_nonempty = lines.filter( lambda x: len(x) > 0 )
	counts = lines_nonempty.flatMap(lambda x: x.split(' ')) \
	              .map(lambda x: (x, 1)) \
	              .reduceByKey(add)
	output = counts.collect()
	for (word, count) in output:
	    print("%s: %i" % (word, count))

	sc.stop()