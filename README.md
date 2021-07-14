AWS utilities for speeding up work.

In order for scripts to work you have to add neccesssary users
to your AWS account and allow them to do certain operations.


```
python main.py --start_region eu-west-1 --start_ami ami-849thd7fuh79 --profile default --instance_type p2.xlarge

```  
you are gonna get output similar to:

```
Regions for spot:['ap-south-1', 'eu-west-1', 'ap-northeast-2', 'ap-northeast-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2', 'us-west-2']
```
