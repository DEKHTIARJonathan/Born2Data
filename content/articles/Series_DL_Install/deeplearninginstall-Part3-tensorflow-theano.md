Title: Deep Learning Installation Tutorial - Part 3 - CNTK, Keras, and PyTorch
HeadTitle: Deep Learning Installation Tutorial - Part 3
Date: 2017-08-08 10:15
Category: Deep Learning
Tags: Deep Learning, Python, Tutorial, Installation, Machine Learning, CNTK, Keras, PyTorch
Slug: deeplearning_install-part3
Author: Jonathan DEKHTIAR
Headline: How to install CNTK, Keras, and PyTorch

# Deep Learning Installation Tutorial - Index

Dear fellow deep learner, here is a tutorial to quickly install some of the major Deep Learning libraries and set up a complete development environment.

* [**Part 1 :** Installation - Nvidia Drivers, CUDA and CuDNN](/2017/deeplearning_install-part1.html)
* [**Part 2 :** Installation - Caffe, Tensorflow and Theano](/2017/deeplearning_install-part2.html)
* [**Part 3 :** Installation - CNTK, Keras and PyTorch](/2017/deeplearning_install-part3.html)
* [**Part 4 :** Installation - Docker for Deep Learning](/2017/deeplearning_install-part4.html)

---

# Deep Learning Installation Tutorial - Part 3 - CNTK, Keras and PyTorch

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

