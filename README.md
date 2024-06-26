# STVchrono
Dataset of the paper:

**The STVchrono Dataset: Towards Continuous Change Recognition in Time**

## Dataset annotation files

Download through [Google Drive Link](https://drive.google.com/drive/folders/1CHXSSAh2C8RtSgeMnbem_7c9C5Uk6wTb?usp=sharing)

- Continual Change Captioning (image pair)
  - file: stvchrono_v1_continual-change-captioning_image-pair.json
    
- Continual Change Captioning (image sequence)
  - file: stvchrono_v1_continual-change-captioning_image-sequence.json

- Change-aware Sequential Instance Segmentation 
  - file: stvchrono_v1_change-aware-sequential-instance-segmentation.json 

### Data format:
STVchrono includes three annotation files. Each files is structured in JSON format and divided into two main sections: `train` and `test`. Within these sections, the data are organized as follows:

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

```
