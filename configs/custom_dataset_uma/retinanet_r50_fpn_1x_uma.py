_base_ = [
    '../_base_/models/retinanet_r50_fpn_uma.py',
    '../_base_/datasets/uma_detection.py',
    '../_base_/schedules/schedule_uma.py', '../_base_/default_runtime.py',
    '../retinanet/retinanet_tta.py'
]
work_dir = './work_dirs/retinanet_r50_fpn_1x_dfs'

# optimizer
optim_wrapper = dict(
    optimizer=dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001))
