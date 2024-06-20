from login.models import Test

test_count = Test.objects.count()
print(test_count)  