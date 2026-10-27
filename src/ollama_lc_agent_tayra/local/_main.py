# SPDX-FileCopyrightText: 2026-present Tayra Sakurai <tayra_sakurai@icloud.com>
#
# SPDX-License-Identifier: AGPL-3.0-or-later
"""Main suite functions."""
from langchain.agents import create_agent
from langchain.agents.middleware import dynamic_prompt, ModelRequest
import argparse
import ollama

__all__ = [ 'main' ]


def main() -> None:
    """The main suite to be processed for commands."""
    parser = argparse.ArgumentParser(
        description='Makes a local chat client.'
    )
    subparsers = parser.add_subparsers(
        title='command',
        help='The action to execute.'
    )
    sub_a = subparsers.add_parser(
        'load',
        help='Loads the document from the selected directory.'
    )
    sub_a.add_argument(
        'doc_directory',
        type=str,
        help='The directory where the documents.'
    )
    sub_a.add_argument(
        'db_directory',
        type=str,
        help='Where to store the database.'
    )
    sub_a.add_argument(
        '-m',
        '--model',
        type=str,
        help='Model used to generate the embedding vectors.',
        default='embeddinggemma:latest'
    )
    sub_b = subparsers.add_parser(
        'init',
        description='Starts a chat session with the agent.'
    )
    sub_b.add_argument(
        '-s',
        '--session',
        type=str,
        help='The session identifier.'
    )
    sub_b.add_argument(
        '-m',
        '--model',
        type=str,
        help='The model name.',
        default='gemma4:e2b'
    )
    sub_b.add_argument(
        '-e',
        '--embedding',
        type=str,
        help='The embedding model.',
        default='embeddinggemma:latest'
    )
