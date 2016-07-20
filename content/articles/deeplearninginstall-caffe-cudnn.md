Title: Deep Learning Installation Tutorial - Part 1 - Caffe & CuDNN
Date: 2016-05-27 10:12
Category: Deep Learning
Tags: Deep Learning, Python, Tutorial, Installation, Machine Learning, GPU
Slug: deeplearning_install-part1
Author: Jonathan DEKHTIAR
Headline: How to install Caffe & CuDNN Libraries

# Deep Learning Installation Tutorial - Part 1 - NVIDIA DIGITS & CAFFE

There are three major GPU utilizing Deep Learning frameworks available – Theano, Torch and caffe. NVIDIA DIGITS is a web server providing a convenient web interface for training and testing Deep Neural Networks based on caffe. I intend to cover in a future article how to work with caffe. Here I will show you how to set up CUDA

First of all you need an AWS account and g2.2xlarge instance up and running. That is mostly self-explanatory – for the command line parts (and some tips) you might want to have a look at my previous tutorial “Guide to EC2 from the Command Line“. Make sure to add an inbound rule for port 5000 for your IP – b/c this is where the DIGITS server is made available at.

---
### Prerequisites

*This Tutorial has been tested and runned on Ubuntu 14.04 on the 30th May 2016 *  
**Feel free to share and spread the word if you liked the article**

Don't forget to get your system up to date

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
```

---
##### A. NVIDIA Drivers:

Lets remove first everything that point to any existing nvidia installation:

```bash
sudo apt-get remove nvidia*
sudo apt-get autoremove
```

Then let's intall the dependencies :

```bash
sudo apt-get install dkms build-essential linux-headers-generic
```

Then we will need to blacklist the "nouveau" driver:

```bash
sudo vi /etc/modprobe.d/blacklist-nouveau.conf
```

You will need to add the following lines:

```text
blacklist nouveau
blacklist lbm-nouveau
options nouveau modeset=0
alias nouveau off
alias lbm-nouveau off
```

Disable the Kernel nouveau by typing the following commands:
echo options nouveau modeset=0 | sudo tee -a /etc/modprobe.d/nouveau-kms.conf
sudo update-initramfs -u

If you don't have installed or updated the driver of your NVIDIA Graphic Card, please download and install the driver: [nvidia's website](http://www.nvidia.com/Download/index.aspx){:target="\_blank"}


Execute the following commands to install the NVIDIA Drivers.

```bash
wget http://us.download.nvidia.com/XFree86/Linux-x86_64/361.45.11/NVIDIA-Linux******************.run
chmod +x NVIDIA-Linux******************.run
```

Let's install the dependencies:

```bash
sudo apt-add-repository ppa:ubuntu-x-swat/x-updates #if it fails, you may need to repeat the operation.
sudo apt-get update
sudo apt-get install nvidia-current
sudo apt-get upgrade
```
Let's launch the NVIDIA Driver Installation:

```bash
sudo ./NVIDIA-Linux******************.run
```

Follow the instructions displayed on screen.

* You may have a warning "The distribution-provided pre-install script failed! Are you sure you want to continue ?" => **You can continue**.
* Register the kernel module with DKMS => **YES !**
* If you don't have 32bits compatibility you will get a warning => **OK !**
* Run NVIDIA-Xconfig => **YES !**

And restart
```bash
sudo reboot
```

You can test the installation is okay by executing :
```bash
root@machine:~/$ ls -la /dev | grep nvidia
crw-rw-rw-  1 root root    195, 255 mai   30 11:41 nvidiactl
crw-rw-rw-  1 root root    247,   0 mai   30 11:41 nvidia-uvm
crw-rw-rw-  1 root root    247,   1 mai   30 11:41 nvidia-uvm-tools
```

Or by executing: *(The output might be different from mine depending on your hardware, I have 3 GTX Titan X.)*
```bash
root@machine: nvidia-smi

+------------------------------------------------------+
| NVIDIA-SMI 352.93     Driver Version: 352.93         |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX TIT...  Off  | 0000:05:00.0     Off |                  N/A |
| 22%   59C    P0    74W / 250W |     23MiB / 12284MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   1  GeForce GTX TIT...  Off  | 0000:06:00.0     Off |                  N/A |
| 22%   60C    P0    72W / 250W |     23MiB / 12284MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   2  GeForce GTX TIT...  Off  | 0000:09:00.0     Off |                  N/A |
|  0%   54C    P0    53W / 250W |     23MiB / 12284MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID  Type  Process name                               Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

##### B. Installing CUDA 7.5

Main source for this step is [Markus Beissinger’s blog post](http://markus.com/install-theano-on-aws/){:target="\_blank"} on setting up Theano.

```bash
sudo apt-get install -y gcc g++ gfortran build-essential \
  git wget linux-image-generic libopenblas-dev python-dev \
  python-pip python-nose python-numpy python-scipy

# downloading the (currently) most recent version of CUDA 7.5
sudo wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/cuda-repo-ubuntu1404_7.5-18_amd64.deb

# installing CUDA
sudo dpkg -i cuda-repo-ubuntu1404_7.5-18_amd64.deb

sudo apt-get update
sudo apt-get install cuda

# setting the environment variables so CUDA will be found
echo -e "\nexport PATH=/usr/local/cuda/bin:$PATH" >> .bashrc
echo -e "\nexport LD_LIBRARY_PATH=/usr/local/cuda/lib64" >> .bashrc
```

Now close your shell or the SSH connection and re-open it.

```bash
# installing the samples and checking the GPU
cuda-install-samples-7.5.sh ~/
cd NVIDIA\_CUDA-7.5\_Samples/1\_Utilities/deviceQuery  
make  
./deviceQuery
```

If no error shows up, CUDA is successfully installed.

##### C. Installing CuDNN

To further speed up deep learning relevant calculations it is a good idea to set up the cuDNN library. For that purpose you will have to get an NVIDIA developer account and join the CUDA registered developer program. The last step requires NVIDIA to unlock your account  and that might take one or two days. But you can get started also without cuDNN library. As soon as you have the okay from them – [download cuDNN](https://developer.nvidia.com/cuDNN/){:target="\_blank"} and upload it to your instance.

```bash
cd ~
wget http://developer.download.nvidia.com/*********************************************/cudnn-7.5-linux-x64-v5.0-ga.tgz

# unpack the library
tar -zxvf cudnn-7.5-linux-x64-v5.0-ga.tgz

sudo cp cuda/include/cudnn.h /usr/local/cuda-7.5/include
sudo cp cuda/lib64/libcudnn* /usr/local/cuda-7.5/lib64
```


##### D. Installing Caffe

Main source for this and the following step is the [readme of the DIGITS project](https://github.com/NVIDIA/DIGITS/blob/master/README.md){:target="\_blank"}.

Run the following commands to get access to the required repositories:
```bash
CUDA_REPO_PKG=cuda-repo-ubuntu1404_7.5-18_amd64.deb &&
    wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/$CUDA_REPO_PKG &&
    sudo dpkg -i $CUDA_REPO_PKG

ML_REPO_PKG=nvidia-machine-learning-repo_4.0-2_amd64.deb &&
    wget http://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1404/x86_64/$ML_REPO_PKG &&
    sudo dpkg -i $ML_REPO_PKG
```

### Let's install DIGITS from package manager

Run the following commands to install DIGITS

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install digits
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

### Let's install DIGITS from sources

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
