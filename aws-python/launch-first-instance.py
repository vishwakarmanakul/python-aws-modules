import boto3
aws_management_console= boto3.session.Session(profile_name='aws-python-user')
ec2_console= aws_management_console.client('ec2')
response= ec2_console.run_instances(
    ImageId='ami-0e731c8a588258d0d',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1
)
