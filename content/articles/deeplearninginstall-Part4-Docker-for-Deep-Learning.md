Title: Deep Learning Installation Tutorial - Part 4 - Docker for Deep Learning
HeadTitle: Deep Learning Installation Tutorial - Part 4
Date: 2017-08-09 10:15
Category: Deep Learning
Tags: Deep Learning, Python, Tutorial, Installation, Machine Learning, CNTK, Keras, PyTorch
Slug: deeplearning_install-part4
Author: Jonathan DEKHTIAR
Headline: How to install Docker for Deep Learning

# Deep Learning Installation Tutorial - Index

Dear fellow deep learner, here is a tutorial to quickly install some of the major Deep Learning libraries and set up a complete development environment.

* [**Part 1 :** Installation - Nvidia Drivers, CUDA and CuDNN](/2017/deeplearning_install-part1.html)
* [**Part 2 :** Installation - Caffe, Tensorflow and Theano](/2017/deeplearning_install-part2.html)
* [**Part 3 :** Installation - CNTK, Keras and PyTorch](/2017/deeplearning_install-part3.html)
* [**Part 4 :** Installation - Docker for Deep Learning](/2017/deeplearning_install-part4.html)

---

# Deep Learning Installation Tutorial - Part 4 - Docker for Deep Learning

There are a few major libraries available for Deep Learning development and research – Caffe, Keras, TensorFlow, Theano, and Torch, MxNet, etc.
These libraries use GPU computation power to speed up deep neural networks training which can be very long on CPU (+/- 40 days for a standard convolutional neural network for the ImageNet Dataset).

NVIDIA is definetely the brand to go for Deep Learning applications, and for now, the only brand broadly supported by deep learning libraries.

In these Tutorials, we will explore how to install and set up an environment to run Deep Learning tasks.

A few useful links :

* **NVIDIA Drivers and Libraries:**
    * **CUDA :** <https://developer.nvidia.com/cuda-zone>
    * **CuDNN :** <https://developer.nvidia.com/cudnn><br><br>
* **Deep Learning Libraries and Frameworks:**
    * **Caffe:** <http://caffe.berkeleyvision.org>
    * **Caffe2:** <https://caffe2.ai>
    * **Microsoft Cognitive Toolkit:** <https://www.microsoft.com/en-us/cognitive-toolkit>
    * **DeepLearning4J:**  <https://deeplearning4j.org>
    * **Keras:** <https://keras.io/>
    * **Lasagne:** <http://lasagne.readthedocs.io/en/latest>
    * **MxNet:** <http://mxnet.io>
    * **PyTorch:** <http://pytorch.org/>
    * **Tensorflow:** <https://www.tensorflow.org/>
    * **Theano:** <http://deeplearning.net/software/theano>
    * **Torch:** <http://torch.ch><br><br>
* **Development Environments:**
    * **Apache Singa:** <http://singa.apache.org>
    * **DeepForge:** <https://github.com/deepforge-dev/deepforge>
    * **Digits:** <https://developer.nvidia.com/digits>
    * **Polyaxon:** <https://github.com/polyaxon/polyaxon><br><br>
* **Virtualisation Platforms:**
    * **Docker:** <https://www.docker.com>
    * **Nvidia-Docker:** <https://github.com/NVIDIA/nvidia-docker><br><br>

---

In this post, we will install the following libraries:

