# [ADK2022] 최우수상
![시상식](![image](https://github.com/user-attachments/assets/221be4ba-46be-4dee-b6c1-33492bb8e345)

[관련 기사](https://www.dailyonehealth.com/news/articleView.html?idxno=2579)

# Installation
```bash
pip install openmim
mim install mmcv-full
cd mmpose
pip install -e .
```

# Train
- hrnet_w48_coco_384x384_udp
```bash
python tools/train.py configs/custom/hrnet_w48_coco_384x384_udp.py
```


- hrformer_base_coco_384x384
```bash
python tools/train.py configs/custom/hrformer_base_coco_384x384.py
```


# Test
test.ipynb
