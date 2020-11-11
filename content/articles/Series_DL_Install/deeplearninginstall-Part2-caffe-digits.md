Title: Deep Learning Installation Tutorial - Part 2 - Caffe, Tensorflow and Theano
HeadTitle: Deep Learning Installation Tutorial - Part 2
Date: 2017-05-13 10:15
Category: Deep Learning
Tags: Deep Learning, Python, Tutorial, Installation, Machine Learning, Caffe, TensorFlow, Theano, Tensor, NumPy
Slug: deeplearning_install-part2
Author: Jonathan DEKHTIAR
Headline: How to install Caffe, Tensorflow and Theano

# Deep Learning Installation Tutorial - Index

Dear fellow deep learner, here is a tutorial to quickly install some of the major Deep Learning libraries and set up a complete development environment.

* [**Part 1 :** Installation - Nvidia Drivers, CUDA and CuDNN](/2017/deeplearning_install-part1.html)
* [**Part 2 :** Installation - Caffe, Tensorflow and Theano](/2017/deeplearning_install-part2.html)
* [**Part 3 :** Installation - CNTK, Keras and PyTorch](/2017/deeplearning_install-part3.html)
* [**Part 4 :** Installation - Docker for Deep Learning](/2017/deeplearning_install-part4.html)

---

# Deep Learning Installation Tutorial - Part 2 - Caffe, Tensorflow and Keras

There are a few major libraries available for Deep Learning development and research – Caffe, Keras, TensorFlow, Theano, and Torch, MxNet, etc.
These libraries use GPU computation power to speed up deep neural networks training which can be very long on CPU (+/- 40 days for a standard convolutional neural network for the ImageNet Dataset).

NVIDIA is definitely the GPU brand to go for Deep Learning applications, and for now, the only brand broadly supported by deep learning libraries.

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
    * **TensorLayer:** <http://tensorlayer.readthedocs.io/en/stable/>
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

* **Caffe:** "Caffe is a deep learning framework made with expression, speed, and modularity in mind." ([Source](http://caffe.berkeleyvision.org/))
* **Tensorflow:** "TensorFlow is an open source software library for numerical computation using data flow graphs." ([Source](http://deeplearning.net/software/theano/))
* **Theano:** "Theano is a Python library that allows you to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently with a tight integration with NumPy" ([Source](http://deeplearning.net/software/theano/))

---

### A. Installing Caffe

Caffe is one of the main deep learning libraries for visual data analysis, and it was the first library I learned to train deep neural networks. Fast and reliable, working on android, I really appreciate using this library.

In July 2017, Caffe is compiled to use Cuda Toolkit 8.0, cuDNN 5.1 and OpenCV 2 or 3.

First, we need to make sure the system is up to date:
```bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
```

Then, we want to install the dependencies:

```bash
sudo apt-get install -y gcc g++ gfortran cmake build-essential linux-image-generic
sudo apt-get install -y git wget pkg-config

sudo apt-get install -y   
sudo apt-get install -y libprotobuf-dev libleveldb-dev libsnappy-dev libhdf5-serial-dev protobuf-compiler libopencv-dev
sudo apt-get install -y --no-install-recommends libboost-all-dev
sudo apt-get install -y libgflags-dev libgoogle-glog-dev liblmdb-dev libblas-dev libatlas-base-dev libopenblas-dev

# (Python 2.7 development files)
sudo apt-get install -y python-dev
sudo apt-get install -y python-pip
sudo apt-get install -y python-nose python-numpy python-scipy

# (or, Python 3.5 development files)
sudo apt-get install -y python3-dev
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-nose python3-numpy python3-scipy
```

```bash
# Python2
sudo pip install numpy scipy scikit-learn protobuf

# Python3
sudo pip3 install numpy scipy scikit-learn protobuf
```

Then we need the Python Package **CUDAMat**:
```bash
git clone https://github.com/cudamat/cudamat
cd cudamat

# Python2
python setup.py build
sudo python setup.py install

# Python3
python3 setup.py build
sudo python3 setup.py install
```

**For AWS Users:** You will need to disable the camera driver or the computer will complain while working with images:
```bash
sudo ln /dev/null /dev/raw1394
```

**Now, we are ready to install Caffe:**

```bash
cd ..
git clone https://github.com/BVLC/caffe.git
cd caffe
cp Makefile.config.example Makefile.config
make all
make test
make runtest
make pycaffe
```

Let us check that the installation is correct:
```bash
make pycaffe
```

Now, we need to compile the pycaffe library:
```bash
echo -e "\nexport PYTHONPATH=/path/to/caffe/python:$PYTHONPATH" >> .bashrc
```

You can now test your caffe installation:

```bash
python
>>> import caffe
```

---

### B. Installing TensorFlow

TensorFlow is one of the most supported library for deep learning applications and research. A low-level library which is extremely flexible when you need to access low-level features and precisely your models.

It is also one of the easiest library to install:

**CPU-Only Installation:**
```bash
# Python2
sudo pip install tensorflow

# Python3
sudo pip3 install tensorflow
```

**GPU-Enabled Installation:**
```bash
# Python2
sudo pip install tensorflow-gpu

# Python3
sudo pip3 install tensorflow-gpu
```

Let us try the installation:
```bash
python
>>> import tensorflow as tf
>>> hello = tf.constant('Hello, TensorFlow!')
>>> sess = tf.Session()
>>> sess.run(hello)
'Hello, TensorFlow!'
>>> a = tf.constant(10)
>>> b = tf.constant(32)
>>> sess.run(a + b)
42
```

---

### C. Installing Theano

Theano is great library that allows you to manage your data in a very similar way that NumPy does, which is very pratical for long time python users.

This library is also quite easy to install:

```bash
# Python2
sudo pip install Theano

# Python3
sudo pip3 install Theano
```

Let us try the installation:
```bash
python
>>> from theano import tensor as T, function, printing
>>> x = T.dvector()
>>> hello_world_op = printing.Print('hello world')
>>> printed_x = hello_world_op(x)
>>> f = function([x], printed_x)
>>> r = f([1, 2, 3])
hello world __str__ = [ 1.  2.  3.]
```

---

### D. Conclusion

We have now installed Caffe, TensorFlow and Theano. You can try to explore many of the available ressources online or keep installing the other libraries.

* [**Part 1 :** Installation - Nvidia Drivers, CUDA and CuDNN](/2017/deeplearning_install-part1.html)
* [**Part 2 :** Installation - Caffe, Tensorflow and Theano](/2017/deeplearning_install-part2.html)
* [**Part 3 :** Installation - CNTK, Keras and PyTorch](/2017/deeplearning_install-part3.html)
* [**Part 4 :** Installation - Docker for Deep Learning](/2017/deeplearning_install-part4.html)
