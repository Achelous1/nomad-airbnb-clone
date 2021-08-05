from django.core.management.base import BaseCommand


class Command(BaseCommand):

    """Custom manage.py iloveyou command"""

    help = "This command tells me that he loves me"

    # 커맨드에 인수를 추가할 수 있는 메서드
    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that I love you?",
        )

    # 실직적으로 실행되는 커맨드 메서드
    def handle(self, *args, **options):
        print(self, args, options)
        times = options.get("times")
        for t in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS("I love you"))
