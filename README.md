# A simple Word Count Example using pyspark on AWS EMR

#### Clone the repository
- Clone this repo to your local machine.

#### Create cluster
- We'll start off by creating an AWS EMR cluster, just as in the first assignment. Head over to [AWS EMR](https://aws.amazon.com/emr/) and get started.
- Click on Create cluster and configure as per below - 

![img](http://imgur.com/Ed6DlBS.jpg)

- The cluster remains in the 'Starting' state for about 10 - 15 minutes. Once the cluster is ready for use, the status will change to 'Waiting'. You can now go ahead and use it.

#### Create private key for ssh access
- Click on "Learn how to create an EC2 key pair" to create and modify your EC2 key pair.

#### Allow inbound SSH traffic on the master node
- On the left top corner goto Services->EC2
- On the left hand panel goto Security Groups under Network & Security
- Select the group named "ElasticMapReduce-master" and click Edit in the Inbound tab below
- Add rule, select SSH for type and My IP as source. Save

#### Upload input file on S3
- Now head over to Services->S3 and create a bucket named csds
- In the bucket, create a folder named csds-spark-emr
- Upload the input.txt file from this repo
- In permissions, tick the box for read everywhere. Nothing to do in properties
- Head forward and submit the file
- Click on the uploaded file and click the Make public button just to make sure

#### Creating wordcount.py on the Master node
- Now on our created cluster page (Cluster list->our cluster)
- Near the "Master public DNS:" field click the SSH button
- Follow the instructions and SSH on the master node
- In /home/hadoop create wordcount.py (vi wordcount.py)
- Copy over the contents from wordcount.py in this repo
- In wordcount.py change the input file s3 url to point to input.txt in your bucket, created above
- Save

#### Executing wordcount.py
- Go through the code in wordcount.py and checkout what it does
- Execute the script using "spark-submit wordcount.py | tee output.txt"
- This will also generate output.txt with a copy of the logs
- You may have the output file copied to your s3 bucket by using the cmd "aws s3 cp output.txt s3://my_bucket/my_folder/"
- You should see the result of your code among other logs, should look like

And: 2<br>
on: 1<br>
then: 1<br>
Aberbrothok: 2<br>
bell: 1<br>
that: 1<br>
of: 2<br>
knew: 1<br>
Had: 1<br>
placed: 1<br>
Abbot: 2<br>
they: 1<br>
worthy: 1<br>
blest: 1<br>
Rock: 2<br>
Inchcape: 1<br>
the: 3<br>
The: 1<br>
perilous: 1<br>

- You're encouraged to play around with the code, check out the documentation and try things out

#### Terminate the cluster
- Don't forget to terminate your cluster after you're done
- You'll need to follow the same steps next time you create a new cluster with the exception of creating private key for SSH, you can use the same private key for all clusters
- Also make sure to allow inbound SSH traffic on the master every time your machine changes IP, which might happen when you switch between WiFi networks
