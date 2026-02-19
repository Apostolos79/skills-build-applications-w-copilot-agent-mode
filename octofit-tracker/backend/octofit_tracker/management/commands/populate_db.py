from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

# Import models from models.py
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password')
        captain = User.objects.create_user(username='captain', email='captain@marvel.com', password='password')

        # Create activities
        Activity.objects.create(user='ironman', team='Marvel', type='run', duration=30)
        Activity.objects.create(user='batman', team='DC', type='cycle', duration=45)
        Activity.objects.create(user='superman', team='DC', type='swim', duration=60)
        Activity.objects.create(user='captain', team='Marvel', type='run', duration=25)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=55)
        Leaderboard.objects.create(team='DC', points=105)

        # Create workouts
        Workout.objects.create(name='Pushups', difficulty='Easy')
        Workout.objects.create(name='Pullups', difficulty='Medium')
        Workout.objects.create(name='Squats', difficulty='Easy')
        Workout.objects.create(name='Deadlift', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
