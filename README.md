# Project-4_hadoop-mapper
<div id="header" align="center">
  <img src="https://media.giphy.com/media/o0eOCNkn7cSD6/giphy.gif" width="100"/>
</div>

<div id="badges" align="center">
  <a href="https://www.linkedin.com/in/sakabuana31/">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" height="25px" alt="LinkedIn Badge"/>
  </a>
  <a href="mailto:sakabuana.pa@gmail.com">
  <img src="https://img.shields.io/badge/-Email-c14438?style=flat-square&logo=Gmail&logoColor=white" height="25px" alt="Email Badge">
  </a>
</div>

<h1 align="center">
  hey there
  <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30px"/>
</h1>

### :dart: Goals :
> Learn to mount hadoop on docker and analyza data in it

### :file_folder: Configuration Files :

| Folder | Fungsi |
| --------------- | --------------- |
| data  | This is a directory that contains a data as input and output source for analyzing data  |
| datanode  | This is a directory that contains the configuration files and scripts for the Hadoop DataNode service. The DataNode is responsible for storing and retrieving data from HDFS.  |
| historyserver | This is a directory that contains the Hadoop job history files. The Hadoop JobHistoryServer service reads these files and provides a web interface for viewing the details of completed MapReduce jobs. |
| map_reduce | This is a directory that contains a Python MapReduce script to run this docker hadoop for this project. It uses Hadoop Streaming to run a MapReduce job that counts the number of occurrences of each word in a text file. |
| map-reduce-example | This is a directory that contains a sample MapReduce job written in Python. It counts the number of occurrences of each word in a text file. |
| namenode | This is a directory that contains the configuration files and scripts for the Hadoop NameNode service. The NameNode is responsible for managing the metadata of the HDFS file system. |
| nodemanager | This is a directory that contains the configuration files and scripts for the Hadoop NodeManager service. The NodeManager is responsible for launching and monitoring containers for running application tasks. |
| resourcemanager | This is a directory that contains the configuration files and scripts for the Hadoop ResourceManager service. The ResourceManager is responsible for managing the allocation of resources for running applications in the cluster. |