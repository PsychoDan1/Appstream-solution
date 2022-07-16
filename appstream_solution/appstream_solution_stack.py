from aws_cdk import Stack, aws_iam as iam
import aws_cdk as cdk
import os
from constructs import Construct
import aws_cdk.aws_appstream as appstream

class AppstreamSolutionStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cfn_fleet = appstream.CfnFleet(self, "AppstreamNonProd-Phoenix-solution-fleet",
            instance_type="stream.standard.large",
            name="AppstreamNonProd-Phoenix-solution-fleet",
            compute_capacity = appstream.CfnFleet.ComputeCapacityProperty(
                desired_instances = 20
            ),
            description = "AppstreamNonProd-Phoenix-solution",
            disconnect_timeout_in_seconds = 7200,
            idle_disconnect_timeout_in_seconds = 960,
            enable_default_internet_access = False,
            fleet_type = "ALWAYS_ON",
            image_name = "LinuxOSv4_AppStream",
            max_user_duration_in_seconds = 57600,
            stream_view = "DESKTOP",
            tags = [cdk.CfnTag(
                key = "Name",
                value = "AppstreamNonProd-Phoenix-solution"
            )],
            vpc_config = appstream.CfnFleet.VpcConfigProperty(
                security_group_ids = ["sg-015ddf2746c8025a2"],
                subnet_ids = ["subnet-0b6b0d8d84785308e","subnet-0fb64d475f117c104"]
            )

        )
