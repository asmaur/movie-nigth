from django_celery_beat.models import PeriodicTask
from django_celery_beat.models import IntervalSchedule

def schedule_setup():
    #schedule, _ = schedule = IntervalSchedule(period=IntervalSchedule.MINUTES, every=1) #CrontabSchedule(minute="1")
    schedule, _ = IntervalSchedule.objects.get_or_create(period=IntervalSchedule.MINUTES, every=1)
    task = PeriodicTask.objects.get_or_create(
          name="Notify movie night star",
          interval=schedule,
          #args=args,
          task="movies.tasks.notify_of_starting_soon"
      )
