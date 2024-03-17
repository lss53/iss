---
title: "Host Hugo on Cloudflare Pages"
date: 2024-03-16
draft: false
authors: ["诗往"]
description: "Deploy the Hugo website using Cloudflare Pages."
featuredImage: "featured-image.webp"

tags: ["hugo", "cloudflare"]
categories: ["hobby"]
series: ["blog"]
series_weight: 2
lightgallery: true
license: '<a rel="license external nofollow noopener noreffer" href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank">CC BY-NC 4.0</a>'
toc:
  auto: false
---

[Hugo](https://gohugo.io/) is a tool for generating static sites, written in Go. It is incredibly fast and has great high-level, flexible primitives for managing your content using Markdown and JSON.

In this guide, you will create a new Hugo application and deploy it using Cloudflare Pages. You will use the hugo CLI to create a new Hugo site.

<!--more-->

## Before you continue

All of the framework guides assume you already have a fundamental understanding of [Git](https://git-scm.com/). If you are new to Git, refer to this [summarized Git handbook](https://guides.github.com/introduction/git-handbook/) on how to set up Git on your local machine.

If you clone with SSH, you must [generate SSH keys](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) on each computer you use to push or pull from GitHub.

Refer to the [GitHub documentation](https://guides.github.com/introduction/git-handbook/) and [Git documentation](https://git-scm.com/book/en/v2) for more information.

Go to [Deploy with Cloudflare Pages](https://developers.cloudflare.com/pages/framework-guides/deploy-a-hugo-site/#deploy-with-cloudflare-pages) if you already have a Hugo site hosted with your [Git provider](https://developers.cloudflare.com/pages/get-started/git-integration/).

## Install Hugo

Install the Hugo CLI, using the specific instructions for your operating system below:

### Linux

Your Linux distro’s package manager may include Hugo. If this is the case, install it directly using your distro’s package manager – for instance, in Ubuntu, run the following command:
  
```bash
$ sudo apt-get install hugo
```

If your package manager does not include Hugo or you would like to download a release directly, refer to the [Manual](https://developers.cloudflare.com/pages/framework-guides/deploy-a-hugo-site/#manual-installation) section.

### Homebrew (macOS)

If you use the package manager [Homebrew](https://brew.sh/), run the `brew install` command in your terminal to install Hugo:
  
```bash
$ brew install hugo
```

### Windows (Chocolatey)

If you use the package manager [Chocolatey](https://chocolatey.org/), run the `choco install` command in your terminal to install Hugo:

```bash
$ choco install hugo --confirm
```

### Windows (Scoop)

If you use the package manager [Scoop](https://scoop.sh/), run the `scoop install` command in your terminal to install Hugo:
  
```bash
$ scoop install hugo
```

### Manual installation

The Hugo GitHub repository contains pre-built versions of the Hugo command-line tool for various operating systems, which can be found on [the Releases page](https://github.com/gohugoio/hugo/releases).

For more instruction on installing these releases, refer to [Hugo’s documentation](https://gohugo.io/getting-started/installing/).

## Create a new project

With Hugo installed, refer to [Hugo’s Quick Start](https://gohugo.io/getting-started/quick-start/) to create your project or create a new project by running the `hugo new` command in your terminal:

```bash
$ hugo new site my-hugo-site
```

Hugo sites use themes to customize the look and feel of the statically built HTML site. There are a number of themes available at [themes.gohugo.io](https://themes.gohugo.io/) – for now, use the [Terminal theme](https://github.com/panr/hugo-theme-terminal) by running the following commands in your terminal:

```bash
$ cd my-hugo-site
$ git init
$ git submodule add https://github.com/panr/hugo-theme-terminal.git themes/terminal
$ git submodule update --init --recursive
```

You should also copy the default configuration provided by the theme into the `config.toml` file in your project’s directory. Take the following information and customize it per your site’s needs:
  
```toml
baseurl = "/"
languageCode = "en-us"
theme = "terminal"
paginate = 5

[params]
  # dir name of your main content (default is `content/posts`).
  # the list of set content will show up on your index page (baseurl).
  contentTypeName = "posts"

  # ["orange", "blue", "red", "green", "pink"]
  themeColor = "orange"

  # if you set this to 0, only submenu trigger will be visible
  showMenuItems = 2

  # show selector to switch language
  showLanguageSelector = false

  # set theme to full screen width
  fullWidthTheme = false

  # center theme with default width
  centerTheme = false

  # set a custom favicon (default is a `themeColor` square)
  # favicon = "favicon.ico"

  # set post to show the last updated
  # If you use git, you can set `enableGitInfo` to `true` and then post will automatically get the last updated
  showLastUpdated = false
  # Provide a string as a prefix for the last update date. By default, it looks like this: 2020-xx-xx [Updated: 2020-xx-xx] :: Author
  # updatedDatePrefix = "Updated"

  # set all headings to their default size (depending on browser settings)
  # it's set to `true` by default
  # oneHeadingSize = false

[params.twitter]
  # set Twitter handles for Twitter cards
  # see https://developer.twitter.com/en/docs/tweets/optimize-with-cards/guides/getting-started#card-and-content-attribution
  # do not include @
  creator = ""
  site = ""

[languages]
  [languages.en]
    languageName = "English"
    title = "Terminal"
    subtitle = "A simple, retro theme for Hugo"
    owner = ""
    keywords = ""
    copyright = ""
    menuMore = "Show more"
    readMore = "Read more"
    readOtherPosts = "Read other posts"
    missingContentMessage = "Page not found..."
    missingBackButtonLabel = "Back to home page"

    [languages.en.params.logo]
      logoText = "Terminal"
      logoHomeLink = "/"

    [languages.en.menu]
      [[languages.en.menu.main]]
        identifier = "about"
        name = "About"
        url = "/about"
      [[languages.en.menu.main]]
        identifier = "showcase"
        name = "Showcase"
        url = "/showcase"
```

## Create a post

Create a new post to give your Hugo site some initial content. Run the `hugo new` command in your terminal to generate a new post:
  
```bash
$ hugo new posts/hello-world.md
```

Inside of `hello-world.md`, add some initial content to create your post. Remove the `draft` line in your post’s frontmatter when you are ready to publish the post. Any posts with `draft: true` set will be skipped by Hugo’s build process.

## Create a GitHub repository

Create a new GitHub repository by visiting [repo.new](https://repo.new/). After creating a new repository, go to your newly created project directory to prepare and push your local application to GitHub by running the following commands in your terminal:

```bash
$ git remote add origin https://github.com/<your-gh-username>/<repository-name>
$ git branch -M main
$ git push -u origin main
```

## Deploy with Cloudflare Pages

To deploy your site to Pages:

1.Log in to the [Cloudflare dashboard](https://dash.cloudflare.com/) and select your account.
2.In Account Home, select **Workers & Pages** > **Create application** > **Pages** > **Connect to Git**.
3.Select the new GitHub repository that you created and, in the **Set up builds and deployments** section, provide the following information:

|  Configuration  | option  |
|  :----:  |  :----:  | 
|  Production branch  |  main  |
|  Build command  |  hugo  |
|  Build directory  |  public  |
	
> Base URL configuration
>
> Hugo allows you to configure the `baseURL` of your application. This allows you to utilize the `absURL` helper to construct full canonical URLs. In order to do this with Pages, you must provide the `-b` or `--baseURL` flags with the `CF_PAGES_URL` environment variable to your `hugo` build command.
>
>Your final build command may look like this:
>
> ```bash
> $ hugo -b $CF_PAGES_URL
> ```
> 

After completing deployment configuration, select the **Save and Deploy**. You should see Cloudflare Pages installing `hugo` and your project dependencies, and building your site, before deploying it.

> For the complete guide to deploying your first site to Cloudflare Pages, refer to the [Get started guide](https://developers.cloudflare.com/pages/get-started/).

After deploying your site, you will receive a unique subdomain for your project on `*.pages.dev`. Every time you commit new code to your Hugo site, Cloudflare Pages will automatically rebuild your project and deploy it. You will also get access to [preview deployments](https://developers.cloudflare.com/pages/configuration/preview-deployments/) on new pull requests, so you can preview how changes look to your site before deploying them to production.

## Use a specific or newer Hugo version

To use a [specific or newer version of Hugo](https://github.com/gohugoio/hugo/releases), create the `HUGO_VERSION` environment variable in your Pages project > **Settings** > **Environment variables**. Set the value as the Hugo version you want to specify (v0.112.0 or later is recommended for newer versions).

For example, `HUGO_VERSION: 0.115.4`.

> If you plan to use [preview deployments](https://developers.cloudflare.com/pages/configuration/preview-deployments/), make sure you also add environment variables to your **Preview** environment.

## Learn more
By completing this guide, you have successfully deployed your Hugo site to Cloudflare Pages. To get started with other frameworks, [refer to the list of Framework guides](https://developers.cloudflare.com/pages/framework-guides/).