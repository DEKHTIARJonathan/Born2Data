Title: Deep Learning Installation Tutorial - Part 3 - TensorFlow
Date: 2016-05-29 10:12
Category: Deep Learning
Tags: Deep Learning, Python, Tutorial, Installation, Machine Learning, GPU
Slug: deeplearning_install-partxx
Author: Jonathan DEKHTIAR
Headline: Deep Learning Tutorial: How to install TensorFlow

# Deep Learning Installation Tutorial - Index

Hello everyone, here is a tutorial to quickly install main Deep Learning libraries and set up a complete environment.

* [**Part 1 :** Installation - Nvidia Drivers, CUDA, CuDNN](/2016/deeplearning_install-part1.html)
* [**Part 2 :** Installation - Caffe and DIGITS](/2016/deeplearning_install-part2.html)
* [**Part 3 :** Installation - Tensorflow and Theano (coming soon)](#)
* [**Part 4 :** Installation - Keras and Lasagne (coming soon)](#)
* [**Part 4 :** Installation - Docker for Deep Learning (coming soon)](#)

---

# Deep Learning Installation Tutorial - Part 2 - NVIDIA DIGITS & CAFFE

There are a few major libraries for Deep Learning applications available – Caffe, Keras, TensorFlow, Theano, and Torch.
These libraries use GPU Computation power to speed up training which can be very long on CPU (+/- 40days for a ConvNet for the ImageNet Dataset).

NVIDIA is definetely the brand to go for Deep Learning applications, and for now, the only well and broadly supported hardware.

In these Tutorials, we will explore how to install and set up an environment to run Deep Learning tasks.

A few useful links :

* **CUDA:** <https://developer.nvidia.com/cuda-zone>
* **CuDNN:** <https://developer.nvidia.com/cudnn>
* **Caffe:** <http://caffe.berkeleyvision.org/>
* **DIGITS:** <https://developer.nvidia.com/digits>
* **Tensorflow:** <https://www.tensorflow.org/>
* **Theano:** <http://deeplearning.net/software/theano/index.html>
* **Keras:** <https://keras.io/>
* **Lasagne:** <http://lasagne.readthedocs.io/en/latest/>
* **Docker:** <https://www.docker.com/>
* **Nvidia-Docker:** <https://github.com/NVIDIA/nvidia-docker>

In this post, we will install:

* **Caffe:** "Caffe is a deep learning framework made with expression, speed, and modularity in mind." ([Source](http://caffe.berkeleyvision.org/))
* **DIGITS:**

---

### A. Installing Caffe

Main source for this and the following step is the [readme of the DIGITS project](https://github.com/NVIDIA/DIGITS/blob/master/README.md){:target="\_blank"}.

If a 404 error shows up, please correct the file name according to this webpage : [NVIDIA Binaries](http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1404/x86_64){:target="\_blank"}

Run the following commands to get access to the required repositories:
```bash
CUDA_REPO_PKG=cuda-repo-ubuntu1404_7.5-18_amd64.deb &&
    wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/$CUDA_REPO_PKG &&
    sudo dpkg -i $CUDA_REPO_PKG

ML_REPO_PKG=nvidia-machine-learning-repo-ubuntu1404_4.0-2_amd64.deb &&
    wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1404/x86_64/$ML_REPO_PKG &&
    sudo dpkg -i $ML_REPO_PKG
```

---

### B. Let's install DIGITS from package manager

NVIDIA DIGITS is a web server providing a convenient web interface for training and testing Deep Neural Networks based on caffe. I intend to cover in a future article how to work with caffe. Here I will show you how to set up CUDA

Run the following commands to install DIGITS

```bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install digits -y
```

The installation could be pretty long (I had more than 600Mb of packages to download).

#### CUDA repository

Get access to machine learning packages from NVIDIA by downloading and installing the cuda-repo-ubuntu1404 package (instructions above). You could also get this package by downloading the deb (network) installer from the CUDA downloads website. This provides access to the repository containing packages like cuda-toolkit-7-5 and cuda-toolkit-7-0, etc.

#### Machine Learning repository

Get access to machine learning packages from NVIDIA by downloading and installing the nvidia-machine-learning-repo package (instructions above). This provides access to the repository containing packages like digits, caffe-nv, torch, libcudnn4, etc.

#### DIGITS Commands

##### STOP SERVER

```bash
sudo stop nvidia-digits-server
```

##### START SERVER

```bash
sudo start nvidia-digits-server
```

##### Troubleshooting

If you have another server running on port 80 already, you may need to reconfigure DIGITS to use a different port.

```bash
sudo dpkg-reconfigure digits
```

To make other configuration changes, try this (you probably want to leave most options as "unset" or "default" by hitting ENTER repeatedly):

```bash
cd /usr/share/digits
# set new config
sudo python -m digits.config.edit -v
# restart server
sudo stop nvidia-digits-server
sudo start nvidia-digits-server
```

---

### C. Let's install DIGITS from sources

#### Prerequisites
Run the following commands to install Prerequisites

```bash
sudo apt-get install python-dev python-pip graphviz -y
sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler -y
sudo apt-get install --no-install-recommends libboost-all-dev -y
sudo apt-get install libatlas-base-dev -y
sudo apt-get install python-dev -y
```

#### Download DIGITS' Sources

```bash
cd ~
git clone https://github.com/NVIDIA/DIGITS.git digits
```

#### Install DIGITS

```bash
cd ~/digits
sudo pip install -r requirements.txt
sudo apt-get install python-pil python-numpy python-scipy python-protobuf python-gevent python-flask python-flaskext.wtf gunicorn python-h5py
sudo apt-get install caffe-nv python-caffe-nv # or build from sources
sudo apt-get install torch7-nv # or build from sources
```

#### Development mode

```bash
./digits-devserver
```

Starts a development server (werkzeug backend) at http://localhost:5000/.

```bash
$ ./digits-devserver --help
usage: digits-devserver [-h] [-p PORT] [-c] [-d] [--version]

Run the DIGITS development server

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Port to run app on (default 5000)
  -c, --config          Edit the application configuration
  -d, --debug           Run the application in debug mode (reloads when the
                        source changes and gives more detailed error messages)
  --version             Print the version number and exit
```

#### Production mode

```bash
./digits-server
```

Starts a production server (gunicorn backend) at http://localhost:34448.

If you get any errors about an invalid configuration, use the development server first to set your configuration.

If you have installed the nginx.site to /etc/nginx/sites-enabled/, then you can view your app at http://localhost/.

#### Troubleshooting

Most configuration options should have appropriate defaults. If you need to edit your configuration for some reason, try one of these commands:

```bash
# Set options before starting the server
./digits-devserver --config
# Advanced options
python -m digits.config.edit --verbose
```
