---
title: "在 Cloudflare Pages 上托管 Hugo"
date: 2024-03-16
draft: false
authors: ["诗往"]
description: "使用 Cloudflare Pages 部署 Hugo 网站"
featuredImage: "featured-image.webp"

tags: ["hugo", "Cloudflare"]
categories: ["hobby"]
series: ["blog"]
series_weight: 2
lightgallery: true
toc:
  auto: false
---

[Hugo](https://gohugo.io/) 是一个用 Go 语言编写的静态网站生成工具。它速度非常快，并提供高级、灵活的原语，可使用 Markdown 和 JSON 管理您的内容。

在本指南中，您将创建一个新的 Hugo 应用程序并使用 Cloudflare Pages 部署它。您将使用 `hugo` CLI 创建一个新的 Hugo 网站。

<!--more-->

## 继续之前

所有框架指南都假设您已经对 [Git](https://git-scm.com/) 有基本的了解。如果您不熟悉 Git，请参阅这份 [Git 手册摘要](https://guides.github.com/introduction/git-handbook/)，了解如何在本地机器上设置 Git。

如果您使用 SSH 克隆，则必须在用于推送或拉取 GitHub 的每台计算机上[生成 SSH 密钥](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)。

​有关更多信息，请参阅 [GitHub 文档](https://guides.github.com/introduction/git-handbook/) 和 [Git 文档](https://git-scm.com/book/en/v2)。

如果您已经有一个使用 [Git 提供程序](https://developers.cloudflare.com/pages/get-started/git-integration/)托管的 Hugo 网站，请转到“[使用 Cloudflare Pages 部署](https://developers.cloudflare.com/pages/framework-guides/deploy-a-hugo-site/#deploy-with-cloudflare-pages)”。

## 安装 Hugo

使用以下针对您的操作系统的特定说明安装 Hugo CLI：

### Linux

您的 Linux 发行版的包管理器可能包含 Hugo。如果是这种情况，请直接使用您的发行版的包管理器安装它。例如，在 Ubuntu 中，运行以下命令：

```bash
$ sudo apt-get install hugo
```

如果您的包管理器不包含 Hugo，或者您想直接下载版本，请参阅“[手动](https://developers.cloudflare.com/pages/framework-guides/deploy-a-hugo-site/#manual-installation)”部分。

### Homebrew (macOS)

如果您使用包管理器 [Homebrew](https://brew.sh/)，请在终端中运行 `brew install` 命令来安装 Hugo：

```bash
$ brew install hugo
```

### Windows (Chocolatey)

如果您使用包管理器 [Chocolatey](https://chocolatey.org/)，请在终端中运行 `choco install` 命令来安装 Hugo：

```bash
$ choco install hugo --confirm
```

### Windows (Scoop)

如果您使用包管理器 [Scoop](https://scoop.sh/)，请在终端中运行 `scoop install` 命令来安装 Hugo：

```bash
$ scoop install hugo
```

### 手动安装

Hugo GitHub 存储库包含针对各种操作系统的预构建版本的 Hugo 命令行工具，可以在[“发布”页面](https://github.com/gohugoio/hugo/releases)上找到。

有关安装这些版本的更多说明，请参阅 [Hugo 文档](https://gohugo.io/getting-started/installing/)。

创建新项目

安装 Hugo 后，请参阅 [Hugo 快速入门指南](https://gohugo.io/getting-started/quick-start/)来创建您的项目，或者在终端中运行 `hugo new` 命令来创建新项目：

```bash
$ hugo new site my-hugo-site
```

Hugo 网站使用主题来定制静态构建的 HTML 网站的外观和感觉。 [themes.gohugo.io](https://themes.gohugo.io/) 上提供了许多主题 - 现在，通过在终端中运行以下命令来使用 [Terminal 主题](https://github.com/panr/hugo-theme-terminal)：

```bash
$ cd my-hugo-site
$ git init
$ git submodule add https://github.com/panr/hugo-theme-terminal.git themes/terminal
$ git submodule update --init --recursive
```

您还应该将主题提供的默认配置复制到项目目录中的 `config.toml` 文件中。获取以下信息并根据您的网站需求进行自定义：

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

## 创建帖子

创建一篇新帖子，为您的 Hugo 网站提供一些初始内容。在终端中运行 `hugo new` 命令以生成新帖子：

```bash
$ hugo new posts/hello-world.md
```

在 `hello-world.md` 中，添加一些初始内容来创建您的帖子。当您准备好发布帖子时，删除帖子frontmatter中的 `draft` 行。任何设置了 `draft: true` 的帖子都将被 Hugo 的构建过程跳过。

## 创建 GitHub 存储库

访问 [repo.new](https://repo.new/) 创建一个新的 GitHub 存储库。创建新的存储库后，转到新创建的项目目录，通过在终端中运行以下命令来准备并将本地应用程序推送到 GitHub：

```bash
$ git remote add origin https://github.com/<your-gh-username>/<repository-name>
$ git branch -M main
$ git push -u origin main
```

## 使用 Cloudflare Pages 部署

要将您的网站部署到 Pages：

1.登录 [Cloudflare 仪表板](https://dash.cloudflare.com/)并选择您的帐户。

2.在帐户主页中，选择 **Workers & Pages** > **创建应用程序** > **Pages** > **连接到 Git**。

3.选择您创建的新 GitHub 存储库，并在“**设置构建和部署**”部分提供以下信息：

|  配置选项  | 值  |
|  ----  |  ----  | 
|  生产分支  |  main  |
|  构建命令  |  hugo  |
|  构建目录  |  public  |

> 基本 URL 配置
> 
> Hugo 允许您配置应用程序的 `baseURL`。这允许您利用 `absURL` 帮助器来构建完整的规范 URL。为了使用 Pages 执行此操作，您必须将 `-b` 或 `--baseURL` 标志与 `CF_PAGES_URL` 环境变量一起提供给您的 `hugo` build 命令。
>
> 您最终的构建命令可能如下所示：
>```bash
> $ hugo -b $CF_PAGES_URL
>```
>

完成部署配置后，选择“**保存并部署**”。您应该会看到 Cloudflare Pages 安装 `hugo` 和您的项目依赖项，并构建您的网站，然后将其部署。

> 有关将您的第一个网站部署到 Cloudflare Pages 的完整指南，请参阅[入门指南](https://developers.cloudflare.com/pages/get-started/)。

部署您的网站后，您将在 `*.pages.dev` 上收到一个针对您的项目的唯一子域。每次您将新代码提交到 Hugo 网站时，Cloudflare Pages 都会自动重建您的项目并进行部署。您还可以访问新拉取请求的[预览部署](https://developers.cloudflare.com/pages/configuration/preview-deployments/)，以便在将更改部署到生产环境之前预览它们对您网站的影响。

## 使用特定或更新的 Hugo 版本

要使用[特定或更新版本的 Hugo](https://github.com/gohugoio/hugo/releases)，请在您的 Pages 项目 > **设置** > **环境变量**中创建 `HUGO_VERSION` 环境变量。将值设置为您要指定的 Hugo 版本（建议使用 v0.112.0 或更高版本）。

例如，`HUGO_VERSION: 0.115.4`。

> 如果您计划使用[预览部署](https://developers.cloudflare.com/pages/configuration/preview-deployments/)，请确保您还将环境变量添加到您的**预览**环境中。

## 了解更多

通过完成本指南，您已成功将您的 Hugo 网站部署到 Cloudflare Pages。要开始使用其他框架，[请参阅框架指南列表](https://developers.cloudflare.com/pages/framework-guides/)。