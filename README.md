# Intro
程序分为一下几个步骤：
1. 读取图像使用Union Find算法分出标定点以及轮廓
    - 因为线条有厚度，用Erosion算法减少样本点数量方便计算也节省时间
2. 根据标定点和轮廓数据，计算出从标定点到每一个轮廓的点的距离和角度
3. 一角度为基准对N个样本进行平均计算
4. 拿到平均后的数据，重建坐标系，输出结果图像
# How to run it
`git clone 'https://github.com/YifeiJing/process-circles.git'`

```
cd process-circles
pip install -r requirements.txt
python src/main.py 测试集
open result.jpg
```

## Example output
```
(process-circles) rvalue:~/repos/process-circles$ python src/main.py 测试集
Analyzing 测试集/Test 005.png
Image size: (1872, 2390)
Processing 11494 points
Center detected: (928, 1192)
Analyzing 测试集/Test 001.png
Image size: (1872, 2760)
Processing 13057 points
Center detected: (941, 1302)
Analyzing 测试集/Test 003.png
Image size: (1759, 2462)
Processing 11425 points
Center detected: (828, 1223)
Analyzing 测试集/Test 006.png
Image size: (1872, 2760)
Processing 13057 points
Center detected: (919, 951)
Analyzing 测试集/Test 004.png
Image size: (1753, 2489)
Processing 11501 points
Center detected: (822, 1250)
Analyzing 测试集/Test 002.png
Image size: (1772, 2697)
Processing 12179 points
Center detected: (841, 1239)
Analyzing 测试集/Test 007.png
Image size: (1789, 2548)
Processing 11631 points
Center detected: (894, 1457)
Combination started on 7 targets ...
Finished without error. Can check result.jpg
```
