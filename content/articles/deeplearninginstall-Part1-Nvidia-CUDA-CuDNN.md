Title: Deep Learning Installation Tutorial - Part 1 - Nvidia Drivers, CUDA, CuDNN
Date: 2016-10-12 10:15
Category: Deep Learning
Tags: Deep Learning, Python, Tutorial, Installation, Machine Learning, GPU, NVIDIA, CUDA, CuDNN
Slug: deeplearning_install-part1
Author: Jonathan DEKHTIAR
Headline: How to install Nvidia Drivers, CUDA, CuDNN

# Deep Learning Installation Tutorial - Index

Hello everyone, here is a tutorial to quickly install main Deep Learning libraries and set up a complete environment.

* [**Part 1 :** Installation - Nvidia Drivers, CUDA, CuDNN](/2016/deeplearning_install-part1.html)
* [**Part 2 :** Installation - Caffe and DIGITS](/2016/deeplearning_install-part2.html)
* [**Part 3 :** Installation - Tensorflow and Theano (coming soon)](#)
* [**Part 4 :** Installation - Keras and Lasagne (coming soon)](#)
* [**Part 5 :** Installation - (Nvidia) Docker for Deep Learning (coming soon)](#)

---

# Deep Learning Installation Tutorial - Part 1 - Nvidia Drivers, CUDA, CuDNN

There are a few major libraries for Deep Learning applications available – Caffe, Keras, TensorFlow, Theano, and Torch.
These libraries use GPU Computation power to speed up training which can be very long on CPU (+/- 40days for a ConvNet for the ImageNet Dataset).

NVIDIA is definetely the brand to go for Deep Learning applications, and for now, the only well and broadly supported hardware.

In these Tutorials, we will explore how to install and set up an environment to run Deep Learning tasks.

A few useful links :

* **CUDA :** <https://developer.nvidia.com/cuda-zone>
* **CuDNN :** <https://developer.nvidia.com/cudnn>
* **Caffe :** <http://caffe.berkeleyvision.org/>
* **DIGITS :** <https://developer.nvidia.com/digits>
* **Tensorflow :** <https://www.tensorflow.org/>
* **Theano :** <http://deeplearning.net/software/theano/index.html>
* **Keras :** <https://keras.io/>
* **Lasagne :** <http://lasagne.readthedocs.io/en/latest/>
* **Docker :** <https://www.docker.com/>
* **NVIDIA-DOCKER :** <https://github.com/NVIDIA/nvidia-docker>

In this post, we will install drivers and dependencies for GPU Computation.

* **CUDA:** "CUDA is a parallel computing platform and application programming interface (API) model created by Nvidia" ([Source](https://en.wikipedia.org/wiki/CUDA))
* **CuDNN:** "The NVIDIA CUDA Deep Neural Network library (cuDNN) is a GPU-accelerated library of primitives for deep neural networks." ([Source](https://developer.nvidia.com/cudnn))

A compilation of tools porvided by NVIDIA, very useful for Deep Learning but not only.

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
sudo apt-get install dkms build-essential linux-headers-generic apt-show-versions
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
root@machine: apt-show-versions cuda
**cuda:amd64/unknown 7.5-18 uptodate**

root@machine: cat /proc/driver/nvidia/version
NVRM version: NVIDIA UNIX x86_64 Kernel Module  352.99  Mon Jul  4 23:52:14 PDT 2016
GCC version:  gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.3)
```

Or by executing:
*(The output might be different from mine depending on the version you installed and your hardware, I have 3 GTX Titan X.)*
```bash
root@machine: nvidia-smi

+------------------------------------------------------+
| NVIDIA-SMI 352.99    Driver Version: 352.99          |
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
| 22%   54C    P0    53W / 250W |     23MiB / 12284MiB |      0%      Default |
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
