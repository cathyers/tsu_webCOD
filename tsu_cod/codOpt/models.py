# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AmcsdXCod(models.Model):
    ext_id = models.CharField(max_length=7, blank=True, null=True)
    cod_id = models.IntegerField()
    relation_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amcsd_x_cod'


class ChemspiderXCod(models.Model):
    ext_id = models.IntegerField()
    cod_id = models.IntegerField()
    relation_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chemspider_x_cod'


class CodAmcsd(models.Model):
    codid = models.IntegerField(unique=True, blank=True, null=True)
    amcsd_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cod_amcsd'


class Data(models.Model):
    file = models.IntegerField(primary_key=True)
    a = models.FloatField(blank=True, null=True)
    siga = models.FloatField(blank=True, null=True)
    b = models.FloatField(blank=True, null=True)
    sigb = models.FloatField(blank=True, null=True)
    c = models.FloatField(blank=True, null=True)
    sigc = models.FloatField(blank=True, null=True)
    alpha = models.FloatField(blank=True, null=True)
    sigalpha = models.FloatField(blank=True, null=True)
    beta = models.FloatField(blank=True, null=True)
    sigbeta = models.FloatField(blank=True, null=True)
    gamma = models.FloatField(blank=True, null=True)
    siggamma = models.FloatField(blank=True, null=True)
    vol = models.FloatField(blank=True, null=True)
    sigvol = models.FloatField(blank=True, null=True)
    celltemp = models.FloatField(blank=True, null=True)
    sigcelltemp = models.FloatField(blank=True, null=True)
    diffrtemp = models.FloatField(blank=True, null=True)
    sigdiffrtemp = models.FloatField(blank=True, null=True)
    cellpressure = models.FloatField(blank=True, null=True)
    sigcellpressure = models.FloatField(blank=True, null=True)
    diffrpressure = models.FloatField(blank=True, null=True)
    sigdiffrpressure = models.FloatField(blank=True, null=True)
    thermalhist = models.CharField(max_length=255, blank=True, null=True)
    pressurehist = models.CharField(max_length=255, blank=True, null=True)
    compoundsource = models.CharField(max_length=255, blank=True, null=True)
    nel = models.CharField(max_length=4, blank=True, null=True)
    sg = models.CharField(max_length=32, blank=True, null=True)
    sghall = models.CharField(db_column='sgHall', max_length=64, blank=True, null=True)  # Field name made lowercase.
    commonname = models.CharField(max_length=1024, blank=True, null=True)
    chemname = models.CharField(max_length=2048, blank=True, null=True)
    mineral = models.CharField(max_length=255, blank=True, null=True)
    formula = models.CharField(max_length=255, blank=True, null=True)
    calcformula = models.CharField(max_length=255, blank=True, null=True)
    z = models.SmallIntegerField(db_column='Z', blank=True, null=True)  # Field name made lowercase.
    zprime = models.FloatField(db_column='Zprime', blank=True, null=True)  # Field name made lowercase.
    acce_code = models.CharField(max_length=6, blank=True, null=True)
    authors = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    journal = models.CharField(max_length=255, blank=True, null=True)
    year = models.SmallIntegerField(blank=True, null=True)
    volume = models.SmallIntegerField(blank=True, null=True)
    issue = models.CharField(max_length=10, blank=True, null=True)
    firstpage = models.CharField(max_length=20, blank=True, null=True)
    lastpage = models.CharField(max_length=20, blank=True, null=True)
    doi = models.CharField(max_length=127, blank=True, null=True)
    method = models.CharField(max_length=18, blank=True, null=True)
    radiation = models.CharField(max_length=32, blank=True, null=True)
    wavelength = models.FloatField(blank=True, null=True)
    radtype = models.CharField(db_column='radType', max_length=80, blank=True, null=True)  # Field name made lowercase.
    radsymbol = models.CharField(db_column='radSymbol', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rall = models.FloatField(db_column='Rall', blank=True, null=True)  # Field name made lowercase.
    robs = models.FloatField(db_column='Robs', blank=True, null=True)  # Field name made lowercase.
    rref = models.FloatField(db_column='Rref', blank=True, null=True)  # Field name made lowercase.
    wrall = models.FloatField(db_column='wRall', blank=True, null=True)  # Field name made lowercase.
    wrobs = models.FloatField(db_column='wRobs', blank=True, null=True)  # Field name made lowercase.
    wrref = models.FloatField(db_column='wRref', blank=True, null=True)  # Field name made lowercase.
    rfsqd = models.FloatField(db_column='RFsqd', blank=True, null=True)  # Field name made lowercase.
    ri = models.FloatField(db_column='RI', blank=True, null=True)  # Field name made lowercase.
    gofall = models.FloatField(blank=True, null=True)
    gofobs = models.FloatField(blank=True, null=True)
    gofgt = models.FloatField(blank=True, null=True)
    duplicateof = models.IntegerField(blank=True, null=True)
    optimal = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)
    flags = models.CharField(max_length=37, blank=True, null=True)
    text = models.TextField()
    svnrevision = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    onhold = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data'


