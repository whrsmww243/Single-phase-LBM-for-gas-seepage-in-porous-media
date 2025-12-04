from PIL import Image
import numpy as np

def image_to_binary_txt(image_path, output_txt):
    # 打开图片并转换为灰度图
    img = Image.open(image_path).convert('L')

    # 获取图片尺寸（宽度, 高度）
    width, height = img.size
    print(f"图片像素大小：{width}（宽）x {height}（高）")
    
    # 将图像数据转换为numpy数组
    img_array = np.array(img)
    
    # 阈值处理：将灰度值大于128的设为1（白），其余为0（黑）
    binary_array = (img_array > 128).astype(int)
    
    # 将矩阵展平为单列并保存为txt
    with open(output_txt, 'w') as f:
        for value in binary_array.flatten():
            f.write(f"{value}\n")

# 使用示例
image_to_binary_txt('实例对照3.png', 'output.txt')
