import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.metrics import r2_score



def r2(y_true, y_predict):
    device = y_true.device
    y_true = y_true.detach().cpu().numpy()
    y_predict = y_predict.detach().cpu().numpy()
    return torch.tensor(r2_score(y_true, y_predict), device=device)

def kl_loss(y_true, y_predict):
    loss = nn.KLDivLoss(reduction="batchmean", log_target=True)
    return loss(y_true, y_predict)

def mse(y_true, y_predict):
    loss = nn.MSELoss()
    return loss(y_true, y_predict)

def chiSquared(y_true, y_predict):
    loss = torch.sum((torch.pow(y_true - y_predict, 2) + 0.00001) / y_true + 0.00001)
    return loss

def jenson_loss(y_true, y_predict):
    y_true =  F.softmax(y_true, dim=1)
    y_predict=  F.softmax(y_predict, dim=1)
    total_m = 0.5 * (y_true + y_predict)
    loss = F.kl_div(F.log_softmax(y_predict, dim=1), total_m, reduction="batchmean") 
    loss += F.kl_div(F.log_softmax(y_predict, dim=1), total_m, reduction="batchmean") 
    return (0.5 * loss)

def canberra_distance(y_true, y_predict):
    loss = torch.abs(y_true - y_predict + 0.00001)/(torch.abs(y_true) + torch.abs(y_predict) + 0.00001)
    return torch.sum(loss)

def area_under_curve(y_true, y_predict):
    loss = nn.L1Loss()
    return loss(y_true, y_predict)