class Databases(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    website = models.CharField(max_length=256, blank=True, null=True)
    url_prefix = models.CharField(max_length=512, blank=True, null=True)
    url_postfix = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'databases'


class Dois(models.Model):
    doi = models.CharField(unique=True, max_length=127, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dois'


class DrugbankXCod(models.Model):
    ext_id = models.CharField(max_length=7, blank=True, null=True)
    cod_id = models.IntegerField()
    relation_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drugbank_x_cod'


class Fingerprints(models.Model):
    smiles_id = models.IntegerField(blank=True, null=True)
    fp0 = models.BigIntegerField(blank=True, null=True)
    fp1 = models.BigIntegerField(blank=True, null=True)
    fp2 = models.BigIntegerField(blank=True, null=True)
    fp3 = models.BigIntegerField(blank=True, null=True)
    fp4 = models.BigIntegerField(blank=True, null=True)
    fp5 = models.BigIntegerField(blank=True, null=True)
    fp6 = models.BigIntegerField(blank=True, null=True)
    fp7 = models.BigIntegerField(blank=True, null=True)
    fp8 = models.BigIntegerField(blank=True, null=True)
    fp9 = models.BigIntegerField(blank=True, null=True)
    fp10 = models.BigIntegerField(blank=True, null=True)
    fp11 = models.BigIntegerField(blank=True, null=True)
    fp12 = models.BigIntegerField(blank=True, null=True)
    fp13 = models.BigIntegerField(blank=True, null=True)
    fp14 = models.BigIntegerField(blank=True, null=True)
    fp15 = models.BigIntegerField(blank=True, null=True)
    fp16 = models.BigIntegerField(blank=True, null=True)
    fp17 = models.BigIntegerField(blank=True, null=True)
    fp18 = models.BigIntegerField(blank=True, null=True)
    fp19 = models.BigIntegerField(blank=True, null=True)
    fp20 = models.BigIntegerField(blank=True, null=True)
    fp21 = models.BigIntegerField(blank=True, null=True)
    fp22 = models.BigIntegerField(blank=True, null=True)
    fp23 = models.BigIntegerField(blank=True, null=True)
    fp24 = models.BigIntegerField(blank=True, null=True)
    fp25 = models.BigIntegerField(blank=True, null=True)
    fp26 = models.BigIntegerField(blank=True, null=True)
    fp27 = models.BigIntegerField(blank=True, null=True)
    fp28 = models.BigIntegerField(blank=True, null=True)
    fp29 = models.BigIntegerField(blank=True, null=True)
    fp30 = models.BigIntegerField(blank=True, null=True)
    fp31 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fingerprints'


class Jaltnames(models.Model):
    journal_id = models.IntegerField(blank=True, null=True)
    jsequence_id = models.IntegerField(blank=True, null=True)
    altname = models.CharField(unique=True, max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jaltnames'


class Journals(models.Model):
    name = models.CharField(unique=True, max_length=250, blank=True, null=True)
    abbrev = models.CharField(max_length=250, blank=True, null=True)
    jcode = models.CharField(max_length=16, blank=True, null=True)
    firstyear = models.IntegerField(blank=True, null=True)
    lastyear = models.IntegerField(blank=True, null=True)
    issnprint = models.CharField(db_column='ISSNprint', max_length=10, blank=True, null=True)  # Field name made lowercase.
    issnonline = models.CharField(db_column='ISSNonline', max_length=10, blank=True, null=True)  # Field name made lowercase.
    coden = models.CharField(max_length=6, blank=True, null=True)
    doiprefix = models.CharField(max_length=20, blank=True, null=True)
    publisher_id = models.IntegerField(blank=True, null=True)
    jsequence_id = models.IntegerField(blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'journals'
        unique_together = (('name', 'issnprint'), ('name', 'coden'),)


class Jsequences(models.Model):
    name = models.CharField(unique=True, max_length=250, blank=True, null=True)
    abbrev = models.CharField(unique=True, max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jsequences'


class Messages(models.Model):
    text = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class MpodXCod(models.Model):
    ext_id = models.IntegerField()
    cod_id = models.IntegerField()
    relation_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mpod_x_cod'


class News(models.Model):
    begin_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()
    text = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class Numbers(models.Model):
    start_id = models.IntegerField(primary_key=True)
    end_id = models.IntegerField()
    curr_id = models.IntegerField(unique=True)
    journal = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'numbers'


class Programs(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=32, blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    path = models.CharField(max_length=512, blank=True, null=True)
    repository = models.CharField(max_length=512, blank=True, null=True)
    url = models.CharField(max_length=512, blank=True, null=True)
    osname = models.CharField(max_length=30, blank=True, null=True)
    osdistro = models.CharField(max_length=30, blank=True, null=True)
    osversion = models.CharField(max_length=30, blank=True, null=True)
    osversionname = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programs'


class PubchemXCod(models.Model):
    ext_id = models.IntegerField(blank=True, null=True)
    cod_id = models.IntegerField(blank=True, null=True)
    relation_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pubchem_x_cod'


class Publishers(models.Model):
    abbrev = models.CharField(unique=True, max_length=10, blank=True, null=True)
    name = models.CharField(unique=True, max_length=250, blank=True, null=True)
    doiprefix = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publishers'


class RdfRelations(models.Model):
    relation = models.CharField(max_length=256, blank=True, null=True)
    uri_prefix = models.CharField(max_length=512, blank=True, null=True)
    vocabulary = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rdf_relations'


class Smiles(models.Model):
    codid = models.IntegerField(unique=True)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'smiles'


class Spacegroups(models.Model):
    itcn = models.IntegerField(db_column='ITCn', blank=True, null=True)  # Field name made lowercase.
    hall = models.CharField(db_column='Hall', max_length=16, blank=True, null=True)  # Field name made lowercase.
    schoenflies = models.CharField(db_column='Schoenflies', max_length=6, blank=True, null=True)  # Field name made lowercase.
    hm = models.CharField(db_column='HM', max_length=16, blank=True, null=True)  # Field name made lowercase.
    hmu = models.CharField(db_column='HMu', max_length=16, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='class', max_length=12, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    nau = models.IntegerField(db_column='Nau', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spacegroups'


class Successors(models.Model):
    journal_id = models.IntegerField(blank=True, null=True)
    successor_journal_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'successors'


class Validation(models.Model):
    codid = models.IntegerField(blank=True, null=True)
    program = models.CharField(max_length=255, blank=True, null=True)
    program_id = models.SmallIntegerField(blank=True, null=True)
    level = models.CharField(max_length=10, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'validation'
        unique_together = (('codid', 'level', 'message'),)


class WikipediaXCod(models.Model):
    ext_id = models.CharField(max_length=255, blank=True, null=True)
    cod_id = models.IntegerField()
    relation_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wikipedia_x_cod'
