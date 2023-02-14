
import matplotlib.pyplot as plt
import cv2
import numpy as np

import torch
import torch.nn as nn
import kornia as K

# 继承torch.nn.Module
class MyAugmentation(nn.Module):
  def __init__(self):
    super(MyAugmentation, self).__init__()
    # we define and cache our operators as class members
    self.k1 = K.augmentation.ColorJitter(0.15, 0.25, 0.25, 0.25)
    self.k2 = K.augmentation.RandomAffine([-45., 45.], [0., 0.15], [0.5, 1.5], [0., 0.15])
  
  def forward(self, img: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    # 1. apply color only in image
    # 2. apply geometric tranform
    img_out = self.k2(self.k1(img))

    # 3. infer geometry params to mask
    # TODO: this will change in future so that no need to infer params
    mask_out = self.k2(mask, self.k2._params)

    return img_out, mask_out

def load_data(data_path: str) -> torch.Tensor:
  data: np.ndarray = cv2.imread(data_path, cv2.IMREAD_COLOR)
  data_t: torch.Tensor = K.image_to_tensor(data, keepdim=False)
  data_t = K.color.bgr_to_rgb(data_t)
  data_t = K.enhance.normalize(data_t, torch.tensor(0.), torch.tensor(255.))
  img, labels = data_t[..., :571], data_t[..., 572:]
  return img, labels

# load data (B, C, H, W)
img, labels = load_data("causevic16semseg3.png")

# create augmentation instance
aug = MyAugmentation()

# apply the augmenation pipelone to our batch of data
img_aug, labels_aug = aug(img, labels)

# visualize
img_out = torch.cat([img, labels], dim=-1)
plt.imshow(K.tensor_to_image(img_out))
plt.axis('off')

# generate several samples
num_samples: int = 10

for img_id in range(num_samples):
  # generate data
  img_aug, labels_aug = aug(img, labels)
  img_out = torch.cat([img_aug, labels_aug], dim=-1)

  # save data
  plt.figure()
  plt.imshow(K.tensor_to_image(img_out))
  plt.axis('off')
  plt.savefig(f"img_{img_id}.png", bbox_inches='tight')