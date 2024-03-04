import boto3
aws_management_console= boto3.session.Session(profile_name='aws-python-user')
ec2_console= aws_management_console.client(service_name='ec2')
response= ec2_console.terminate_instances(

    InstanceIds= ['i-0eb94b8a5549accff']
)