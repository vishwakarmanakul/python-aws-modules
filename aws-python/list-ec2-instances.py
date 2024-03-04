import boto3

try:
    aws_management_console= boto3.session.Session(region_name='us-east-1')
    ec2_console= aws_management_console.client(service_name='ec2')
    result= ec2_console.describe_instances()['Reservations']
    for each_instance in result:
        for instance_id in each_instance['Instances']:
            print(instance_id['InstanceId'])

except AttributeError as e:
    pass