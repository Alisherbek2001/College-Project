from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from common.models import BaseModel

class Slider(BaseModel):
    title = models.CharField(_("Slider title"),max_length=255)
    image = models.ImageField(_("Slider image"),upload_to='slider/')
    description = models.TextField(_("Slider description"))
    
    class Meta:
        verbose_name = _("Slider")
        verbose_name_plural = _("Sliders")
        
    def __str__(self) -> str:
        return self.title
    
    
class About(BaseModel):
    title = models.CharField(_("About title"),max_length=255)
    slug = models.CharField(_("About slug"),max_length=255,null=True,blank=True)
    image = models.ImageField(_("About image"),upload_to='about/')
    description = models.TextField(_("About description"))
    
    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("Abouts")
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)
        
    def __str__(self) -> str:
        return self.title
    

class OurHistory(BaseModel):
    history_year = models.CharField(_('History year'),max_length=255)
    description = models.TextField(_("History description"))
    image = models.ImageField(_('History image'),upload_to='history/')
    
    class Meta:
        verbose_name = _('History')
        verbose_name_plural = _('Histories')
        
    def __str__(self) -> str:
        return self.history_year
    
class Result(BaseModel):
    name = models.CharField(_("Name"),max_length=255)
    amount = models.PositiveIntegerField(_("Amount"),default=0)
    icon = models.ImageField(_('Icon'),upload_to='result/')
    
    class Meta:
        verbose_name = _('Result')
        verbose_name_plural = _("Results")
        
    def __str__(self) -> str:
        return self.name
    
class Partner(BaseModel):
    name = models.CharField(_('Partner name'),max_length=255)
    icon = models.ImageField(_("Partner icon"),upload_to='partner/')
    link = models.CharField(_('Partner link'),max_length=255)
    
    class Meta:
        verbose_name = _("Partner")
        verbose_name_plural = _('Partners')
    
    def __str__(self) -> str:
        return self.name
    
class AboutCard(BaseModel):
    name = models.CharField(_("Card name"),max_length=225)
    icon = models.ImageField(_('Card icon'),max_length=255)
    description = models.TextField(_('Card description'),max_length=255)
    
    class Meta:
        verbose_name = _("About page card")
        verbose_name_plural = _("About page cards")
        
    def __str__(self) -> str:
        return self.name
    
class Teacher(BaseModel):
    name = models.CharField(_('Teacher'),max_length=255)
    image = models.ImageField(_('Teacher image'),upload_to='teacher/')
    direction = models.CharField(_("Teacher's direction"),max_length=255)
    facebook_link = models.CharField(_('Facebook link'),max_length=255,null=True,blank=True)
    twitter_link = models.CharField(_('Twitter link'),max_length=255,null=True,blank=True)
    linkedin_link = models.CharField(_('Linkedin link'),max_length=255,null=True,blank=True)
    skype_link = models.CharField(_('Skype link'),max_length=255,null=True,blank=True)
    
    class Meta:
        verbose_name = _("Teacher")
        verbose_name_plural = _("Teachers")
    
    def __str__(self) -> str:
        return self.name