* **CNTK:** "The Microsoft Cognitive Toolkit (https://cntk.ai), is a unified deep-learning toolkit that describes neural networks as a series of computational steps via a directed graph." ([Source](https://github.com/Microsoft/cntk))
* **Keras:** "Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano. It was developed with a focus on enabling fast experimentation. Being able to go from idea to result with the least possible delay is key to doing good research." ([Source](https://github.com/fchollet/keras))
* **PyTorch:** "PyTorch is a Python package that provides Tensor computation (like NumPy) with strong GPU acceleration and Deep neural networks built on a tape-based autograd system" ([Source](https://github.com/pytorch/pytorch))

---

### A. Installing CNTK

The Microsoft Cognitive Toolkit - CNTK - is a unified deep-learning toolkit by Microsoft.

**First, we need to install the dependencies:**
```bash
sudo apt-get install openmpi-bin
```

**Then we can install the correct binaries:**

In order to install the CNTK library, please pick the correct link corresponding to your situation (you can find the latest versions on the [official website](https://docs.microsoft.com/en-us/cognitive-toolkit/Setup-Linux-Python))

<table class="table table-striped table-bordered" style="width:100%">
    <thead>
        <tr>
            <th style="text-align:center">Python</th>
            <th style="text-align:center">Flavor</th>
            <th>URL</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="text-align:center">2.7</td>
            <td>CPU-Only</td>
            <td>
                <a href="https://cntk.ai/PythonWheel/CPU-Only/cntk-2.1-cp27-cp27mu-linux_x86_64.whl">
                     https://cntk.ai/PythonWheel/CPU-Only/cntk-2.1-cp27-cp27mu-linux_x86_64.whl
                </a>
            </td>
        </tr>
        <tr>
            <td></td>
            <td>GPU</td>
            <td>
                <a href="https://cntk.ai/PythonWheel/GPU/cntk-2.1-cp27-cp27mu-linux_x86_64.whl">
                    https://cntk.ai/PythonWheel/GPU/cntk-2.1-cp27-cp27mu-linux_x86_64.whl
                </a>
            </td>
        </tr>
        <tr>
            <td style="text-align:center">3.4</td>
            <td>CPU-Only</td>
            <td>
                <a href="https://cntk.ai/PythonWheel/CPU-Only/cntk-2.1-cp34-cp34m-linux_x86_64.whl">
                    https://cntk.ai/PythonWheel/CPU-Only/cntk-2.1-cp34-cp34m-linux_x86_64.whl
                </a>
            </td>
        </tr>
        <tr>
            <td></td>
            <td>GPU</td>
            <td>
                <a href="https://cntk.ai/PythonWheel/GPU/cntk-2.1-cp34-cp34m-linux_x86_64.whl">
                    https://cntk.ai/PythonWheel/GPU/cntk-2.1-cp34-cp34m-linux_x86_64.whll
                </a>
            </td>
        </tr>
        <tr>
            <td style="text-align:center">3.5</td>
            <td>CPU-Only</td>
            <td>
                <a href="https://cntk.ai/PythonWheel/CPU-Only/cntk-2.1-cp35-cp35m-linux_x86_64.whl">
                    https://cntk.ai/PythonWheel/CPU-Only/cntk-2.1-cp35-cp35m-linux_x86_64.whl
                </a>
            </td>
        </tr>
        <tr>
            <td></td>
            <td>GPU</td>
            <td>
                <a href="https://cntk.ai/PythonWheel/GPU/cntk-2.1-cp35-cp35m-linux_x86_64.whl">
                    https://cntk.ai/PythonWheel/GPU/cntk-2.1-cp35-cp35m-linux_x86_64.whl
                </a>
            </td>
        </tr>
        <tr>
            <td style="text-align:center">3.6</td>
            <td>CPU-Only</td>
            <td>
                <a href="https://cntk.ai/PythonWheel/CPU-Only/cntk-2.1-cp36-cp36m-linux_x86_64.whl">
                    https://cntk.ai/PythonWheel/CPU-Only/cntk-2.1-cp36-cp36m-linux_x86_64.whl
                </a>
            </td>
        </tr>
        <tr>
            <td></td>
            <td>GPU</td>
            <td>
                <a href="https://cntk.ai/PythonWheel/GPU/cntk-2.1-cp36-cp36m-linux_x86_64.whl">
                    https://cntk.ai/PythonWheel/GPU/cntk-2.1-cp36-cp36m-linux_x86_64.whl
                </a>
            </td>
        </tr>
    </tbody>
</table>

Installing the chosen binary with pip:
```bash
# Python2
sudo pip install <url>

# Python3
sudo pip3 install <url>
```

**Now let us perform a small test:**

```bash
python
>>> import cntk
>>> cntk.__version__
'2.1'
```

---

### B. Installing Keras

Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano. It was developed with a focus on enabling fast experimentation. Being able to go from idea to result with the least possible delay is key to doing good research.

It is also one of the easiest library to install:

**Installation:**
```bash
# Python2
sudo pip install keras

# Python3
sudo pip3 install keras
```

Let us try the installation:
```bash
python
>>> import keras
>>> print(keras.__version__)
2.0.6
>>> print(keras.backend.backend())
'tensorflow'
```

**Change the Keras Backend:**

By default, Keras use Tensorflow as backend, if you prefer it can use CNTK or Theano.

```python
import os, importlib
from keras import backend as K

def set_keras_backend(backend):

    if K.backend() != backend:
        os.environ['KERAS_BACKEND'] = backend
        importlib.reload(K)
        assert K.backend() == backend

set_keras_backend("theano")
set_keras_backend("tensorflow")
set_keras_backend("cntk")
```

---

### C. Installing PyTorch

PyTorch is a deep learning framework that puts Python first.

This library is also quite easy to install:

I recommend using the official install command generator available on the [official website](http://pytorch.org/).

<center><img alt="pyTorch installation" src="/images/deeplearning_install-part3/pyTorch.png" style="max-height: 250px;"></center>

```bash
# Python 2.7
pip install http://download.pytorch.org/whl/cu80/torch-0.2.0.post1-cp27-cp27m-manylinux1_x86_64.whl
pip install torchvision

# if the above command does not work, then you have python 2.7 UCS2, use this command
pip install http://download.pytorch.org/whl/cu80/torch-0.2.0.post1-cp27-cp27mu-manylinux1_x86_64.whl
pip install torchvision

# Python 3.5
pip3 install http://download.pytorch.org/whl/cu80/torch-0.2.0.post1-cp35-cp35m-manylinux1_x86_64.whl
pip3 install torchvision

# Python 3.6
pip3 install http://download.pytorch.org/whl/cu80/torch-0.2.0.post1-cp36-cp36m-manylinux1_x86_64.whl
pip3 install torchvision
```

Let us try the installation:
```bash
python
>>> import torch
>>> torch.manual_seed(1)
>>> V_data = [1., 2., 3.]
>>> V = torch.Tensor(V_data)
>>> print(V[0])
1.0
```

---

### D. Conclusion

We have now installed CNTK, Keras and PyTorch. You can try to explore many of the available ressources online or keep installing the other libraries.

* [**Part 1 :** Installation - Nvidia Drivers, CUDA and CuDNN](/2017/deeplearning_install-part1.html)
* [**Part 2 :** Installation - Caffe, Tensorflow and Theano](/2017/deeplearning_install-part2.html)
* [**Part 3 :** Installation - CNTK, Keras and PyTorch](/2017/deeplearning_install-part3.html)
* [**Part 4 :** Installation - Docker for Deep Learning](/2017/deeplearning_install-part4.html)
