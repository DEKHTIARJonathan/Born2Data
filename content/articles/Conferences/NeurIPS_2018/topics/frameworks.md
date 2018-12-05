Title: NeurIPS 2018 - Research Log
HeadTitle: NeurIPS 2018 - Research Log
Date: 2018-12-03 10:15
Category: Deep Learning
Tags: Deep Learning, Research, Statistics, Computer Vision, NLP, NIPS, NeurIPS
Slug: NeurIPS_2018/topics/frameworks
Author: Jonathan DEKHTIAR
Headline: A condensed research review of the talks and poster sessions I attended.
Status: draft

# A. Computer Vision
--------------------

### 1. Faster Neural Networks Straight from JPEG - Uber AI Labs

- **Link to paper:** <https://papers.nips.cc/paper/7649-faster-neural-networks-straight-from-jpeg.pdf>

- **Useful code to reproduce:** <https://github.com/uber-research/jpeg2dct>



The core idea is pretty straightforward, instead of feeding a CNN Pixel values across
the 3 RGB channels, the feed the network with the JPEGEncoded version of the image.

This brings two interesting properties:

- **Computation Related:** Save some data loading computation as we don't have to decode the image.

- **Memory related:** The JPEG Encoded image is already a compressed representation of the image.
Thus saving memory and which could also facilitate learning.

This paper claims a **77% speed increase on ResNet 50** while keeping the same accuracy. It shall be crosschecked
with efficient data loading pipeline such as DALI, probably we can expect a bit less, still it looks promising).

One of the few concerns that might be raised with this paper is the following:

- **Data Augmentation:** as it is impossible (to the best of my knowledge) to perform any data augmentation (crop, brightness, contrast, etc...).
This enforce a quite inefficient pipeline at training: JPEG_Decode => Augment (possibly N times) => JPEG_Encode => Access to DCT coefficients.

----------------------

### 2. An Intriguing Failing of Convolutional Neural Networks and the CoordConv Solution - Uber AI Labs

**Link to paper:** <https://arxiv.org/abs/1807.03247/>

**Blog Post:** <https://eng.uber.com/coordconv/>

----------------------

### 3. Which Neural Net Architectures Give Rise To Exploding and Vanishing Gradients?

**Link to paper:** <https://arxiv.org/abs/1807.03247/>


----------------------

### 4. Scalable Methods for 8-bit Training of Neural Networks

**Link to paper:** <https://arxiv.org/abs/1805.11046>

**Blog Post:** <https://ai.intel.com/scalable-methods-for-8-bit-training-of-neural-networks-blog/>

**Github Repo :** <https://github.com/eladhoffer/quantized.pytorch>


----------------------

### 5. A Linear Speedup Analysis of Distributed Deep Learning with Sparse and Quantized Communication

**Link to paper:** <https://papers.nips.cc/paper/7519-a-linear-speedup-analysis-of-distributed-deep-learning-with-sparse-and-quantized-communication>


----------------------

### 6. Batch-Instance Normalization for Adaptively Style-Invariant Neural Networks

**Link to paper:** https://arxiv.org/abs/1805.07925>

**Github Repo:** <https://github.com/hyeonseob-nam/Batch-Instance-Normalization>


----------------------

### 7. BML: A High-performance, Low-cost Gradient Synchronization Algorithm for DML Training

**Link to paper:** <https://papers.nips.cc/paper/7678-bml-a-high-performance-low-cost-gradient-synchronization-algorithm-for-dml-training>

*Need to test*


----------------------

### 8. ChannelNets: Compact and Efficient Convolutional Neural Networks via Channel-Wise Convolutions

**Link to paper:** <https://arxiv.org/abs/1809.01330>

**Github Repo:** <https://github.com/HongyangGao/ChannelNets>


----------------------

### 9. Heterogeneous Bitwidth Binarization in Convolutional Neural Networks

**Link to paper:** <https://arxiv.org/abs/1805.10368>

**Github Repo:** *Coming soon in PyTorch*


----------------------

### 10. Bayesian Distributed Stochastic Gradient Descent

**Link to paper:** <https://papers.nips.cc/paper/7874-bayesian-distributed-stochastic-gradient-descent>

----------------------

### 11. Frequency-Domain Dynamic Pruning for Convolutional Neural Networks

**Link to paper:** <https://papers.nips.cc/paper/7382-frequency-domain-dynamic-pruning-for-convolutional-neural-networks.pdf>

----------------------

### 12. Kalman Normalization: Normalizing Internal Representations Across Network Layers

**Link to paper:** <https://papers.nips.cc/paper/7288-kalman-normalization-normalizing-internal-representations-across-network-layers>

**Related study:** <https://arxiv.org/abs/1802.03133>

----------------------

### 13. Moonshine: Distilling with Cheap Convolutions

**Link to paper:** <https://arxiv.org/abs/1711.02613>

**Github Repo:** <https://github.com/BayesWatch/pytorch-moonshine>

----------------------

### 14. Deep Neural Networks with Box Convolutions

**Link to paper:** <https://papers.nips.cc/paper/7859-deep-neural-networks-with-box-convolutions>

**Paper Summary (by 1st author):** <https://gist.github.com/shrubb/f131e99eb3352cdebe506d2ad988c1b7>

----------------------

### 16. Mesh-TensorFlow: Deep Learning for Supercomputers

**Link to paper:** <https://arxiv.org/abs/1811.02084>

**Github Repo:** <https://github.com/tensorflow/mesh/tree/master/mesh_tensorflow>

----------------------

### 17. Visualizing the Loss Landscape of Neural Nets

**Link to paper:** <https://arxiv.org/abs/1712.09913>

**Github Repo:** <https://github.com/tomgoldstein/loss-landscape>

----------------------

### 18. Learning Overparameterized Neural Networks via Stochastic Gradient Descent on Structured Data

**Link to paper:** <https://arxiv.org/abs/1808.01204>

**Slides:** <https://nips.cc/media/Slides/nips/2018/220cd(04-10-05)-04-10-20-12563-Learning_Overpa.pdf>

----------------------

### 19. Gradient Sparsification for Communication-Efficient Distributed Optimization

**Link to paper:** <https://arxiv.org/abs/1710.09854>

----------------------

### 20. GradiVeQ: Vector Quantization for Bandwidth-Efficient Gradient Aggregation in Distributed CNN Training

**Link to paper:** <https://arxiv.org/abs/1811.03617>

----------------------

### 15. Which Neural Net

**Link to paper:** <https://arxiv.org/abs/1807.03247/>
