from django.db import models
from django.shortcuts import reverse


class New(models.Model):
    MODES_OF_SAVING = (
        ('pub', 'publishded successfully'),
        ('dra', 'saved as draft'),
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    authors = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # auth.Uer mige to admin bbnin ki bode nvisnde(foreigh key) -- casecade yni ag nvsnde paak krd postesam paak( khhod django nvvshte)
    # bsort pish farz moghe iijad post jadid user khood trf return mishee ,, option khodesh
    date_of_creation = models.DateTimeField(auto_now_add=True)
    #zaman akharin virayesh:
    date_modify = models.DateTimeField(auto_now=True)
    # entekhab halat namayesh
    status = models.CharField(choices=MODES_OF_SAVING, max_length=3)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('new_pos', args=[self.id])


