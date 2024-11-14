# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import click

from llama_stack_client.lib.cli.common.utils import print_table_from_response


@click.command("list")
@click.pass_context
def list_eval_tasks(ctx):
    """Show available eval tasks on distribution endpoint"""

    client = ctx.obj["client"]

    headers = []
    eval_tasks_list_response = client.eval_tasks.list()
    if eval_tasks_list_response and len(eval_tasks_list_response) > 0:
        headers = sorted(eval_tasks_list_response[0].__dict__.keys())

    if eval_tasks_list_response:
        print_table_from_response(eval_tasks_list_response, headers)
