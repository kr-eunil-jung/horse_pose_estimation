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