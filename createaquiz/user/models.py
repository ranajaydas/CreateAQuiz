from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from core.utils import ImageResizeUploadS3


class Profile(ImageResizeUploadS3, models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='')
    slug = models.SlugField(max_length=30, unique=True)
    about = models.TextField()
    joined = models.DateTimeField("Date Joined", auto_now_add=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # Maximum size of image allowed without resizing (in pixels)
    max_image_size = (300, 300)

    def __str__(self):
        return self.user.get_username()

    def get_absolute_url(self):
        return reverse('public_profile', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('profile_update')

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     max_size = self.max_image_size
    #
    #     img_name = self.image.name.split('.')[0].lower()
    #     img_extension = self.image.name.split('.')[1].lower()
    #
    #     img_read = storage.open(self.image.name, 'r')
    #     img = Image.open(img_read)
    #
    #     if img.height > max_size[1] or img.width > max_size[0]:
    #         output_size = max_size
    #         img.thumbnail(output_size)
    #         in_mem_file = io.BytesIO()
    #         if img_extension == 'png':
    #             img.save(in_mem_file, format='PNG')
    #         else:
    #             if img.mode not in ('L', 'RGB'):
    #                 img = img.convert('RGB')
    #             img.save(in_mem_file, format='JPEG')
    #         img_write = storage.open(self.image.name, 'w+')
    #         img_write.write(in_mem_file.getvalue())
    #         img_write.close()
    #
    #     img_read.close()
