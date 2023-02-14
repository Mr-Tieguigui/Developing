# Kornia 
Kornia 是PyTorch 的一个可微分的计算机视觉库。它由一组例程和可微模块组成，用于解决通用的计算机视觉问题。该软件包的核心是使用PyTorch作为其主要后端，以提高效率和利用反向模式自动微分来定义和计算复杂函数的梯度。

[项目网址](https://kornia.readthedocs.io/en/latest/)
## 项目业务流:
1. 加载图像
使用Matplotib可视化图像
2.色彩空间转换

3. 图像增强
调整亮度
调整对比度
调整饱和度
调整伽玛
调整色调
4. 提取和组合张量补丁
安装和获取数据
使用模块
使用函数
填充
5. 筛选运算符
框模糊
模糊池
高斯模糊
最大池
中值模糊
运动模糊
6. 边缘检测
一阶导数
二阶导数
索贝尔边缘
拉普拉斯边缘
精明的边缘
7. 形态算子简介
下载科尔尼亚
准备映像
形态学
结论
8. 使用透视变换的变形图像
安装库并获取数据
导入库并加载数据
定义要翘曲的点，计算单应性和翘曲
绘制扭曲数据
9. 使用变形仿射变换旋转图像
定义旋转矩阵
将变换应用于原始图像
旋转一批图像
10. 使用高斯模糊运算符模糊图像
制备
例
11. 使用未锐化蒙版锐化图像
12. 使用Canny运算符获取边
制备
例
13. 连接组件算法
14. 调整抗锯齿大小
安装科尔尼亚
准备数据
普通调整大小与抗脱脂调整大小
15. 具有本地特征的图像抗锯齿
16. 将 RGB 转换为 RAW
下载必要的文件和库
导入必要的库
通过 rawpy 准备原始文件
通过进行转换将数据导入科尼亚
可视 化
陷阱：旋转给出不同的CFA
17. 图像直方图和均衡技术
安装科尔尼亚
准备数据
图像直方图
直方图拉伸
直方图均衡
自适应直方图均衡
对比度受限自适应直方图均衡 （CLAHE）
18. 将 RGB 转换为 YUV420
获取要使用的数据和库
导入所需的库
定义用于读取 yuv 文件到火炬张量的函数以在 Kornia 中使用
对图像的外观进行采样 Y、u、v 通道分离，然后通过 kornia 转换为 rgn（在本例中返回 numpy）
我们可以在一些内部 Kornia 算法实现中使用它们。让我们假装我们想在红色通道上做 LoFTR

## 数据增强
1. Kornia 和 PyTorch Lightning GPU 数据增强
2. 数据增强语义分割
安装和获取数据
定义扩充管道
3. 按顺序增强
安装和获取数据
定义增强顺序和不同的标签
前向计算
逆变换
4. 随机马赛克
安装和获取数据
5. 补丁顺序
安装和获取数据
补丁扩充顺序，patchwise_apply=True
补丁增强顺序，patchwise_apply=假

## 一些简单代码示例
### 1. 图像滤波
```python
import cv2
from matplotlib import pyplot as plt
import numpy as np
 
import torch
import torchvision
import kornia as K
 
# 我们使用 OpenCV 将图像加载到以 numpy.ndarray 表示的内存中
img_bgr: np.ndarray = cv2.imread('drslump.jpg', cv2.IMREAD_COLOR)
 
# 将numpy数组转换为torch
x_bgr: torch.Tensor = K.utils.image_to_tensor(img_bgr)  # CxHxWx
x_bgr = x_bgr[None,...].float() / 255.
 
x_rgb: torch.Tensor = K.color.bgr_to_rgb(x_bgr)
 
# 定义图像显示方法
def imshow(input: torch.Tensor):
    if input.shape != x_rgb.shape:
        input = K.geometry.resize(input, size=(x_rgb.shape[-2:]))
    out = torch.cat([x_rgb, input], dim=-1)
    out = torchvision.utils.make_grid(out, nrow=2, padding=5)
    out_np: np.ndarray = K.utils.tensor_to_image(out)
    plt.imshow(out_np)
    plt.axis('off')
    plt.show()
 
# box blur
x_blur: torch.Tensor = K.filters.box_blur(x_rgb, (9, 9))
imshow(x_blur)
```
### 2. 图像匹配
图像匹配是在同一场景的两幅图像之间寻找像素和区域对应关系的过程。 这种对应对于场景的 3D 重建和相对相机位姿估计很有用。 它也被称为“宽基线立体声”，您可以在宽基线立体声博客上了解更多信息

我们为图像匹配提供了许多模块和功能：从局部特征检测器、描述符、描述符匹配、几何模型估计等构建块，建议从高级 API 开始，例如 LoFTR，您可以使用它来查找两个图像之间的对应关系。
```python
from kornia.feature import LoFTR
 
matcher = LoFTR(pretrained="outdoor")
input = {"image0": img1, "image1": img2}
correspondences_dict = matcher(input)
```
### 3. 图像分割数据扩增
官方例子：
```python
!wget http://www.zemris.fer.hr/~ssegvic/multiclod/images/causevic16semseg3.png
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
    self.k3 = K.augmentation.RandomPerspective(0.5, p=1.0)

  def forward(self, img: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    # 1. apply color only in image
    # 2. apply geometric tranform
    img_out = self.k3(self.k2(self.k1(img)))

    # 3. infer geometry params to mask
    # TODO: this will change in future so that no need to infer params
    mask_out = self.k3(self.k2(mask, self.k2._params), self.k3._params)

    return img_out, mask_out

def load_data(data_path: str) -> torch.Tensor:
  data: np.ndarray = cv2.imread(data_path, cv2.IMREAD_COLOR)
  data_t: torch.Tensor = K.image_to_tensor(data, keepdim=False)
  data_t = K.bgr_to_rgb(data_t)
  data_t = K.normalize(data_t, torch.tensor([0.]), torch.tensor([255.]))
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
```