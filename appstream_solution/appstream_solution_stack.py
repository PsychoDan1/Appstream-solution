from email.mime import application
from aws_cdk import Stack
import aws_cdk as cdk
import os
from constructs import Construct
import aws_cdk.aws_appstream as appstream
import yaml

with open('./appstream_solution/manifest.yml', 'rb') as f:
        config = yaml.safe_load(f)

core_config = config['environment']


class AppstreamSolutionStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cfn_fleet = appstream.CfnFleet(self, "AppstreamNonProd-Phoenix-solution-fleet",
                                       instance_type = core_config['instanceType'],
                                       name = core_config['name'],
                                       compute_capacity = appstream.CfnFleet.ComputeCapacityProperty(
                                       desired_instances = 20
                                       ),
            
                                       description = core_config['name'],
                                       disconnect_timeout_in_seconds = core_config['disconnectTimeoutInSeconds'],
                                       idle_disconnect_timeout_in_seconds = core_config['idleDisconnectTimeoutInSeconds'],
                                       enable_default_internet_access = False,
                                       fleet_type = "ALWAYS_ON",
                                       image_name = core_config['imageName'],
                                       max_user_duration_in_seconds = core_config['maxUserDurationInSeconds'],
                                       stream_view = core_config['streamView'],
                                       tags = [cdk.CfnTag(
                                           key = "Name",
                                           value = core_config['name']
                                       )],
            
                                       vpc_config = appstream.CfnFleet.VpcConfigProperty(
                                           security_group_ids = ["sg-015ddf2746c8025a2"],
                                           subnet_ids = core_config['subnets']
                                       )
                                     )

        cfn_stack = appstream.CfnStack (self, "AppstreamNonProd-Phoenix-solution-Stack"),
        application_settings = appstream.CfnStack.ApplicationSettingsProperty(
            enabled = False
        ),
        description = 'Phoenix Appstream Solution Stack',
        display_name = core_config['name'],
        redirect_url = core_config['redirectURL']
        storage_connectors  = [appstream.CfnStack.StorageConnectorProperty(
            connector_type = 'HOMEFOLDERS'
        )],
        streaming_experiance_seetings = appstream.CfnStack.StreamingExperienceSettingsProperty(
            preferred_protocol = 'TCP'
        ),
        user_settings = [appstream.CfnStack.UserSettingProperty(
            action = 'PRINTING_TO_LOCAL_DEVICE',
            permission = 'ENABLED'
        )]
            