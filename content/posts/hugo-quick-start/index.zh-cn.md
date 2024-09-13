---
title: "Hugo 快速入门"
date: 2024-02-17
draft: false
authors: ["诗往"]
description: "几分钟内学会创建 Hugo 网站。"
featuredImage: "featured-image.webp"

tags: ["hugo"]
categories: ["blog"]
series: ["hobby"]
series_weight: 1
lightgallery: true

toc:
  auto: false
---

几分钟内学会创建 Hugo 网站入门教程。

<!--more-->

## 前提条件

在开始此教程之前，你必须：

- [安装 Hugo](https://gohugo.io/installation/)（扩展版，v0.112.0 或更高版本）

- [安装 Git](https://gohugo.io/installation/)

你还必须能够熟练地使用命令行。

## 创建网站

### 命令

> 如果您是 Windows 用户：
> 
> - 请勿使用命令提示符
> - 请勿使用 Windows PowerShell
> - 从 [PowerShell](https://learn.microsoft.com/zh-cn/powershell/scripting/install/installing-powershell-on-windows) 或 Linux 终端（例如 WSL 或 Git Bash）运行这些命令
>
>PowerShell 和 Windows PowerShell 是[不同的应用程序](https://learn.microsoft.com/zh-cn/powershell/scripting/whats-new/differences-from-windows-powershell?view=powershell-7.3)。

验证您是否已安装 Hugo v0.112.0 或更高版本。

```bash
hugo version
```

运行这些命令创建带有 [Ananke](https://github.com/theNewDynamic/gohugo-theme-ananke) 主题的 Hugo 网站。下一部分提供了每条命令的解释。

```bash
hugo new site quickstart
cd quickstart
git init
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
echo "theme = 'ananke'" >> hugo.toml
hugo server
```

在终端显示的 URL 中查看您的网站。按 `Ctrl + C` 停止 Hugo 的开发服务器。


### 命令说明

在 `quickstart` 目录中为您的项目创建目录结构。

```bash
hugo new site quickstart
```

将当前目录更改为项目的根目录。
```bash
cd quickstart
```

在当前目录中初始化一个空 Git 存储库。

```bash
git init
```

将 Ananke 主题克隆到 themes 目录中，将其作为 Git 子模块添加到您的项目中。

```bash
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
```

在网站配置文件中添加一行，指示当前主题。

```bash
echo "theme = 'ananke'" >> hugo.toml
```

启动 Hugo 的开发服务器以查看网站。
```bash
hugo server
```

按 `Ctrl + C` 停止 Hugo 的开发服务器。

## 添加内容

向您的网站添加新页面。

```bash
hugo new content posts/my-first-post.md
```

Hugo 在 `content/posts` 目录中创建了该文件。使用您的编辑器打开该文件。

```markdown
+++
title = 'My First Post'
date = 2024-01-14T07:07:07+01:00
draft = true
+++
```

请注意，[front matter](https://gohugo.io/content-management/front-matter/) 中的 `draft` 值为 true。默认情况下，在构建网站时，Hugo 不会发布草稿内容。详细了解[草稿、未来和已过期的内容](https://gohugo.io/getting-started/usage/#draft-future-and-expired-content)。

在帖子的正文中添加一些 [Markdown](https://commonmark.org/help/)，但不要更改 `draft` 值。

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

保存文件，然后启动 Hugo 的开发服务器以查看网站。您可以运行以下命令之一来包括草稿内容。

```bash
hugo server --buildDrafts
hugo server -D
```

在终端显示的 URL 中查看您的网站。在您继续添加和更改内容时，让开发服务器保持运行。

当对您的新内容满意时，将 front matter `draft` 参数设置为 `false`。

> Hugo 的渲染引擎符合 Markdown 的 CommonMark [规范](https://spec.commonmark.org/)。CommonMark 组织提供了一个有用的[实时测试工具](https://spec.commonmark.org/dingus/)。

## 配置网站

使用您的编辑器，在项目的根目录中打开网站配置文件 (hugo.toml)。

```toml
baseURL = 'https://example.org/'
languageCode = 'en-us'
title = 'My New Hugo Site'
theme = 'ananke'
```

进行以下更改：

- 设置站点的 baseURL。此值必须以协议开头并以斜杠结尾，如上所示。
- 将 languageCode 设置为您的语言和地区（如`zh-cn`）。
- 设置生产站点的标题。

启动 Hugo 的开发服务器以查看您的更改，请记住包括草稿内容。

```bash
hugo server -D
```

> 大多数主题作者都会提供示例配置。请务必访问您主题的存储库或文档网站，以了解详细信息。
> 
> Ananke 主题的作者 [The New Dynamic](https://www.thenewdynamic.com/) 提供有关配置和使用的[文档](https://github.com/theNewDynamic/gohugo-theme-ananke#readme)。他们还提供了一个[演示网站](https://gohugo-ananke-theme-demo.netlify.app/)。

## 发布网站

在此步骤中，您将发布您的网站，但您不会部署它。

当您发布您的网站时，Hugo 会在您项目的根目录中的 `public` 目录中创建整个静态站点。这包括 HTML 文件以及图像、CSS 文件和 JavaScript 文件等。

当您发布您的网站时，您通常不希望包含[草稿、未来或过期的内容](https://gohugo.io/getting-started/usage/#draft-future-and-expired-content)。命令很简单。

```bash
hugo
```

要了解如何部署您的网站，请参阅[托管和部署](https://gohugo.io/hosting-and-deployment/)部分。












