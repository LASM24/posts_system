from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

class Post(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to='posts')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['-created']

    def __str__(self):
        return self.title

@receiver(post_delete, sender=Post)
def delete_post_image(sender, instance, **kwargs):
    # Borra la imagen asociada al post al eliminar el post
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
