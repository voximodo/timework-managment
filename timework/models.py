from django.db import models

class Worker(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.second_name

class Card(models.Model):
    uid = models.CharField(max_length=30)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self):
        return self.worker.first_name + " " + self.worker.second_name + " : " + self.uid

class Reader(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location + " : " + self.name

class Record(models.Model):
    date = models.DateTimeField()
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.worker.first_name + " " + self.worker.second_name +  " : " + self.type + " - " + self.reader.name + " - " + str(self.date)

class Messages(models.Model):
    body = models.CharField(max_length=60)
    date = models.DateTimeField()
    worker = models.ForeignKey(Worker, models.CASCADE)

    def __str__(self):
        return self.worker.first_name + " " + self.worker.second_name + " : " + self.body + " - " + str(self.date)
