---
title: "在 Netlify 上托管 Hugo"
date: 2024-03-17
draft: false
authors: ["诗往"]
description: "使用 Netlify 部署 Hugo 网站"
featuredImage: ""

tags: ["hugo", "netlify"]
categories: ["hobby"]
series: ["blog"]
series_weight: 3
lightgallery: true
toc:
  auto: false
---

Hugo 是一个用 Go 编写的快速灵活的开源静态站点生成器。

## 主要特点

这些功能为 Hugo 站点提供了重要的好处，包括使用 Netlify 构建和部署的站点。

- 构建速度。Hugo 拥有每页不到 1 毫秒的近乎即时的构建时间。对于具有大量页面的大型站点，这可以在站点开发以及 Netlify 构建和部署过程中节省大量时间。

- 主题的选择。Hugo 生态系统包括各种用于设置静态内容样式的预制[主题](https://themes.gohugo.io/)。

- 强大的模板。Hugo 使用 Go 模板和 和 库来控制模板。
`html/templatetext/template`

- 即时预览。[LiveReload](https://gohugo.io/getting-started/usage/#livereload) 工具已集成到 Hugo 中，可在开发过程中提供热重载体验。

- URL 管理。Hugo 内置了对 [URL 操作](https://gohugo.io/content-management/urls/)和[重定向的支持](https://gohugo.io/content-management/urls/#aliases)。

- 函数和变量。在构建模板时，可以使用 Go 函数、内置的 [Hugo 特定函数](https://gohugo.io/functions/)和各种[变量](https://gohugo.io/variables/)。


## Netlify 集成

Netlify 上的 Hugo 站点可以从自动框架检测和对 Hugo 版本选择的控制中受益。它们还需要主题设置注意事项。

### 自动框架检测

当您[链接项目的存储库](https://docs.netlify.com/welcome/add-new-site/#import-from-an-existing-repository)时，Netlify 会尝试检测您的站点正在使用的框架。如果您的站点是使用 Hugo 构建的，Netlify 会提供建议的构建命令和发布目录。如果您使用 CLI 为本地开发环境运行 [Netlify Dev](https://docs.netlify.com/cli/local-development/)，Netlify 还会建议使用 dev 命令和端口。您可以覆盖建议的值或改为在配置文件中设置它们，但自动框架检测可能有助于简化在 Netlify 上设置站点的过程。`hugopublichugo server -w1313`

对于手动配置，请查看 Hugo 的[典型构建设置](https://docs.netlify.com/frameworks/#hugo)。

## Hugo 版本

默认情况下，我们将使用预装在站点初始构建映像中的 Hugo 版本。由于预安装的版本可能与您的本地版本不匹配，因此我们建议设置环境变量。您可以将变量设置为 0.19 之后任何已发布版本的版本字符串，例如 .`HUGO_VERSION0.80.0`

1. 首先，使用 .`hugo version`

2. 然后，在设置站点时在 Netlify UI 中或存储库中存储的 [Netlify 配置文件](https://docs.netlify.com/configure-builds/file-based-configuration/)中添加[环境变量](https://docs.netlify.com/environment-variables/overview/)。

按照步骤[从现有存储库导入](https://docs.netlify.com/welcome/add-new-site)，然后在“**配置站点和部署**”步骤中，选择“**添加环境变量**”。选择“**新建变量**”，然后输入键和值。

或者，将以下内容添加到站点的[根目录](https://docs.netlify.com/configure-builds/overview/#definitions-1)中，其中是一个版本字符串，例如 .`netlify.tomlYOUR_HUGO_VERSION0.80.0`

```toml
[build]
  command = "hugo"
  publish = "public"

[build.environment]
  HUGO_VERSION = "YOUR_HUGO_VERSION"
```

> 构建失败？
> 
> 如果您在Netlify上构建Hugo站点时遇到错误，请记住设置为您在本地使用的版本。`exit code: 255HUGO_VERSION`

## Hugo主题

Hugo 主题默认在 Netlify 上工作。但是，与任何持续集成系统一样，Netlify 不能使用该方法安装的主题。相反，您应该为您的网站安装一个 Hugo 主题作为 [git 子模块](https://git-scm.com/docs/gitsubmodules)。`git clone`

下面是一个示例：

```bash
cd YOUR_PROJECT_DIRECTORY
git init
git submodule add https://github.com/THEME_CREATOR/THEME_NAME
```

## 更多资源
[典型的 Hugo 构建设置](https://docs.netlify.com/frameworks/#hugo)
[在 Netlify 上托管 Hugo](https://gohugo.io/hosting-and-deployment/hosting-on-netlify/)
[Hugo 文档](https://gohugo.io/documentation/)