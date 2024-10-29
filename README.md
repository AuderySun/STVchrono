# [[CVPR 2024] The STVchrono Dataset: Towards Continuous Change Recognition in Time](https://openaccess.thecvf.com/content/CVPR2024/papers/Sun_The_STVchrono_Dataset_Towards_Continuous_Change_Recognition_in_Time_CVPR_2024_paper.pdf)

Dataset of the CVPR 2024 paper STVchrono Dataset

## Dataset annotation files

We have updated our STVchrono dataset based on Mapillary. Please download the latest version (stvchrono_based_mapillary.zip) from this repository.

You can download the images from Mapillary using the image ID, which is saved in content.name. 

Here is an example: 'LlY70YKk5onM1fsNga0KrA' and 'tpsBxjm7qB7kF1aYcQP7LA' are image IDs.
```
"contents": [
    {
        "name": "2018-09-27_LlY70YKk5onM1fsNga0KrA.jpg",
        "url": "",
        "width": 640,
        "height": 480
    },
    {
        "name": "2018-12-28_tpsBxjm7qB7kF1aYcQP7LA.jpg",
        "url": "",
        "width": 640,
        "height": 480
    }
]
```



~~Download through [Google Drive Link](https://drive.google.com/drive/folders/1CHXSSAh2C8RtSgeMnbem_7c9C5Uk6wTb?usp=sharing)~~
~~- Continual Change Captioning (image pair)~~
~~- file: stvchrono_v1_continual-change-captioning_image-pair.json~~
~~- Continual Change Captioning (image sequence)~~
~~- file: stvchrono_v1_continual-change-captioning_image-sequence.json~~
~~- Change-aware Sequential Instance Segmentation~~
~~- file: stvchrono_v1_change-aware-sequential-instance-segmentation.json~~

### Data format:
We will provide an update on the data format soon.

~~STVchrono includes three annotation files. Each files is structured in JSON format and divided into two main sections: `train` and `test`. Within these sections, the data are organized as follows:~~

      city: The name of the city where the images were taken, indicating the geographical source of the images.
      image_IDs: This is a list of the IDs for the image series, with their order indicating their sequence. 
                 These IDs are the panorama IDs on Google Street View, serving as unique identifiers to locate the corresponding panoramic images on Google Street View.
      change_caption: This describes the trends and changes observed across the image sequence. The text describes change trends and comparative differences between images in the sequence (eg: 1 to 5) or image pairs (A and B).


## Accessing dataset images

To download panoramas collected for STVchrono using the Google Street View API, you can use the provided Python script `download_panorama_via_streetview_api.py`. 
Before running the script, ensure you have Python installed and have obtained a Google Street View API key, which is necessary for accessing the panoramas. 
```
python download_panorama_via_streetview_api.py
```

## Contact
If you have any questions or concerns regarding the dataset, please contact us at qiu.yue@aist.go.jp and yanjun.son@aist.go.jp


## Citation

If you use or discuss our STVchrono, please cite our paper:
```
@inproceedings{inproceedings,
author = {Sun, Yanjun and Yue, Qiu and Khan, Mariia and Matsuzawa, Fumiya and Iwata, Kenji},
year = {2024},
pages = {14111-14120},
title = {The STVchrono Dataset: Towards Continuous Change Recognition in Time},
booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
}
```
