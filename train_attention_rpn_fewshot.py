_base_=["configs/detection/attention_rpn/coco/attention-rpn_r50_c4_4xb2_coco_30shot-fine-tuning.py"]

work_dir="./work_dir_attention_rpn"
data_root="data/ocean_coco/"

num_support_ways = 2
num_support_shots = 10
data = dict(
    train=dict(
        type='QueryAwareDataset',
        num_support_ways=num_support_ways,
        num_support_shots=num_support_shots,
        dataset=dict(
            type='FewShotCocoODefaultDataset',
            ann_cfg=[dict(method='Attention_RPN', setting='30SHOT')],
            data_root=data_root,
            img_prefix="images/",
            num_novel_shots=30,
            classes='ALL_CLASSES',
            dataset_name='query_support_dataset'
        )
    ),
    val=dict(
        type='FewShotCocoODataset',
        ann_cfg=[dict(
            type='ann_file',
            ann_file='annotations/valid_annotations.coco.json'
        )],
        data_root=data_root,
        img_prefix="images/",
        classes='ALL_CLASSES'),
    test=dict(
        type='FewShotCocoODataset',
        ann_cfg=[dict(
            type='ann_file',
            ann_file='annotations/valid_annotations.coco.json'
        )],
        data_root=data_root,
        img_prefix="images/",
        classes='ALL_CLASSES',
        test_mode=True),
    model_init=dict(
        copy_from_train_dataset=True,
        samples_per_gpu=16,
        workers_per_gpu=1,
        type='FewShotCocoODataset',
        data_root=data_root,
        img_prefix="images/",
        classes='ALL_CLASSES',
        dataset_name='model_init_dataset'))

optimizer = dict(
    type='SGD',
    lr=0.001,
    momentum=0.9,
    weight_decay=0.0001,
    paramwise_cfg=dict(
        custom_keys=dict({'roi_head.bbox_head': dict(lr_mult=2.0)})))
optimizer_config = dict(grad_clip=None)
lr_config = dict(
    warmup='linear',
    warmup_iters=400,
    warmup_ratio=0.1,
    step=[3000, 5000])
runner = dict(max_iters=6000)
evaluation = dict(
    interval=500,  # Evaluation interval
    class_splits=['BASE_CLASSES', 'NOVEL_CLASSES'])
checkpoint_config = dict(interval=3000)


log_config = dict(interval=50)
log_level = 'INFO'
workflow = [('train', 1)]
use_infinite_sampler = True
seed = 0

load_from = 'https://download.openmmlab.com/mmfewshot/detection/attention_rpn/coco/attention-rpn_r50_c4_4xb2_coco_base-training_20211102_003348-da28cdfd.pth'
norm_cfg = dict(type='IN', requires_grad=False)
model = dict(
    frozen_parameters=['backbone'],
    rpn_head=dict(
        num_support_ways=num_support_ways,
        num_support_shots=num_support_shots,
    ),
    roi_head=dict(
        num_support_ways=num_support_ways,
        num_support_shots=num_support_shots,
    ),
)