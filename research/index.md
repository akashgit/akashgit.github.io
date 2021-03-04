---
layout: default
title: Research
---

### Publications
#### For the most recent work, please look up my home page or my [google scholar page](https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en).
<p>
<a href="https://akashgit.github.io/autoencoding_vi_for_topic_models"><b>Autoencoding Variational Inference for Topic Models</b></a>.&nbsp;Akash Srivastava and Charles Sutton. In <i>International Conference on Learning Representations (ICLR)</i>.  2017.
</p>

<p>
   [<a href="https://arxiv.org/abs/1703.01488">arXiv</a>
	| <a href="javascript:toggle('bibsrivastava17lda', 'bib_link_srivastava17lda', 'bib')"  id="bib_link_srivastava17lda">bib</a>
	| <a href="javascript:toggle('abssrivastava17lda', 'abs_link_srivastava17lda', 'abstract')" id="abs_link_srivastava17lda">abstract</a>
	| <a href="https://openreview.net/forum?id=BybtVK9lg">discussion</a>
	| <a href="https://github.com/akashgit/autoencoding_vi_for_topic_models">source code</a>
   
 ]
</p>



<div id="divsrivastava17lda"></div>
<div style="display:none;" id="abssrivastava17lda"><div class="abstract">Topic models are one of the most popular methods for learning representations of text, but a major challenge is that any change to the topic model requires mathematically deriving a new inference algorithm. A promising approach to address this problem is autoencoding variational Bayes (AEVB), but it has proven diffi- cult to apply to topic models in practice. We present what is to our knowledge the first effective AEVB based inference method for latent Dirichlet allocation (LDA), which we call Autoencoded Variational Inference For Topic Model (AVITM). This model tackles the problems caused for AEVB by the Dirichlet prior and by component collapsing. We find that AVITM matches traditional methods in accuracy with much better inference time. Indeed, because of the inference network, we find that it is unnecessary to pay the computational cost of running variational optimization on test data. Because AVITM is black box, it is readily applied to new topic models. As a dramatic illustration of this, we present a new topic model called ProdLDA, that replaces the mixture model in LDA with a product of experts. By changing only one line of code from LDA, we find that ProdLDA yields much more interpretable topics, even if LDA is trained via collapsed Gibbs sampling.</div></div>

<div style="display:none;" id="bibsrivastava17lda"><pre class="bibtex">@inproceedings{srivastava17lda,
  author = {Srivastava, Akash and Sutton, Charles},
  booktitle = {International Conference on Learning Representations (ICLR)},
  title = {Autoencoding Variational Inference for Topic Models},
  year = {2017}
}
</pre></div>


	         


<p>
<a href="https://arxiv.org/abs/1705.07761"><b>VEEGAN: Reducing Mode Collapse in GANs using Implicit Variational Learning</b></a>.&nbsp;Akash Srivastava, Lazar Valkov, Chris Russell, Michael Gutmann and Charles Sutton.
	In <i>Advances in Neural Information Processing Systems (NIPS)</i>.  2017.

</p>

<p>
   [ <a href="https://arxiv.org/abs/1705.07761">.pdf</a>
	| <a href="javascript:toggle('bibsrivastava17veegan', 'bib_link_srivastava17veegan', 'bib')"  id="bib_link_srivastava17veegan">bib</a>
	| <a href="javascript:toggle('abssrivastava17veegan', 'abs_link_srivastava17veegan', 'abstract')" id="abs_link_srivastava17veegan">abstract</a>
	| <a href="https://akashgit.github.io/VEEGAN/">code and data</a>
   
   ]
</p>



