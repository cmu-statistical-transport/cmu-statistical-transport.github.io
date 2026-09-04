---
layout: default
title: Home
---

# Statistical Transport Talk Series

**When:** Wednesdays at 1:00pm EST
**Where:** Hybrid - DeGroot Hall (Statistics Department, CMU) / Zoom

---

## About

We are a group of students and faculty at (mostly) the Department of Statistics and Data Science at CMU interested in discussing the role of transport maps in statistics and machine learning. A non-exhaustive list of topics we have been reviewing are: statistical theory (rates of convergence), trajectory inference, applications to causal inference and genomics.

---



## Upcoming Talks

| Date | Speaker | Affiliation | Title |
| 09/09/2026 | Tristan Saidi | CMU Stats & Data Science | Second-order Sinkhorn Geometry for Applications in Statistics and Machine Learning |
| 16/09/2026 | Sivaraman Balakrishan | CMU Stats & Data Science | TBA |

---

## Next Talk
### 09/09/2026 - Tristan Saidi - CMU Stats & Data Science ###
**Second-order Sinkhorn Geometry for Applications in Statistics and Machine Learning**

Entropic optimal transport (EOT) has been widely studied and adopted due to its computational advantages over unregularized optimal transport, as well as the fact that many entropically regularized quantities admit root-n estimation. Unlike unregularized optimal transport, however, EOT does not naturally come equipped with a Riemannian interpretation. In this talk, I will discuss recent work by Lavenant et al. (2026) that proposes a geometry on the space of probability measures which provides a quadratic approximation to the Sinkhorn divergence, a central object in EOT. This construction admits a Riemannian interpretation and offers a promising framework for developing procedures on the space of probability measures that both rely on an underlying Riemannian geometry and retain favorable statistical properties such as root-n estimability. If time permits, I will also discuss ongoing work with collaborators aimed at developing the geometric and statistical infrastructure surrounding this framework.


## Past Talks

### 05/18/2026 -  Katy Craig - UCSB Math  ### 
**Denoising with a Wasserstein Loss**

A fundamental inverse problem in the experimental sciences is to recover an unknown distribution from measurements distorted by a known noise process. In many applications, including high energy particle physics, measurements are given by empirical measures on a high dimensional ground space, making classical binned methods, such as Richardson-Lucy deconvolution, computationally intractable. Motivated by these limitations, the present work studies an alternative formulation of the unfolding problem in which a Wasserstein loss quantifies the similarity between the measurements and the output of the noise model. We establish necessary and sufficient conditions for existence and uniqueness of optimizers and develop a provably convergent Sinkhorn algorithm to compute optimizers. Our algorithm requires only empirical observations of the noise model and measured data and scales with the size of the data, rather than the ambient dimension. Numerical experiments on one- and two-dimensional problems inspired by jet mass unfolding in particle physics demonstrate that the optimal transport approach offers robust, accurate performance compared to classical Richardson–Lucy deconvolution, particularly when binning artifacts are significant.

### 04/20/2026 - Florian Gunsilius - Emory University, Department of Economics ###
**Partial Identification with Schrödinger Bridges**

In many empirical settings, the available data and maintained assumptions do not suffice to point-identify parameters of interest. Partial identification addresses this by characterizing sets guaranteed to contain the true parameter value, often through linear programs that optimize over models compatible with the observed data. These programs can become intractable when the relevant variables are multivalued or even continuous - a "curse of cardinality.'' We phrase these linear programs as optimal transport problems on the path space of hypothetical responses. This insight makes it possible to regularize the problem with an entropy penalty, recasting it as a multi-marginal Schrödinger bridge. We show the latter can be solved efficiently and without sampling via the Sinkhorn algorithm, even when all variables are continuous. We establish convergence of the regularized value to the sharpest bound, derive consistency rates for a plug-in estimator, and obtain its asymptotic distribution. The framework provides the first tractable, non-simulation-based method for computing sharp bounds in nonparametric partial identification problems defined via linear programs. One example are instrumental variable models with continuous treatments and instruments - a setting that has been out of reach for existing approaches.



