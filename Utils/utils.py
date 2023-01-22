import torch
import torch.nn.functional as F


def gradient(img: torch.tensor):
    img = torch.tensor(img, dtype=torch.int32)
    imgx_padded_end = F.pad(img, (0, 1), "constant", 0)
    imgx_padded_start = F.pad(img, (1, 0), "constant", 0)
    imgy_padded_end = F.pad(img, (0, 0, 0, 1), "constant", 0)
    imgy_padded_start = F.pad(img, (0, 0, 1, 0), "constant", 0)
    
    dx = torch.flatten(imgx_padded_start - imgx_padded_end)
    dy = torch.flatten(imgy_padded_start - imgy_padded_end)
    return dx, dy
