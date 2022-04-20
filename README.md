# Few-Shot O - MMFewShot 手把手教學

[<img src=https://i.imgur.com/PXp4VHu.png  width="150" height="50">](https://mmfewshot.readthedocs.io/)

OpenMMLab是香港中文大學多媒體實驗室(MMLab)與商湯科技合作建立的AI開源算法平台。在2021年OpenMMLab為發展Few-Shot Classification 與Few-Shot Object Detection這兩個題目開啟了MMFewShot這個新專案。詳見[官網](https://mmfewshot.readthedocs.io/en/latest/?badge=latest)。

**Contents of MMFewShot**
* Few-shot classification/object detection algorithms
* Inheritable modules and configure file system
* Pre-trained model weights

## Tutorials
🔥Introduction and Meta-Inference[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1jzebGHDGS6xDKn18vNkEhieYtHtBsHb7?usp=sharing)

🔥Meta-Training[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/12zKAJYg_tGxovuGnmh_Df-GRJ7-AHeU4/view?usp=sharing)

## Official Documents

Official Introduction to mmfewshot
* [Installation](docs/install.md)
* [Concepts of FSL](docs/en/intro.md).
* [Basic usage of mmfewshot](docs/en/get_started.md)

## Model Zoo

Algorithms that MMFewShot implemented, with downloadable pre-trained weight.

<details open>
<summary>Classification</summary>

- [x] [Baseline](configs/classification/baseline/README.md) (ICLR'2019)
- [x] [Baseline++](configs/classification/baseline_plus/README.md) (ICLR'2019)
- [x] [NegMargin](configs/classification/neg_margin/README.md) (ECCV'2020)
- [x] [MatchingNet](configs/classification/matching_net/README.md) (NeurIPS'2016)
- [x] [ProtoNet](configs/classification/proto_net/README.md) (NeurIPS'2017)
- [x] [RelationNet](configs/classification/relation_net/README.md) (CVPR'2018)
- [x] [MetaBaseline](configs/classification/meta_baseline/README.md) (ICCV'2021)
- [x] [MAML](configs/classification/maml/README.md) (ICML'2017)

</details>

<details open>
<summary>Detection</summary>

- [x] [TFA](configs/detection/tfa/README.md) (ICML'2020)
- [x] [FSCE](configs/detection/fsce/README.md) (CVPR'2021)
- [x] [AttentionRPN](configs/detection/attention_rpn/README.md) (CVPR'2020)
- [x] [MetaRCNN](configs/detection/meta_rcnn/README.md) (ICCV'2019)
- [x] [FSDetView](configs/detection/fsdetview/README.md) (ECCV'2020)
- [x] [MPSR](configs/detection/mpsr/README.md) (ECCV'2020)

</details>

## Citation

```bibtex
@misc{mmfewshot2021,
    title={OpenMMLab Few Shot Learning Toolbox and Benchmark},
    author={mmfewshot Contributors},
    howpublished = {\url{https://github.com/open-mmlab/mmfewshot}},
    year={2021}
}
```
```bibtex
@article{wang2020few,
    title={Frustratingly Simple Few-Shot Object Detection},
    author={Wang, Xin and Huang, Thomas E. and  Darrell, Trevor and Gonzalez, Joseph E and Yu, Fisher}
    booktitle = {International Conference on Machine Learning (ICML)},
    month = {July},
    year = {2020}
}
```
## Acknowledgements
* https://github.com/open-mmlab/mmfewshot
    * Official repository of mmfewshot
* https://github.com/ucbdrive/few-shot-object-detection
    * Method of data preparation
* https://app.roboflow.com/
    * Data source, method of data preparation
