import numpy as np
import scipy.sparse as sp
import torch

import sklearn.metrics

def calc_sym_renorm_adj(dir_adj):
    n_vertex = dir_adj.shape[0]
    id = sp.csc_matrix(sp.identity(n_vertex))

    adj = dir_adj + dir_adj.T.multiply(dir_adj.T > dir_adj) - dir_adj.multiply(dir_adj.T > dir_adj)
    adj_ = adj + id

    row_sum = adj_.sum(axis=1).A1
    row_sum_inv_sqrt = np.power(row_sum, -0.5)
    row_sum_inv_sqrt[np.isinf(row_sum_inv_sqrt)] = 0.
    deg_inv_sqrt_ = sp.diags(row_sum_inv_sqrt)

    sym_renorm_adj = deg_inv_sqrt_.dot(adj_).dot(deg_inv_sqrt_)

    return sym_renorm_adj

def calc_rw_renorm_adj(dir_adj):
    n_vertex = dir_adj.shape[0]
    id = sp.csc_matrix(sp.identity(n_vertex))

    adj = dir_adj + dir_adj.T.multiply(dir_adj.T > dir_adj) - dir_adj.multiply(dir_adj.T > dir_adj)
    adj_ = adj + id

    row_sum = adj_.sum(axis=1).A1
    row_sum_inv = np.power(row_sum, -1)
    row_sum_inv[np.isinf(row_sum_inv)] = 0.
    deg_inv_ = sp.diags(row_sum_inv)

    rw_renorm_adj = deg_inv_.dot(adj_)

    return rw_renorm_adj

def calc_adj_mul_feat(adj, features, alpha, K):
    emb = alpha * features
    for k in range(K):
        features = adj.dot(features)
        emb = emb + (1 - alpha) / K * features
    
    emb = np.array(emb.toarray(), dtype=np.float32)

    return emb

def cnv_sparse_mat_to_coo_tensor(sp_mat, device):
    # convert a compressed sparse row (csr) or compressed sparse column (csc) matrix to a hybrid sparse coo tensor
    sp_coo_mat = sp_mat.tocoo().astype(np.float32)
    i = torch.from_numpy(np.vstack((sp_coo_mat.row, sp_coo_mat.col)).astype(np.int32))
    v = torch.from_numpy(sp_coo_mat.data)
    s = torch.Size(sp_coo_mat.shape)

    return torch.sparse_coo_tensor(indices=i, values=v, size=s, dtype=torch.float32, device=device, requires_grad=False)

def calc_accuracy(output, labels):
    preds = output.max(1)[1].type_as(labels)
    correct = preds.eq(labels).double().sum()
    accuracy = correct / len(labels)

    return accuracy

def calc_nmi(output, labels):
    preds = output.max(1)[1].type_as(labels)
    #correct = preds.eq(labels).double().sum()
    print(preds)
    print(labels)
    nmi = sklearn.metrics.normalized_mutual_info_score(labels, preds)
    #accuracy = correct / len(labels)

    return nmi

def calc_f1(output, labels):
    preds = output.max(1)[1].type_as(labels)
    #correct = preds.eq(labels).double().sum()
    f1 = sklearn.metrics.f1_score(labels, preds, average="micro")
    #accuracy = correct / len(labels)

    return f1