<div id="divsrivastava17veegan"></div>
<div style="display:none;" id="abssrivastava17veegan"><div class="abstract">Deep generative models provide powerful tools for distributions over complicated manifolds, such as those of natural images. But many of these methods, including generative adversarial networks (GANs), can be difficult to train, in part because they are prone to mode collapse, which means that they characterize only a few modes of the true distribution. To address this, we introduce VEEGAN, which features a reconstructor network, reversing the action of the generator by mapping from data to noise. Our training objective retains the original asymptotic consistency guarantee of GANs, and can be interpreted as a novel autoencoder loss over the noise. In sharp contrast to a traditional autoencoder over data points, VEEGAN does not require specifying a loss function over the data, but rather only over the representations, which are standard normal by assumption. On an extensive set of synthetic and real world image datasets, VEEGAN indeed resists mode collapsing to a far greater extent than other recent GAN variants, and produces more realistic samples.</div></div>

<div style="display:none;" id="bibsrivastava17veegan"><pre class="bibtex">@inproceedings{srivastava17veegan,
  author = {Srivastava, Akash and Valkov, Lazar and Russell, Chris and Gutmann, Michael and Sutton, Charles},
  booktitle = {Advances in Neural Information Processing Systems (NIPS)},
  title = {VEEGAN: Reducing Mode Collapse in GANs using Implicit Variational Learning},
  year = {2017}
}
</pre></div>

<p>
<a href="http://arxiv.org/abs/1602.06886"><b>Clustering with a Reject Option: Interactive Clustering as Bayesian Prior Elicitation</b></a>.&nbsp;Akash Srivastava, James Zou, Ryan P. Adams and Charles Sutton.
	In <i>Workshop on Human Interpretability in Machine Learning (co-located with ICML) and Interactive Data Exploration and Analytics Workshop,KDD (Oral)</i>.  2016.

</p>

<p>
   [ <a href="http://arxiv.org/abs/1602.06886">.pdf</a>
	| <a href="javascript:toggle('bibarxiv:tinder2016', 'bib_link_arxiv:tinder2016', 'bib')"  id="bib_link_arxiv:tinder2016">bib</a>
	| <a href="javascript:toggle('abstinder2016', 'abs_link_tinder2016', 'abstract')" id="abs_link_tinder2016">abstract</a>
   ]
</p>



<div id="divtinder2016"></div>
<div style="display:none;" id="abstinder2016"><div class="abstract">A good clustering can help a data analyst to explore and understand a data set, 
but what constitutes a good clustering may depend on domain-specific and application
 specific criteria. These criteria can be difficult to formalize, even when it is easy 
for an analyst to know a good clustering when she sees one. We present a new approach 
to interactive clustering for data exploration, called TINDER, based on a particularly simple
feedback mechanism, in which an analyst can choose to reject individual clusters and 
request new ones. The new clusters should be different from previously rejected clusters
while still fitting the data well. We formalize this interaction in a novel Bayesian prior
elicitation framework. In each iteration, the prior is adapted to account for all the 
previous feedback, and a new clustering is then produced from the posterior distribution.
To achieve the computational efficiency necessary for an interactive setting, we propose 
an incremental optimization method over data minibatches using Lagrangian relaxation. 
Experiments demonstrate that TINDER can produce accurate and diverse clusterings.</div></div>

<div style="display:none;" id="bibarxiv:tinder2016"><pre class="bibtex">@inproceedings{arxiv:tinder2016,
  author = {Srivastava, Akash and Zou, James and Adams, Ryan P. and Sutton, Charles},
  booktitle = {Workshop on Human Interpretability in Machine Learning (co-located with ICML)},
  journal = {ArXiv e-prints},
  title = {Clustering with a Reject Option: Interactive Clustering as Bayesian Prior Elicitation},
  year = {2016}
}
</pre></div>

<p>
<a href="https://arxiv.org/abs/1806.04854"><b>Fast and Scalable Bayesian Deep Learning by Weight-Perturbation in Adam</b></a>.&nbsp;Mohammad Emtiyaz Khan, Voot Tangkaratt, Didrik Nielsen, Wu Lin, Yarin Gal, Akash Srivastava. In <i>International Conference on Machine Learning (ICML)</i>.  2018.
</p>

