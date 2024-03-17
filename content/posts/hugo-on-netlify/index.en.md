---
title: "Hugo on Netlify"
date: 2024-03-17
draft: false
authors: ["诗往"]
description: "Deploy the Hugo website using Netlify."
featuredImage: "featured-image.webp"

tags: ["hugo", "netlify"]
categories: ["hobby"]
series: ["blog"]
series_weight: 3
lightgallery: true
license: '<a rel="license external nofollow noopener noreffer" href="https://creativecommons.org/licenses/by-nc/4.0/" target="_blank">CC BY-NC 4.0</a>'
toc:
  auto: false
---

Hugo is a fast and flexible open source static site generator written in Go.

## Key features
These features provide important benefits for Hugo sites, including ones built and deployed with Netlify.

- Build speed. Hugo boasts near-instant build times of less than one millisecond per page. For large sites with a lot of pages, this can translate into significant time savings during site development and Netlify build and deploy processes.

- Choice of themes. The Hugo ecosystem includes a wide range of premade [themes](https://themes.gohugo.io/) for styling static content.

- Robust templating. Hugo uses Go templates with and libraries to control templating.`html/templatetext/template`

- Instant previews. The [LiveReload](https://gohugo.io/getting-started/usage/#livereload) tool is integrated into Hugo for a hot reloading experience during development.

- URL management. Hugo has built-in support for [URL manipulations](https://gohugo.io/content-management/urls/) and redirects.

- Functions and variables. When building out templates, you can use Go functions, built-in [Hugo-specific functions](https://gohugo.io/functions/), and a variety of [variables](https://gohugo.io/variables/).

## Netlify integration

Hugo sites on Netlify can benefit from automatic framework detection and control over Hugo version selection. They also require theme setup considerations.

### Automatic framework detection

When you [link a repository](https://docs.netlify.com/welcome/add-new-site/#import-from-an-existing-repository) for a project, Netlify tries to detect the framework your site is using. If your site is built with Hugo, Netlify provides a suggested build command and publish directory. If you’re using the CLI to run [Netlify Dev](https://docs.netlify.com/cli/local-development/) for a local development environment, Netlify also suggests a dev command and port. You can override suggested values or set them in a configuration file instead, but automatic framework detection may help simplify the process of setting up a site on Netlify.hugopublichugo server -w1313

For manual configuration, check out the [typical build settings](https://docs.netlify.com/frameworks/#hugo) for Hugo.

## Hugo version

By default we’ll use the Hugo version that is preinstalled in your site’s initial [build image](https://docs.netlify.com/configure-builds/overview/#build-image-selection). Because the preinstalled version may not match your local version, we recommend setting a environment variable. You can set the variable to the version string for any released version after 0.19, for example, .`HUGO_VERSION0.80.0`

1. First, confirm your local Hugo version with .hugo version

2. Then add an [environment variable](https://docs.netlify.com/environment-variables/overview/) in the Netlify UI as you set up your site or in a [Netlify configuration file](https://docs.netlify.com/configure-builds/file-based-configuration/) stored in your repository.

- Follow the steps to [import from an existing repository](https://docs.netlify.com/welcome/add-new-site) and on the Configure site and deploy step, select Add environment variables. Select New variable and then enter the key and value. 

- Alternatively, add the following to in your site’s [base directory](https://docs.netlify.com/configure-builds/overview/#definitions-1), where is a version string such as .`netlify.tomlYOUR_HUGO_VERSION0.80.0`

```toml
[build]
  command = "hugo"
  publish = "public"

[build.environment]
  HUGO_VERSION = "YOUR_HUGO_VERSION"
```

> Failed build?
> 
> If you get an error with when building a Hugo site on Netlify, remember to set to the version you are using locally.`exit code: 255HUGO_VERSION`

## Hugo themes

Hugo themes work by default on Netlify. Like any continuous integration system, however, Netlify can’t use a theme installed by the method. Instead, you should install a Hugo theme for your site as a [git submodule](https://git-scm.com/docs/gitsubmodules).`git clone`

Here’s an example:

```bash
cd YOUR_PROJECT_DIRECTORY
git init
git submodule add https://github.com/THEME_CREATOR/THEME_NAME
```

## More resources

[Typical Hugo build settings](https://docs.netlify.com/frameworks/#hugo)
[Host Hugo on Netlify](https://gohugo.io/hosting-and-deployment/hosting-on-netlify/)
[Hugo documentation](https://gohugo.io/documentation/)