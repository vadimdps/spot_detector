import argparse
import sys

import boto3
from botocore.config import Config

boto3.session.Session(profile_name='docu')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--profile',
                        default="default",
                        help='AWS profile.')

    parser.add_argument('--start_region',
                        default="eu-west-1",
                        help='Start region where generic ami.')
    parser.add_argument('--start_ami',
                        required=True,
                        help='Start ami for copy.')

    parser.add_argument('--instance_type',
                        default="p2.xlarge",
                        help='Instance type.')

    args = parser.parse_args()
    # Prepare image to processed
    starting_region = args.start_region
    starting_ami = args.start_ami
    instance_type = args.instance_type
    profile = args.profile

    config = Config(
        region_name=starting_region,
        signature_version='v4',
        retries={
            'max_attempts': 10,
            'mode': 'standard'
        }
    )
    session = boto3.session.Session(profile_name=profile,
                                    region_name=starting_region)
    ec2_client = session.client('ec2')

    regions_response = ec2_client.describe_regions()['Regions']
    available_regions = []
    not_available_regions = []
    for region in regions_response:
        current_region = region['RegionName']
        print(f"Start processing region:{current_region}")
        config = Config(
            region_name=f"{current_region}",
            signature_version='v4',
            retries={
                'max_attempts': 10,
                'mode': 'standard'
            }
        )
        ec2_client = boto3.client('ec2', config=config)

        spot_instance_pricing = ec2_client.describe_spot_price_history(InstanceTypes=[instance_type])
        if len(spot_instance_pricing['SpotPriceHistory']) == 0:
            print(f"Region:{current_region} does not have such instances:{instance_type}")
            not_available_regions.append(current_region)
        else:
            available_regions.append(current_region)

    print(f"Regions for spot:{available_regions}")

sys.exit(0)