<p>
   [ <a href="javascript:toggle('bibarxiv:vadam2018', 'bib_link_arxiv:vadam2018', 'bib')"  id="bib_link_arxiv:vadam2018">bib</a> | <a href="javascript:toggle('absvadam2018', 'abs_link_vadam2018', 'abstract')" id="abs_link_vadam2018">abstract</a>
   ]
</p>

<div id="divvadam2018"></div>
<div style="display:none;" id="absvadam2018"><div class="abstract">Uncertainty computation in deep learning is essential to design robust and reliable systems. Variational inference (VI) is a promising approach for such computation, but requires more effort to implement and execute compared to maximum-likelihood methods. In this paper, we propose new natural-gradient algorithms to reduce such efforts for Gaussian mean-field VI. Our algorithms can be implemented within the Adam optimizer by perturbing the network weights during gradient evaluations, and uncertainty estimates can be cheaply obtained by using the vector that adapts the learning rate. This requires lower memory, computation, and implementation effort than existing VI methods, while obtaining uncertainty estimates of comparable quality. Our empirical results confirm this and further suggest that the weight-perturbation in our algorithm could be useful for exploration in reinforcement learning and stochastic optimization.</div></div>

<div style="display:none;" id="bibarxiv:vadam2018"><pre class="bibtex">@inproceedings{arxiv:vadam2018,
  author = {Khan Mohammad Emtiyaz, Liu Zuozhu, Tangkaratt Voot, Nielsen Didrik, Gal Yarin, Srivastava Akash},
  booktitle = {International Conference on Machine Learning (ICML)},
  title = {Vadam: Fast and Scalable Variational Inference by Perturbing Adam},
  year = {2018}
}
</pre></div>

<p>
<a href="https://arxiv.org/abs/1804.00218"><b>Synthesis of Differentiable Functional Programs for Lifelong Learning</b></a>.&nbsp;Lazar Valkov, Dipak Chaudhari, Akash Srivastava, Swarat Chaudhuri and Charles Sutton. In <i>Advances in Neural Information Processing Systems (NIPS)</i>.  2018.
</p>

<p>
   [ <a href="javascript:toggle('bibarxiv:houdini2018', 'bib_link_arxiv:houdini2018', 'bib')"  id="bib_link_arxiv:houdini2018">bib</a> | <a href="javascript:toggle('absns2018', 'abs_link_ns2018', 'abstract')" id="abs_link_ns2018">abstract</a>
   ]
</p>


<div id="divns2018"></div>
<div style="display:none;" id="absns2018"><div class="abstract">We present a neurosymbolic approach to the lifelong learning
        of algorithmic tasks that mix perception and procedural
        reasoning. Reusing high-level concepts across domains and learning
        complex procedures are two key challenges in lifelong learning. We
        show that a combination of gradient-based learning and {symbolic
        program synthesis} can be a more effective response to these
        challenges than purely neural methods. Concretely, our approach,
        called Houdini, represents neural networks as strongly typed,
        end-to-end differentiable functional programs that use 
        symbolic higher-order combinators to compose a library of neural
        functions. Our learning algorithm consists of: (1) a program synthesizer
        that performs a type-directed search over programs in this language,
        and decides on the library functions that should be reused and the
        architectures that should be used to combine them; and (2) a neural
        module that trains synthesized programs using stochastic gradient
        descent. We evaluate our approach on three algorithmic tasks.
        Our experiments show that our type-directed search technique
        is able to significantly prune the search space of programs,
        and that the overall approach transfers high-level concepts
        more effectively than monolithic neural networks as well as
        traditional transfer learning.</div></div>
	
<div style="display:none;" id="bibarxiv:houdini2018"><pre class="bibtex">@inproceedings{arxiv:houdini2018,
  author = {Valkov Lazar, Chaudhari Dipak, Srivastava Akash, Chaudhuri Swarat and Sutton Charles},
  booktitle = {Advances in Neural Information Processing Systems (NIPS)},
  title = {Synthesis of Differentiable Functional Programs for Lifelong Learning},
  year = {2018}
}
</pre></div>


