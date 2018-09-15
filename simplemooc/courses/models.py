from django.db import models

# Create your models here.
#ajuda na busca, contem em nome e descricao
class courseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains = query) | \
            models.Q(description__icontains = query)
        )

class Course(models.Model):
    name = models.CharField('Nome', max_length = 100)
    
    slug = models.SlugField('Atalho')
    
    about = models.TextField('Sobre o Curso', blank=True)

    description = models.TextField('Descrição Simples', blank=True)
    
    start_date = models.DateField(
        'Data de Início', null=True, blank=True
    )
    image = models.ImageField(upload_to='courses/images', verbose_name='Imagem', null=True, blank=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = courseManager()

    #para acertar o nome no admin exibicao
    def __str__(self):
        return self.name
    #muda o nome de courses para curso interfere no django admin
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        #vc indica uma lista de campos para o django ordenar
        ordering = ['name']