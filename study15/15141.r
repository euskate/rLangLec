library(rhdfs)
hdfs.init()
hdfs.create.file("/path/to/file.txt", "Hello World!")
