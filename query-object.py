
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)

    @property
    def full_name(self):
        "Returns the person's full name."
        return f"{self.first_name} {self.last_name}"
    
    class Meta():
        db_table = "persons"


class Result(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    cgpa = models.FloatField()
    SEMESTER_LIST = {
        "1":"First Semester",
        "2":"Second Semester",
        "3":"Third Semester",
    }
    semester = models.CharField(max_length=255, choices=SEMESTER_LIST)

    class Meta():
        db_table = "results"


persons = Person.objects.filter(first_name="Sourov",last_name="Sourov")
    # Result.objects.create(person=persons, cgpa="3.85", semester="1")
    for person in persons:
        result = person.result_set.first()
        if result:
            print(result.cgpa)





for person in persons:
        if person.id == 1:
            result = person.result_set.create(cgpa="3.85", semester="1")
            if result:
            # print(model_to_dict(person))
                print(result.get_semester_display())
