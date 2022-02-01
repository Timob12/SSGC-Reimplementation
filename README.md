# SSGC-Reimplementation

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Og2ujgpE3wugJb3KLSt0oBOm_DRXvRxL?usp=sharing)

From https://github.com/allenhaozhu/SSGC download "data" and "DocumentClassification/data" and add those to this directory (files are too large to push them to github). "DocumentClassification/data" needs to be downloaded as a zip file and extracted (again, look at the authors repo; he linked it).

The implementation works without problem for all datasets except for the large OGB datasets and some document classification datasets. I simply do not have the memory to load them or generate even sparse matrices.

However, in principle the implementation should also work for them, as long as you have enough RAM.

I observed a strong difference in the accuray of this method on the arxiv OGB dataset between my implementation and the results stated in the paper (50% vs 70%). Maybe my code is faulty somewhere.

Epoch and run count have been reduced by me on some tasks to make the execution of them feasible.
