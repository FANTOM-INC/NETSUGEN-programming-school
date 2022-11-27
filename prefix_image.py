from pathlib import Path


def prefix_image(path):
    files = path.glob('*')
    image_files = sorted(
        [f for f in files if f.suffix in ['.jpg', '.png', '.gif']])

    for i in range(len(image_files)):
        new_image_file_name = "{}_".format(i) + image_files[i].name
        new_path = path / new_image_file_name
        image_files[i].rename(new_path)


if __name__ == '__main__':
    path = Path.cwd() / 'sample_file'
    prefix_image(path)