### 04/13/2026 -  Nicolas Garcia Trillos  - UW Madison, Department of Statistics ###
**Wasserstein-Cramér-Rao theory of unbiased estimation and tradeoffs between accuracy and robustness of estimators**

The quantity of interest in the classical Cramér-Rao theory of unbiased estimation (i.e., the Cramér-Rao lower bound, exact efficiency in exponential families, and asymptotic efficiency of maximum likelihood estimation) is the variance, which represents the instability of an estimator when its value is compared to the value for an independently sampled data set from the same distribution. In this talk, we will be interested in a quantity that represents the instability of an estimator when its value is compared to the value for an infinitesimal additive perturbation of the original data set; we refer to this as the “sensitivity” of an estimator. The resulting theory of sensitivity is based on the Wasserstein geometry in the same way that the classical theory of variance is based on the Fisher-Rao (equivalently, Hellinger) geometry. I’ll present a collection of results which are analogous to the classical case: a Wasserstein-Cramér-Rao lower bound for the sensitivity of any unbiased estimator, a characterization of models in which there exist unbiased estimators achieving the lower bound exactly, and a guarantee that Wasserstein projection estimators achieve the lower bound asymptotically. For both the classical and Wasserstein settings a strong geometric intuition guides the corresponding statistical theories. This same geometric perspective allows us to formulate and answer a natural and important question: how can we construct estimators that, at least asymptotically, balance between accuracy (variance) and robustness (sensitivity) optimally?

### 04/06/2026 -  Aram-Alexandre Pooladian  - Yale ###
**Blind denoising diffusion models and the blessings of dimensionality**
 We provide a mathematical theory for blind denoising diffusion models (BDDMs)---generative models based on denoisers where, crucially, the denoiser is not given the noise level in either the training or sampling stage. We show that when sampling via BDDMs, the noise level can be accurately estimated from a single noisy sample, provided that the intrinsic dimension of the data is sufficiently small compared to the ambient dimension. Consequently, we show that blind denoising diffusion models implicitly track a certain noise schedule along the diffusion, allowing us to justify their correctness as samplers. This joint work with Zahra Kadkhodaie, Sinho Chewi, and Eero Simoncelli (view on arXiv:2602.09639).




### 03/23/2026 -  Romain Lopez  - NYU, Courant Institute and Department of Biology ###
**Modeling Complex System Dynamics with Flow Matching Across Time and Conditions**

Modeling the dynamics of complex real-world systems from temporal snapshot data is crucial for understanding phenomena such as gene regulation, climate change, and financial market fluctuations. Researchers have recently proposed a few methods based either on the Schroedinger Bridge or Flow Matching to tackle this problem, but these approaches remain limited in their ability to effectively combine data from multiple time points and different experimental settings. This integration is essential in real-world scenarios where observations from certain combinations of time points and experimental conditions are missing, either because of experimental costs or sensory failure. To address this challenge, we propose a novel method named Multi-Marginal Flow Matching (MMFM). MMFM first constructs a flow using smooth spline-based interpolation across time points and conditions and regresses it with a neural network using the classifier-free guided Flow Matching framework. This framework allows for the sharing of contextual information about the dynamics across multiple trajectories. We demonstrate the effectiveness of our method on both synthetic and real-world datasets, including a recent single-cell genomics data set with around a hundred chemical perturbations across time points. Our results show that MMFM significantly outperforms existing methods at imputing data at missing time points. 

### 03/16/2026 -  Sanjit Dandapanthula - CMU ###
**Towards a theoretical understanding of reward hacking in guided diffusion models**
Diffusion and flow-based models have become the dominant paradigm for generative modeling. In many practical settings, through the Doob h-transform framework, additional guidance is employed at inference time to obtain samples which maximize a reward function. Despite the widespread use of reward guidance methods, it is known that they empirically suffer from reward hacking, where the guided model over-optimizes the reward function at the cost of previously learned structure. Still, the source of the reward hacking phenomenon remains poorly understood.

