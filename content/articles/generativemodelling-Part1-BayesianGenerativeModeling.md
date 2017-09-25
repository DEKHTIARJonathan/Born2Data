Title: A Guide Through Generative Models - Part 1 - Bayesian Sampling
HeadTitle: A Guide Through Generative Models - Part 1
Date: 2017-09-24 12:00
Category: Generative Model
Tags: Deep Learning, Python, Tutorial, Guide, Machine Learning, GAN, VAE, Bayesian, Generative
Slug: generative_models-part1
Author: Jonathan DEKHTIAR
Headline: How To Generate new Data with Bayesian Sampling
Status: draft

# A Guide Through Generative Models - Index

Dear fellow machine learner, in this serie, we are going to explore some Unsupervised Learning algorithm in the objective to design a generative system capable of reproducing new data not existing in the original dataset.

* **Part 1 :** Bayesian Inference and Single Mode Learning - *This article*
* [**Part 2 :** Improving Bayesian Inference with Multi-Modes learning](#Coming_Soon)
* [**Part 3 :** Variational AutoEncoders: Deep Learning with Bayes](#Coming_Soon)
* [**Part 4 :** Generative Adversarial Neural Networks aka. GANs](#Coming_Soon)

---

# 1. Rapid Overview of Unsupervised Learning and Generative AI

## 1.1 Supervised vs Unsupervised Learning

Most of the classical and widely-known techniques in Machine Learning fit in the realm of **Supervised Learning**. They usually pursue one of these two goals: classification (i.e. predicting a label/category) or regression (i.e. predicting the value of a given parameter). The key idea in **Supervised Learning** is that the machine learning model is *trained* to map some entries (i.e. data) with a specific output. We find in this area, objectives like *object classification*, *time series prediction*, etc.

On the other hand, **Unsupervised Learning** does not focus on learning to map an input with an output, they mostly try to discover or learn the data distribution. Such an objective is used for data clustering and generative models.

## 1.2 Generative Models and sampling from a latent space

As stated before, with *Unsupervised Learning* we focus on learning a distribution, the distribution of the input data. This distribution can be used then be used to generate new data sample that comes from the same (or a similar-looking) data distribution.

#### How a distribution can allow me to generate data samples ?

Let us consider a simple example with with a gaussian distribution defined as followed: $x \sim \mathcal{N} (200, 40)$.
The chart below will allow you to visualise its *probability density function* also called *pdf*.

<center><img alt="gaussian distribution" src="/images/generative_models-part1/gaussian_distribution.png" style="max-height: 250px;"></center>

Knowing this distribution, is there any way to generate a data point that follows the given distribution ?

**Absolutely!** And this is a very simple process:

1. Randomly sample from the latent space with $z \in [0, 1]$: $random\_sample() = z$.
2. Use the *percent point function* of the normal distribution which gives the following mapping: $f: z \mapsto x$

Alright, let's try this in python now:

```python
import scipy.stats
import numpy as np

def generate_new_data(mu, sigma):
    z = np.random.rand()
    return z, scipy.stats.norm(mu, sigma).ppf(z) # ppf : Percent Point Function

# ================= Sanity Checks =================

test1 = np.round(scipy.stats.norm(200, 40).ppf(0.5))
test2 = np.round(scipy.stats.norm(200, 40).ppf(0.5 + 0.3413))
test3 = np.round(scipy.stats.norm(200, 40).ppf(0.5 + 0.3413 + 0.1359))

print("Test 1 (should give: 200) = %d" % test1)
# >>> Test 1 (should give: 200) = 200
print("Test 2 (should give: 200 + sigma = 240) = %d" % test2)
# >>> Test 2 (should give: 200 + sigma = 240) = 240
print("Test 3 (should give: 200 + 2 * sigma = 280) = %d" % test3)
# >>> Test 3 (should give: 200 + 2 * sigma = 280) = 280

# ======== Let's sample 5 new data point ==========
for _ in range(5):
    print("Latent Variable: z = %.3f => Result: x_new = %.2f" % generate_new_data(200, 40))

# >>> Latent Variable: z = 0.268 => Result: x_new = 175.35
# >>> Latent Variable: z = 0.779 => Result: x_new = 230.87
# >>> Latent Variable: z = 0.757 => Result: x_new = 227.93
# >>> Latent Variable: z = 0.776 => Result: x_new = 230.39
# >>> Latent Variable: z = 0.346 => Result: x_new = 184.14
```

All of this can be done a bit more rapidly using only numpy (even if it is less comprehensive):

```python
import numpy as np

for _ in range(5):
    print("Result: x_new = %.2f" % np.random.normal(200, 40))

# >>> Result: x_new = 238.21
# >>> Result: x_new = 199.43
# >>> Result: x_new = 206.17
# >>> Result: x_new = 153.71
# >>> Result: x_new = 242.44
```

In summary, we sample $z$ from the latent space, and use the *ppf* function to transform the ramdomly chosen sample into actual target data similar to the dataset used to learn the distribution.

# 2. Using Bayes Classifier as a Generative Model

The *Bayes Classifier* is maybe one of the most widely known Machine Learning model. However, it is more frequently used a **classifier**, and today this is not our focus.

#### Alright, so can I use the Bayes Classifier to generate new data ?

For the following we will use the following notations:

* $x$: the input data.
* $y$: the data label.
* $p(x|y)$: probability of x given its label y (general notation, apply to any value of y).
* $p(x|y=1)$: probability of x given its label y=1 (same as above, except this time we focus on the case y=1).
* $p(y|x)$: probability of y given a data point x.

In the list above, you will recognise: $p(y|x)$ which is classical objective in classification, however this article focus on generating new data points. Thus, we will focus on the opposite objective: learning $p(x|y)$. In short, the objective is to focus on learning for each **class** $y_i$ the following conditional probability: $p(x|y)$ rather than directly trying to model $p(y|x)$.

## 2.1. Overview of the complete process from a theorical perspective

### 2.1.1. Training the Bayes Classifier to learn the data distribution

In order to learn the data distribution, we will need to fit as many Gaussians to the data than we have labels. The objective is to learn one $p(x|y)$ as a Gaussian for each label.

In order to learn $p(x|y)$, we will process as followed for each label $y_i$:

1. Find all the data points $x_i$ that belong to the class $y_i$.
2. Compute the following:
    1. $\mu_{y_i}$ = mean of those $x_i$.
    2. $\sigma_{y_i}$ = standard deviation of those $x_i$.

### 2.1.2. Choosing a label at random to generate with the learned distribution $p(x|y)$ a new data point.

In order to sample a new data point, we firstly need to choose from which label (i.e. $y_i$) we want it to be generated.

**Problem:** What if the dataset is not *balanced* ? Example: we have $40%$ of data with the label 'A' and $60% with label 'B'?
It seems obvious that we randomly pick a label, it will give us a biaised situation generating more data with label 'A' than it should have to.

*Solution:* Instead of randomly sampling from a uniform distribution, we can learn the distribution of $y$ and sample from it:
$$p(y == k) = \dfrac{\text{# of images of class k}}{\text{# total of images}}$$

### 2.1.3. A label $y = k$ has been randomly sampled, now let's generate a new data point.

Now to perform the final step, we can just sample from the Gaussian learned: $x \sim \mathcal{N} (\mu_{y_i}, \sigma_{y_i})$.

---

### D. Conclusion

We have seen in this article how to generate new data samples, however they do not look very good. We will explore in the upcoming articles how to improve these results and obtain more realistic generated sampled.

* **Part 1 :** Bayesian Inference and Single Mode Learning - *This article*
* [**Part 2 :** Improving Bayesian Inference with Multi-Modes learning](#Coming_Soon)
* [**Part 3 :** Variational AutoEncoders: Deep Learning with Bayes](#Coming_Soon)
* [**Part 4 :** Generative Adversarial Neural Networks aka. GANs](#Coming_Soon)