<p>
<a href="http://xuk.ai/assets/xu2019rave.pdf"><b>Variational Russian Roulette for Deep Bayesian Nonparametrics.</b></a>.&nbsp;Kai Xu, Akash Srivastava and Charles Sutton. In <i>International Conference on Machine Learning (ICML)</i>.  2019.
</p>

<p>
   [ <a href="javascript:toggle('bibarxiv:vrr2019', 'bib_link_arxiv:vrr2019', 'bib')"  id="bib_link_arxiv:vrr2019">bib</a> | <a href="javascript:toggle('absvrr2019', 'abs_link_vrr2019', 'abstract')" id="abs_link_vrr2019">abstract</a>
   ]
</p>


<div id="divvrr2019"></div>
<div style="display:none;" id="absvrr2019"><div class="abstract">Bayesian nonparametric models provide a principled way to automatically adapt the complexity
of a model to the amount of the data available, but
computation in such models is difficult. Amortized variational approximations are appealing because of their computational efficiency, but current methods rely on a fixed finite truncation of
the infinite model. This truncation level can be
difficult to set, and also interacts poorly with amortized methods due to the over-pruning problem.
Instead, we propose a new variational approximation, based on a method from statistical physics
called Russian roulette sampling. This allows
the variational distribution to adapt its complexity during inference, without relying on a fixed
truncation level, and while still obtaining an unbiased estimate of the gradient of the original variational objective. We demonstrate this method
on infinite sized variational auto-encoders using a
Beta-Bernoulli (Indian buffet process) prior.</div></div>
	
<div style="display:none;" id="bibarxiv:vrr2019"><pre class="bibtex">@inproceedings{arxiv:vrr2019,
  author = {Kai Xu, Akash Srivastava and Charles Sutton},
  booktitle = {International Conference on Machine Learning (ICML) (NIPS)},
  title = {Variational Russian Roulette for Deep Bayesian Nonparametrics.},
  year = {2019}
}
</pre></div>

<p>
<a href="rmn.pdf"><b>Generative Ratio Matching Networks</b></a>.&nbsp;Akash Srivastava, Kai Xu, Michael U. Gutmann and Charles Sutton.In <i>International Conference on Learning Representations (ICLR)</i>.  2020.
</p>

<p>
   [ <a href="javascript:toggle('absrmn2018', 'abs_link_rmn2018', 'abstract')" id="abs_link_rmn2018">abstract</a>
| <a href="https://openreview.net/pdf?id=SJg7spEYDS">pdf</a> | <a href="https://anonymous.4open.science/r/240c54df-b287-411e-a125-056d6ecc757b/">source code</a>
   ]
</p>

<div id="divrmn2018"></div>
<div style="display:none;" id="absrmn2018"><div class="abstract">Deep generative models can learn to generate realistic-looking images, but many of the most effective methods are adversarial and involve a saddlepoint optimization, which require careful balancing of training between a generator network and a critic network. Maximum mean discrepancy networks (MMD-nets) avoid this issue by using kernel as a fixed adversary, but unfortunately they have not on their own been able to match the generative quality of adversarial training. In this work, we take their insight of using kernels as fixed adversaries further and present a novel method for training deep generative models that does not involve saddlepoint optimization. We call our method generative ratio matching or GRAM for short. In GRAM, the generator and the critic networks do not play a zero-sum game against each other, instead they do so against a fixed kernel. Thus GRAM networks are not only stable to train like MMD-nets but they also match and beat the generative quality of adversarially trained generative networks.</div></div>


<p>
<a href="cole.pdf"><b>Scalable Spike Source Localization in Extracellular
Recordings using Amortized Variational Inference</b></a>.&nbsp;Cole L. Hurwitz, Kai Xu, Akash Srivastava, Alessio Paolo Buccino and Matthias Hennig. In <i>Advances in Neural Information Processing Systems (NeurIPS)</i>.  2019.
</p>

<p>
   [ <a href="javascript:toggle('abscole2019', 'abs_link_cole2019', 'abstract')" id="abs_link_cole2019">abstract</a>
   ]
