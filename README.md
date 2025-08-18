# [[CVPR 2024] The STVchrono Dataset: Towards Continuous Change Recognition in Time](https://openaccess.thecvf.com/content/CVPR2024/papers/Sun_The_STVchrono_Dataset_Towards_Continuous_Change_Recognition_in_Time_CVPR_2024_paper.pdf)

Dataset of the CVPR 2024 paper STVchrono Dataset

## Dataset annotation files

We have updated our STVchrono dataset using Mapillary data. Please download the latest version (stvchrono_based_mapillary.zip) from this repository.
And you can also access the STVchrono dataset based on Google Street View from [here](https://drive.google.com/drive/folders/1CHXSSAh2C8RtSgeMnbem_7c9C5Uk6wTb).


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
Here, `LlY70YKk5onM1fsNga0KrA` and `tpsBxjm7qB7kF1aYcQP7LA` are image IDs to retrieve images (Mapillary example).
For Google Street View samples, the IDs in image_IDs represent panorama IDs.



### Data format:

Each task in the dataset is structured as a JSON object with the following fields:

- **id**: Unique identifier of the task.  
- **name**: Path-like string indicating city and place.  
- **status / externalStatus**: Workflow status (e.g., `completed`, `approved`).  
- **contents**: List of images in the task.  
  - `name`: Image filename, containing the **date** and **Mapillary image ID** (e.g., `2018-09-27_LlY70YKk5onM1fsNga0KrA.jpg`).  
  - `url`: Direct download URL (may be empty if not provided).  
  - `width`, `height`: Image resolution.  
- **attributes**: List of annotated captions describing changes across the image sequence.  
  - Each entry contains:
    - `type`: Annotation type (`textarea`, `switch`, etc.).  
    - `name`: Human-readable description (with both English and Japanese hints).  
    - `key`: Unique key for this attribute.  
    - `value`: **Change caption**, describing visual differences across images (e.g., “A building on the right of A is not visible in B.”).  
- **tags**: Task labels for filtering and workflow (e.g., `Checked_QA`, `2images`).  
- **assignee / reviewer / approver**: Annotation and review metadata.  
- **timestamps**: `createdAt`, `updatedAt`. 


## Accessing dataset images

To download panoramas collected for STVchrono using the Google Street View API, you can use the provided Python script `download_panorama_via_streetview_api.py`. 
Before running the script, ensure you have Python installed and have obtained a Google Street View API key, which is necessary for accessing the panoramas. 
```
python download_panorama_via_streetview_api.py
```

To download images collected from Mapillary, please refer to this [repo](https://github.com/Stefal/mapillary_download).

## Contact
If you have any questions or concerns regarding the dataset, please get in touch with us at qiu.yue@aist.go.jp and yanjun.son@aist.go.jp


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
