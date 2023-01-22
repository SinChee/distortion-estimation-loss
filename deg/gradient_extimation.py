import numpy as np

import torch
import torch.nn as nn
from Utils.utils import gradient


class FeatureExtractor(nn.Module):
    def __init__(self, noise_model) -> None:
        super().__init__()
        self.noise_model = noise_model
        
    def forward(self, img_clean: torch.tensor, img_noisy: torch.tensor):
        self.img_clean = img_clean
        self.img_noisy = img_noisy
        gradX_clean, gradY_clean = gradient(img_clean)
        gradX_noisy, gradY_noisy = gradient(img_noisy)
        self._pixel, self.gradX_clean_count = self.image_gradient_statistics(gradX_clean)
        _, self.gradY_clean_count = self.image_gradient_statistics(gradY_clean)
        _, self.gradX_noisy_count = self.image_gradient_statistics(gradX_noisy)
        _, self.gradY_noisy_count = self.image_gradient_statistics(gradY_noisy)
        return (self.gradX_clean_count, self.gradY_clean_count, self.gradX_noisy_count, self.gradY_noisy_count)
    
    def image_gradient_statistics(self, grad: torch.tensor):
        device = grad.device
        grad = grad.detach().cpu().numpy()
        count, pixel = np.histogram(grad, bins=[x for x in range(-255, 257)])
        return torch.tensor(pixel, device=device), torch.tensor(count, device=device)


