import os


# [xxx/xxx]/filename.ext
def extract_dir_path(path):
    return os.path.dirname(path)


# xxx/xxx/[filename].ext
def extract_filename(path):
    basename = os.path.basename(path)
    filename, _ = os.path.splitext(basename)
    if not filename:
        raise RuntimeError("filename is empty: " + path)
    return filename


# xxx/xxx/filename.[ext]
def extract_ext(path):
    root, ext = os.path.splitext(path)
    if not ext:
        raise RuntimeError("extension is empty: " + path)
    return ext[1:]


def is_video_file(path):
    AVALIABLE_EXTS = [
        'avi',
        'mkv',
        'mp4',
        'rmvb',
        'wmv',
    ]

    if not os.path.isfile(path):
        return False

    ext = extract_ext(path)
    return ext in AVALIABLE_EXTS


class VideoFile:

    def __init__(self, path):
        self.dir_path = extract_dir_path(path)
        self.filename = extract_filename(path)
        self.ext = extract_ext(path)

    @property
    def path(self):
        return os.path.join(
            self.dir_path,
            '{0}.{1}'.format(self.filename, self.ext),
        )
