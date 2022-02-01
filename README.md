# SSGC-Reimplementation

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Og2ujgpE3wugJb3KLSt0oBOm_DRXvRxL?usp=sharing)

Re-implementation of the S²GC model described in [Zhu and Koniusz, 2021](https://openreview.net/pdf?id=CYO5T-YjWZV). 

The reproduction takes place entirely in SSGC.ipynb. The rest of the files are from the [original repository](https://github.com/allenhaozhu/SSGC) of the paper.

# Setup
* Download the data-directory from [link](https://github.com/allenhaozhu/SSGC) and add it to "SSGC-Reimplementation"
* Download and unpack from [link](https://drive.google.com/file/d/10kx3z3bjYFoeRjjg1_DZOAP39Jln0BCh/view?usp=sharing) and add it at "SSGC-Reimplementation/DocumentClassification/data"

# Results

This re-implementation produces mostly very similar, if slightly worse, results to the ones described in the paper. 

## Node Classification
Datasets                          | Cora   | Citeseer | Pubmed  |
:-------------------------:|:------:|:--------:|:-------:|
Test Accuracy - original   | 83.5 % | 73.6%    | 80.2%          
Test Accuracy - reproduced | 81.1%  | 69.9%    | 79.6% 

## Text Classification

Datasets           | 20NG | R8 | R52 | Ohsumed | MR
:----------------:|:------:| :------:| :------:| :------:| :------:|
Test Accuracy - original   | 88.6 % | 97.4% | 94.5% | 68.5% | 76.7%          
Test Accuracy - reproduced | -  | 95.6% | 93.3% | 65.8% | 70.0% 

# Notes

* The implementation works without problem for all datasets except for the large OGB datasets and one document classification dataset. I simply do not have the memory to load them or generate even sparse matrices.

* However, in principle the implementation should also work for them, as long as you have enough RAM.

* Epoch and run count have been reduced by me on some tasks to make the execution of them feasible.