In this talk, we carefully analyze the effect of two approximations to the Doob h-transform which are commonly made for computational feasibility: non-memoryless noise schedules and plug-in estimation of the Doob h-function. We demonstrate that even in the simple setting of a Gaussian target under a quadratic reward, these approximations lead to significant reward hacking. Further, we prove that exponentially many particles are required in the plug-in approximation to resolve the reward hacking problem in the tails of the distribution. We then extend our results to Gaussian mixtures and propose a simple schedule for the reward scale to mitigate within-mode reward hacking. Finally, we validate our theoretical results with experiments.

This is a work in progress, done in collaboration with Nicholas Boffi.

### 03/09/2026 - JungHo Lee - Statistics and Data Science, CMU ###
**Transporting policies across networks via Gromov-Wasserstein optimal transport**
 We consider the problem of learning a treatment rule (policy) in a source population and deploying it in a different target population. This is challenging when the two populations differ substantially and units are connected within each population, since units are not directly comparable across networks and a policy’s welfare can depend on the network-wide treatment assignment pattern (interference). We discuss a potential approach based on Gromov-Wasserstein optimal transport for policy transfer in such settings. The key idea is to align the two populations using relational dissimilarities that (i) summarize interference-relevant structure, and (ii) provide the basis for constructing a Gromov-Wasserstein coupling between the source and target. This talk will mostly be informal.

### 02/23/2026 - Jiequn Han - Flatiron Institute ###
**Generative Modeling without Clean Data: Self-Consistent Transport under Black-Box Corruptions**

Generative modeling aims to learn an underlying data distribution from samples. In many scientific and engineering settings, however, clean samples are never observed; instead, data are available only after passing through a noisy, possibly nonlinear and ill-conditioned corruption channel. The challenge is therefore to learn a generative model for the clean distribution using only corrupted observations and access to the forward process.

In this talk, I introduce the Self-Consistent Stochastic Interpolant (SCSI), a transport-based framework that inverts such corruption channels at the level of distributions. The method iteratively refines a transport map so that, when composed with the forward model, it reproduces the observed corrupted distribution. This fixed-point formulation yields an efficient and flexible algorithm requiring only black-box evaluations of the forward operator. We establish convergence guarantees under suitable assumptions and demonstrate strong empirical performance on high-dimensional problems in imaging and scientific reconstruction.

Joint work with Chirag Modi, Eric Vanden-Eijnden, and Joan Bruna (arXiv:2512.10857).

---

### 02/16/2026 - Alberto Gonzalez Sanz - Columbia University, Statistics Department ###
**Quadratically Regularized Optimal Transport**

Optimal transport is well known to suffer from the curse of dimensionality: when marginals are approximated from data, empirical optimal transport converges exponentially slowly as the dimension increases. Entropically regularized optimal transport (EOT) avoids this issue and enjoys parametric sample complexity, but at the cost of producing dense couplings and numerical instability for small regularization parameters. Quadratically regularized optimal transport (QOT) offers a compelling alternative, yielding sparse and computationally stable solutions, yet is commonly believed to inherit the curse of dimensionality due to the lack of smoothness and strong concavity in its dual formulation.

In this talk, we show that this belief is false. We prove that QOT also achieves parametric sample complexity by establishing central limit theorems for its dual potentials, optimal couplings, and transport costs. Our approach relies on new regularity results for the support of the optimal QOT coupling, including Lipschitz properties of its sections, combined with VC-theoretic arguments to control statistical complexity. Along the way, we obtain gradient estimates of independent interest, notably C^{1,1} regularity of the population potentials.

---

### 02/02/2026 - Kyle Schindl - Iowa State, Statistics Department ###
**Distributional Discontinuity Design**

