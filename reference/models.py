from django.db import models


class Case(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=4)  # 4 digit year
    TYPE_CHOICES = (
        ('Civil', 'Civil'),
        ('Criminal', 'Criminal'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, db_index=True)


class Tournament(models.Model):
    # potentially break out by location later
    name = models.CharField(max_length=100)
    date = models.DateField()
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, null=True)


class WitnessType(models.Model):
    # preseed with expert, character, crying, victim, defendant
    description = models.CharField(max_length=4)


class Witness(models.Model):
    name = models.CharField(max_length=100)
    types = models.ManyToManyField(WitnessType)
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, null=True)
    side_constrained = models.BooleanField(default=None)


class Competitor(models.Model):
    name = models.CharField(max_length=100)
    grad_year = models.CharField(max_length=4)
    # potential things to add captain, eboard etc (could we detect a difference between eboard and not?)


class WitnessRole(models.Model):
    attorney = models.ForeignKey(
        Competitor, on_delete=models.SET_NULL, related_name='attorney', null=True)
    portrayed_by = models.ForeignKey(
        Competitor, on_delete=models.SET_NULL, related_name='portrayed_by', null=True)
    role = models.ForeignKey(Witness, on_delete=models.SET_NULL, null=True)
    SIDE_CHOICES = (
        ('P', 'P'),
        ('D', 'D'),
    )
    side = models.CharField(max_length=1, choices=SIDE_CHOICES, db_index=True)


class Team(models.Model):
    tournament = models.ForeignKey(
        Tournament, on_delete=models.SET_NULL, null=True)
    p_opener = models.ForeignKey(
        Competitor, on_delete=models.SET_NULL, related_name='p_open', null=True)
    p_closer = models.ForeignKey(
        Competitor, on_delete=models.SET_NULL, related_name='p_close', null=True)
    pw_1 = models.ForeignKey(
        WitnessRole, on_delete=models.SET_NULL, related_name='pw_1', null=True)
    pw_2 = models.ForeignKey(
        WitnessRole, on_delete=models.SET_NULL, related_name='pw_2', null=True)
    pw_3 = models.ForeignKey(
        WitnessRole, on_delete=models.SET_NULL, related_name='pw_3', null=True)
    d_opener = models.ForeignKey(
        Competitor, on_delete=models.SET_NULL, related_name='d_open', null=True)
    d_closer = models.ForeignKey(
        Competitor, on_delete=models.SET_NULL, related_name='d_close', null=True)
    dw_1 = models.ForeignKey(
        WitnessRole, on_delete=models.SET_NULL, related_name='dw_1', null=True)
    dw_2 = models.ForeignKey(
        WitnessRole, on_delete=models.SET_NULL, related_name='dw_2', null=True)
    dw_3 = models.ForeignKey(
        WitnessRole, on_delete=models.SET_NULL, related_name='dw_3', null=True)
