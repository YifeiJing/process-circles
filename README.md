# Intro
程序分为一下几个步骤：
1. 读取图像使用Union Find算法分出标定点以及轮廓
    - 因为线条有厚度，用Erosion算法减少样本点数量方便计算也节省时间
2. 根据标定点和轮廓数据，计算出从标定点到每一个轮廓的点的距离和角度
3. 一角度为基准对两个样本进行平均计算
4. 拿到平均后的数据，重建坐标系，输出结果图像
# How to run it
`git clone 'https://github.com/YifeiJing/process-circles.git'`

```
cd process-circles
pip install -r requirements.txt
python src/main.py 测试集/Test\ 001.png 测试集/Test\ 002.png
open result.jpg
```
