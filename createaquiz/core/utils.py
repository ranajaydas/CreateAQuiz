import io
from django.core.files.storage import default_storage as storage
from django.template.defaulttags import register
from PIL import Image


class ImageResizeUploadS3:
    """Inheritable class to resize images before uploading to Amazon S3."""
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            max_size = self.max_image_size

            img_name = self.image.name.split('.')[0].lower()
            img_extension = self.image.name.split('.')[1].lower()

            img_read = storage.open(self.image.name, 'r')
            img = Image.open(img_read)

            if img.height > max_size[1] or img.width > max_size[0]:
                output_size = max_size
                img.thumbnail(output_size)
                in_mem_file = io.BytesIO()
                if img_extension == 'png':
                    img.save(in_mem_file, format='PNG')
                else:
                    if img.mode not in ('L', 'RGB'):
                        img = img.convert('RGB')
                    img.save(in_mem_file, format='JPEG', quality=60)
                img_write = storage.open(self.image.name, 'w+')
                img_write.write(in_mem_file.getvalue())
                img_write.close()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