</p>

<div id="divcole2019"></div>
<div style="display:none;" id="abscole2019"><div class="abstract">Extracellular recordings using modern, dense probes provide detailed footprints of
action potentials (spikes) from thousands of neurons simultaneously. Inferring the
activity of single neurons from these recordings, however, is a complex blind source
separation problem, complicated both by the high intrinsic data dimensionality and
large data volume. Despite these complications, dense probes can allow for the
estimation of a spike’s source location, a powerful feature for determining the firing
neuron’s position and identity in the recording. Here we present a novel, generative
model for inferring the source of individual spikes given observed electrical traces.
To allow for scalable, efficient inference, we implement our model as a variational
autoencoder and perform amortized variational inference. We evaluate our method
on biophysically realistic simulated datasets, showing that our method outperforms
heuristic localization methods such as center of mass and can improve spike sorting
performance significantly. We further apply our model to real data to show that it
is an effective, interpretable tool for analyzing large-scale extracellular recordings.</div></div>

---
### Preprints

<p>
<a href="https://openreview.net/pdf?id=r1e74a4twH"><b>CZ-GEM: A Framework For Disentangled Representation Learning</b></a>.&nbsp;Akash Srivastava, Yamini Bansal, Yukun Ding, Bernhard Egger, Prasanna Sattigeri, Josh Tenenbaum, David D. Cox, Dan Gutfreund.
</p>

<p>
   [ <a href="javascript:toggle('abscz2020', 'abs_link_cz2020', 'abstract')" id="abs_link_cz2020">abstract</a> 
   | <a href="https://github.com/AnonymousAuthors000/CZ-GEM">source code</a> ]
</p>

<div id="divcz2020"></div>
<div style="display:none;" id="abscz2020"><div class="abstract">Learning disentangled representations of  data is one of the central themes in unsupervised learning in general and generative modelling in particular.  In this work,  we tackle a slightly more intricate scenario where the observations are generated from a conditional distribution of some known control variate and some latent noise variate.  To this end, we present a hierarchical model and a training method (CZ-GEM) that leverages some of the recent developments in likelihood-based and likelihood-free generative models.  We show that by formulation, CZ-GEM introduces the right inductive biases that ensure the disentanglement of the control from the noise variables, while also keeping the components of the control variate disentangled. This is achieved without compromising on the quality of the generated samples. Our approach is simple, general, and can be applied both in supervised and unsupervised settings.</div></div>

<p>
<a href="simvae.pdf"><b>SimVAE: Simulator-Assisted Training for
Interpretable Generative Models</b></a>.&nbsp;Akash Srivastava, Jessie Rosenberg, Dan Gutfreund and David D. Cox.
</p>

<p>
   [ <a href="javascript:toggle('abssimvae2019', 'abs_link_simvae2019', 'abstract')" id="abs_link_simvae2019">abstract</a>
   ]
</p>

<div id="divsimvae2019"></div>
<div style="display:none;" id="abssimvae2019"><div class="abstract">This paper presents a simulator-assisted training method (SimVAE) for variational
autoencoders (VAE) that leads to a disentangled and interpretable latent space.
Training SimVAE is a two step process in which first a deep generator network
(decoder) is trained to approximate the simulator. During this step the simulator acts
as the data source or as a teacher network. Then an inference network (encoder)
is trained to invert the decoder. As such, upon complete training, the encoder
represents an approximately inverted simulator. By decoupling the training of
the encoder and decoder we bypass some of the difficulties that arise in training
generative models such as VAEs and generative adversarial networks (GANs). We
show applications of our approach in a variety of domains such as circuit design,
graphics de-rendering and other natural science problems that involve inference
via simulation.</div></div>

<p>
<a href="BregmanGAN2020.pdf"><b>BreGMN: scaled-Bregman Generative Modeling
Networks</b></a>.&nbsp;Akash Srivastava, Kristjan Greenewald and Farzaneh Mirzazadeh.
</p>

