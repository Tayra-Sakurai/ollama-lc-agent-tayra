# Contributing the ollama LC Agent Tayra

Thank you for having interest to contribute `ollama-lc-agent-tayra`.

To keep this library organized, please follow the policies in this file and [Code of Conduct](./CODE_OF_CONDUCT.md).

## Publishing an Issue

Please feel free to make an issue if you have an idea or you find a problem in using this library.
However, you should follow these rules when you make or leave a comment to an issue.

### Issue Creation Rules

You must keep these conditions about every issue.

1. An issue must be related to a **unique problem or suggestion**.
2. Each issue must have **at least one label(s)**.
3. Each issue must categorized in **one type**.

### Issue Template Usage

You are recommended to use an **issue template** when you make a new issue.

You should fill all fields in the template.

### Cautions

You **must not** show your personal information in the issues and comments.

## Modifying the Project

Please follow the following procedure.

### Step 1: Fork the Repository

Please **fork** the repository's `main` branch.
No Pull Request do we approve of the modifications made directly to our repository.

### Step 2: Make a New Branch

Please make a new branch following the nomenclature follwing below.

#### The Nomenclature of a Branch

The branch name format is:

```text
(type)/[(ai-agent-name)/](pull-request-title)
```

where texts surrounded by `(` and `)` must be replaced by the values based on the following nomenclature.

- The `(type)` is the modification type name from the [following table](#the-table-of-type-name).
- The `(ai-agent-name)` is the AI agent name used for modify this repository.
- `(pull-request-title)` must be the title of Pull Request to be made.

#### The Table of Type Name

| Type Name | Description |
|:---:|:----|
| `fix` | A bugfix |
| `feat` | Addition of a feature |
| `test` | Addition or modifications on tests |
| `access` | Improvements on accessibility |
| `other` | Others |

### Step 3: Making the Modifications

Please make the modifications on your forked repository.

### Step 4: Test the Library

Please run the following command to test the program.

```bash
hatch test --all
```

### Step 5: Make a Pull Request

Please make a Pull Request with all fields of template filled.
