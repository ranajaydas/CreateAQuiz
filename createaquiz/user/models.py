from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image
import sys


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='')
    slug = models.SlugField(max_length=30, unique=True)
    about = models.TextField()
    joined = models.DateTimeField("Date Joined", auto_now_add=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.user.get_username()

    def get_absolute_url(self):
        return reverse('public_profile', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('profile_update')

    def save(self, *args, **kwargs):
        """Resize image before uploading to S3."""
        # Opening the uploaded image in memory
        image = Image.open(self.image)
        output = BytesIO()

        # Resize/modify the image
        image = image.resize((300, 300))

        # After modifications, save it to the output
        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')
        image.save(output, format='JPEG', quality=90)
        output.seek(0)

        # Change the imagefield value to be the newley modifed image value
        self.image = InMemoryUploadedFile(file=output,
                                          field_name='ImageField',
                                          name=self.image.name.split('.')[0]+'.jpg',
                                          content_type='image/jpeg',
                                          size=sys.getsizeof(output),
                                          charset=None)

        super(Profile, self).save(*args, **kwargs)
