import boto3

ec2=boto3.client('ec2',region_name='us-east-1')
value=ec2.describe_instances()
for index_data in value['Reservations']:
    instance_id = index_data['Instances'][0]['InstanceId']
    value = ec2.reboot_instances(InstanceIds=[instance_id,], DryRun=False)
    print("Instance ID: {} is rebooted".format(instance_id))
print("yuvi")