---
title: "Hello Hugo"
date: 2024-02-17
draft: false
authors: ["诗往"]
description: "Learn to create a Hugo site in minutes."
featuredImage: "featured-image.webp"

tags: ["hugo"]
categories: ["hobby"]
series: ["blog"]
series_weight: 1
lightgallery: true
license: '<a rel="license external nofollow noopener noreffer" href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank">CC BY-NC 4.0</a>'
toc:
  auto: false
---

Learn to create a Hugo site in minutes.

<!--more-->

## Prerequisites

Before you begin this tutorial you must:

- [Install Hugo](https://gohugo.io/installation/) (extended edition, v0.112.0 or later)
- [Install Git](https://gohugo.io/installation/)

You must also be comfortable working from the command line.

## Create a site

### Commands

> If you are a Windows user:
> 
> - Do not use the Command Prompt
> - Do not use Windows PowerShell
> - Run these commands from [PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows) or a Linux terminal such as WSL or Git Bash
> 
> PowerShell and Windows PowerShell [are different applications](https://learn.microsoft.com/en-us/powershell/scripting/whats-new/differences-from-windows-powershell?view=powershell-7.3).

Verify that you have installed Hugo v0.112.0 or later.

```bash
hugo version
```

Run these commands to create a Hugo site with the [Ananke](https://github.com/theNewDynamic/gohugo-theme-ananke) theme. The next section provides an explanation of each command.

```bash
hugo new site quickstart
cd quickstart
git init
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
echo "theme = 'ananke'" >> hugo.toml
hugo server
```

View your site at the URL displayed in your terminal. Press `Ctrl + C` to stop Hugo’s development server.

### Explanation of commands

Create the directory structure for your project in the quickstart directory.

```bash
hugo new site quickstart
```

Change the current directory to the root of your project.

```bash
cd quickstart
```

Initialize an empty Git repository in the current directory.

```bash
git init
```

Clone the Ananke theme into the themes directory, adding it to your project as a Git submodule.

```bash
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
```

Append a line to the site configuration file, indicating the current theme.

```bash
echo "theme = 'ananke'" >> hugo.toml
```

Start Hugo’s development server to view the site.

```bash
hugo server
```

Press `Ctrl + C` to stop Hugo’s development server.

## Add content

Add a new page to your site.

```bash
hugo new content posts/my-first-post.md
```

Hugo created the file in the `content/posts` directory. Open the file with your editor.

```bash
+++
title = 'My First Post'
date = 2024-01-14T07:07:07+01:00
draft = true
+++
```

Notice the `draft` value in the [front matter](https://gohugo.io/content-management/front-matter/) is true. By default, Hugo does not publish draft content when you build the site. Learn more [about draft, future, and expired content](https://gohugo.io/getting-started/usage/#draft-future-and-expired-content).

Add some [Markdown](https://commonmark.org/help/) to the body of the post, but do not change the `draft` value.

```markdown
+++
title = 'My First Post'
date = 2024-01-14T07:07:07+01:00
draft = true
+++
## Introduction

This is **bold** text, and this is *emphasized* text.

Visit the [Hugo](https://gohugo.io) website!
```

Save the file, then start Hugo’s development server to view the site. You can run either of the following commands to include draft content.

```bash
hugo server --buildDrafts
hugo server -D
```

View your site at the URL displayed in your terminal. Keep the development server running as you continue to add and change content.

When satisfied with your new content, set the front matter `draft` parameter to `false`.

> Hugo’s rendering engine conforms to the CommonMark [specification](https://spec.commonmark.org/) for Markdown. The CommonMark organization provides a useful [live testing tool](https://spec.commonmark.org/dingus/) powered by the reference implementation.

## Configure the site

With your editor, open the site configuration file (hugo.toml) in the root of your project.

```toml
baseURL = 'https://example.org/'
languageCode = 'en-us'
title = 'My New Hugo Site'
theme = 'ananke'
```

Make the following changes:

- Set the baseURL for your production site. This value must begin with the protocol and end with a slash, as shown above.

- Set the languageCode to your language and region.

- Set the title for your production site.

Start Hugo’s development server to see your changes, remembering to include draft content.

```bash
hugo server -D
```

> Most theme authors provide configuration guidelines and options. Make sure to visit your theme’s repository or documentation site for details.
> 
> [The New Dynamic](https://www.thenewdynamic.com/), authors of the Ananke theme, provide [documentation](https://github.com/theNewDynamic/gohugo-theme-ananke#readme) for configuration and usage. They also provide a [demonstration site](https://gohugo-ananke-theme-demo.netlify.app/).

## Publish the site

In this step you will publish your site, but you will not deploy it.

When you publish your site, Hugo creates the entire static site in the `public` directory in the root of your project. This includes the HTML files, and assets such as images, CSS files, and JavaScript files.

When you publish your site, you typically do not want to include [draft, future, or expired content](https://gohugo.io/getting-started/usage/#draft-future-and-expired-content). The command is simple.

```bash
hugo
```

To learn how to deploy your site, see the hosting and deployment section.