We introduce distributional discontinuity design, a framework for studying distributional causal effects for a scalar outcome at the boundary of a discontinuity in treatment assignment (a generalization of the regression discontinuity design). Our causal estimand is the Wasserstein distance between limiting conditional outcome distributions above and below the treatment discontinuity; a single scale-interpretable measure of distribution shift. We show that this weakly bounds the average treatment effect, where equality holds if and only if the treatment effect is purely additive. Moreover, we show that the Wasserstein distance can be decomposed into squared differences in $L$-moments, thereby quantifying the contribution from location, scale, skewness, etc. to the overall distributional distance. This decomposition provides a novel way of encoding the heterogeneity in the treatment effect.

Next, we extend this framework to distributional kink designs by evaluating the Wasserstein derivative at a deterministic policy kink; this describes the flow of probability mass through the kink. In both settings, we allow the treatment assignment to be either sharp or fuzzy. Notably, we derive new identification results for fuzzy kink designs. Finally, we apply our method on real data by re-analyzing several natural experiments to compare our distributional effects to traditional causal estimands.

---

### 11/20/2025 - Ernesto Araya - Ludwig-Maximilians-Universität München ###
**Matching correlated VAR time series**

We study the problem of aligning time series databases, where a multivariate time series is observed along with a perturbed and permuted version, and the goal is to recover the unknown matching between them. To model this, we introduce a probabilistic framework in which both series follow a correlated vector autoregressive (VAR) process jointly. This generalizes the classical problem of matching independent point clouds to the time series setting, with envisaged applications in privacy and sensor fusion. We derive the maximum likelihood estimator (MLE), leading to a quadratic optimization over permutations, and theoretically analyze an estimator based on linear assignment.

For the linear assignment approach, we establish recovery guarantees, identifying correlation thresholds that allow for perfect or partial recovery. We also explore convex relaxations of the MLE, including relaxations over the Birkhoff polytope, which allow the joint estimation of the hidden permutation and the autoregressive process parameters. To solve it, we propose an algorithm based on alternating optimization. Empirically, we find that the linear assignment method often matches or outperforms MLE relaxations, even when the latter have oracle access to the underlying VAR parameters, for recovering the matching. These findings highlight the theoretical and practical effectiveness of efficient algorithms for structured time series alignment.

---

### 10/23/2025 - Andres Riveros - Columbia University , Statistics Department ###
**Quadratically Regularized Optimal Transport**

In optimal transport, quadratic regularization (QOT) is an alternative to entropic regularization (EOT) when sparse couplings or small regularization parameters are desired. Here, quadratic regularization means that transport couplings are penalized by the squared L2 norm, or equivalently, the χ2 divergence. In this talk, I will present results from two papers (joint work with Alberto González-Sanz and Marcel Nutz) about the analytical properties of the QOT problem. One involves quantifying the behavior of the sparsity of the support as the regularization parameter shrinks, while the other provides an efficient algorithm to compute QOT that avoids some of the few drawbacks of the celebrated Sinkhorn algorithm.

---

### 10/06/2025 - Florian Gunsilius - Emory University, Department of Economics ###
**Optimal transport and difference in differences**

---

### 09/25/2025 - Sanjit Dandapanthula - CMU, Department of Statistics and Data Science ### 
**Gromov-Wasserstein distances between Gaussian distributions**

---

## Members

### Faculty
- Sivaraman Balakrishnan
- Florian Gunsilius
- Arun Kumar Kuchibhotla
- Mikael Kuusela
- Gonzalo Mena
- Larry Wasserman

### Students
- Tristan Saidi
- Soheun Yi

---

## Contact

If you want to participate, attend, or present your work, please contact the organizers:

**Gonzalo Mena**
Email: [gmena@andrew.cmu.edu](mailto:gmena@andrew.cmu.edu)
**Tristan Saidi**
Email: [tsaidi@andrew.cmu.edu](mailto:tsaidi@andrew.cmu.edu)
**Soheun Yi**
Email: [soheunyi@andrew.cmu.edu](mailto:tsaidi@andrew.cmu.edu)

