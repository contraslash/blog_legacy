Title: Using Singularity containers in HTCondor
Date: 2016-12-17T15:18:33+00:00
Description: Singularity is the new kid in the neighborhood. using containers, it allows reproducibility of a computation 
Tags: Singularity,HTCondor
---
# Using Singularity containers in HTCondor

### Introduction
Designed around the notion of extreme mobility of compute and reproducible science, Singularity enables users to have full control of their operating system environment. 

### Installing Singularity
Singularity needs to be installer in a modern linux distribution, it's installed as follows
```
VERSION=2.2
wget https://github.com/singularityware/singularity/releases/download/$VERSION/singularity-$VERSION.tar.gz
tar xvf singularity-$VERSION.tar.gz
cd singularity-$VERSION
./configure --prefix=/usr/local
make
sudo make install
```
Then, check that everything is alright

> singularity -v

### Configuring HTCondor
It can be used along with HTCondor by adding some entries to the HTCondor configuration file:

> sudo nano /etc/condor/config.d/condor_config.local

```
# Tell HTCondor where is the singularity executable
SINGULARITY = /usr/local/bin/singularity

SINGULARITY_JOB = (TARGET.DESIRED_OS isnt MY.OpSysAndVer) && ((TARGET.DESIRED_OS is "CentOS6") || (TARGET.DESIRED_OS is "CentOS7"))
SINGULARITY_IMAGE_EXPR = (TARGET.DESIRED_OS is "CentOS6") ? "/tmp/Centos7.img" : "/tmp/Centos7.img"
# Maps $_CONDOR_SCRATCH_DIR on the host to /srv inside the image.
SINGULARITY_TARGET_DIR = /srv
# Writable scratch directories inside the image.  Auto-deleted after the job exits.
MOUNT_UNDER_SCRATCH = /tmp, /var/tmp
```
Then restart HTCondor `sudo service condor restart` and check if the machine has singularity enable.

> condor_status -const HasSingularity

### Testing your configuration
Lets first create a singularity container from Docker Centos image

```
sudo singularity create --size 2048 /tmp/Centos7.img
sudo singularity import /tmp/Centos7.img docker://centos:latest
sudo singularity exec --writable /tmp/Centos7.img  echo "Hello World"  > /tmp/hola
```

An then, create a HTCondor submit file

> nano /tmp/sing.submit

```
executable = /bin/hostname
universe = vanilla
+SingularityImage = "/tmp/Centos7.img"
+DESIRED_OS="CentOS6"
output = example1.$(cluster).$(process).out
error =  example1.$(cluster).$(process).err
log =    example1.$(cluster).$(process).log
queue 1
```
Then execute and wait 
> condor_submit /tmp/sing.submit


You can find more information [here](http://singularity.lbl.gov/about)