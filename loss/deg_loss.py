import torch
import torch.nn as nn
from loss.loss import *

LOSS = {
    "R2": r2,
    "KL Divergence": kl_loss,
    "MSE": mse,
    "Chi Squared": chiSquared,
    "Canberra Distance": canberra_distance,
    "Jenson Distance": jenson_loss,
    "AOC": area_under_curve
}

class Loss(nn.Module):
    def __init__(self, loss="Canberra Distance") -> None:
        super().__init__()
        self.loss = LOSS[loss] if isinstance(loss, str) else loss
    
    def info() -> None:
        print("Avalible Loss:", list(LOSS.keys()))
    
    def forward(self, cleanX, cleanY, noisyX, noisyY) -> torch.float32:
        loss_x = self.loss(cleanX, noisyX)
        loss_y = self.loss(cleanY, noisyY)
        loss = torch.sqrt(torch.pow(loss_x, 2) + torch.pow(loss_y, 2))
        return loss

