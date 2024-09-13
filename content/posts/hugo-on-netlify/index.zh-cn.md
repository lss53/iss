---
title: "在 Netlify 上使用 Hugo"
date: 2024-03-17
draft: false
authors: ["诗往"]
description: "使用 Netlify 部署 Hugo 网站"
featuredImage: "featured-image.webp"

tags: ["hugo", "netlify"]
categories: ["blog"]
series: ["hobby"]
series_weight: 3
lightgallery: true
toc:
  auto: false
---

Hugo 是一个用 Go 编写的快速灵活的开源静态站点生成器。

## 主要特点

这些特点为 Hugo 网站带来了重要的优势，包括使用 Netlify 构建和部署的网站。

- **构建速度快**。 Hugo 拥有接近瞬时的构建时间，每页不到 1 毫秒。对于拥有大量页面的大型网站，这可以节省大量的网站开发和 Netlify 构建和部署过程时间。

- **主题的选择**。Hugo 生态系统包括各种用于设置静态内容样式的预制[主题](https://themes.gohugo.io/)。

- **强大的模板功能**。 Hugo 使用 Go 模板和 `html/template` 以及 `text/template` 库来控制模板。

- **即时预览**。[LiveReload](https://gohugo.io/getting-started/usage/#livereload) 工具已集成到 Hugo 中，可在开发过程中提供热重载体验。

- **URL 管理**。Hugo 内置了对 [URL 操作](https://gohugo.io/content-management/urls/)和[重定向的支持](https://gohugo.io/content-management/urls/#aliases)。

- **函数和变量**。在构建模板时，可以使用 Go 函数、内置的 [Hugo 特定函数](https://gohugo.io/functions/)和各种[变量](https://gohugo.io/variables/)。


## Netlify 集成

Netlify 上的 Hugo 网站可以受益于自动框架检测和 Hugo 版本选择控制。它们还需要考虑主题设置。

### 自动框架检测

当你[链接一个项目的仓库](https://docs.netlify.com/welcome/add-new-site/#import-from-an-existing-repository)时，Netlify 会尝试检测你的网站使用的框架。如果你的网站是用 Hugo 构建的，Netlify 会提供建议的构建命令和发布目录：`hugo` 和 `public`。如果你使用 CLI 运行 [Netlify Dev](https://docs.netlify.com/cli/local-development/) 进行本地开发环境，Netlify 还会建议一个开发命令和端口：`hugo server -w` 和 `1313`。你可以覆盖建议的值，或者在配置文件中设置它们，但是自动框架检测可以帮助简化在 Netlify 上设置网站的过程。

对于手动配置，请查看 Hugo 的[典型构建设置](https://docs.netlify.com/frameworks/#hugo)。

### Hugo 版本

默认情况下，我们将使用预装在你的网站初始构建镜像中的 Hugo 版本。由于预装版本可能与你的本地版本不匹配，我们建议设置一个 `HUGO_VERSION` 环境变量。你可以将该变量设置为 0.19 之后任何发布版本的版本字符串，例如 `0.80.0` 。

1. 首先，使用 `hugo version` 确认你的本地 Hugo 版本。

2. 然后，设置你的网站时，在 Netlify UI 中添加一个[环境变量](https://docs.netlify.com/environment-variables/overview/)，或者在存储在你的仓库中的 [Netlify 配置文件](https://docs.netlify.com/configure-builds/file-based-configuration/)中添加。

  - 按照步骤从[现有的仓库导入](https://docs.netlify.com/welcome/add-new-site)，在“**配置网站和部署**”步骤中，选择“**添加环境变量**”。选择“**新建变量**”，然后输入键和值。

  - 或者，将以下内容添加到你的网站[根目录](https://docs.netlify.com/configure-builds/overview/#definitions-1)下的 `netlify.toml` 中，其中 `YOUR_HUGO_VERSION` 是一个版本字符串，例如 `0.80.0` ：
  
```toml
[build]
  command = "hugo"
  publish = "public"

[build.environment]
  HUGO_VERSION = "YOUR_HUGO_VERSION"
```

{{< admonition tip >}}

构建失败？

如果你在 Netlify 上构建 Hugo 网站时遇到 `exit code: 255` 错误，请记住将 `HUGO_VERSION` 设置为你本地使用的版本。

{{< /admonition >}}


### Hugo主题

Hugo 主题在 Netlify 上默认工作。然而，像任何持续集成系统一样，Netlify 不能使用通过 `git clone` 方法安装的主题。相反，你应该将 Hugo 主题作为 [git 子模块](https://git-scm.com/docs/gitsubmodules)安装到你的网站上。

举例如下：

```bash
cd YOUR_PROJECT_DIRECTORY
git init
git submodule add https://github.com/THEME_CREATOR/THEME_NAME
```

## 更多资源

- [典型的 Hugo 构建设置](https://docs.netlify.com/frameworks/#hugo)

- [在 Netlify 上托管 Hugo](https://gohugo.io/hosting-and-deployment/hosting-on-netlify/)

- [Hugo 文档](https://gohugo.io/documentation/)