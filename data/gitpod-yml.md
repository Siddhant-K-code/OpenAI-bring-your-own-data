<!--  This is document is take from www.gitpod.io/docs -->

# .gitpod.yml

A workspace gets configured through a `.gitpod.yml` file, located at the root of your project, written in YAML syntax. Here's an example:

```yaml
# Commands to start on workspace startup
tasks:
  - name: Setup & Build
    before: yarn global add express
    init: yarn install
    command: yarn build

# Ports to expose on workspace startup
ports:
  - port: 3000
    onOpen: open-preview
    name: Website
    description: Website Preview
```

To see a full reference of all available properties, please refer to the [`.gitpod.yml reference`](/docs/references/gitpod-yml) page.

`youtube: E95oV_iqUtI`

## How to provide the .gitpod.yml config file

In order to tell Gitpod how to prepare a dev environment for your project, you check in a `.gitpod.yml` file into the root of your repository. This way you can
version your workspace configuration together with your code. If, for example, you need to go back to
an old branch that required a different configuration, Gitpod will start with the correct configuration, since that
bit of configuration is part of your codebase.

## Generate Your Gitpod Config File

The quickest way to create a `.gitpod.yml` file is with the `gp` CLI. In the terminal of a Gitpod workspace, type:

```sh
gp init
```

This generates example content you can adjust to meet your needs.

Alternatively, you can use the interactive mode with `gp init -i`. It will ask you about the different configuration options, generate the `.gitpod.yml` file and open it in an editor tab so you can review and extend as necessary.

Gitpod provides auto-complete, hover info and validation for the `.gitpod.yml` file so you get instant feedback and can rest assure your configuration is valid.

## See it in action

To test your `.gitpod.yml` file, you need to commit and push the file to your repository and open a new workspace either by using the [Gitpod extension](/docs/configure/user-settings/browser-extension#browser-extension) or prefixing your repo URL with `https://gitpod.io/#`.

If you don't want to have multiple commits as you're testing and making changes to your `.gitpod.yml`, you can make changes from a new branch.