<p>
   [ <a href="javascript:toggle('absbregmn2019', 'abs_link_bregmn2019', 'abstract')" id="abs_link_bregmn2019">abstract</a>
   ]
</p>

<div id="divbregmn2019"></div>
<div style="display:none;" id="absbregmn2019"><div class="abstract">The family of f-divergences is ubiquitously applied to generative modeling in
order to adapt the distribution of the model to that of the data. Well-definedness
of f-divergences, however, requires the distributions of the data and model to
overlap completely in every time step of training. As a result, as soon as the support
of distributions of data and model contain non-overlapping portions, gradientbased training of the corresponding model becomes hopeless. Recent advances
in generative modeling are full of remedies for handling this support mismatch
problem: key ideas include either modifying the objective function to integral
probability measures (IPMs) that are well-behaved even on disjoint probabilities,
or optimizing a well-behaved variational lower bound instead of the true objective.
We, on the other hand, establish that a complete change of the objective function is
unnecessary, and instead an augmentation of the base measure of the problematic
divergence can resolve the issue. Based on this observation, we propose a generative
model which leverages the class of Scaled Bregman Divergences and generalizes
both f-divergences and Bregman divergences. We analyze this class of divergences
and show that with the appropriate choice of base measure it can resolve the support
mismatch problem and incorporate geometric information. Finally, we study the
performance of the proposed method and demonstrate promising results on MNIST,
CelebA and CIFAR-10 datasets.</div></div>

<p>
<a href="pam-naacl.pdf"><b>Variational Inference In Pachinko Allocation Machines</b></a>.&nbsp;Akash Srivastava and Charles Sutton.
</p>

<p>
   [ <a href="javascript:toggle('abspam2018', 'abs_link_pam2018', 'abstract')" id="abs_link_pam2018">abstract</a>
   ]
</p>

<div id="divpam2018"></div>
<div style="display:none;" id="abspam2018"><div class="abstract">The Pachinko Allocation Machine (PAM) is a deep topic model that allows representing rich correlation structures among topics by a directed acyclic graph over topics. Because of the flexibility of the model, however, approximate inference is very difficult. Perhaps for this reason, only a small number of potential PAM architectures have been explored in the literature. In this paper we present an efficient and flexible amortized variational inference method for PAM, using a deep inference network to parameterize the approximate posterior distribution in a manner similar to the variational autoencoder. Our inference method produces more coherent topics than state-of-art inference methods for PAM while being an order of magnitude faster, which allows exploration of a wider range of PAM architectures than have previously been studied.</div></div>





	
	
---
### Thesis
<p>
<b>Burst Detection Modulated Document Clustering: A Partially Feature-Pivoted Approach To First Story Detection</b>.&nbsp;Akash Srivastava.
	MSc Thesis.

</p>

<p>
   [ <a href="javascript:toggle('absfsd2018', 'abs_link_fsd2018', 'abstract')" id="abs_link_fsd2018">abstract</a>
   ]
</p>

<div id="divfsd2018"></div>
<div style="display:none;" id="absfsd2018"><div class="abstract">First Story Detection or FSD is one of the 5 tasks defined under the Topic Detection andTracking program with the purpose to identify the onset of a previously unseen event in
a stream of news stories. In this work, we report on the development and evaluation of
a feature-pivoted approach to this task. Our method uses the output of a burst detection
algorithm to modulate the traditional document clustering based approach to FSD.
For burst detection, we work exclusively with words in the input and use a 2 step
filtration routine that filters out all the words for which the cumulative term frequencies
or the Autocorrelation values of their corresponding signal representations are below
a pre-computed threshold. The output is then grouped into sets of words that have
similar burst patterns in time. A confidence score is generated for each set of words,
quantifying the chance of the set being the first story on the event that it relates to. In
the final step all the detected first stories are passed through a restricted clustering unit
that uses cosine similarity to cluster together stories that are on the same topic, hence
reducing false alarms. Our experiments show that the resultant FSD system performs
substantially better than the document-pivoted state-of-art baseline system.</div></div>
