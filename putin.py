from PIL import Image

def image_tiling(image_path, output_path, crop_coords):
    image = Image.open(image_path)
    width, height = image.size
    new_image = Image.new('RGB', (width, height))

    cropped_image = image.crop(crop_coords)
    cropped_width, crooped_height = cropped_image.size


    for left_pos in range(0, width, cropped_width):
        for top_pos in range(0, height, crooped_height):
            new_image.paste(cropped_image, (left_pos, top_pos))

    new_image.save(output_path)


if __name__ == "__main__":
    coords = (125, 712, 642, 963)
    image_tiling("humming-dogs.jpg", "hummingdogs_tilled.jpg",coords)