* **Docker:** "Docker is an open platform for developers and sysadmins to build, ship, and run distributed applications, whether on laptops, data center VMs, or the cloud." ([Source](https://www.docker.com/))
* **Nvidia-Docker:** "Nvidia-Docker is a plugin to the original Docker platform which allow containers to interact with Nvidia GPUs." ([Source](https://github.com/NVIDIA/nvidia-docker))

---

### A. Installing Docker

Docker is a very pratical and lightweight platform to quickly deploy virtual machines called **containers**. This article will not explore the difference between a virtual machine and a container, just remember these few facts:

* Faster to launch
* Reduced footprint on system memory
* Reduced footprint on disk.
* Open-Source platform
* Hardware-agnostic
* Platform-agnostic

**To install docker, we need to add the Docker official repository:**
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

**Once done, we need to update the repositories:**
```bash
sudo apt-get update
```

**Finally install docker:**
```bash
sudo apt-get install -y docker-ce
```

**Check the installation is correct:**
```bash
sudo systemctl status docker

# Output:
docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
   Active: active (running) since Sun 2016-05-01 06:53:52 CDT; 1 weeks 3 days ago
     Docs: https://docs.docker.com
 Main PID: 749 (docker)
```

Docker is now up and running, the daemon will automatically start at boot. However, the use of the **sudo command** is required to interact with the Docker-CLI (Command Line interface). In order to simplify the use of Docker, we will give to ourself the right to directly use the Docker-CLI.
```bash
sudo usermod -aG docker ${USER}
su - ${USER} # Reload the user rights

#### If you need to give access to docker to a user which you are not logged in, you can use the following command:
sudo usermod -aG docker username
```

**Now let us perform a small test:**
```bash
docker run hello-world

# Output
Hello from Docker.
This message shows that your installation appears to be working correctly.
```
If you correctly see this message, everything is fine and you are ready to install nvidia-docker. If it doesn't work, check your networking settings (proxy, vpn, etc.)

**A few helpful commands:**

* `docker ps` : List the containers currently running on your machine.
* `docker ps -a` : List all the containers existing on your machine.
* `docker images` : List the images currently available on your machine.
* `docker rmi IMAGE_ID` : Remove an image based on its image_id (available through `docker images`).
* `docker pull USER/IMAGE_NAME` : Download a given image to your machine.
* `docker run .....` : Create a new container.
* `docker start CONTAINER_ID` : Start an existing container based on its container_id (available through `docker ls`).
* `docker start ALIAS` : Start an existing container based on its alias (available through `docker ls`).
* `docker stop CONTAINER_ID` : Stop a container based on its container_id (available through `docker ls`).
* `docker stop ALIAS` : Stop a container based on its alias (available through `docker ls`).
* `docker rm CONTAINER_ID` : Delete a container based on its container_id (available through `docker ls`).
* `docker rm ALIAS` : Delete a container based on its alias (available through `docker ls`).
* `docker attach -it CONTAINER_ID bash` : Create an SSH session into a running container based on its container_id (available through `docker ls`).
* `docker attach -it ALIAS bash` : Create an SSH session into a running container based on its alias (available through `docker ls`).

---

### B. Installing Nvidia-Docker

Docker is up and running, and that's awesome! However, due to hardware-agnostic and platform-agnostic containers, it is possible to access the GPUs from inside a container. Which is, you must admit, a big lame for any deep learner. So Nvidia came up with a *plugin* designed to solve this problem: **Nvidia-Docker**.

**Installation:**
```bash
# Install nvidia-docker and nvidia-docker-plugin
wget -P /tmp https://github.com/NVIDIA/nvidia-docker/releases/download/v1.0.1/nvidia-docker_1.0.1-1_amd64.deb
sudo dpkg -i /tmp/nvidia-docker*.deb && rm /tmp/nvidia-docker*.deb

# Test nvidia-smi
nvidia-docker run --rm nvidia/cuda nvidia-smi

# Output:
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 375.66                 Driver Version: 375.66                    |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX TIT...  Off  | 0000:05:00.0      On |                  N/A |
| 22%   39C    P8    16W / 250W |      1MiB / 12207MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   1  GeForce GTX TIT...  Off  | 0000:06:00.0     Off |                  N/A |
| 22%   39C    P8    14W / 250W |      1MiB / 12207MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
|   2  GeForce GTX TIT...  Off  | 0000:09:00.0     Off |                  N/A |
| 22%   34C    P8    14W / 250W |      1MiB / 12207MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID  Type  Process name                               Usage      |
|=============================================================================|
+-----------------------------------------------------------------------------+
```
If you see the **nvidia-smi** report as shown above, then everything is perfectly up and running.

We can now start using docker quickly deploy containers with all the necessary libraries to train our models.

---

### C. What can I do with Docker and Nvidia-Docker?
<span></span>
#### C.1 Docker ❤️ Nvidia Digits

Nvidia a system called Digits to quickly prototype and launch deep learning models.
Of course, we can simply run this platform using nvidia-docker.

```bash
# We download the image from the Docker-Hub: https://hub.docker.com/r/nvidia/digits/
docker pull nvidia/digits

# Run DIGITS on host port 5678
nvidia-docker run -d -p 5678:5000 -v /datafolder/digits/data/:/data/ -v /datafolder/digits/jobs/:/jobs --name digits nvidia/digits
```

Open now : <https://server-ip:5678>

<center><img alt="digits-docker" src="/images/deeplearning_install-part4/digits.png" style="max-height: 250px;"></center>


<span></span>
#### C.2 Docker ❤️ Tensorflow

You want to run Tensorflow ? No problem, Docker can do this!
```bash
# We download the image from the Docker-Hub: https://hub.docker.com/r/tensorflow/tensorflow/
docker pull tensorflow/tensorflow:latest-gpu-py3

# Run Tensorflow with port 8888 and 6006 open: 8888 => Jupyter Notebook and 6006 => TensorBoard.
nvidia-docker run -d -p 6006:6006 -p 8888:8888 -v /datafolder/tensorflow/:/notebooks/sharedfolder -e PASSWORD=MY_CUSTOM_PASSWORD --name tensorflow tensorflow/tensorflow:latest-gpu-py3
```

Open now : <https://server-ip:8888>
<center><img alt="tensorflow-docker" src="/images/deeplearning_install-part4/tensorflow.png" style="max-height: 250px;"></center>

<span></span>
#### C.2 Docker ❤️ Every Deep Learning Libraries

You don't know what to install but you would love to install something ? There's a container for this: **All-in-one Docker image for Deep Learning**

The following has been installed:

* Tensorflow
* Caffe
* Theano
* Keras
* Lasagne
* Torch (includes nn, cutorch, cunn and cuDNN bindings)
* iPython/Jupyter Notebook (including iTorch kernel)
* Numpy, SciPy, Pandas, Scikit Learn, Matplotlib
* A few common libraries used for deep learning

```bash
# We download the image from the Docker-Hub: https://hub.docker.com/r/gw000/keras/
docker pull floydhub/dl-docker:gpu_temp

# Run the image with port 7777 and 6000 open: 7777 => Jupyter Notebook and 6000 => TensorBoard.
nvidia-docker run -d -p 7777:8888 -p 6000:6006 -v /datafolder/deep_learning/:/root/sharedfolder --name deeplearning_all_in_one floydhub/dl-docker:gpu_temp jupyter notebook

nvidia-docker run -it --rm -p 7894:8888 -p 6894:6006 -v /media/drive1/docker/DL_all_in_one/:/root/sharedfolder --name deeplearning_all_in_one floydhub/dl-docker:gpu_temp jupyter notebook
```

Open now : <https://server-ip:7777>
<center><img alt="tensorflow-docker" src="/images/deeplearning_install-part4/tensorflow.png" style="max-height: 250px;"></center>

---

### D. Conclusion

We have now installed CNTK, Keras and PyTorch. You can try to explore many of the available ressources online or keep installing the other libraries.

* [**Part 1 :** Installation - Nvidia Drivers, CUDA and CuDNN](/2017/deeplearning_install-part1.html)
* [**Part 2 :** Installation - Caffe, Tensorflow and Theano](/2017/deeplearning_install-part2.html)
* [**Part 3 :** Installation - CNTK, Keras and PyTorch](/2017/deeplearning_install-part3.html)
* [**Part 4 :** Installation - Docker for Deep Learning](/2017/deeplearning_install-part4.html)
