
from multiselectfield import MultiSelectField
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings



ot = (
    (1,'근지구력'),
    (2,'심폐지구력'),
    (3,'근력'),
    )

part_ =(
    (1,'윗가슴'),
    (2,'스트레칭'),
    (3,'가슴중앙'),
    (4,'아랫가슴'),
    (5,'승모근'),
    (6,'광배근'),
    (7,'척추기립근'),
    (8,'전면삼각근'),
    (9,'후면삼각근'),
    (10,'측면삼각근'),
    (11,'이두근'),
    (12,'삼두근'),
    (13,'복근'),
    (14,'대퇴이두근'),
    (15,'대퇴사두근'),
    (16,'비복근'),
)


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    image = ProcessedImageField( upload_to='images/', blank=True,
                                processors=[ResizeToFill(720,480)],
                                format='JPEG',
                                options={'quality': 80})
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    otwo = MultiSelectField(choices=ot,max_choices=6)
    workout = models.CharField(max_length=30)
    part = MultiSelectField(choices=part_, max_choices=6)


class Comment(models.Model):
    content = models.CharField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
