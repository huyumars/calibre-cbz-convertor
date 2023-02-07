from calibre.customize.conversion import OutputFormatPlugin
from calibre.ptempfile import TemporaryDirectory
from calibre.utils.zipfile import ZipFile
from os import path


class CBZOutput(OutputFormatPlugin):
    name = "CBZ Output"
    author = "Mars, Hu"
    version = (0, 0, 1)
    file_type = "cbz"
    commit_name = "cbz_output"

    def convert(self, oeb_book, output_path, input_plugin, opts, log):
        cbz = ZipFile(output_path, mode="w")
        with TemporaryDirectory('_img_extract_') as tdir:
            for item in oeb_book.manifest:
                if item.media_type.startswith('image'):
                    filename = tdir + "/" + path.basename(item.href)
                    with open(filename, "wb") as binary_file:
                        # Write bytes to file
                        binary_file.write(item.data)
                    cbz.write(filename, path.basename(item.href))
