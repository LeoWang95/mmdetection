# dataset settings
dataset_type = 'CocoDataset'
data_root = 'data/FireDetector_uma/'

# Example to use different file client
# Method 1: simply set the data root and let the file I/O module
# automatically infer from prefix (not support LMDB and Memcache yet)

# data_root = 's3://openmmlab/datasets/detection/coco/'

# Method 2: Use `backend_args`, `file_client_args` in versions before 3.0.0rc6
# backend_args = dict(
#     backend='petrel',
#     path_mapping=dict({
#         './data/': 's3://openmmlab/datasets/detection/',
#         'data/': 's3://openmmlab/datasets/detection/'
#     }))
backend_args = None
class_name = ('fire',) 
num_classes = len(class_name)
metainfo = dict(
    classes=class_name,
    palette=["#F72585", "#7209B7", "#3A0CA3", "#4361EE", "#4CC9F0", "#4CC6F0"]   # 画图时候的颜色，随便设置即可
)
train_pipeline = [
    dict(type='LoadImageFromFile', backend_args=backend_args),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', scale=(640, 640), keep_ratio=True),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PackDetInputs')
]
test_pipeline = [
    dict(type='LoadImageFromFile', backend_args=backend_args),
    dict(type='Resize', scale=(640, 640), keep_ratio=True),
    # If you don't have a gt annotation, delete the pipeline
    dict(type='LoadAnnotations', with_bbox=True),
    dict(
        type='PackDetInputs',
        meta_keys=('img_id', 'img_path', 'ori_shape', 'img_shape',
                   'scale_factor'))
]
train_dataloader = dict(
    batch_size=16,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    batch_sampler=dict(type='AspectRatioBatchSampler'),
    dataset=dict(
        type=dataset_type,
        metainfo=metainfo,
        data_root=data_root,
        ann_file='annotations/train.json',
        data_prefix=dict(img='train/'),
        filter_cfg=dict(filter_empty_gt=True, min_size=32),
        pipeline=train_pipeline,
        backend_args=backend_args))
val_dataloader = dict(
    batch_size=16,
    num_workers=2,
    persistent_workers=True,
    drop_last=False,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        metainfo=metainfo,
        data_root=data_root,
        ann_file='annotations/val.json',
        data_prefix=dict(img='valid/'),
        test_mode=True,
        pipeline=test_pipeline,
        backend_args=backend_args))

test_dataloader = dict(
    batch_size=16,
    num_workers=2,
    persistent_workers=True,
    drop_last=False,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        metainfo=metainfo,
        data_root=data_root,
        ann_file='annotations/test.json',
        data_prefix=dict(img='test/'),
        test_mode=True,
        pipeline=test_pipeline,
        backend_args=backend_args))       
# test_dataloader = dict(
#     dataset=dict(
#         type=dataset_type,
#         metainfo=metainfo,
#         data_root=data_root,
#         ann_file='annotations/test.json',
#         data_prefix=dict(img='imgs/')))
test_dataloader = val_dataloader
# val_evaluator = dict(ann_file=data_root + 'annotations/test.json')
val_evaluator = dict(
    type='CocoMetric',
    ann_file=data_root + 'annotations/val.json',
    metric='bbox',
    format_only=False,
    backend_args=backend_args)
test_evaluator = dict(
    type='CocoMetric',
    ann_file=data_root + 'annotations/test.json',
    metric='bbox',
    classwise = True,
    format_only=False,
    backend_args=backend_args)
# test_evaluator = val_evaluator
# test_evaluator = dict(type='CocoMetric',ann_file=data_root + 'annotations/test.json',classwise = True)

# inference on test dataset and
# format the output results for submission.
# test_dataloader = dict(
#     batch_size=1,
#     num_workers=2,
#     persistent_workers=True,
#     drop_last=False,
#     sampler=dict(type='DefaultSampler', shuffle=False),
#     dataset=dict(
#         type=dataset_type,
#         metainfo=metainfo,
#         data_root=data_root,
#         ann_file='annotations/test.json',
#         data_prefix=dict(img='imgs/'),
#         test_mode=True,
#         pipeline=test_pipeline))
# test_evaluator = dict(
#     type='CocoMetric',
#     metric='bbox',
#     classwise = True,
#     format_only=True,
#     ann_file=data_root + 'annotations/test.json',
#     outfile_prefix='./work_dirs/dfs_detection/test')
