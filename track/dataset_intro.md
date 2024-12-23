# 数据集介绍

本实验采用Huang等人提出的Anti-UAV410数据集，该数据集是一个专为红外小目标设计的高质量数据集，覆盖了复杂的场景、多样的目标运动姿态以及现实世界中的各种挑战性条件。该数据集包括410个红外视频，超过438k个手动标注的边界框，为红外小目标跟踪提供了重要的基准。

Anti-UAV410专注于远距离成像下的小型无人机目标跟踪，如图所示，该数据集涵盖了森林，山脉，湖泊和城市建筑的背景，引入红外小目标跟踪任务的两大挑战，及微小目标和动态背景杂波。考虑到原生数据集规模庞大，本实验只在部分视频序列上进行，如图所示，序列1的图像尺寸为640✖️512，背景包括天空，云层和城市建筑，目标在图像中呈现块状，在初始帧中，目标处于云层与天空之间，随后向右上方运动，同时伴随着姿态变化，在139帧达到最高点，在这个过程中，目标淹没在云层中，且姿态不断变化；随后，目标垂直向下运动，在394帧到达楼房背景的边界并继续想下运动，盘旋数帧后迅速向上移动；此后的的运动状态与前面描述类似。序列1中，目标微弱且亮度与云层、建筑背景相似，为跟踪带来巨大的困难。

如图所示，序列2尺寸为640✖️512，背景为海面，初始帧中，目标在图像中比较显著，但是水面产生大量的杂波干扰，目标向右运动且移动速度较快，在150帧时，背景发生变化，出现了船舶，在这个过程中，由于目标运动过快，红外传感器方位和角度频繁变化，目标在图像中的位置随之无规律剧烈变化；此后目标继续向右移动，背景不断变化，342帧出现建筑，534帧出现另外一个船舶干扰，1118中出现海岸线背景。序列2的跟踪难点在于图像运动迅速且背景变化频繁。

为了应对复杂的评价体系，Anti-UAV410数据集作者对图像帧做了更为细致的标注，这些标签及描述如下表所示：

OC遮挡，FM快速移动，IC，DBC动态杂波，TS微小目标，SV尺度变化也可以加一个

图@展示了实验选用数据集的目标属性统计分布，从图中可以看出，两个序列在各种场景下都有足够的样本，为后序实验提供了良好的实验基础。


# 检测器训练

Anti-UAV410数据集采用JSON文件保存标签，对于目标的位置和尺寸信息采用(xlt, ylt, w, h)的格式，其中(xlt, ylt)表示目标检测框左上角的坐标，w, h分别表示宽度尺寸和高度尺寸，且数值为像素绝对值，为了训练检测器，需要将其转化成(xc,yc,w,h)的格式，符号的含意与上一章相同，数值为相对值。

为了提高检测器的精度与泛化能力，本实验在Anti-UAV410数据集中均匀随机地选取3000张图像作为检测器的训练样本，数据集划分与实验环境配置与上一章相同。如@图所示，训练损失在50轮左右逐渐收敛，。。。

# 测试结果

| algorithm | mota | motp | ids | fp | fn |
|-----------+------+------+-----+----+----|
sort          74.3% 0.235   7     11   368 
deepsort      74.8% 0.238   7     7    364 
bytrack       73.2% 0.233   7     19   376

| algorithm | mota | motp | ids | fp | fn |
|-----------+------+------+-----+----+----|
sort          74.3% 0.235   7     11   368 
deepsort      74.8% 0.238  76     7    364 
bytrack       73.7% 0.182  76     0    318

数据集1

如图所示，目标在被建筑遮挡后重新出现时，出现了ID切换，这是由于轨迹丢失太久造成的，改进匹配策略之后，会对未激活轨迹再次进行匹配以恢复轨迹，如图所示（这里要用391的图像）,改进后的算法成功恢复了轨迹，缓解了ID切换的问题。

如图所示（476）帧，目标由天空进入云层后，发生目标切换，这种情况是检测器漏检造成的的轨迹碎片化导致的，在使用IRST-YOLOv8后,成功检测到了目标（473）


数据集2

如图所示，目标在经过障碍物时556-567帧，由于被遮挡，此时轨迹丢失，由于探测器移动过快，图像中出现模糊，此后的数帧都没有捕捉到目标，直到589帧目标才重新出现，此时ID已经经过5次切换。

改进后，在第568帧成功捕捉到目标。

如图所示，923帧 925帧由于背景切换导致检

如图199-200帧，此时探测器移动幅度过大且发生了背景切换，目标在图像中的位置变化巨大，导致轨迹丢失，即使此时目标的置信度很高，跟踪器也没有成功快速地恢复轨迹，之后的数帧都处于失配状态，直到218帧才真重新出现，改进后的算法虽然没有解决目标位置突变引起的轨迹丢失问题，但是3帧后成功恢复了（203）后续的轨迹。