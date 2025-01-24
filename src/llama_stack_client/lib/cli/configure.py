# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import os

import click
import yaml
from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator

from llama_stack_client.lib.cli.constants import (
    LLAMA_STACK_CLIENT_CONFIG_DIR, get_config_file_path)


def get_config():
    config_file = get_config_file_path()
    if config_file.exists():
        with open(config_file, "r") as f:
            return yaml.safe_load(f)
    return None


@click.command()
@click.option("--host", type=str, help="Llama Stack distribution host")
@click.option("--port", type=str, help="Llama Stack distribution port number")
@click.option("--use-https", type=bool, default=False, help="Llama Stack distribution uses HTTPS")
@click.option("--endpoint", type=str, help="Llama Stack distribution endpoint")
@click.option("--api-key", type=str, help="Llama Stack distribution API key")
def configure(host: str | None, port: str | None, use_https: bool | None, endpoint: str | None, api_key: str | None):
    """Configure Llama Stack Client CLI"""
    os.makedirs(LLAMA_STACK_CLIENT_CONFIG_DIR, exist_ok=True)
    config_path = get_config_file_path()

    if endpoint:
        final_endpoint = endpoint
    else:
        if host and port:
            if use_https:
                final_endpoint = f"https://{host}:{port}"
            else:
                final_endpoint = f"http://{host}:{port}"
        else:
            host = prompt(
                "> Enter the host name of the Llama Stack distribution server: ",
                validator=Validator.from_callable(
                    lambda x: len(x) > 0,
                    error_message="Host cannot be empty, please enter a valid host",
                ),
            )
            port = prompt(
                "> Enter the port number of the Llama Stack distribution server: ",
                validator=Validator.from_callable(
                    lambda x: x.isdigit(),
                    error_message="Please enter a valid port number",
                ),
            )
            api_key = prompt(
                "> Enter the API key (leave empty if no key is needed): ",
            )

            is_https = prompt(
                "> Is Llama Stack distribution server using HTTPS? (y/n): ",
                validator=Validator.from_callable(
                    lambda x: x.lower() in ["y", "n", "yes", "no"],
                    error_message="Please enter a valid response for HTTPS, yes or no",
                ),
            )
            if is_https == "y":
                final_endpoint = f"https://{host}:{port}"
            else:
                final_endpoint = f"http://{host}:{port}"

    # Prepare config dict before writing it
    config_dict = {
        "endpoint": final_endpoint,
    }
    if api_key:
        config_dict["api_key"] = api_key

    with open(config_path, "w") as f:
        f.write(
            yaml.dump(
                config_dict,
                sort_keys=True,
            )
        )

    print(f"Done! You can now use the Llama Stack Client CLI with endpoint {final_endpoint}")
