from django.db import models


class Personal(models.Model):
    firest_name     =       models.CharField(max_length=130)
    last_name       =       models.CharField(max_length=130)
    born            =       models.DateField()
    died            =       models.DateField(null=True, blank=True)

    class Meta:
        ordering=('firest_name', 'last_name')

    def __str__(self):
        if self.died:
            return '{}, {} ,({})'.format(
                self.firest_name,
                self.last_name,
                self.born,
                self.died
            )
        return '{}, {}, ({})'.format(
            self.firest_name,
            self.last_name,
            self.born
        )


class Movie(models.Model):
    director       = models.ForeignKey(to='Personal', on_delete=models.SET_NULL, related_name='directed',null=True, blank=True)
    writer         =models.ManyToManyField(to='Personal', related_name='writenin_credits',blank=True)
    actors         =models.ManyToManyField(to='Personal', through='Role',related_name='acting_credits',blank=True)
    
    NOT_RATED=0
    RATED_G=1
    RATED_PG=2
    RATED_R=3
    RATINGS=(
        (NOT_RATED, 'NR - Not Rated'),
        (RATED_G,' G - General Audience'),
        (RATED_PG, 'PG - Parent Guidence Suggested'),
        (RATED_R, 'R - Restricted'),

    )
    title       =   models.CharField(max_length=140)
    plot        =   models.TextField()
    year        =   models.PositiveIntegerField()
    rating      =   models.IntegerField(
        choices=RATINGS,
        default=NOT_RATED)
    
    runtime     =   models.IntegerField()
    website     =   models.URLField(
        blank=True)
    class Meta:
        ordering=('-year', 'title')

    def __str__(self):
        return '{} ({})'.format(
            self.title,self.year
        )

class Role(models.Model):
    movie       =       models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    person       =       models.ForeignKey(Personal, on_delete=models.DO_NOTHING)
    name        =       models.CharField(max_length=140)

    def __str__(self):
        return '{}, {}, {}'.format(
            self.movie_id, self.person_id, self.name
        )

    class Meta:
        unique_together = (
            'movie',
            'person',
            'name',
        )


