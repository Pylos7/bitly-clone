from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
# save a shortened link - name -, url, slug, # of clicks
class Link(models.Model):
	name = models.CharField(max_length=50, unique=True)
	url = models.URLField(max_length=200)
	# mysite.com/link/1
	# mysite.com/link/name-of-link
	slug = models.SlugField(unique=True, blank=True)
	# my first link
 	# my-first-link
	clicks = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f"{self.name} | {self.clicks}"
	
	def click(self):
		self.clicks += 1
		self.save()

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)

		return super().save(*args, **kwargs)