from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image
import sys


class ImageResizeUploadToS3Model:
    """Image Resize Model inherited by other models."""

    def save(self, *args, **kwargs):
        """Resize image before uploading to Amazon S3."""
        # Opening the uploaded image in memory
        image = Image.open(self.image)
        output = BytesIO()
        image_name = self.image.name.split('.')[0].lower()
        image_extension = self.image.name.split('.')[1].lower()

        # Resize/modify the image
        image = image.resize((300, 300))

        # After modifications, save it to the output
        if image.mode not in ('L', 'RGB') and image_extension != 'png':
            image = image.convert('RGB')

        if image_extension == 'png':
            image.save(output, format='PNG')
            content_type = 'image/png'
        else:
            image.save(output, format='JPEG', quality=90)
            content_type = 'image/jpeg'
            image_extension = 'jpg'
        output.seek(0)

        # Change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(file=output,
                                          field_name='ImageField',
                                          name=image_name + '.' + image_extension,
                                          content_type=content_type,
                                          size=sys.getsizeof(output),
                                          charset=None)

        super().save(*args, **kwargs)
