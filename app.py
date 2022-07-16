#!/usr/bin/env python3
import os

import aws_cdk as cdk

from appstream_solution.appstream_solution_stack import AppstreamSolutionStack


app = cdk.App()
AppstreamSolutionStack(app, "AppstreamSolutionStack",
            env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'),
            region=os.getenv('CDK_DEFAULT_REGION')))

app.synth()
