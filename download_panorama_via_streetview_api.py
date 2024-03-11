import json
import argparse
import requests
from PIL import Image, UnidentifiedImageError
from io import BytesIO
from typing import Dict, Union, List, Optional

def get_streetview(pano_id: str, api_key: str, width: int = 640, height: int = 640,
                   heading: int = 0, fov: int = 120, pitch: int = 0) -> Optional[Image.Image]:
    """
    Fetches a street view image from the Google Maps API and returns it as a PIL Image object.

    Args:
        pano_id (str): The panorama ID to fetch the street view image for.
        api_key (str): Your Google Maps API key.
        width (int): Width of the requested image in pixels. Default is 640.
        height (int): Height of the requested image in pixels. Default is 640.
        heading (int): Compass heading of the camera. Valid values are [0,360]. Default is 0.
        fov (int): Field of view in degrees. Default is 120.
        pitch (int): Up or down angle of the camera relative to the Street View vehicle. Default is 0.

    Returns:
        Optional[Image.Image]: The street view image as a PIL Image object, or None if an error occurs.
    """
    params: Dict[str, Union[str, int]] = {
        "size": f"{width}x{height}",
        "fov": fov,
        "pitch": pitch,
        "heading": heading,
        "pano": pano_id,
        "key": api_key,
    }
    url = 'https://maps.googleapis.com/maps/api/streetview'

    response = requests.get(url, params=params, stream=True)

    if response.status_code == 200:
        try:
            img = Image.open(BytesIO(response.content))
            return img
        except UnidentifiedImageError:
            print('Cannot identify image file.')
    else:
        print(f"Error or non-image content: Status code {response.status_code}")

    return None

def load_panoid(data_json: str) -> List[str]:
    """
    Loads panorama IDs from a JSON file.

    Args:
        data_json (str): The path to the JSON file containing panorama IDs.

    Returns:
        List[str]: A list of panorama IDs.
    """
    with open(data_json, 'r') as f:
        data = json.load(f)

    train_pano_ids = [j for i in data['train'] for j in i['images_IDs']]
    test_pano_ids = [j for i in data['test'] for j in i['images_IDs']]

    return train_pano_ids + test_pano_ids

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Downloads street view images using panorama IDs.")

    parser.add_argument('--google_maps_api_key', type=str, required=True,
                        help="Your Google Maps API key.")
    parser.add_argument('--data_json', type=str, default='stvchrono_v1_continual-change-captioning_image-pair.json',
                        help="Path to the JSON file containing panorama IDs.")
    parser.add_argument('--image_save_path', type=str, default='../panoramas',
                        help="Path where the downloaded images will be saved.")

    args = parser.parse_args()

    pano_ids = load_panoid(args.data_json)

    for pano in pano_ids:
        img = get_streetview(pano, args.google_maps_api_key)
        if img is not None:
            save_path = f"{args.image_save_path}/{pano}.jpg"
            img.save(save_path, 'JPEG')
            print(f"Image saved to {save_path}")
        else:
            print(f"Failed to download image for panorama ID: {pano}")
