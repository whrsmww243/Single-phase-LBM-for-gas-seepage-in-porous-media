import numpy as np
import matplotlib.pyplot as plt

def txt_to_image(input_txt, original_width, original_height, output_image):
    # 从txt文件读取数据并转换为numpy数组
    with open(input_txt, 'r') as f:
        data = np.array([int(line.strip()) for line in f])
    
    # 重塑为原始图像尺寸的二维矩阵
    binary_matrix = data.reshape((original_height, original_width))
    
    # 显示图像
    plt.imshow(binary_matrix, cmap='gray', vmin=0, vmax=1)
    plt.axis('off')  # 关闭坐标轴
    plt.title(f"Reconstructed Image ({original_width}x{original_height})")
    
    # 保存图像
    plt.savefig(output_image, bbox_inches='tight', pad_inches=0)
    plt.show()

# 使用示例（需替换为实际的原始图像尺寸）
txt_to_image('output2.txt', original_width=2046, original_height=1252, output_image='实例对照3.png')
