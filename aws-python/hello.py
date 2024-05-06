import boto3
aws_managemebt_console= boto3.session.Session(profile_name='default')
aws_console= aws_managemebt_console.resource('iam')
for each_user in aws_console.users.all():
    print(each_user.name)